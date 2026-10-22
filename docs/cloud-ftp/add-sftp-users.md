---
url: https://docs.cloud.google.com/cloud-ftp/add-sftp-users/
title: Add users to an SFTP server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:04.406859+00:00
---

# Add users to an SFTP server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-ftp/add-sftp-users/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud FTP ](https://docs.cloud.google.com/cloud-ftp)
  * [ Guides ](https://docs.cloud.google.com/cloud-ftp/overview)



Send feedback 

#  Add users to an SFTP server Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to add users to a Cloud FTP server. Users such as external partners and internal stakeholders can use the server to securely transfer files to and from Cloud Storage.

At a high level, these are the steps to add a user to an SFTP server:

  1. Configure permissions for the user.
  2. Create an SFTP user and map their directories to Cloud Storage buckets.



For steps to create a server, see [Create an external SFTP server](https://docs.cloud.google.com/cloud-ftp/create-external-sftp-server) and [Create an internal SFTP server](https://docs.cloud.google.com/cloud-ftp/create-internal-sftp-server).

## Considerations

  * You can grant a user access to a maximum of 10 buckets.

  * A user can have a maximum of 10 public keys.




## Before you begin

  1. [Create one or more Cloud Storage buckets](https://docs.cloud.google.com/storage/docs/creating-buckets) to store the data that the user will work with, if the buckets don't already exist.

  2. Get the user's public key from each SSH key pair that they will use to connect to the server.

If the user doesn't have an SSH key pair, use the following steps to generate one.

#### Generate an SSH key pair

#### Which key format do you need?

The key format that you need depends on which client you use to connect to the SFTP server. For more information, see [Supported SFTP clients](https://docs.cloud.google.com/cloud-ftp/third-party-clients).

### PEM format

     1. To create an OpenSSH key pair (PEM format), use the [`ssh-keygen` utility](https://man.openbsd.org/ssh-keygen).

On the client machine that will connect to the SFTP server, run the following command:
            
            ssh-keygen -t rsa -b 4096 -f ~/.ssh/KEY_PAIR_NAME

Replace `KEY_PAIR_NAME` with a name for the key pair, such as `sftp_user_key`.

     2. Extract the public key:
            
            cat ~/.ssh/KEY_PAIR_NAME.pub

### PPK format

     1. To create a PuTTY key pair (PPK format), use the [`PuTTYgen`](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) tool.

On the client machine that will connect to the SFTP server, run the following command:
            
            puttygen -t rsa -b 4096 -o KEY_PAIR_NAME.ppk

Replace `KEY_PAIR_NAME` with a name for the key pair, such as `sftp_user_key`.

     2. Extract the public key:
            
            puttygen -L KEY_PAIR_NAME.ppk




### Required roles

To get the permission that you need to add SFTP users, ask your administrator to grant you the [FTP Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/ftp#ftp.admin) (`roles/ftp.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `ftp.users.create` permission, which is required to add SFTP users. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Configure permissions for a user

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** You can run the gcloud CLI in the Google Cloud console without installing the Google Cloud CLI. To run the gcloud CLI in the Google Cloud console, [use Cloud Shell](https://console.cloud.google.com/?cloudshell=true). 
  2. Set the project:
         
         gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with the ID of the project that contains the SFTP server.

  3. Create a service account for the user, if a service account doesn't already exist. The service account accesses Cloud Storage resources on behalf of the user.
         
         gcloud iam service-accounts create USERNAME-sa \
             --description="USERNAME SFTP Service Account" \
             --display-name="USERNAME SFTP Service Account"

Replace `USERNAME` with a unique username for the SFTP user. The username must start with a lowercase letter and can include lowercase letters, numbers, or hyphens. Maximum length is 32 characters.

On success, a message like `Created service account [example-userid-sa]` is displayed.

  4. Grant IAM roles to the administrator who creates the SFTP user:

     1. Grant yourself the Service Account User (`roles/iam.serviceAccountUser`) role:
            
            gcloud iam service-accounts add-iam-policy-binding USERNAME-sa@PROJECT_ID.iam.gserviceaccount.com \
                --member="user:ADMINISTRATOR_EMAIL" \
                --role="roles/iam.serviceAccountUser"

Replace `ADMINISTRATOR_EMAIL` with the email address of the principal who is creating the SFTP user. If you're creating the user (as opposed to an application), then this value is the email address that you use to access Google Cloud.

On success, a message like the following is displayed:
            
            Updated IAM policy for serviceAccount [example-userid-sa@example-project.iam.gserviceaccount.com].
            bindings:
            - members:
            - user:admin@example.com
            role: roles/iam.serviceAccountUser
            etag: BwZJk7OiSzw=
            version: 1
            

     2. Grant yourself the Storage Bucket Viewer (`roles/storage.bucketViewer`) role on the bucket: 
            
            gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
                --member="user:ADMINISTRATOR_EMAIL" \
                --role="roles/storage.bucketViewer"

Replace `BUCKET_NAME` with the name of the bucket.

Repeat this step for each bucket that the user needs to access.

     3. Grant yourself the Storage Object Viewer (`roles/storage.objectViewer`) role on the bucket:
            
            gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
                --member="user:ADMINISTRATOR_EMAIL" \
                --role="roles/storage.objectViewer"

Repeat this step for each bucket that the user needs to access.

  5. Grant the user's service account the IAM role that's necessary to access the bucket:
         
         gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
             --member="serviceAccount:USERNAME-sa@PROJECT_ID.iam.gserviceaccount.com" \
             --role="ROLE"

Replace `ROLE` with one of the following IAM roles:

     * For read-only access, use the `roles/storage.objectViewer` role.
     * For read and write access, use the `roles/storage.objectAdmin` role.

Repeat this step for each bucket that the user needs to access.

  6. Authorize the Cloud FTP Service Agent to generate tokens for the user's service account:

     1. Get the email address of the server's service agent. For steps, see [Get details about a server](https://docs.cloud.google.com/cloud-ftp/get-server-information#get-server).

     2. Authorize the Cloud FTP Service Agent:
            
            gcloud iam service-accounts add-iam-policy-binding USERNAME-sa@PROJECT_ID.iam.gserviceaccount.com \
                --member="serviceAccount:SERVICE_AGENT_EMAIL" \
                --role="roles/iam.serviceAccountTokenCreator"

Replace `SERVICE_AGENT_EMAIL` with the service agent's email address.




Next, create a user.

## Create an SFTP server user

After you configure permissions for a user, you create the user and map their directories to one or more Cloud Storage buckets.

###  gcloud 

  1. To create a user for an SFTP server, run the [`gcloud alpha storage ftp users create` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/ftp/users/create).

Before using any of the command data below, make the following replacements: 

     * CREDENTIAL_NAME: a unique name to identify the user credentials.
     * SSH_PUBLIC_KEY: the body of the user's SSH public key, in OpenSSH format. For example, `ssh-rsa AAAAB3NzaC1ycRexample...`.
     * USERNAME: the SFTP user's username.
     * SERVICE_ACCOUNT: the user's service account. For example, `username-sa@example-project.iam.gserviceaccount.com`.
     * LOCATION_ID: the [location](https://docs.cloud.google.com/cloud-ftp/locations) of the server, such as `us-west1`.
     * SERVER_ID: the server ID.
     * BUCKET_NAME: the name of a bucket that the SFTP user is granted access to, such as `example-bucket`. Omit the `gs://`.
     * (Optional) BUCKET_PREFIX: the path of a folder within the bucket to set as the root directory for this directory mapping. If you omit the `bucket_prefix` property, then Cloud FTP uses the bucket root.
     * DIRECTORY: the logical landing directory path that is presented to the SFTP user. For example, `/home/uploads`. 

If you map multiple buckets or folders, then provide a unique directory path for each mapping.

Nested logical directories aren't supported. If you provide multiple mappings for a directory, then provide the directories in a flat structure instead of a nested structure. For example, use `/dir1` and `/dir2` instead of `/dir1` and `/dir1/dir2`.

     * SFTP_PERMISSION: the access level for the directory. For read-only access, set this value to `READ_ONLY`. For read and write access, set this value to `READ_WRITE`.

Note the following:

     * To grant a user access to multiple buckets, provide the `--storage-directory-mapping` flag multiple times, with a directory mapping for each bucket.
     * To configure multiple public keys for a user, provide multiple credentials in the `credentials.json` file.

Save the following content in a file called `credentials.json`: 
    
    [
      {
        "credentialName": "CREDENTIAL_NAME",
        "credentialType": "PUBLIC_KEY",
        "sshPublicKeyBody": "SSH_PUBLIC_KEY"
      }
    ]

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud alpha storage ftp users create USERNAME \
        --customer-service-account=SERVICE_ACCOUNT --location=LOCATION_ID \
        --server=SERVER_ID \
        --storage-directory-mapping=bucket=BUCKET_NAME,bucket_prefix=BUCKET_PREFIX,directory=DIRECTORY,permission=SFTP_PERMISSION \
        --user-credentials-from-file=credentials.json

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud alpha storage ftp users create USERNAME `
        --customer-service-account=SERVICE_ACCOUNT --location=LOCATION_ID `
        --server=SERVER_ID `
        --storage-directory-mapping=bucket=BUCKET_NAME,bucket_prefix=BUCKET_PREFIX,directory=DIRECTORY,permission=SFTP_PERMISSION `
        --user-credentials-from-file=credentials.json

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud alpha storage ftp users create USERNAME ^
        --customer-service-account=SERVICE_ACCOUNT --location=LOCATION_ID ^
        --server=SERVER_ID ^
        --storage-directory-mapping=bucket=BUCKET_NAME,bucket_prefix=BUCKET_PREFIX,directory=DIRECTORY,permission=SFTP_PERMISSION ^
        --user-credentials-from-file=credentials.json

It takes a few seconds for the user to be created. 
  2. Give the user the following information, which they need to connect to the server:

     * The user's SFTP username.

     * The server's access configuration, which depends on the server type:

       * For an external server, the server's IP address.

       * For an internal server, the URI of the server's service attachment.

For steps to get the server's access configuration, see [Get details about a server](https://docs.cloud.google.com/cloud-ftp/get-server-information#get-server).

     * (Optional) The key fingerprint of the server.




###  REST 

  1. To create a user for an SFTP server, use the [`servers.users.create` method](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers.users/create).

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the Google Cloud project ID of the server.
     * LOCATION_ID: the [location](https://docs.cloud.google.com/cloud-ftp/locations) of the server, such as `us-west1`.
     * SERVER_ID: the server ID.
     * USERNAME: the SFTP user's username.
     * BUCKET_NAME: the name of a bucket that the SFTP user is granted access to, such as `example-bucket`. Omit the `gs://`.
     * (Optional) BUCKET_PREFIX: the path of a folder within the bucket to set as the root directory for this directory mapping. If you omit this value, then Cloud FTP uses the bucket root. 
     * DIRECTORY: the logical landing directory path that is presented to the SFTP user. For example, `/home/uploads`. If you omit this value, then Cloud FTP sets the landing directory to `/`.

If you map multiple buckets or folders, then provide a unique directory path for each mapping.

Nested logical directories aren't supported. If you provide multiple mappings for a directory, then provide the directories in a flat structure instead of a nested structure. For example, use `/dir1` and `/dir2` instead of `/dir1` and `/dir1/dir2`.

     * SFTP_PERMISSION: the access level for the directory. For read-only access, set this value to `READ_ONLY`. For read and write access, set this value to `READ_WRITE`.
     * SERVICE_ACCOUNT: the user's service account. For example, `username-sa@example-project.iam.gserviceaccount.com`.
     * CREDENTIAL_NAME: a unique name to identify the user credentials.
     * SSH_PUBLIC_KEY: the body of the user's SSH public key, in OpenSSH format. For example, `ssh-rsa AAAAB3NzaC1ycRexample...`.

Note the following:

     * To grant a user access to multiple buckets, provide multiple bucket mappings in the `storageDirectoryMappings` list.
     * To configure multiple public keys for a user, provide multiple credentials in the `userCredentials` list.

HTTP method and URL: 
    
    POST https://ftp.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/servers/SERVER_ID/users?userId=USERNAME

Request JSON body: 
    
    {
      "storageDirectoryMappings": [
        {
          "bucket": "BUCKET_NAME",
          "bucketPrefix": "BUCKET_PREFIX",
          "directory": "DIRECTORY",
          "permission": "SFTP_PERMISSION"
        }
      ],
      "customerServiceAccount": "SERVICE_ACCOUNT",
      "userCredentials": [
        {
          "credentialName": "CREDENTIAL_NAME",
          "credentialType": "PUBLIC_KEY",
          "sshPublicKeyBody": "SSH_PUBLIC_KEY"
        }
      ]
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://ftp.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/servers/SERVER_ID/users?userId=USERNAME"

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
        -Uri "https://ftp.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/servers/SERVER_ID/users?userId=USERNAME" | Select-Object -Expand Content

The response identifies a [long-running operation](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.operations). It takes a few seconds for the user to be created. 
  2. Give the user the following information, which they need to connect to the server:

     * The user's SFTP username.

     * The server's access configuration, which depends on the server type:

       * For an external server, the server's IP address.

       * For an internal server, the URI of the server's service attachment.

For steps to get the server's access configuration, see [Get details about a server](https://docs.cloud.google.com/cloud-ftp/get-server-information#get-server).

     * (Optional) The key fingerprint of the server.




###  Client libraries 

### C#

To learn how to install and use the client library for Cloud FTP, see [Cloud FTP client libraries](https://docs.cloud.google.com/cloud-ftp/reference/libraries). For more information, see the [Cloud FTP C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest). 

To authenticate to Cloud FTP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Ftp.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using System.Threading.Tasks;
    
    public sealed partial class GeneratedCloudFtpClientSnippets
    {
        /// <summary>Snippet for CreateUserAsync</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public async Task CreateUserAsync()
        {
            // Create client
            [CloudFtpClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.CloudFtpClient.html) cloudFtpClient = await [CloudFtpClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.CloudFtpClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.CloudFtpClient.html#Google_Cloud_Ftp_V1_CloudFtpClient_CreateAsync_System_Threading_CancellationToken_)();
            // Initialize request argument(s)
            string parent = "projects/[PROJECT]/locations/[LOCATION]/servers/[SERVER]";
            [User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.User.html) user = new [User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.User.html)();
            string userId = "";
            // Make the request
            Operation<User, OperationMetadata> response = await cloudFtpClient.[CreateUserAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.CloudFtpClient.html#Google_Cloud_Ftp_V1_CloudFtpClient_CreateUserAsync_Google_Cloud_Ftp_V1_CreateUserRequest_Google_Api_Gax_Grpc_CallSettings_)(parent, user, userId);
    
            // Poll until the returned long-running operation is complete
            Operation<User, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
            // Retrieve the operation result
            [User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.User.html) result = completedResponse.Result;
    
            // Or get the name of the operation
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name
            Operation<User, OperationMetadata> retrievedResponse = await cloudFtpClient.[PollOnceCreateUserAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.CloudFtpClient.html#Google_Cloud_Ftp_V1_CloudFtpClient_PollOnceCreateUserAsync_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
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
    
    	req := &ftppb.CreateUserRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ftp/apiv1/ftppb#CreateUserRequest.
    	}
    	op, err := c.CreateUser(ctx, req)
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
    import com.google.cloud.ftp.v1.[CreateUserRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.CreateUserRequest.html);
    import com.google.cloud.ftp.v1.[ServerName](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.ServerName.html);
    import com.google.cloud.ftp.v1.[User](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.User.html);
    import com.google.longrunning.[Operation](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html);
    
    public class AsyncCreateUser {
    
      public static void main(String[] args) throws Exception {
        asyncCreateUser();
      }
    
      public static void asyncCreateUser() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([CloudFtpClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.CloudFtpClient.html) cloudFtpClient = [CloudFtpClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.CloudFtpClient.html).create()) {
          [CreateUserRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.CreateUserRequest.html) request =
              [CreateUserRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.CreateUserRequest.html).newBuilder()
                  .setParent([ServerName](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.ServerName.html).of("[PROJECT]", "[LOCATION]", "[SERVER]").toString())
                  .[setUserId](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.CreateUserRequest.Builder.html#com_google_cloud_ftp_v1_CreateUserRequest_Builder_setUserId_java_lang_String_)("userId-836030906")
                  .setUser([User](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.User.html).newBuilder().build())
                  .setRequestId("requestId693933066")
                  .build();
          ApiFuture<Operation> future = cloudFtpClient.[createUserCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-ftp/latest/com.google.cloud.ftp.v1.CloudFtpClient.html#com_google_cloud_ftp_v1_CloudFtpClient_createUserCallable__)().futureCall(request);
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
     *  Required. A unique user ID for the SFTP user. The user ID must start with a
     *  lowercase letter and can include lowercase letters, numbers, or hyphens.
     */
    // const userId = 'abc123'
    /**
     *  Required. The resource being created
     */
    // const user = {}
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
    
    async function callCreateUser() {
      // Construct request
      const request = {
        parent,
        userId,
        user,
      };
    
      // Run request
      const [operation] = await ftpClient.createUser(request);
      const [response] = await operation.promise();
      console.log(response);
    }
    
    callCreateUser();

### PHP

To learn how to install and use the client library for Cloud FTP, see [Cloud FTP client libraries](https://docs.cloud.google.com/cloud-ftp/reference/libraries). For more information, see the [Cloud FTP PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-ftp/latest). 

To authenticate to Cloud FTP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Ftp\V1\Client\CloudFtpClient;
    use Google\Cloud\Ftp\V1\CreateUserRequest;
    use Google\Cloud\Ftp\V1\StorageDirectoryMapping;
    use Google\Cloud\Ftp\V1\StorageDirectoryMapping\Permission;
    use Google\Cloud\Ftp\V1\User;
    use Google\Cloud\Ftp\V1\UserCredential;
    use Google\Cloud\Ftp\V1\UserCredential\Type;
    use Google\Rpc\Status;
    
    /**
     * Creates a new User in a given project and location and Server.
     *
     * @param string $formattedParent                        Value for parent. Please see
     *                                                       {@see CloudFtpClient::serverName()} for help formatting this field.
     * @param string $userId                                 A unique user ID for the SFTP user. The user ID must start with a
     *                                                       lowercase letter and can include lowercase letters, numbers, or hyphens.
     * @param string $userCustomerServiceAccount             Service account in customer project attached to this SFTP User.
     * @param string $userUserCredentialsCredentialName      Name of the user credential.
     * @param int    $userUserCredentialsCredentialType      Type of credential.
     * @param string $userStorageDirectoryMappingsBucket     Name of the bucket.
     * @param string $userStorageDirectoryMappingsDirectory  Directory where the user lands in the SFTP server.
     * @param int    $userStorageDirectoryMappingsPermission Permission to the bucket.
     */
    function create_user_sample(
        string $formattedParent,
        string $userId,
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
        $request = (new CreateUserRequest())
            ->setParent($formattedParent)
            ->setUserId($userId)
            ->setUser($user);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $cloudFtpClient->createUser($request);
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
        $formattedParent = CloudFtpClient::serverName('[PROJECT]', '[LOCATION]', '[SERVER]');
        $userId = '[USER_ID]';
        $userCustomerServiceAccount = '[CUSTOMER_SERVICE_ACCOUNT]';
        $userUserCredentialsCredentialName = '[CREDENTIAL_NAME]';
        $userUserCredentialsCredentialType = Type::TYPE_UNSPECIFIED;
        $userStorageDirectoryMappingsBucket = '[BUCKET]';
        $userStorageDirectoryMappingsDirectory = '[DIRECTORY]';
        $userStorageDirectoryMappingsPermission = Permission::PERMISSION_UNSPECIFIED;
    
        create_user_sample(
            $formattedParent,
            $userId,
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
    
    
    def sample_create_user():
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
    
        request = [ftp_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest).[CreateUserRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.CreateUserRequest.html)(
            parent="parent_value",
            user_id="user_id_value",
            user=user,
        )
    
        # Make the request
        operation = client.[create_user](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.services.cloud_ftp.CloudFtpClient.html#google_cloud_ftp_v1_services_cloud_ftp_CloudFtpClient_create_user)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    
    

### Ruby

To learn how to install and use the client library for Cloud FTP, see [Cloud FTP client libraries](https://docs.cloud.google.com/cloud-ftp/reference/libraries). For more information, see the [Cloud FTP Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ftp/latest). 

To authenticate to Cloud FTP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/ftp/v1"
    
    ##
    # Snippet for the create_user call in the CloudFtp service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::Ftp::V1::CloudFtp::Rest::Client#create_user.
    #
    def create_user
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::Ftp::V1::CloudFtp::Rest::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::Ftp::V1::CreateUserRequest.new
    
      # Call the create_user method.
      result = client.create_user request
    
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

  * [Connect to an external SFTP server](https://docs.cloud.google.com/cloud-ftp/connect-to-external-server).
  * [Connect to an internal SFTP server](https://docs.cloud.google.com/cloud-ftp/connect-to-internal-server).
  * [Transfer data by using SFTP commands](https://docs.cloud.google.com/cloud-ftp/sftp-commands).
  * Learn about [data protection, backup, and recovery options](https://docs.cloud.google.com/storage/docs/protection-backup-recovery-overview) for Cloud Storage buckets.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
