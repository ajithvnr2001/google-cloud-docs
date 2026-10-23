---
url: https://docs.cloud.google.com/oracle/database/docs/backup-database/
title: View backups for an Autonomous AI Database \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:06.678599+00:00
---

# View backups for an Autonomous AI Database  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/backup-database/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  View backups for an Autonomous AI Database Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to view backups for an Autonomous AI Database in Google Cloud.

Autonomous AI Database lets you create automatic backups of your data that can be used to restore lost data or provide protection against errors. Backups are highly available and are stored for the retention period defined in your Autonomous AI Database's settings.

In Oracle Database@Google Cloud, Autonomous AI Database backup retention is set in days and can range from 1 to 60 days, with a default value of 60 days. The retention period is set when you [create a database](https://docs.cloud.google.com/oracle/database/docs/create-databases) and can't be modified in Google Cloud after creation. To modify the retention period in OCI, see [About Backup and Recovery on Autonomous AI Database](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/backup-intro.html#GUID-3BF27FDE-F847-4A86-9C8B-4ED9B0C1D1B2).

Backups beyond the set retention period are automatically deleted. Automatic backups are managed by Oracle Cloud Infrastructure (OCI) and [billed separately](https://www.oracle.com/autonomous-database/pricing/), in addition to database storage.

To see your database's backup settings, [View database information](https://docs.cloud.google.com/oracle/database/docs/view-database-information).

To learn more about how backup and recovery works for an Autonomous AI Database, see [About Backup and Recovery on Autonomous AI Database](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/backup-intro.html#GUID-3BF27FDE-F847-4A86-9C8B-4ED9B0C1D1B2).

## View backups for an Autonomous AI Database

To view the available backups for an Autonomous AI Database, do the following:

### Console

  1. Go to the **Autonomous AI Database** page.

[Go to Autonomous AI Database](https://console.cloud.google.com/oracle/autonomous-databases/)

  2. Click the name of the Autonomous AI Database for which you want to view the backups.

  3. On the **Autonomous AI Database details** page, select the **Backups** tab.

You can view the details of the available backups.




### gcloud

Use the `gcloud oracle-database autonomous-database-backups list` command to view the available backups.
    
    
    gcloud oracle-database autonomous-database-backups list
    --filter='autonomous_database_id="DATABASE_NAME"'
    --location=REGION_ID
    --project=PROJECT_NAME
    

Replace the following:

  * DATABASE_NAME: name of the database you want to view backups for.
  * REGION_ID: the region of your database.
  * PROJECT_NAME: the name of your Google Cloud project.



###  API 

To list backups of an Autonomous AI Database, run the following `curl` command.
    
    
     curl -X GET   
    
     -H "Authorization: Bearer $(gcloud auth print-access-token)"   
    
     -H "Content-Type: application/json"   
    
     "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/autonomousDatabaseBackups?autonomous_database_id="DATABASE_ID""
     

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project. If you're using a Shared VPC, then this project ID is the ID of your host project.
  * REGION: the region of your database.
  * DATABASE_ID: the ID of your database.



### C#
    
    
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using [Google.Cloud.OracleDatabase.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.html);
    using System;
    using System.Threading.Tasks;
    
    public sealed partial class GeneratedOracleDatabaseClientSnippets
    {
        /// <summary>Snippet for ListAutonomousDatabaseBackupsAsync</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public async Task ListAutonomousDatabaseBackupsAsync()
        {
            // Create client
            [OracleDatabaseClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OracleDatabaseClient.html) oracleDatabaseClient = await [OracleDatabaseClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OracleDatabaseClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OracleDatabaseClient.html#Google_Cloud_OracleDatabase_V1_OracleDatabaseClient_CreateAsync_System_Threading_CancellationToken_)();
            // Initialize request argument(s)
            string parent = "projects/[PROJECT]/locations/[LOCATION]";
            // Make the request
            PagedAsyncEnumerable<ListAutonomousDatabaseBackupsResponse, AutonomousDatabaseBackup> response = oracleDatabaseClient.[ListAutonomousDatabaseBackupsAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OracleDatabaseClient.html#Google_Cloud_OracleDatabase_V1_OracleDatabaseClient_ListAutonomousDatabaseBackupsAsync_Google_Api_Gax_ResourceNames_LocationName_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_)(parent);
    
            // Iterate over all response items, lazily performing RPCs as required
            await foreach ([AutonomousDatabaseBackup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseBackup.html) item in response)
            {
                // Do something with each item
                Console.WriteLine(item);
            }
    
            // Or iterate over pages (of server-defined size), performing one RPC per page
            await foreach ([ListAutonomousDatabaseBackupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListAutonomousDatabaseBackupsResponse.html) page in response.AsRawResponses())
            {
                // Do something with each page of items
                Console.WriteLine("A page of results:");
                foreach ([AutonomousDatabaseBackup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseBackup.html) item in page)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
            }
    
            // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
            int pageSize = 10;
            Page<AutonomousDatabaseBackup> singlePage = await response.ReadPageAsync(pageSize);
            // Do something with the page of items
            Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
            foreach ([AutonomousDatabaseBackup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseBackup.html) item in singlePage)
            {
                // Do something with each item
                Console.WriteLine(item);
            }
            // Store the pageToken, for when the next page is required.
            string nextPageToken = singlePage.NextPageToken;
        }
    }

### Go
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListAutonomousDatabaseBackupsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListAutonomousDatabaseBackupsRequest.
    	}
    	it := c.ListAutonomousDatabaseBackups(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*oracledatabasepb.ListAutonomousDatabaseBackupsResponse)
    	}
    }
    

### Java
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.cloud.oracledatabase.v1.[AutonomousDatabaseBackup](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabaseBackup.html);
    import com.google.cloud.oracledatabase.v1.[ListAutonomousDatabaseBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListAutonomousDatabaseBackupsRequest.html);
    import com.google.cloud.oracledatabase.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.LocationName.html);
    import com.google.cloud.oracledatabase.v1.[OracleDatabaseClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.html);
    
    public class AsyncListAutonomousDatabaseBackups {
    
      public static void main(String[] args) throws Exception {
        asyncListAutonomousDatabaseBackups();
      }
    
      public static void asyncListAutonomousDatabaseBackups() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([OracleDatabaseClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.html) oracleDatabaseClient = [OracleDatabaseClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.html).create()) {
          [ListAutonomousDatabaseBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListAutonomousDatabaseBackupsRequest.html) request =
              [ListAutonomousDatabaseBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListAutonomousDatabaseBackupsRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.LocationName.html).of("[PROJECT]", "[LOCATION]").toString())
                  .setFilter("filter-1274492040")
                  .setPageSize(883849137)
                  .setPageToken("pageToken873572522")
                  .build();
          ApiFuture<AutonomousDatabaseBackup> future =
              oracleDatabaseClient.[listAutonomousDatabaseBackupsPagedCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.html#com_google_cloud_oracledatabase_v1_OracleDatabaseClient_listAutonomousDatabaseBackupsPagedCallable__)().futureCall(request);
          // Do something.
          for ([AutonomousDatabaseBackup](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabaseBackup.html) element : future.get().iterateAll()) {
            // doThingsWith(element);
          }
        }
      }
    }

### Node.js
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. The parent value for ListAutonomousDatabaseBackups in the
     *  following format: projects/{project}/locations/{location}.
     */
    // const parent = 'abc123'
    /**
     *  Optional. An expression for filtering the results of the request. Only the
     *  **autonomous_database_id** field is supported in the following format:
     *  `autonomous_database_id="{autonomous_database_id}"`. The accepted values
     *  must be a valid Autonomous Database ID, limited to the naming
     *  restrictions of the ID: ^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$).
     *  The ID must start with a letter, end with a letter or a number, and be
     *  a maximum of 63 characters.
     */
    // const filter = 'abc123'
    /**
     *  Optional. The maximum number of items to return.
     *  If unspecified, at most 50 Autonomous DB Backups will be returned.
     *  The maximum value is 1000; values above 1000 will be coerced to 1000.
     */
    // const pageSize = 1234
    /**
     *  Optional. A token identifying a page of results the server should return.
     */
    // const pageToken = 'abc123'
    
    // Imports the Oracledatabase library
    const {OracleDatabaseClient} = require('[@google-cloud/oracledatabase](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/overview.html)').v1;
    
    // Instantiates a client
    const oracledatabaseClient = new [OracleDatabaseClient](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/overview.html)();
    
    async function callListAutonomousDatabaseBackups() {
      // Construct request
      const request = {
        parent,
      };
    
      // Run request
      const iterable = oracledatabaseClient.[listAutonomousDatabaseBackupsAsync](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/v1.oracledatabaseclient.html)(request);
      for await (const response of iterable) {
          console.log(response);
      }
    }
    
    callListAutonomousDatabaseBackups();

### PHP
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    use Google\Cloud\OracleDatabase\V1\AutonomousDatabaseBackup;
    use Google\Cloud\OracleDatabase\V1\Client\OracleDatabaseClient;
    use Google\Cloud\OracleDatabase\V1\ListAutonomousDatabaseBackupsRequest;
    
    /**
     * Lists the long-term and automatic backups of an Autonomous Database.
     *
     * @param string $formattedParent The parent value for ListAutonomousDatabaseBackups in the
     *                                following format: projects/{project}/locations/{location}. Please see
     *                                {@see OracleDatabaseClient::locationName()} for help formatting this field.
     */
    function list_autonomous_database_backups_sample(string $formattedParent): void
    {
        // Create a client.
        $oracleDatabaseClient = new OracleDatabaseClient();
    
        // Prepare the request message.
        $request = (new ListAutonomousDatabaseBackupsRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $oracleDatabaseClient->listAutonomousDatabaseBackups($request);
    
            /** @var AutonomousDatabaseBackup $element */
            foreach ($response as $element) {
                printf('Element data: %s' . PHP_EOL, $element->serializeToJsonString());
            }
        } catch (ApiException $ex) {
            printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
        }
    }
    
    /**
     * Helper to execute the sample.
     *
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function callSample(): void
    {
        $formattedParent = OracleDatabaseClient::locationName('[PROJECT]', '[LOCATION]');
    
        list_autonomous_database_backups_sample($formattedParent);
    }

### Python
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [oracledatabase_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest)
    
    
    def sample_list_autonomous_database_backups():
        # Create a client
        client = [oracledatabase_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest).[OracleDatabaseClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest/google.cloud.oracledatabase_v1.services.oracle_database.OracleDatabaseClient.html)()
    
        # Initialize request argument(s)
        request = [oracledatabase_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest).[ListAutonomousDatabaseBackupsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest/google.cloud.oracledatabase_v1.types.ListAutonomousDatabaseBackupsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_autonomous_database_backups](https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest/google.cloud.oracledatabase_v1.services.oracle_database.OracleDatabaseClient.html#google_cloud_oracledatabase_v1_services_oracle_database_OracleDatabaseClient_list_autonomous_database_backups)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    
    

### Ruby
    
    
    require "google/cloud/oracle_database/v1"
    
    ##
    # Snippet for the list_autonomous_database_backups call in the OracleDatabase service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::OracleDatabase::V1::OracleDatabase::Client#list_autonomous_database_backups.
    #
    def list_autonomous_database_backups
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::OracleDatabase::V1::OracleDatabase::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::OracleDatabase::V1::ListAutonomousDatabaseBackupsRequest.new
    
      # Call the list_autonomous_database_backups method.
      result = client.list_autonomous_database_backups request
    
      # The returned object is of type Gapic::PagedEnumerable. You can iterate
      # over elements, and API calls will be issued to fetch pages as needed.
      result.each do |item|
        # Each element is of type ::Google::Cloud::OracleDatabase::V1::AutonomousDatabaseBackup.
        p item
      end
    end

## What's next

  * [Restore an Autonomous AI Database from backup](https://docs.cloud.google.com/oracle/database/docs/restore-database)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
