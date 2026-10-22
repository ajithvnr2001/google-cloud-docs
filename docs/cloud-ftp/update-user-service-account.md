---
url: https://docs.cloud.google.com/cloud-ftp/update-user-service-account/
title: Update the service account for an SFTP user \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:31.286631+00:00
---

# Update the service account for an SFTP user  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-ftp/update-user-service-account/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud FTP ](https://docs.cloud.google.com/cloud-ftp)
  * [ Guides ](https://docs.cloud.google.com/cloud-ftp/overview)



Send feedback 

#  Update the service account for an SFTP user Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to update the service account for a Cloud FTP user. The service account accesses Cloud Storage resources on behalf of the user.

At a high level, these are the steps to update the service account for a user:

  1. Configure a service account with the appropriate IAM roles.
  2. Update the service account that's attached to the user.



We recommend that you use a dedicated service account for each user so that you can manage SFTP access separately for each user.

## Required roles

To get the permission that you need to update SFTP users, ask your administrator to grant you the [FTP Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/ftp#ftp.admin) (`roles/ftp.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `ftp.users.update` permission, which is required to update SFTP users. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Configure a service account

  1. Create a service account for the user, if a service account doesn't already exist.
         
         gcloud iam service-accounts create USERNAME-sa \
             --description="USERNAME SFTP Service Account" \
             --display-name="USERNAME SFTP Service Account"

Replace `USERNAME` with a unique username for the SFTP user. The username must start with a lowercase letter and can include lowercase letters, numbers, or hyphens.

On success, a message like `Created service account [example-userid-sa]` is displayed.

  2. Grant yourself the Service Account User (`roles/iam.serviceAccountUser`) role:
         
         gcloud iam service-accounts add-iam-policy-binding USERNAME-sa@PROJECT_ID.iam.gserviceaccount.com \
             --member="user:ADMINISTRATOR_EMAIL" \
             --role="roles/iam.serviceAccountUser"

Replace `ADMINISTRATOR_EMAIL` with the email address of the principal who is updating the SFTP user. If you're updating the user (as opposed to an application), then this value is the email address that you use to access Google Cloud.

On success, a message like the following is displayed:
         
         Updated IAM policy for serviceAccount [example-userid-sa@example-project.iam.gserviceaccount.com].
         bindings:
         - members:
         - user:admin@example.com
         role: roles/iam.serviceAccountUser
         etag: BwZJk7OiSzw=
         version: 1
         

  3. Grant the user's service account the IAM role that's necessary to access the bucket:
         
         gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
             --member="serviceAccount:USERNAME-sa@PROJECT_ID.iam.gserviceaccount.com" \
             --role="ROLE"

Replace `ROLE` with one of the following IAM roles:

     * For read-only access, use the `roles/storage.objectViewer` role.
     * For read and write access, use the `roles/storage.objectAdmin` role.

Repeat this step for each bucket that the user needs to access.

  4. Authorize the Cloud FTP Service Agent to generate tokens for the user's service account:

     1. Get the email address of the SFTP server's service agent. For steps, see [Get details about a server](https://docs.cloud.google.com/cloud-ftp/get-server-information#get-server).

     2. Authorize the Cloud FTP Service Agent:
            
            gcloud iam service-accounts add-iam-policy-binding USERNAME-sa@PROJECT_ID.iam.gserviceaccount.com \
                --member="serviceAccount:SERVICE_AGENT_EMAIL" \
                --role="roles/iam.serviceAccountTokenCreator"

Replace `SERVICE_AGENT_EMAIL` with the service agent's email address.




Next, update the user's service account.

## Update a user's service account

###  gcloud 

To update the service account that's attached to an SFTP user, run the [`gcloud alpha storage ftp users update` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/ftp/users/update).

Before using any of the command data below, make the following replacements: 

  * USERNAME: the SFTP user's username.
  * LOCATION_ID: the [location](https://docs.cloud.google.com/cloud-ftp/locations) of the server, such as `us-west1`.
  * SERVER_ID: the server ID.
  * SERVICE_ACCOUNT: the user's service account. For example, `username-sa@example-project.iam.gserviceaccount.com`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud alpha storage ftp users update USERNAME --location=LOCATION_ID \
        --server=SERVER_ID --customer-service-account=SERVICE_ACCOUNT

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud alpha storage ftp users update USERNAME --location=LOCATION_ID `
        --server=SERVER_ID --customer-service-account=SERVICE_ACCOUNT

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud alpha storage ftp users update USERNAME --location=LOCATION_ID ^
        --server=SERVER_ID --customer-service-account=SERVICE_ACCOUNT

It takes a few seconds for the user to be updated. 

###  REST 

To update the service account that's attached to an SFTP user, use the [`servers.users.patch` method](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers.users/patch). In the `updateMask` query parameter, provide the `customerServiceAccount` field.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID of the server.
  * LOCATION_ID: the [location](https://docs.cloud.google.com/cloud-ftp/locations) of the server, such as `us-west1`.
  * SERVER_ID: the server ID.
  * USERNAME: the SFTP user's username.
  * SERVICE_ACCOUNT: the user's service account. For example, `username-sa@example-project.iam.gserviceaccount.com`.



HTTP method and URL: 
    
    
    PATCH https://ftp.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/servers/SERVER_ID/users/USERNAME?updateMask=customerServiceAccount

Request JSON body: 
    
    
    {
      "customerServiceAccount": "SERVICE_ACCOUNT"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://ftp.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/servers/SERVER_ID/users/USERNAME?updateMask=customerServiceAccount"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://ftp.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/servers/SERVER_ID/users/USERNAME?updateMask=customerServiceAccount" | Select-Object -Expand Content

The response identifies a [long-running operation](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.operations). It takes a few seconds for the user to be updated. 

###  Client libraries 

### C#

To learn how to install and use the client library for Cloud FTP, see [Cloud FTP client libraries](https://docs.cloud.google.com/cloud-ftp/reference/libraries). For more information, see the [Cloud FTP C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest). 

To authenticate to Cloud FTP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Ftp.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System.Threading.Tasks;
    
    public sealed partial class GeneratedCloudFtpClientSnippets
    {
        /// <summary>Snippet for UpdateUserAsync</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public async Task UpdateUserAsync()
        {
            // Create client
            [CloudFtpClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.CloudFtpClient.html) cloudFtpClient = await [CloudFtpClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.CloudFtpClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.CloudFtpClient.html#Google_Cloud_Ftp_V1_CloudFtpClient_CreateAsync_System_Threading_CancellationToken_)();
            // Initialize request argument(s)
            [User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.User.html) user = new [User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.User.html)();
            [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html) updateMask = new [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)();
            // Make the request
            Operation<User, OperationMetadata> response = await cloudFtpClient.[UpdateUserAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.CloudFtpClient.html#Google_Cloud_Ftp_V1_CloudFtpClient_UpdateUserAsync_Google_Cloud_Ftp_V1_UpdateUserRequest_Google_Api_Gax_Grpc_CallSettings_)(user, updateMask);
    
            // Poll until the returned long-running operation is complete
            Operation<User, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
            // Retrieve the operation result
            [User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.User.html) result = completedResponse.Result;
    
            // Or get the name of the operation
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name
            Operation<User, OperationMetadata> retrievedResponse = await cloudFtpClient.[PollOnceUpdateUserAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.CloudFtpClient.html#Google_Cloud_Ftp_V1_CloudFtpClient_PollOnceUpdateUserAsync_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
            // Check if the retrieved long-running operation has completed
            if (retrievedResponse.IsCompleted)
            {
                // If it has completed, then access the result
                [User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.User.html) retrievedResult = retrievedResponse.Result;
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
    
    	req := &ftppb.UpdateUserRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ftp/apiv1/ftppb#UpdateUserRequest.
    	}
    	op, err := c.UpdateUser(ctx, req)
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
    import com.google.cloud.ftp.v1.[UpdateUserRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.UpdateUserRequest.html);
    import com.google.cloud.ftp.v1.[User](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.User.html);
    import com.google.longrunning.[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    
    public class AsyncUpdateUser {
    
      public static void main(String[] args) throws Exception {
        asyncUpdateUser();
      }
    
      public static void asyncUpdateUser() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([CloudFtpClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.CloudFtpClient.html) cloudFtpClient = [CloudFtpClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.CloudFtpClient.html).create()) {
          [UpdateUserRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.UpdateUserRequest.html) request =
              [UpdateUserRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.UpdateUserRequest.html).newBuilder()
                  .setUpdateMask([FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().build())
                  .setUser([User](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.User.html).newBuilder().build())
                  .build();
          ApiFuture<Operation> future = cloudFtpClient.[updateUserCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.CloudFtpClient.html#com_google_cloud_ftp_v1_CloudFtpClient_updateUserCallable__)().futureCall(request);
          // Do something.
          [Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html) response = future.get();
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
     *  Optional. Field mask is used to specify the fields to be overwritten in the
     *  User resource by the update.
     *  The fields specified in the update_mask are relative to the resource, not
     *  the full request. A field will be overwritten if it is in the mask. If the
     *  user does not provide a mask then all fields present in the request will be
     *  overwritten.
     */
    // const updateMask = {}
    /**
     *  Required. The resource being updated
     */
    // const user = {}
    
    // Imports the Ftp library
    const {CloudFtpClient} = require('[@google-cloud/ftp](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/overview.html)').v1;
    
    // Instantiates a client
    const ftpClient = new [CloudFtpClient](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/overview.html)();
    
    async function callUpdateUser() {
      // Construct request
      const request = {
        user,
      };
    
      // Run request
      const [operation] = await ftpClient.updateUser(request);
      const [response] = await operation.promise();
      console.log(response);
    }
    
    callUpdateUser();

### PHP

To learn how to install and use the client library for Cloud FTP, see [Cloud FTP client libraries](https://docs.cloud.google.com/cloud-ftp/reference/libraries). For more information, see the [Cloud FTP PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-ftp/latest). 

To authenticate to Cloud FTP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Ftp\V1\Client\CloudFtpClient;
    use Google\Cloud\Ftp\V1\StorageDirectoryMapping;
    use Google\Cloud\Ftp\V1\StorageDirectoryMapping\Permission;
    use Google\Cloud\Ftp\V1\UpdateUserRequest;
    use Google\Cloud\Ftp\V1\User;
    use Google\Cloud\Ftp\V1\UserCredential;
    use Google\Cloud\Ftp\V1\UserCredential\Type;
    use Google\Rpc\Status;
    
    /**
     * Updates the parameters of a single User.
     *
     * @param string $userCustomerServiceAccount             Service account in customer project attached to this SFTP User.
     * @param string $userUserCredentialsCredentialName      Name of the user credential.
     * @param int    $userUserCredentialsCredentialType      Type of credential.
     * @param string $userStorageDirectoryMappingsBucket     Name of the bucket.
     * @param string $userStorageDirectoryMappingsDirectory  Directory where the user lands in the SFTP server.
     * @param int    $userStorageDirectoryMappingsPermission Permission to the bucket.
     */
    function update_user_sample(
        string $userCustomerServiceAccount,
        string $userUserCredentialsCredentialName,
        int $userUserCredentialsCredentialType,
        string $userStorageDirectoryMappingsBucket,
        string $userStorageDirectoryMappingsDirectory,
        int $userStorageDirectoryMappingsPermission
    ): void {
        // Create a client.
        $cloudFtpClient = new CloudFtpClient();
    
        // Prepare the request message.
        $userCredential = (new UserCredential())
            ->setCredentialName($userUserCredentialsCredentialName)
            ->setCredentialType($userUserCredentialsCredentialType);
        $userUserCredentials = [$userCredential];
        $storageDirectoryMapping = (new StorageDirectoryMapping())
            ->setBucket($userStorageDirectoryMappingsBucket)
            ->setDirectory($userStorageDirectoryMappingsDirectory)
            ->setPermission($userStorageDirectoryMappingsPermission);
        $userStorageDirectoryMappings = [$storageDirectoryMapping];
        $user = (new User())
            ->setCustomerServiceAccount($userCustomerServiceAccount)
            ->setUserCredentials($userUserCredentials)
            ->setStorageDirectoryMappings($userStorageDirectoryMappings);
        $request = (new UpdateUserRequest())
            ->setUser($user);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $cloudFtpClient->updateUser($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var User $result */
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
        $userCustomerServiceAccount = '[CUSTOMER_SERVICE_ACCOUNT]';
        $userUserCredentialsCredentialName = '[CREDENTIAL_NAME]';
        $userUserCredentialsCredentialType = Type::TYPE_UNSPECIFIED;
        $userStorageDirectoryMappingsBucket = '[BUCKET]';
        $userStorageDirectoryMappingsDirectory = '[DIRECTORY]';
        $userStorageDirectoryMappingsPermission = Permission::PERMISSION_UNSPECIFIED;
    
        update_user_sample(
            $userCustomerServiceAccount,
            $userUserCredentialsCredentialName,
            $userUserCredentialsCredentialType,
            $userStorageDirectoryMappingsBucket,
            $userStorageDirectoryMappingsDirectory,
            $userStorageDirectoryMappingsPermission
        );
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
    
    
    def sample_update_user():
        # Create a client
        client = [ftp_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest).[CloudFtpClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.services.cloud_ftp.CloudFtpClient.html)()
    
        # Initialize request argument(s)
        user = [ftp_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest).[User](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.User.html)()
        user.customer_service_account = "customer_service_account_value"
        user.user_credentials.credential_name = "credential_name_value"
        user.user_credentials.credential_type = "PUBLIC_KEY"
        user.storage_directory_mappings.bucket = "bucket_value"
        user.storage_directory_mappings.directory = "directory_value"
        user.storage_directory_mappings.permission = "READ_WRITE"
    
        request = [ftp_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest).[UpdateUserRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.UpdateUserRequest.html)(
            user=user,
        )
    
        # Make the request
        operation = client.[update_user](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.services.cloud_ftp.CloudFtpClient.html#google_cloud_ftp_v1_services_cloud_ftp_CloudFtpClient_update_user)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    
    

### Ruby

To learn how to install and use the client library for Cloud FTP, see [Cloud FTP client libraries](https://docs.cloud.google.com/cloud-ftp/reference/libraries). For more information, see the [Cloud FTP Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ftp/latest). 

To authenticate to Cloud FTP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/ftp/v1"
    
    ##
    # Snippet for the update_user call in the CloudFtp service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::Ftp::V1::CloudFtp::Rest::Client#update_user.
    #
    def update_user
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::Ftp::V1::CloudFtp::Rest::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::Ftp::V1::UpdateUserRequest.new
    
      # Call the update_user method.
      result = client.update_user request
    
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

  * [Update buckets for an SFTP user](https://docs.cloud.google.com/cloud-ftp/update-user-buckets)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
