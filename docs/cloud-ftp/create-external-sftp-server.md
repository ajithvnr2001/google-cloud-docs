---
url: https://docs.cloud.google.com/cloud-ftp/create-external-sftp-server/
title: Create an external SFTP server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:24:48.491575+00:00
---

# Create an external SFTP server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-ftp/create-external-sftp-server/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud FTP ](https://docs.cloud.google.com/cloud-ftp)
  * [ Guides ](https://docs.cloud.google.com/cloud-ftp/overview)



Send feedback 

#  Create an external SFTP server Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to create an external SFTP server by using Cloud FTP. An external SFTP server can be accessed over the internet. Partners who are outside of your network can use the server to securely transfer files to and from Cloud Storage.

You can restrict access to an external SFTP server based on the IP addresses of your users.

For steps to create an internal server, which can be accessed only within your Virtual Private Cloud (VPC) network, see [Create an internal SFTP server](https://docs.cloud.google.com/cloud-ftp/create-internal-sftp-server). You can't change whether a server is external or internal after the server has been created.

## Before you begin

###  Console 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Cloud FTP API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=ftp.googleapis.com)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Cloud FTP API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=ftp.googleapis.com)

  10. If you want to restrict access to the server based on your users' IP addresses, collect a list of CIDR blocks that are allowed to access the server.



###  gcloud 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. Enable the Cloud FTP API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable ftp.googleapis.com

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  13. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  14. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  15. Enable the Cloud FTP API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable ftp.googleapis.com

  16. If you want to restrict access to the server based on your users' IP addresses, collect a list of CIDR blocks that are allowed to access the server.



### Required roles

To get the permission that you need to create an SFTP server, ask your administrator to grant you the [Cloud FTP Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/ftp#ftp.admin) (`roles/ftp.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `ftp.servers.create` permission, which is required to create an SFTP server. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create an external server

###  Console 

  1. In the Google Cloud console, go to the **Cloud FTP** page. 

[Go to Cloud FTP](https://console.cloud.google.com/transfer/ftp-servers)

  2. Click **Create server**.

  3. On the **Server configuration** tab, enter basic details for the server:

     1. In the **Server ID** field, enter a unique ID for the server.

     2. In the **Region** list, select the [Google Cloud location](https://docs.cloud.google.com/cloud-ftp/locations) for the server.

For the fastest data transfer speeds, create the server in the same location as the Cloud Storage bucket that stores your data. If the bucket's location isn't supported by Cloud FTP, then select the nearest available location.

     3. (Optional) Enter a display name for the server.

     4. Click **Continue**.

  4. On the **Networking and security** tab, configure connectivity for the server:

     1. Select **External (Public IP)**.

     2. In the **Allowed IP ranges** field, provide a CIDR block that is allowed to access the server, and then press `Enter`. For example, `192.0.2.0/24`. You must provide at least one value, and can provide a maximum of 500 CIDR blocks. To allow connections from all IP addresses, use `0.0.0.0/0`.

  5. Click **Create**.

It takes about 10 minutes for the server to be created.




###  gcloud 

To create an external server, run the [`gcloud alpha storage ftp servers create` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/ftp/servers/create) and provide the `--access-type=EXTERNAL` flag.

Before using any of the command data below, make the following replacements: 

  * SERVER_ID: a unique ID for the server. Must start with a lowercase letter, and end with a lowercase letter or number. Can contain lowercase letters, numbers, and hyphens. Can't begin with the prefix `goog` or contain the string `google`, including close misspellings such as `g00gle`. Maximum length is 30 characters.
  * LOCATION_ID: the [Google Cloud location](https://docs.cloud.google.com/cloud-ftp/locations) of the server, such as `us-west1`.

For the fastest data transfer speeds, create the server in the same location as the Cloud Storage bucket that stores your data. If the bucket's location isn't supported by Cloud FTP, then select the nearest available location.

  * CIDR_BLOCK: a CIDR block that is allowed to access the server. For example, `192.0.2.0/24`. You must provide at least one value, and can provide a maximum of 500 CIDR blocks in a comma-separated list. To allow connections from all IP addresses, use `0.0.0.0/0`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud alpha storage ftp servers create SERVER_ID --access-type=EXTERNAL \
        --location=LOCATION_ID --allowed-cidr-blocks=CIDR_BLOCK

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud alpha storage ftp servers create SERVER_ID --access-type=EXTERNAL `
        --location=LOCATION_ID --allowed-cidr-blocks=CIDR_BLOCK

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud alpha storage ftp servers create SERVER_ID --access-type=EXTERNAL ^
        --location=LOCATION_ID --allowed-cidr-blocks=CIDR_BLOCK

It takes about 10 minutes for the server to be created.

###  REST 

To create an external server, use the [`servers.create` method](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers/create) and provide an `externalConfig` access configuration.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID of the server.
  * LOCATION_ID: the [Google Cloud location](https://docs.cloud.google.com/cloud-ftp/locations) of the server, such as `us-west1`.

For the fastest data transfer speeds, create the server in the same location as the Cloud Storage bucket that stores your data. If the bucket's location isn't supported by Cloud FTP, then select the nearest available location.

  * SERVER_ID: a unique ID for the server. Must start with a lowercase letter, and end with a lowercase letter or number. Can contain lowercase letters, numbers, and hyphens. Can't begin with the prefix `goog` or contain the string `google`, including close misspellings such as `g00gle`. Maximum length is 30 characters.
  * CIDR_BLOCK: a CIDR block that is allowed to access the server. For example, `192.0.2.0/24`. You must provide at least one value, and can provide a maximum of 500 CIDR blocks . To allow connections from all IP addresses, use `0.0.0.0/0`.



HTTP method and URL: 
    
    
    POST https://ftp.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/servers?serverId=SERVER_ID

Request JSON body: 
    
    
    {
      "accessType": "EXTERNAL",
      "externalConfig": {
        "allowedCidrBlocks": [
          "CIDR_BLOCK"
          ]
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://ftp.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/servers?serverId=SERVER_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://ftp.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/servers?serverId=SERVER_ID" | Select-Object -Expand Content

The response identifies a [long-running operation](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.operations). 

It takes about 10 minutes for the server to be created.

###  Client libraries 

To create an external server, set the access type to external and provide an external access configuration.

### C#

To learn how to install and use the client library for Cloud FTP, see [Cloud FTP client libraries](https://docs.cloud.google.com/cloud-ftp/reference/libraries). For more information, see the [Cloud FTP C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest). 

To authenticate to Cloud FTP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Ftp.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using System.Threading.Tasks;
    
    public sealed partial class GeneratedCloudFtpClientSnippets
    {
        /// <summary>Snippet for CreateServerAsync</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public async Task CreateServerAsync()
        {
            // Create client
            [CloudFtpClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.CloudFtpClient.html) cloudFtpClient = await [CloudFtpClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.CloudFtpClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.CloudFtpClient.html#Google_Cloud_Ftp_V1_CloudFtpClient_CreateAsync_System_Threading_CancellationToken_)();
            // Initialize request argument(s)
            string parent = "projects/[PROJECT]/locations/[LOCATION]";
            [Server](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.Server.html) server = new [Server](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.Server.html)();
            string serverId = "";
            // Make the request
            Operation<Server, OperationMetadata> response = await cloudFtpClient.[CreateServerAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.CloudFtpClient.html#Google_Cloud_Ftp_V1_CloudFtpClient_CreateServerAsync_Google_Api_Gax_ResourceNames_LocationName_Google_Cloud_Ftp_V1_Server_System_String_Google_Api_Gax_Grpc_CallSettings_)(parent, server, serverId);
    
            // Poll until the returned long-running operation is complete
            Operation<Server, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
            // Retrieve the operation result
            [Server](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.Server.html) result = completedResponse.Result;
    
            // Or get the name of the operation
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name
            Operation<Server, OperationMetadata> retrievedResponse = await cloudFtpClient.[PollOnceCreateServerAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.CloudFtpClient.html#Google_Cloud_Ftp_V1_CloudFtpClient_PollOnceCreateServerAsync_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
            // Check if the retrieved long-running operation has completed
            if (retrievedResponse.IsCompleted)
            {
                // If it has completed, then access the result
                [Server](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.Server.html) retrievedResult = retrievedResponse.Result;
            }
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
    
    	req := &ftppb.CreateServerRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ftp/apiv1/ftppb#CreateServerRequest.
    	}
    	op, err := c.CreateServer(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	resp, err := op.Wait(ctx)
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
    import com.google.cloud.ftp.v1.[CreateServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.CreateServerRequest.html);
    import com.google.cloud.ftp.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.LocationName.html);
    import com.google.cloud.ftp.v1.[Server](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.Server.html);
    import com.google.longrunning.[Operation](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html);
    
    public class AsyncCreateServer {
    
      public static void main(String[] args) throws Exception {
        asyncCreateServer();
      }
    
      public static void asyncCreateServer() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([CloudFtpClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.CloudFtpClient.html) cloudFtpClient = [CloudFtpClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.CloudFtpClient.html).create()) {
          [CreateServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.CreateServerRequest.html) request =
              [CreateServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.CreateServerRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.LocationName.html).of("[PROJECT]", "[LOCATION]").toString())
                  .[setServerId](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.CreateServerRequest.Builder.html#com_google_cloud_ftp_v1_CreateServerRequest_Builder_setServerId_java_lang_String_)("serverId1379103678")
                  .setServer([Server](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.Server.html).newBuilder().build())
                  .setRequestId("requestId693933066")
                  .build();
          ApiFuture<Operation> future = cloudFtpClient.[createServerCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.CloudFtpClient.html#com_google_cloud_ftp_v1_CloudFtpClient_createServerCallable__)().futureCall(request);
          // Do something.
          [Operation](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html) response = future.get();
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
     *  Required. Value for parent.
     */
    // const parent = 'abc123'
    /**
     *  Required. A unique ID for the server. Must start with a lowercase letter,
     *  and end with a lowercase letter or number. Can contain lowercase letters,
     *  numbers, and hyphens. Maximum length is 30 characters.
     */
    // const serverId = 'abc123'
    /**
     *  Required. The resource being created
     */
    // const server = {}
    /**
     *  Optional. An optional request ID to identify requests. Specify a unique
     *  request ID so that if you must retry your request, the server will know to
     *  ignore the request if it has already been completed. The server will
     *  guarantee that for at least 60 minutes since the first request.
     *  For example, consider a situation where you make an initial request and the
     *  request times out. If you make the request again with the same request
     *  ID, the server can check if original operation with the same request ID
     *  was received, and if so, will ignore the second request. This prevents
     *  clients from accidentally creating duplicate commitments.
     *  The request ID must be a valid UUID with the exception that zero UUID is
     *  not supported (00000000-0000-0000-0000-000000000000).
     */
    // const requestId = 'abc123'
    
    // Imports the Ftp library
    const {CloudFtpClient} = require('[@google-cloud/ftp](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/overview.html)').v1;
    
    // Instantiates a client
    const ftpClient = new [CloudFtpClient](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/overview.html)();
    
    async function callCreateServer() {
      // Construct request
      const request = {
        parent,
        serverId,
        server,
      };
    
      // Run request
      const [operation] = await ftpClient.createServer(request);
      const [response] = await operation.promise();
      console.log(response);
    }
    
    callCreateServer();

### PHP

To learn how to install and use the client library for Cloud FTP, see [Cloud FTP client libraries](https://docs.cloud.google.com/cloud-ftp/reference/libraries). For more information, see the [Cloud FTP PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-ftp/latest). 

To authenticate to Cloud FTP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Ftp\V1\Client\CloudFtpClient;
    use Google\Cloud\Ftp\V1\CreateServerRequest;
    use Google\Cloud\Ftp\V1\Server;
    use Google\Cloud\Ftp\V1\Server\AccessType;
    use Google\Rpc\Status;
    
    /**
     * Creates a new Server in a given project and location.
     *
     * @param string $formattedParent  Value for parent. Please see
     *                                 {@see CloudFtpClient::locationName()} for help formatting this field.
     * @param string $serverId         A unique ID for the server. Must start with a lowercase letter,
     *                                 and end with a lowercase letter or number. Can contain lowercase letters,
     *                                 numbers, and hyphens. Maximum length is 30 characters.
     * @param int    $serverAccessType The access type of the Server.
     */
    function create_server_sample(
        string $formattedParent,
        string $serverId,
        int $serverAccessType
    ): void {
        // Create a client.
        $cloudFtpClient = new CloudFtpClient();
    
        // Prepare the request message.
        $server = (new Server())
            ->setAccessType($serverAccessType);
        $request = (new CreateServerRequest())
            ->setParent($formattedParent)
            ->setServerId($serverId)
            ->setServer($server);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $cloudFtpClient->createServer($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var Server $result */
                $result = $response->getResult();
                printf('Operation successful with response data: %s' . PHP_EOL, $result->serializeToJsonString());
            } else {
                /** @var Status $error */
                $error = $response->getError();
                printf('Operation failed with error data: %s' . PHP_EOL, $error->serializeToJsonString());
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
        $formattedParent = CloudFtpClient::locationName('[PROJECT]', '[LOCATION]');
        $serverId = '[SERVER_ID]';
        $serverAccessType = AccessType::ACCESS_TYPE_UNSPECIFIED;
    
        create_server_sample($formattedParent, $serverId, $serverAccessType);
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
    
    
    def sample_create_server():
        # Create a client
        client = [ftp_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest).[CloudFtpClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.services.cloud_ftp.CloudFtpClient.html)()
    
        # Initialize request argument(s)
        server = [ftp_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest).[Server](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.Server.html)()
        server.access_type = "INTERNAL"
    
        request = [ftp_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest).[CreateServerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.CreateServerRequest.html)(
            parent="parent_value",
            server_id="server_id_value",
            server=server,
        )
    
        # Make the request
        operation = client.[create_server](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.services.cloud_ftp.CloudFtpClient.html#google_cloud_ftp_v1_services_cloud_ftp_CloudFtpClient_create_server)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    
    

### Ruby

To learn how to install and use the client library for Cloud FTP, see [Cloud FTP client libraries](https://docs.cloud.google.com/cloud-ftp/reference/libraries). For more information, see the [Cloud FTP Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ftp/latest). 

To authenticate to Cloud FTP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/ftp/v1"
    
    ##
    # Snippet for the create_server call in the CloudFtp service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::Ftp::V1::CloudFtp::Rest::Client#create_server.
    #
    def create_server
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::Ftp::V1::CloudFtp::Rest::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::Ftp::V1::CreateServerRequest.new
    
      # Call the create_server method.
      result = client.create_server request
    
      # The returned object is of type Gapic::Operation. You can use it to
      # check the status of an operation, cancel it, or wait for results.
      # Here is how to wait for a response.
      result.wait_until_done! timeout: 60
      if result.response?
        p result.response
      else
        puts "No response received."
      end
    end

## What's next

  * [Add users to the server](https://docs.cloud.google.com/cloud-ftp/add-sftp-users)
  * [Connect to an external server](https://docs.cloud.google.com/cloud-ftp/connect-to-external-server)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
