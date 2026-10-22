---
url: https://docs.cloud.google.com/cloud-ftp/get-user-information/
title: Get SFTP user information \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:32.568818+00:00
---

# Get SFTP user information  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-ftp/get-user-information/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud FTP ](https://docs.cloud.google.com/cloud-ftp)
  * [ Guides ](https://docs.cloud.google.com/cloud-ftp/overview)



Send feedback 

#  Get SFTP user information Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to get information about your Cloud FTP users. You can list all users for a server. You can also get detailed information about a specific user, such as the user's Cloud Storage directory mappings and permissions.

## Required roles

To get the permissions that you need to get information about SFTP users, ask your administrator to grant you the [Cloud FTP Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/ftp#ftp.viewer) (`roles/ftp.viewer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to get information about SFTP users. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to get information about SFTP users:

  * List users: `ftp.users.list`
  * Get user details: `ftp.users.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## List users

###  gcloud 

To list SFTP users for a server, run the [`gcloud alpha storage ftp users list` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/ftp/users/list).

Before using any of the command data below, make the following replacements: 

  * LOCATION_ID: the [location](https://docs.cloud.google.com/cloud-ftp/locations) of the server, such as `us-west1`.
  * SERVER_ID: the server ID.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud alpha storage ftp users list --location=LOCATION_ID --server=SERVER_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud alpha storage ftp users list --location=LOCATION_ID --server=SERVER_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud alpha storage ftp users list --location=LOCATION_ID --server=SERVER_ID

###  REST 

To list SFTP users for a server, use the [`servers.users.list` method](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers.users/list).

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID.
  * LOCATION_ID: the [location](https://docs.cloud.google.com/cloud-ftp/locations) of the server, such as `us-west1`.
  * SERVER_ID: the server ID.



HTTP method and URL: 
    
    
    GET https://ftp.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/servers/SERVER_ID/users

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://ftp.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/servers/SERVER_ID/users"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://ftp.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/servers/SERVER_ID/users" | Select-Object -Expand Content

The response body is a JSON object with a list of [`User` resources](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers.users#User).

###  Client libraries 

### C#

To learn how to install and use the client library for Cloud FTP, see [Cloud FTP client libraries](https://docs.cloud.google.com/cloud-ftp/reference/libraries). For more information, see the [Cloud FTP C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest). 

To authenticate to Cloud FTP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using [Google.Cloud.Ftp.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.html);
    using System;
    using System.Threading.Tasks;
    
    public sealed partial class GeneratedCloudFtpClientSnippets
    {
        /// <summary>Snippet for ListUsersAsync</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public async Task ListUsersAsync()
        {
            // Create client
            [CloudFtpClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.CloudFtpClient.html) cloudFtpClient = await [CloudFtpClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.CloudFtpClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.CloudFtpClient.html#Google_Cloud_Ftp_V1_CloudFtpClient_CreateAsync_System_Threading_CancellationToken_)();
            // Initialize request argument(s)
            string parent = "projects/[PROJECT]/locations/[LOCATION]/servers/[SERVER]";
            // Make the request
            PagedAsyncEnumerable<ListUsersResponse, User> response = cloudFtpClient.[ListUsersAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.CloudFtpClient.html#Google_Cloud_Ftp_V1_CloudFtpClient_ListUsersAsync_Google_Cloud_Ftp_V1_ListUsersRequest_Google_Api_Gax_Grpc_CallSettings_)(parent);
    
            // Iterate over all response items, lazily performing RPCs as required
            await foreach ([User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.User.html) item in response)
            {
                // Do something with each item
                Console.WriteLine(item);
            }
    
            // Or iterate over pages (of server-defined size), performing one RPC per page
            await foreach ([ListUsersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ListUsersResponse.html) page in response.AsRawResponses())
            {
                // Do something with each page of items
                Console.WriteLine("A page of results:");
                foreach ([User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.User.html) item in page)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
            }
    
            // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
            int pageSize = 10;
            Page<User> singlePage = await response.ReadPageAsync(pageSize);
            // Do something with the page of items
            Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
            foreach ([User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.User.html) item in singlePage)
            {
                // Do something with each item
                Console.WriteLine(item);
            }
            // Store the pageToken, for when the next page is required.
            string nextPageToken = singlePage.NextPageToken;
        }
    }

### Go

To learn how to install and use the client library for Cloud FTP, see [Cloud FTP client libraries](https://docs.cloud.google.com/cloud-ftp/reference/libraries). For more information, see the [Cloud FTP Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ftp/latest/apiv1). 

To authenticate to Cloud FTP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	ftp "cloud.google.com/go/ftp/apiv1"
    	ftppb "cloud.google.com/go/ftp/apiv1/ftppb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := ftp.[NewCloudFtpRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ftp/latest/apiv1.html#cloud_google_com_go_ftp_apiv1_CloudFtpClient_NewCloudFtpRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ftp/latest/apiv1.html#cloud_google_com_go_ftp_apiv1_CloudFtpClient_Close)()
    
    	req := &ftppb.ListUsersRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ftp/apiv1/ftppb#ListUsersRequest.
    	}
    	it := c.ListUsers(ctx, req)
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
    		_ = it.Response.(*ftppb.ListUsersResponse)
    	}
    }
    

### Java

To learn how to install and use the client library for Cloud FTP, see [Cloud FTP client libraries](https://docs.cloud.google.com/cloud-ftp/reference/libraries). For more information, see the [Cloud FTP Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/overview). 

To authenticate to Cloud FTP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.cloud.ftp.v1.[CloudFtpClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.CloudFtpClient.html);
    import com.google.cloud.ftp.v1.[ListUsersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.ListUsersRequest.html);
    import com.google.cloud.ftp.v1.[ServerName](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.ServerName.html);
    import com.google.cloud.ftp.v1.[User](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.User.html);
    import com.google.cloud.ftp.v1.[UserView](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.UserView.html);
    
    public class AsyncListUsers {
    
      public static void main(String[] args) throws Exception {
        asyncListUsers();
      }
    
      public static void asyncListUsers() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([CloudFtpClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.CloudFtpClient.html) cloudFtpClient = [CloudFtpClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.CloudFtpClient.html).create()) {
          [ListUsersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.ListUsersRequest.html) request =
              [ListUsersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.ListUsersRequest.html).newBuilder()
                  .setParent([ServerName](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.ServerName.html).of("[PROJECT]", "[LOCATION]", "[SERVER]").toString())
                  .setPageSize(883849137)
                  .setPageToken("pageToken873572522")
                  .setFilter("filter-1274492040")
                  .setOrderBy("orderBy-1207110587")
                  .setView([UserView](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.UserView.html).forNumber(0))
                  .build();
          ApiFuture<User> future = cloudFtpClient.[listUsersPagedCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.CloudFtpClient.html#com_google_cloud_ftp_v1_CloudFtpClient_listUsersPagedCallable__)().futureCall(request);
          // Do something.
          for ([User](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.User.html) element : future.get().iterateAll()) {
            // doThingsWith(element);
          }
        }
      }
    }

### Node.js

To learn how to install and use the client library for Cloud FTP, see [Cloud FTP client libraries](https://docs.cloud.google.com/cloud-ftp/reference/libraries). For more information, see the [Cloud FTP Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest). 

To authenticate to Cloud FTP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. Parent value for ListUsersRequest
     */
    // const parent = 'abc123'
    /**
     *  Optional. Requested page size. User may return fewer items than requested.
     *  The maximum value is 1000; The default value is 50 if the field is omitted
     *  (or set to 0).
     */
    // const pageSize = 1234
    /**
     *  Optional. A token identifying a page of results the user should return.
     */
    // const pageToken = 'abc123'
    /**
     *  Optional. Filtering results
     */
    // const filter = 'abc123'
    /**
     *  Optional. Hint for how to order the results
     */
    // const orderBy = 'abc123'
    /**
     *  Optional. The view of the User resource to return.
     */
    // const view = {}
    
    // Imports the Ftp library
    const {CloudFtpClient} = require('[@google-cloud/ftp](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/overview.html)').v1;
    
    // Instantiates a client
    const ftpClient = new [CloudFtpClient](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/overview.html)();
    
    async function callListUsers() {
      // Construct request
      const request = {
        parent,
      };
    
      // Run request
      const iterable = ftpClient.[listUsersAsync](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/v1.cloudftpclient.html)(request);
      for await (const response of iterable) {
          console.log(response);
      }
    }
    
    callListUsers();

### PHP

To learn how to install and use the client library for Cloud FTP, see [Cloud FTP client libraries](https://docs.cloud.google.com/cloud-ftp/reference/libraries). For more information, see the [Cloud FTP PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-ftp/latest). 

To authenticate to Cloud FTP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    use Google\Cloud\Ftp\V1\Client\CloudFtpClient;
    use Google\Cloud\Ftp\V1\ListUsersRequest;
    
    /**
     * Lists Users in a given project and location.
     *
     * @param string $formattedParent Parent value for ListUsersRequest
     *                                Please see {@see CloudFtpClient::serverName()} for help formatting this field.
     */
    function list_users_sample(string $formattedParent): void
    {
        // Create a client.
        $cloudFtpClient = new CloudFtpClient();
    
        // Prepare the request message.
        $request = (new ListUsersRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $cloudFtpClient->listUsers($request);
    
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
        $formattedParent = CloudFtpClient::serverName('[PROJECT]', '[LOCATION]', '[SERVER]');
    
        list_users_sample($formattedParent);
    }

### Python

To learn how to install and use the client library for Cloud FTP, see [Cloud FTP client libraries](https://docs.cloud.google.com/cloud-ftp/reference/libraries). For more information, see the [Cloud FTP Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest). 

To authenticate to Cloud FTP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [ftp_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest)
    
    
    def sample_list_users():
        # Create a client
        client = [ftp_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest).[CloudFtpClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.services.cloud_ftp.CloudFtpClient.html)()
    
        # Initialize request argument(s)
        request = [ftp_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest).[ListUsersRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.ListUsersRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_users](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.services.cloud_ftp.CloudFtpClient.html#google_cloud_ftp_v1_services_cloud_ftp_CloudFtpClient_list_users)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    
    

### Ruby

To learn how to install and use the client library for Cloud FTP, see [Cloud FTP client libraries](https://docs.cloud.google.com/cloud-ftp/reference/libraries). For more information, see the [Cloud FTP Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ftp/latest). 

To authenticate to Cloud FTP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/ftp/v1"
    
    ##
    # Snippet for the list_users call in the CloudFtp service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::Ftp::V1::CloudFtp::Rest::Client#list_users.
    #
    def list_users
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::Ftp::V1::CloudFtp::Rest::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::Ftp::V1::ListUsersRequest.new
    
      # Call the list_users method.
      result = client.list_users request
    
      # The returned object is of type Gapic::PagedEnumerable. You can iterate
      # over elements, and API calls will be issued to fetch pages as needed.
      result.each do |item|
        # Each element is of type ::Google::Cloud::Ftp::V1::User.
        p item
      end
    end

## Get details about a user

To get detailed information about a specific user, such as the user's Cloud Storage directory mappings and permissions, the email address of the service account that accesses Cloud Storage resources on behalf of the user, and the user's credentials, use the following steps.

###  gcloud 

To get details about an SFTP user, run the [`gcloud alpha storage ftp users describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/ftp/users/describe).

Before using any of the command data below, make the following replacements: 

  * USERNAME: the SFTP user's username.
  * LOCATION_ID: the [location](https://docs.cloud.google.com/cloud-ftp/locations) of the server, such as `us-west1`.
  * SERVER_ID: the SFTP server ID.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud alpha storage ftp users describe USERNAME --location=LOCATION_ID \
        --server=SERVER_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud alpha storage ftp users describe USERNAME --location=LOCATION_ID `
        --server=SERVER_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud alpha storage ftp users describe USERNAME --location=LOCATION_ID ^
        --server=SERVER_ID

###  REST 

To get details about an SFTP user, use the [`servers.users.get` method](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers.users/get).

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID.
  * LOCATION_ID: the [location](https://docs.cloud.google.com/cloud-ftp/locations) of the server, such as `us-west1`.
  * SERVER_ID: the SFTP server ID.
  * USERNAME: the SFTP user's username.



HTTP method and URL: 
    
    
    GET https://ftp.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/servers/SERVER_ID/users/USERNAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://ftp.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/servers/SERVER_ID/users/USERNAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://ftp.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/servers/SERVER_ID/users/USERNAME" | Select-Object -Expand Content

The response body is a [`User` resource](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers.users#User). 

###  Client libraries 

### C#

To learn how to install and use the client library for Cloud FTP, see [Cloud FTP client libraries](https://docs.cloud.google.com/cloud-ftp/reference/libraries). For more information, see the [Cloud FTP C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest). 

To authenticate to Cloud FTP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Ftp.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.html);
    using System.Threading.Tasks;
    
    public sealed partial class GeneratedCloudFtpClientSnippets
    {
        /// <summary>Snippet for GetUserAsync</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public async Task GetUserAsync()
        {
            // Create client
            [CloudFtpClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.CloudFtpClient.html) cloudFtpClient = await [CloudFtpClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.CloudFtpClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.CloudFtpClient.html#Google_Cloud_Ftp_V1_CloudFtpClient_CreateAsync_System_Threading_CancellationToken_)();
            // Initialize request argument(s)
            string name = "projects/[PROJECT]/locations/[LOCATION]/servers/[SERVER]/users/[USER]";
            // Make the request
            [User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.User.html) response = await cloudFtpClient.[GetUserAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.CloudFtpClient.html#Google_Cloud_Ftp_V1_CloudFtpClient_GetUserAsync_Google_Cloud_Ftp_V1_GetUserRequest_Google_Api_Gax_Grpc_CallSettings_)(name);
        }
    }

### Go

To learn how to install and use the client library for Cloud FTP, see [Cloud FTP client libraries](https://docs.cloud.google.com/cloud-ftp/reference/libraries). For more information, see the [Cloud FTP Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ftp/latest/apiv1). 

To authenticate to Cloud FTP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	ftp "cloud.google.com/go/ftp/apiv1"
    	ftppb "cloud.google.com/go/ftp/apiv1/ftppb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := ftp.[NewCloudFtpRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ftp/latest/apiv1.html#cloud_google_com_go_ftp_apiv1_CloudFtpClient_NewCloudFtpRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ftp/latest/apiv1.html#cloud_google_com_go_ftp_apiv1_CloudFtpClient_Close)()
    
    	req := &ftppb.GetUserRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ftp/apiv1/ftppb#GetUserRequest.
    	}
    	resp, err := c.GetUser(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### Java

To learn how to install and use the client library for Cloud FTP, see [Cloud FTP client libraries](https://docs.cloud.google.com/cloud-ftp/reference/libraries). For more information, see the [Cloud FTP Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/overview). 

To authenticate to Cloud FTP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.cloud.ftp.v1.[CloudFtpClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.CloudFtpClient.html);
    import com.google.cloud.ftp.v1.[GetUserRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.GetUserRequest.html);
    import com.google.cloud.ftp.v1.[User](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.User.html);
    import com.google.cloud.ftp.v1.[UserName](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.UserName.html);
    import com.google.cloud.ftp.v1.[UserView](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.UserView.html);
    
    public class AsyncGetUser {
    
      public static void main(String[] args) throws Exception {
        asyncGetUser();
      }
    
      public static void asyncGetUser() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([CloudFtpClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.CloudFtpClient.html) cloudFtpClient = [CloudFtpClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.CloudFtpClient.html).create()) {
          [GetUserRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.GetUserRequest.html) request =
              [GetUserRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.GetUserRequest.html).newBuilder()
                  .setName([UserName](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.UserName.html).of("[PROJECT]", "[LOCATION]", "[SERVER]", "[USER]").toString())
                  .setView([UserView](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.UserView.html).forNumber(0))
                  .build();
          ApiFuture<User> future = cloudFtpClient.[getUserCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.CloudFtpClient.html#com_google_cloud_ftp_v1_CloudFtpClient_getUserCallable__)().futureCall(request);
          // Do something.
          [User](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.User.html) response = future.get();
        }
      }
    }

### Node.js

To learn how to install and use the client library for Cloud FTP, see [Cloud FTP client libraries](https://docs.cloud.google.com/cloud-ftp/reference/libraries). For more information, see the [Cloud FTP Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest). 

To authenticate to Cloud FTP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. Name of the resource
     */
    // const name = 'abc123'
    /**
     *  Optional. The view of the User resource to return.
     */
    // const view = {}
    
    // Imports the Ftp library
    const {CloudFtpClient} = require('[@google-cloud/ftp](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/overview.html)').v1;
    
    // Instantiates a client
    const ftpClient = new [CloudFtpClient](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/overview.html)();
    
    async function callGetUser() {
      // Construct request
      const request = {
        name,
      };
    
      // Run request
      const response = await ftpClient.getUser(request);
      console.log(response);
    }
    
    callGetUser();

### PHP

To learn how to install and use the client library for Cloud FTP, see [Cloud FTP client libraries](https://docs.cloud.google.com/cloud-ftp/reference/libraries). For more information, see the [Cloud FTP PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-ftp/latest). 

To authenticate to Cloud FTP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Ftp\V1\Client\CloudFtpClient;
    use Google\Cloud\Ftp\V1\GetUserRequest;
    use Google\Cloud\Ftp\V1\User;
    
    /**
     * Gets details of a single User.
     *
     * @param string $formattedName Name of the resource
     *                              Please see {@see CloudFtpClient::userName()} for help formatting this field.
     */
    function get_user_sample(string $formattedName): void
    {
        // Create a client.
        $cloudFtpClient = new CloudFtpClient();
    
        // Prepare the request message.
        $request = (new GetUserRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var User $response */
            $response = $cloudFtpClient->getUser($request);
            printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
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
        $formattedName = CloudFtpClient::userName('[PROJECT]', '[LOCATION]', '[SERVER]', '[USER]');
    
        get_user_sample($formattedName);
    }

### Python

To learn how to install and use the client library for Cloud FTP, see [Cloud FTP client libraries](https://docs.cloud.google.com/cloud-ftp/reference/libraries). For more information, see the [Cloud FTP Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest). 

To authenticate to Cloud FTP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [ftp_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest)
    
    
    def sample_get_user():
        # Create a client
        client = [ftp_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest).[CloudFtpClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.services.cloud_ftp.CloudFtpClient.html)()
    
        # Initialize request argument(s)
        request = [ftp_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest).[GetUserRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.GetUserRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_user](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.services.cloud_ftp.CloudFtpClient.html#google_cloud_ftp_v1_services_cloud_ftp_CloudFtpClient_get_user)(request=request)
    
        # Handle the response
        print(response)
    
    

### Ruby

To learn how to install and use the client library for Cloud FTP, see [Cloud FTP client libraries](https://docs.cloud.google.com/cloud-ftp/reference/libraries). For more information, see the [Cloud FTP Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ftp/latest). 

To authenticate to Cloud FTP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/ftp/v1"
    
    ##
    # Snippet for the get_user call in the CloudFtp service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::Ftp::V1::CloudFtp::Rest::Client#get_user.
    #
    def get_user
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::Ftp::V1::CloudFtp::Rest::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::Ftp::V1::GetUserRequest.new
    
      # Call the get_user method.
      result = client.get_user request
    
      # The returned object is of type Google::Cloud::Ftp::V1::User.
      p result
    end

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
