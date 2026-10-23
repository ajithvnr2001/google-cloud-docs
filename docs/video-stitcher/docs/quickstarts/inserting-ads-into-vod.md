---
url: https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-vod/
title: Insert ads into VOD assets \u00a0|\u00a0 Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:04.295249+00:00
---

# Insert ads into VOD assets  |  Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-vod/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Guides ](https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-vod)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Insert ads into VOD assets

This page shows you how to insert ads into the playback of a video-on-demand (VOD) asset using the Video Stitcher API and `curl`, PowerShell, or the client libraries.

## Before you begin

Before you call the Video Stitcher API, complete the following steps:

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Video Stitcher API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable videostitcher.googleapis.com

  8. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  9. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/videostitcher.admin`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.

  10. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  11. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  12. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  13. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  14. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  15. Enable the Video Stitcher API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable videostitcher.googleapis.com

  16. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  17. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/videostitcher.admin`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.

  18. This quickstart requires an MPEG-DASH manifest (MPD) file, or an HTTP Live Streaming (HLS) manifest (M3U8) file, and the associated segment files. You can use existing VOD files or you can [create VOD source files](https://docs.cloud.google.com/video-stitcher/docs/create-vod-source-files) using the Transcoder API. 
  19. As an option, you can use a content delivery network (CDN) with this quickstart. If you haven't configured a CDN, follow the steps in the [Media CDN quickstart](https://docs.cloud.google.com/media-cdn/docs/quickstart) with the following modifications: 
     1. Upload MPEG-DASH or HLS manifest files and media segments into the Cloud Storage bucket. 
     2. You don't have to make your Cloud Storage bucket publicly readable.
     3. You can use signed URLs or unsigned URLs. 



## Create a CDN key

The Video Stitcher API can fetch videos from a content delivery network (CDN). If the video asset is protected by URL signing, a CDN key must be registered with the Video Stitcher API.

**Note:** You can skip to the next section if you are not using a CDN or if your CDN uses unsigned URLs.

To register the CDN key, use the [`projects.locations.cdnKeys.create`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.cdnKeys/create) method.

### REST (Media CDN)

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number; this is located in the **Project number** field on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page
  * `LOCATION`: the location in which to create your CDN key; use one of the [supported regions](https://docs.cloud.google.com/video-stitcher/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `us-west1`
    * `asia-east1`
    * `asia-south1`
    * `asia-southeast1`
    * `europe-west1`
    * `southamerica-east1`
  * `CDN_KEY_ID`: A user-defined identifier for the CDN key, which will become the final component of the CDN key's resource name. This ID can only contain lower-case letters, numbers, and hyphens. The first character must be a letter, the last character must be a letter or a number, and the entire ID has a 63 character maximum.
  * `HOSTNAME`: the hostname of the CDN to associate with this CDN key (for example, an IP address like `35.190.60.252` or a domain name like `cdn.example.com`)
  * `MEDIA_CDN_KEYNAME`: the keyset name of the [Media CDN key](https://docs.cloud.google.com/media-cdn/docs/keys-overview)
  * `MEDIA_CDN_PRIVATE_KEY`: The 64-byte Ed25519 private key as a base64-encoded string. See [Create a private key for Media CDN](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-cdn-keys#create-private-key-media-cdn) for more information. 



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "hostname": "HOSTNAME",
      "mediaCdnKey": {
        "keyName": "MEDIA_CDN_KEYNAME",
        "privateKey": "MEDIA_CDN_PRIVATE_KEY"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/cdnKeys?cdnKeyId=CDN_KEY_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "hostname": "HOSTNAME",
      "mediaCdnKey": {
        "keyName": "MEDIA_CDN_KEYNAME",
        "privateKey": "MEDIA_CDN_PRIVATE_KEY"
      }
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/cdnKeys?cdnKeyId=CDN_KEY_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.common.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_NUMBER/locations/LOCATION/cdnKeys/CDN_KEY_ID",
        "verb": "create",
        "cancelRequested": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

This command creates a [long-running operation (LRO)](https://docs.cloud.google.com/video-stitcher/docs/how-to/manage-long-running-operations) that you can query to track progress. Copy the returned `OPERATION_ID`, which is the last part of the `name` field, to use in the next section. 

### REST (Cloud CDN)

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number; this is located in the **Project number** field on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page
  * `LOCATION`: the location in which to create your CDN key; use one of the [supported regions](https://docs.cloud.google.com/video-stitcher/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `us-west1`
    * `asia-east1`
    * `asia-south1`
    * `asia-southeast1`
    * `europe-west1`
    * `southamerica-east1`
  * `CDN_KEY_ID`: A user-defined identifier for the CDN key, which will become the final component of the CDN key's resource name. This ID can only contain lower-case letters, numbers, and hyphens. The first character must be a letter, the last character must be a letter or a number, and the entire ID has a 63 character maximum.
  * `HOSTNAME`: the hostname of the CDN to associate with this CDN key (for example, an IP address like `35.190.60.252` or a domain name like `cdn.example.com`)
  * `GCDN_KEYNAME`: the name of the [Cloud CDN key](https://docs.cloud.google.com/cdn/docs/using-signed-urls#creatingkeys)
  * `GCDN_PRIVATE_KEY`: the base64-encoded string secret for the Cloud CDN key



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "hostname": "HOSTNAME",
      "googleCdnKey": {
        "keyName": "GCDN_KEYNAME",
        "privateKey": "GCDN_PRIVATE_KEY"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/cdnKeys?cdnKeyId=CDN_KEY_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "hostname": "HOSTNAME",
      "googleCdnKey": {
        "keyName": "GCDN_KEYNAME",
        "privateKey": "GCDN_PRIVATE_KEY"
      }
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/cdnKeys?cdnKeyId=CDN_KEY_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.common.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_NUMBER/locations/LOCATION/cdnKeys/CDN_KEY_ID",
        "verb": "create",
        "cancelRequested": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

This command creates a [long-running operation (LRO)](https://docs.cloud.google.com/video-stitcher/docs/how-to/manage-long-running-operations) that you can query to track progress. Copy the returned `OPERATION_ID`, which is the last part of the `name` field, to use in the next section. 

### REST (Akamai CDN)

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number; this is located in the **Project number** field on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page
  * `LOCATION`: the location in which to create your CDN key; use one of the [supported regions](https://docs.cloud.google.com/video-stitcher/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `us-west1`
    * `asia-east1`
    * `asia-south1`
    * `asia-southeast1`
    * `europe-west1`
    * `southamerica-east1`
  * `CDN_KEY_ID`: A user-defined identifier for the CDN key, which will become the final component of the CDN key's resource name. This ID can only contain lower-case letters, numbers, and hyphens. The first character must be a letter, the last character must be a letter or a number, and the entire ID has a 63 character maximum.
  * `HOSTNAME`: the hostname of the CDN to associate with this CDN key (for example, an IP address like `35.190.60.252` or a domain name like `cdn.example.com`)
  * `AKAMAI_TOKEN_KEY`: the base64-encoded string token key for the Akamai CDN edge configuration



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "hostname": "HOSTNAME",
      "akamaiCdnKey": {
        "tokenKey": "AKAMAI_TOKEN_KEY"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/cdnKeys?cdnKeyId=CDN_KEY_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "hostname": "HOSTNAME",
      "akamaiCdnKey": {
        "tokenKey": "AKAMAI_TOKEN_KEY"
      }
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/cdnKeys?cdnKeyId=CDN_KEY_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.common.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_NUMBER/locations/LOCATION/cdnKeys/CDN_KEY_ID",
        "verb": "create",
        "cancelRequested": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

This command creates a [long-running operation (LRO)](https://docs.cloud.google.com/video-stitcher/docs/how-to/manage-long-running-operations) that you can query to track progress. Copy the returned `OPERATION_ID`, which is the last part of the `name` field, to use in the next section. 

### C#

Before trying this sample, follow the C# setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Video.Stitcher.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using [Google.Protobuf](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.html);
    using System.Threading.Tasks;
    
    public class CreateCdnKeySample
    {
        public async Task<CdnKey> CreateCdnKeyAsync(
        string projectId, string location, string cdnKeyId, string hostname,
        string keyName, string privateKey, bool isMediaCdn)
        {
            // Create the client.
            [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html) client = [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_Create)();
    
            [CdnKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CdnKey.html) cdnKey = new [CdnKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CdnKey.html)
            {
                Hostname = hostname
            };
    
            if (isMediaCdn)
            {
                cdnKey.[MediaCdnKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CdnKey.html#Google_Cloud_Video_Stitcher_V1_CdnKey_MediaCdnKey) = new [MediaCdnKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.MediaCdnKey.html)
                {
                    KeyName = keyName,
                    PrivateKey = [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html).[CopyFromUtf8](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_CopyFromUtf8_System_String_)(privateKey)
                };
            }
            else
            {
                cdnKey.[GoogleCdnKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CdnKey.html#Google_Cloud_Video_Stitcher_V1_CdnKey_GoogleCdnKey) = new [GoogleCdnKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.GoogleCdnKey.html)
                {
                    KeyName = keyName,
                    PrivateKey = [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html).[CopyFromUtf8](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_CopyFromUtf8_System_String_)(privateKey)
                };
            }
    
            [CreateCdnKeyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CreateCdnKeyRequest.html) request = new [CreateCdnKeyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CreateCdnKeyRequest.html)
            {
                ParentAsLocationName = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html#Google_Api_Gax_ResourceNames_LocationName_FromProjectLocation_System_String_System_String_)(projectId, location),
                CdnKeyId = cdnKeyId,
                CdnKey = cdnKey
            };
    
            // Make the request.
            Operation<CdnKey, OperationMetadata> response = await client.[CreateCdnKeyAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_CreateCdnKeyAsync_Google_Api_Gax_ResourceNames_LocationName_Google_Cloud_Video_Stitcher_V1_CdnKey_System_String_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete.
            Operation<CdnKey, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    
            // Retrieve the operation result.
            return completedResponse.Result;
        }
    }
    

### Go

Before trying this sample, follow the Go setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/video/stitcher). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	stitcher "cloud.google.com/go/video/stitcher/apiv1"
    	stitcherstreampb "cloud.google.com/go/video/stitcher/apiv1/stitcherpb"
    )
    
    // createCDNKey creates a CDN key. A CDN key is used to retrieve protected media.
    // If isMediaCDN is true, create a Media CDN key. If false, create a Cloud
    // CDN key. To create a privateKey value for Media CDN, see
    // https://cloud.google.com/video-stitcher/docs/how-to/managing-cdn-keys#create-private-key-media-cdn.
    func createCDNKey(w io.Writer, projectID, keyID, privateKey string, isMediaCDN bool) error {
    	// projectID := "my-project-id"
    	// keyID := "my-cdn-key"
    	// privateKey := "my-private-key"
    	// isMediaCDN := true
    	location := "us-central1"
    	hostname := "cdn.example.com"
    	keyName := "cdn-key"
    	ctx := context.Background()
    	client, err := stitcher.[NewVideoStitcherClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_NewVideoStitcherClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("stitcher.NewVideoStitcherClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_Close)()
    
    	var req *stitcherstreampb.CreateCdnKeyRequest
    	if isMediaCDN {
    		req = &stitcherstreampb.CreateCdnKeyRequest{
    			Parent:   fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    			CdnKeyId: keyID,
    			CdnKey: &stitcherstreampb.CdnKey{
    				CdnKeyConfig: &stitcherstreampb.CdnKey_MediaCdnKey{
    					MediaCdnKey: &stitcherstreampb.MediaCdnKey{
    						KeyName:    keyName,
    						PrivateKey: []byte(privateKey),
    					},
    				},
    				Hostname: hostname,
    			},
    		}
    	} else {
    		req = &stitcherstreampb.CreateCdnKeyRequest{
    			Parent:   fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    			CdnKeyId: keyID,
    			CdnKey: &stitcherstreampb.CdnKey{
    				CdnKeyConfig: &stitcherstreampb.CdnKey_GoogleCdnKey{
    					GoogleCdnKey: &stitcherstreampb.GoogleCdnKey{
    						KeyName:    keyName,
    						PrivateKey: []byte(privateKey),
    					},
    				},
    				Hostname: hostname,
    			},
    		}
    	}
    
    	// Creates the CDN key.
    	op, err := client.CreateCdnKey(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.CreateCdnKey: %w", err)
    	}
    	response, err := op.Wait(ctx)
    	if err != nil {
    		return err
    	}
    
    	fmt.Fprintf(w, "CDN key: %v", response.GetName())
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/overview). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.stitcher.v1.[CdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey.html);
    import com.google.cloud.video.stitcher.v1.[CreateCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateCdnKeyRequest.html);
    import com.google.cloud.video.stitcher.v1.[GoogleCdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GoogleCdnKey.html);
    import com.google.cloud.video.stitcher.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LocationName.html);
    import com.google.cloud.video.stitcher.v1.[MediaCdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.MediaCdnKey.html);
    import com.google.cloud.video.stitcher.v1.[VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateCdnKey {
    
      private static final int TIMEOUT_IN_MINUTES = 2;
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String cdnKeyId = "my-cdn-key-id";
        String hostname = "cdn.example.com";
        String keyName = "my-key";
        // To create a privateKey value for Media CDN, see
        // https://cloud.google.com/video-stitcher/docs/how-to/managing-cdn-keys#create-private-key-media-cdn.
        String privateKey = "my-private-key"; // will be converted to a byte string
        Boolean isMediaCdn = true;
    
        createCdnKey(projectId, location, cdnKeyId, hostname, keyName, privateKey, isMediaCdn);
      }
    
      // createCdnKey creates a Media CDN key or a Cloud CDN key. A CDN key is used to retrieve
      // protected media.
      public static [CdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey.html) createCdnKey(
          String projectId,
          String location,
          String cdnKeyId,
          String hostname,
          String keyName,
          String privateKey,
          Boolean isMediaCdn)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html) videoStitcherServiceClient =
            [VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html).create()) {
          [CdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey.html) cdnKey;
          if (isMediaCdn) {
            cdnKey =
                [CdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey.html).newBuilder()
                    .[setHostname](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey.Builder.html#com_google_cloud_video_stitcher_v1_CdnKey_Builder_setHostname_java_lang_String_)(hostname)
                    .[setMediaCdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey.Builder.html#com_google_cloud_video_stitcher_v1_CdnKey_Builder_setMediaCdnKey_com_google_cloud_video_stitcher_v1_MediaCdnKey_)(
                        [MediaCdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.MediaCdnKey.html).newBuilder()
                            .setKeyName(keyName)
                            .setPrivateKey([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)(privateKey))
                            .build())
                    .build();
          } else {
            cdnKey =
                [CdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey.html).newBuilder()
                    .[setHostname](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey.Builder.html#com_google_cloud_video_stitcher_v1_CdnKey_Builder_setHostname_java_lang_String_)(hostname)
                    .[setGoogleCdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey.Builder.html#com_google_cloud_video_stitcher_v1_CdnKey_Builder_setGoogleCdnKey_com_google_cloud_video_stitcher_v1_GoogleCdnKey_)(
                        [GoogleCdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GoogleCdnKey.html).newBuilder()
                            .setKeyName(keyName)
                            .setPrivateKey([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)(privateKey))
                            .build())
                    .build();
          }
    
          [CreateCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateCdnKeyRequest.html) createCdnKeyRequest =
              [CreateCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateCdnKeyRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LocationName.html).of(projectId, location).toString())
                  .[setCdnKeyId](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateCdnKeyRequest.Builder.html#com_google_cloud_video_stitcher_v1_CreateCdnKeyRequest_Builder_setCdnKeyId_java_lang_String_)(cdnKeyId)
                  .setCdnKey(cdnKey)
                  .build();
    
          [CdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey.html) result =
              videoStitcherServiceClient
                  .[createCdnKeyAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html#com_google_cloud_video_stitcher_v1_VideoStitcherServiceClient_createCdnKeyAsync__org_jspecify_annotations_Nullable_com_google_cloud_video_stitcher_v1_LocationName_com_google_cloud_video_stitcher_v1_CdnKey_java_lang_String_)(createCdnKeyRequest)
                  .get(TIMEOUT_IN_MINUTES, TimeUnit.MINUTES);
          System.out.println("Created new CDN key: " + result.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey.html#com_google_cloud_video_stitcher_v1_CdnKey_getName__)());
          return result;
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const location = 'us-central1';
    const hostname = 'cdn.example.com';
    const keyName = 'cdn-key';
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // projectId = 'my-project-id';
    // cdnKeyId = 'my-cdn-key';
    // privateKey = 'my-private-key';
    
    // Imports the Video Stitcher library
    const {VideoStitcherServiceClient} =
      require('[@google-cloud/video-stitcher](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)').v1;
    // Instantiates a client
    const stitcherClient = new [VideoStitcherServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)();
    
    async function createCdnKey() {
      // Construct request
      const request = {
        parent: stitcherClient.[locationPath](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/v1.videostitcherserviceclient.html)(projectId, location),
        cdnKey: {
          hostname: hostname,
        },
        cdnKeyId: cdnKeyId,
      };
    
      if (isMediaCdn === 'true') {
        request.cdnKey.mediaCdnKey = {
          keyName: keyName,
          privateKey: privateKey,
        };
      } else {
        request.cdnKey.googleCdnKey = {
          keyName: keyName,
          privateKey: privateKey,
        };
      }
    
      const [operation] = await stitcherClient.createCdnKey(request);
      const [response] = await operation.promise();
      console.log(`CDN key: ${response.name}`);
    }
    
    createCdnKey().catch(err => {
      console.error(err.message);
      process.exitCode = 1;
    });

### PHP

Before trying this sample, follow the PHP setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/videostitcher/readme). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Stitcher\V1\CdnKey;
    use Google\Cloud\Video\Stitcher\V1\Client\VideoStitcherServiceClient;
    use Google\Cloud\Video\Stitcher\V1\CreateCdnKeyRequest;
    use Google\Cloud\Video\Stitcher\V1\GoogleCdnKey;
    use Google\Cloud\Video\Stitcher\V1\MediaCdnKey;
    
    /**
     * Creates a CDN key. Cloud CDN keys and Media CDN keys are supported.
     *
     * @param string  $callingProjectId   The project ID to run the API call under
     * @param string  $location           The location of the CDN key
     * @param string  $cdnKeyId           The ID of the CDN key to be created
     * @param string  $hostname           The hostname of the CDN key
     * @param string  $keyName            For a Media CDN key, this is the keyset name.
     *                                    For a Cloud CDN key, this is the public name of the
     *                                    CDN key.
     * @param string  $privateKey         For a Media CDN key, this is a 64-byte Ed25519 private
     *                                    key encoded as a base64-encoded string. See
     *                                    https://cloud.google.com/video-stitcher/docs/how-to/managing-cdn-keys#create-private-key-media-cdn
     *                                    for more information. For a Cloud CDN key,
     *                                    this is a base64-encoded string secret.
     * @param bool    $isMediaCdn         If true, create a Media CDN key. If false,
     *                                    create a Cloud CDN key.
     */
    function create_cdn_key(
        string $callingProjectId,
        string $location,
        string $cdnKeyId,
        string $hostname,
        string $keyName,
        string $privateKey,
        bool $isMediaCdn
    ): void {
        // Instantiate a client.
        $stitcherClient = new VideoStitcherServiceClient();
    
        $parent = $stitcherClient->locationName($callingProjectId, $location);
        $cdnKey = new CdnKey();
        $cdnKey->setHostname($hostname);
    
        if ($isMediaCdn == true) {
            $cloudCdn = new MediaCdnKey();
            $cdnKey->setMediaCdnKey($cloudCdn);
        } else {
            $cloudCdn = new GoogleCdnKey();
            $cdnKey->setGoogleCdnKey($cloudCdn);
        }
        $cloudCdn->setKeyName($keyName);
        $cloudCdn->setPrivateKey($privateKey);
    
        // Run CDN key creation request
        $request = (new CreateCdnKeyRequest())
            ->setParent($parent)
            ->setCdnKey($cdnKey)
            ->setCdnKeyId($cdnKeyId);
        $operationResponse = $stitcherClient->createCdnKey($request);
        $operationResponse->pollUntilComplete();
        if ($operationResponse->operationSucceeded()) {
            $result = $operationResponse->getResult();
            // Print results
            printf('CDN key: %s' . PHP_EOL, $result->getName());
        } else {
            $error = $operationResponse->getError();
            // handleError($error)
        }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud.video import [stitcher_v1](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest)
    from google.cloud.video.stitcher_v1.services.video_stitcher_service import (
        [VideoStitcherServiceClient](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.services.video_stitcher_service.VideoStitcherServiceClient.html),
    )
    
    
    def create_cdn_key(
        project_id: str,
        location: str,
        cdn_key_id: str,
        hostname: str,
        key_name: str,
        private_key: str,
        is_cloud_cdn: bool,
    ) -> stitcher_v1.types.CdnKey:
        """Creates a Cloud CDN or Media CDN key.
        Args:
            project_id: The GCP project ID.
            location: The location in which to create the CDN key.
            cdn_key_id: The user-defined CDN key ID.
            hostname: The hostname to which this CDN key applies.
            key_name: For a Media CDN key, this is the keyset name.
                      For a Cloud CDN key, this is the public name of the CDN key.
            private_key: For a Media CDN key, this is a 64-byte Ed25519 private
                         key encoded as a base64-encoded string.
                         See https://cloud.google.com/video-stitcher/docs/how-to/managing-cdn-keys#create-private-key-media-cdn
                         for more information. For a Cloud CDN key, this is a base64-encoded string secret.
            is_cloud_cdn: If true, create a Cloud CDN key. If false, create a Media CDN key.
    
        Returns:
            The CDN key resource.
        """
    
        client = VideoStitcherServiceClient()
    
        parent = f"projects/{project_id}/locations/{location}"
    
        cdn_key = [stitcher_v1](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest).[types](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.html).[CdnKey](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.CdnKey.html)(
            name=cdn_key_id,
            hostname=hostname,
        )
    
        if is_cloud_cdn:
            cdn_key.google_cdn_key = [stitcher_v1](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest).[types](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.html).[GoogleCdnKey](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.GoogleCdnKey.html)(
                key_name=key_name,
                private_key=private_key,
            )
        else:
            cdn_key.media_cdn_key = [stitcher_v1](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest).[types](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.html).[MediaCdnKey](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.MediaCdnKey.html)(
                key_name=key_name,
                private_key=private_key,
            )
    
        operation = client.[create_cdn_key](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.services.video_stitcher_service.VideoStitcherServiceClient.html#google_cloud_video_stitcher_v1_services_video_stitcher_service_VideoStitcherServiceClient_create_cdn_key)(
            parent=parent, cdn_key_id=cdn_key_id, cdn_key=cdn_key
        )
        response = operation.result()
        print(f"CDN key: {response.name}")
        return response
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/video/stitcher"
    
    ##
    # Create a Media CDN or Cloud CDN key
    #
    # @param project_id [String] Your Google Cloud project (e.g. `my-project`)
    # @param location [String] The location (e.g. `us-central1`)
    # @param cdn_key_id [String] The user-defined CDN key ID
    # @param hostname [String] The hostname to which this CDN key applies
    # @param key_name [String] For a Media CDN key, this is the keyset name.
    #   For a Cloud CDN key, this is the public name of the CDN key.
    # @param private_key [String] For a Media CDN key, this is a 64-byte Ed25519
    #   private key encoded as a base64-encoded string. See
    #   https://cloud.google.com/video-stitcher/docs/how-to/managing-cdn-keys#create-private-key-media-cdn
    #   for more information. For a Cloud CDN key, this is a base64-encoded string
    #   secret.
    # @param is_media_cdn [Boolean] If true, create a Media CDN key. If false,
    #  create a Cloud CDN key.
    #
    def create_cdn_key project_id:, location:, cdn_key_id:, hostname:, key_name:,
                       private_key:, is_media_cdn:
      # Create a Video Stitcher client.
      client = Google::Cloud::Video::Stitcher.video_stitcher_service
    
      # Build the resource name of the parent.
      parent = client.location_path project: project_id, location: location
      # Build the path for the CDN key resource.
      cdn_key_path = client.cdn_key_path project: project_id, location: location,
                                         cdn_key: cdn_key_id
    
      # Set the CDN key fields.
      new_cdn_key = if is_media_cdn
                      {
                        name: cdn_key_path,
                        hostname: hostname,
                        media_cdn_key: {
                          key_name: key_name,
                          private_key: private_key
                        }
                      }
                    else
                      {
                        name: cdn_key_path,
                        hostname: hostname,
                        google_cdn_key: {
                          key_name: key_name,
                          private_key: private_key
                        }
                      }
                    end
    
      operation = client.create_cdn_key parent: parent, cdn_key: new_cdn_key,
                                        cdn_key_id: cdn_key_id
    
      # The returned object is of type Gapic::Operation. You can use this
      # object to check the status of an operation, cancel it, or wait
      # for results. Here is how to block until completion:
      operation.wait_until_done!
    
      # Print the CDN key name.
      puts "CDN key: #{operation.response.name}"
    end

### Check for the result

To check if the CDN key has been created, use the [`projects.locations.operations.get`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.operations/get) method. If the response contains `"done: false"`, repeat the command until the response contains `"done: true"`.

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number; this is located in the **Project number** field on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page
  * `LOCATION`: the location of the data; use one of the [supported regions](https://docs.cloud.google.com/video-stitcher/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `us-west1`
    * `asia-east1`
    * `asia-south1`
    * `asia-southeast1`
    * `europe-west1`
    * `southamerica-east1`
  * `OPERATION_ID`: the identifier for the operation



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.common.OperationMetadata",
        "createTime": CREATE_TIME,
        "endTime": END_TIME,
        "target": "projects/PROJECT_NUMBER/locations/LOCATION/cdnKeys/CDN_KEY_ID",
        "verb": "create",
        "cancelRequested": false,
        "apiVersion": "v1"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.video.stitcher.v1.CdnKey",
        "name": "projects/PROJECT_NUMBER/locations/LOCATION/cdnKeys/CDN_KEY_ID",
        "hostname": "HOSTNAME",
        "mediaCdnKey": {
          "keyName": "MEDIA_CDN_KEYNAME"
        }
      }
    }
    

## Create a VOD config

Before you create a VOD session, you need to create a configuration for it. Many VOD sessions can share the same configuration.

To create the config, use the [`projects.locations.vodConfigs.create`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodConfigs/create) method.

### REST

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number; this is located in the **Project number** field on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page
  * `LOCATION`: the location in which to create your VOD config; use one of the [supported regions](https://docs.cloud.google.com/video-stitcher/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `us-west1`
    * `asia-east1`
    * `asia-south1`
    * `asia-southeast1`
    * `europe-west1`
    * `southamerica-east1`
  * `VOD_CONFIG_ID`: a user-defined identifier for the VOD config. This ID can only contain lower-case letters, numbers, and hyphens. The first character must be a letter, the last character must be a letter or a number, and the entire ID has a 63 character maximum.
  * `VOD_URI`: the URI of the media to stitch. This URI must reference either an MPEG-DASH manifest (MPD) file or an HLS manifest (M3U8) file. Use a public URI or an unsigned URI for which you [registered a CDN key](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-cdn-keys). **Note:** You can use the Transcoder API to create these manifest files. See [Create VOD source files](https://docs.cloud.google.com/video-stitcher/docs/create-vod-source-files) for more information. You must make the manifest files public so that the Video Stitcher API can access them.
  * AD_TAG_URI

the public URI of the ad tag; if you don't have one, you can use a [VMAP Pre-roll](https://developers.google.com/interactive-media-ads/docs/sdks/html5/client-side/tags#vmap-pre-roll) sample



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "sourceUri": "VOD_URI",
      "adTagUri": "AD_TAG_URI"
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/vodConfigs?vodConfigId=VOD_CONFIG_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "sourceUri": "VOD_URI",
      "adTagUri": "AD_TAG_URI"
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/vodConfigs?vodConfigId=VOD_CONFIG_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.common.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_NUMBER/locations/LOCATION/vodConfigs/VOD_CONFIG_ID",
        "verb": "create",
        "cancelRequested": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

This command creates a [long-running operation (LRO)](https://docs.cloud.google.com/video-stitcher/docs/how-to/manage-long-running-operations) that you can query to track progress. For more information, see Check for the result. 

### C#

Before trying this sample, follow the C# setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Video.Stitcher.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using System.Threading.Tasks;
    
    public class CreateVodConfigSample
    {
        public async Task<VodConfig> CreateVodConfigAsync(
            string projectId, string location, string vodConfigId, string sourceUri, string adTagUri)
        {
            // Create the client.
            [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html) client = [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_Create)();
    
            [CreateVodConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CreateVodConfigRequest.html) request = new [CreateVodConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CreateVodConfigRequest.html)
            {
                ParentAsLocationName = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html#Google_Api_Gax_ResourceNames_LocationName_FromProjectLocation_System_String_System_String_)(projectId, location),
                VodConfigId = vodConfigId,
                VodConfig = new [VodConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodConfig.html)
                {
                    SourceUri = sourceUri,
                    AdTagUri = adTagUri
                }
            };
    
            // Make the request.
            Operation<VodConfig, OperationMetadata> response = await client.[CreateVodConfigAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_CreateVodConfigAsync_Google_Api_Gax_ResourceNames_LocationName_Google_Cloud_Video_Stitcher_V1_VodConfig_System_String_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete.
            Operation<VodConfig, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    
            // Retrieve the operation result.
            return completedResponse.Result;
        }
    }
    

### Go

Before trying this sample, follow the Go setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/video/stitcher). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	stitcher "cloud.google.com/go/video/stitcher/apiv1"
    	stitcherstreampb "cloud.google.com/go/video/stitcher/apiv1/stitcherpb"
    )
    
    // createVodConfig creates a VOD config. VOD configs are used to configure VOD sessions.
    func createVodConfig(w io.Writer, projectID, vodConfigID, sourceURI string) error {
    	// projectID := "my-project-id"
    	// vodConfigID := "my-vod-config-id"
    
    	// Uri of the media to stitch; this URI must reference either an MPEG-DASH
    	// manifest (.mpd) file or an M3U playlist manifest (.m3u8) file.
    	// sourceURI := "https://storage.googleapis.com/my-bucket/main.mpd"
    
    	// See https://cloud.google.com/video-stitcher/docs/concepts for information
    	// on ad tags and ad metadata. This sample uses an ad tag URL that displays
    	// a VMAP Pre-roll ad
    	// (https://developers.google.com/interactive-media-ads/docs/sdks/html5/client-side/tags).
    	adTagURI := "https://pubads.g.doubleclick.net/gampad/ads?iu=/21775744923/external/vmap_ad_samples&sz=640x480&cust_params=sample_ar%3Dpreonly&ciu_szs=300x250%2C728x90&gdfp_req=1&ad_rule=1&output=vmap&unviewed_position_start=1&env=vp&impl=s&correlator="
    	location := "us-central1"
    	ctx := context.Background()
    	client, err := stitcher.[NewVideoStitcherClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_NewVideoStitcherClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("stitcher.NewVideoStitcherClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_Close)()
    
    	req := &stitcherstreampb.CreateVodConfigRequest{
    		Parent:      fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    		VodConfigId: vodConfigID,
    		VodConfig: &stitcherstreampb.VodConfig{
    			SourceUri: sourceURI,
    			AdTagUri:  adTagURI,
    		},
    	}
    	// Creates the VOD config.
    	op, err := client.CreateVodConfig(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.CreateVodConfig: %w", err)
    	}
    	response, err := op.Wait(ctx)
    	if err != nil {
    		return err
    	}
    
    	fmt.Fprintf(w, "VOD config: %v", response.GetName())
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/overview). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.stitcher.v1.[CreateVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateVodConfigRequest.html);
    import com.google.cloud.video.stitcher.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LocationName.html);
    import com.google.cloud.video.stitcher.v1.[VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html);
    import com.google.cloud.video.stitcher.v1.[VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateVodConfig {
    
      private static final int TIMEOUT_IN_MINUTES = 2;
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String vodConfigId = "my-vod-config-id";
        // URI of the VOD stream to stitch; this URI must reference either an MPEG-DASH
        // manifest (.mpd) file or an M3U playlist manifest (.m3u8) file.
        String sourceUri = "https://storage.googleapis.com/my-bucket/main.mpd";
        // See VMAP Pre-roll
        // (https://developers.google.com/interactive-media-ads/docs/sdks/html5/client-side/tags)
        String adTagUri = "https://pubads.g.doubleclick.net/gampad/ads...";
    
        createVodConfig(projectId, location, vodConfigId, sourceUri, adTagUri);
      }
    
      // Creates a video on demand (VOD) config. VOD configs are used to configure VOD
      // sessions. For more information, see
      // https://cloud.google.com/video-stitcher/docs/how-to/managing-vod-configs.
      public static [VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig.html) createVodConfig(
          String projectId, String location, String vodConfigId, String sourceUri, String adTagUri)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html) videoStitcherServiceClient =
            [VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html).create()) {
          [CreateVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateVodConfigRequest.html) createVodConfigRequest =
              [CreateVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateVodConfigRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LocationName.html).of(projectId, location).toString())
                  .[setVodConfigId](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateVodConfigRequest.Builder.html#com_google_cloud_video_stitcher_v1_CreateVodConfigRequest_Builder_setVodConfigId_java_lang_String_)(vodConfigId)
                  .setVodConfig(
                      [VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig.html).newBuilder().setSourceUri(sourceUri).setAdTagUri(adTagUri).build())
                  .build();
    
          [VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig.html) response =
              videoStitcherServiceClient
                  .[createVodConfigAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html#com_google_cloud_video_stitcher_v1_VideoStitcherServiceClient_createVodConfigAsync__org_jspecify_annotations_Nullable_com_google_cloud_video_stitcher_v1_LocationName_com_google_cloud_video_stitcher_v1_VodConfig_java_lang_String_)(createVodConfigRequest)
                  .get(TIMEOUT_IN_MINUTES, TimeUnit.MINUTES);
          System.out.println("Created new VOD config: " + response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig.html#com_google_cloud_video_stitcher_v1_VodConfig_getName__)());
          return response;
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // projectId = 'my-project-id';
    // location = 'us-central1';
    // vodConfigId = 'my-vod-config-id';
    // sourceUri = 'https://storage.googleapis.com/my-bucket/main.mpd';
    // See VMAP Pre-roll
    // (https://developers.google.com/interactive-media-ads/docs/sdks/html5/client-side/tags)
    // adTagUri = 'https://pubads.g.doubleclick.net/gampad/ads...';
    
    // Imports the Video Stitcher library
    const {VideoStitcherServiceClient} =
      require('[@google-cloud/video-stitcher](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)').v1;
    // Instantiates a client
    const stitcherClient = new [VideoStitcherServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)();
    
    async function createVodConfig() {
      // Construct request
      const request = {
        parent: stitcherClient.[locationPath](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/v1.videostitcherserviceclient.html)(projectId, location),
        vodConfig: {
          sourceUri: sourceUri,
          adTagUri: adTagUri,
        },
        vodConfigId: vodConfigId,
      };
      const [operation] = await stitcherClient.createVodConfig(request);
      const [response] = await operation.promise();
      console.log(`response.name: ${response.name}`);
    }
    
    createVodConfig().catch(err => {
      console.error(err.message);
      process.exitCode = 1;
    });

### PHP

Before trying this sample, follow the PHP setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/videostitcher/readme). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Stitcher\V1\Client\VideoStitcherServiceClient;
    use Google\Cloud\Video\Stitcher\V1\CreateVodConfigRequest;
    use Google\Cloud\Video\Stitcher\V1\VodConfig;
    
    /**
     * Creates a VOD config. VOD configs are used to configure VOD sessions.
     *
     * @param string $callingProjectId     The project ID to run the API call under
     * @param string $location             The location of the VOD config
     * @param string $vodConfigId          The name of the VOD config to be created
     * @param string $sourceUri            Uri of the media to stitch; this URI must
     *                                     reference either an MPEG-DASH manifest
     *                                     (.mpd) file or an M3U playlist manifest
     *                                     (.m3u8) file.
     * @param string $adTagUri             The Uri of the ad tag
     */
    function create_vod_config(
        string $callingProjectId,
        string $location,
        string $vodConfigId,
        string $sourceUri,
        string $adTagUri
    ): void {
        // Instantiate a client.
        $stitcherClient = new VideoStitcherServiceClient();
    
        $parent = $stitcherClient->locationName($callingProjectId, $location);
    
        $vodConfig = (new VodConfig())
            ->setSourceUri($sourceUri)
            ->setAdTagUri($adTagUri);
    
        // Run VOD config creation request
        $request = (new CreateVodConfigRequest())
            ->setParent($parent)
            ->setVodConfigId($vodConfigId)
            ->setVodConfig($vodConfig);
        $operationResponse = $stitcherClient->createVodConfig($request);
        $operationResponse->pollUntilComplete();
        if ($operationResponse->operationSucceeded()) {
            $result = $operationResponse->getResult();
            // Print results
            printf('VOD config: %s' . PHP_EOL, $result->getName());
        } else {
            $error = $operationResponse->getError();
            // handleError($error)
        }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud.video import stitcher_v1
    from google.cloud.video.stitcher_v1.services.video_stitcher_service import (
        VideoStitcherServiceClient,
    )
    
    
    def create_vod_config(
        project_id: str,
        location: str,
        vod_config_id: str,
        vod_uri: str,
        ad_tag_uri: str,
    ) -> stitcher_v1.types.VodConfig:
        """Creates a VOD config.
        Args:
            project_id: The GCP project ID.
            location: The location in which to create the VOD config.
            vod_config_id: The user-defined VOD config ID.
            vod_uri: URI of the VOD to stitch; this URI must reference either an
                        MPEG-DASH manifest (.mpd) file or an M3U playlist manifest
                        (.m3u8) file.
            ad_tag_uri: Uri of the ad tag.
    
        Returns:
            The VOD config resource.
        """
    
        client = VideoStitcherServiceClient()
    
        parent = f"projects/{project_id}/locations/{location}"
    
        vod_config = stitcher_v1.types.VodConfig(
            source_uri=vod_uri,
            ad_tag_uri=ad_tag_uri,
        )
    
        operation = client.create_vod_config(
            parent=parent, vod_config_id=vod_config_id, vod_config=vod_config
        )
        response = operation.result()
        print(f"VOD config: {response.name}")
        return response
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/video/stitcher"
    
    ##
    # Create a VOD config. VOD configs are used to create VOD sessions.
    #
    # @param project_id [String] Your Google Cloud project (e.g. `my-project`)
    # @param location [String] The location (e.g. `us-central1`)
    # @param vod_config_id [String] Your VOD config name (e.g. `my-vod-config`)
    # @param source_uri [String] Uri of the VOD stream to stitch
    #   (e.g. `https://storage.googleapis.com/my-bucket/main.mpd`)
    # @param ad_tag_uri [String] Uri of the ad tag
    #   (e.g. `https://pubads.g.doubleclick.net/gampad/ads...`)
    #
    def create_vod_config project_id:, location:, vod_config_id:, source_uri:,
                          ad_tag_uri:
      # Create a Video Stitcher client.
      client = Google::Cloud::Video::Stitcher.video_stitcher_service
    
      # Build the resource name of the parent.
      parent = client.location_path project: project_id, location: location
    
      # Set the VOD config fields.
      new_vod_config = {
        source_uri: source_uri,
        ad_tag_uri: ad_tag_uri
      }
    
      operation = client.create_vod_config parent: parent,
                                           vod_config_id: vod_config_id,
                                           vod_config: new_vod_config
    
      # The returned object is of type Gapic::Operation. You can use this
      # object to check the status of an operation, cancel it, or wait
      # for results. Here is how to block until completion:
      operation.wait_until_done!
    
      # Print the VOD config name.
      puts "VOD config: #{operation.response.name}"
    end

## Get the config

To get the config, use the [`projects.locations.vodConfigs.get`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodConfigs/get) method.

### REST

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number; this is located in the **Project number** field on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page
  * `LOCATION`: the location of the VOD config; use one of the [supported regions](https://docs.cloud.google.com/video-stitcher/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `us-west1`
    * `asia-east1`
    * `asia-south1`
    * `asia-southeast1`
    * `europe-west1`
    * `southamerica-east1`
  * `VOD_CONFIG_ID`: the user-defined identifier for the VOD config



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/vodConfigs/VOD_CONFIG_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/vodConfigs/VOD_CONFIG_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/vodConfigs/VOD_CONFIG_ID",
      "sourceUri": "VOD_URI",
      "adTagUri": "AD_TAG_URI",
      "state": "READY"
    }
    

### C#

Before trying this sample, follow the C# setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Video.Stitcher.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.html);
    
    public class GetVodConfigSample
    {
        public VodConfig GetVodConfig(
            string projectId, string location, string vodConfigId)
        {
            // Create the client.
            [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html) client = [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_Create)();
    
            [GetVodConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.GetVodConfigRequest.html) request = new [GetVodConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.GetVodConfigRequest.html)
            {
                VodConfigName = [VodConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodConfigName.html).[FromProjectLocationVodConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodConfigName.html#Google_Cloud_Video_Stitcher_V1_VodConfigName_FromProjectLocationVodConfig_System_String_System_String_System_String_)(projectId, location, vodConfigId)
            };
    
            // Call the API.
            [VodConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodConfig.html) response = client.[GetVodConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_GetVodConfig_Google_Cloud_Video_Stitcher_V1_GetVodConfigRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Return the result.
            return response;
        }
    }
    

### Go

Before trying this sample, follow the Go setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/video/stitcher). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"encoding/json"
    	"fmt"
    	"io"
    
    	stitcher "cloud.google.com/go/video/stitcher/apiv1"
    	stitcherstreampb "cloud.google.com/go/video/stitcher/apiv1/stitcherpb"
    )
    
    // getVodConfig gets a previously-created VOD config.
    func getVodConfig(w io.Writer, projectID, vodConfigID string) error {
    	// projectID := "my-project-id"
    	// vodConfigID := "my-vod-config-id"
    	location := "us-central1"
    	ctx := context.Background()
    	client, err := stitcher.[NewVideoStitcherClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_NewVideoStitcherClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("stitcher.NewVideoStitcherClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_Close)()
    
    	req := &stitcherstreampb.GetVodConfigRequest{
    		Name: fmt.Sprintf("projects/%s/locations/%s/vodConfigs/%s", projectID, location, vodConfigID),
    	}
    
    	response, err := client.GetVodConfig(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.GetVodConfig: %w", err)
    	}
    	b, err := json.MarshalIndent(response, "", " ")
    	if err != nil {
    		return fmt.Errorf("json.MarshalIndent: %w", err)
    	}
    
    	fmt.Fprintf(w, "VOD config:\n%s", string(b))
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/overview). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.stitcher.v1.[GetVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetVodConfigRequest.html);
    import com.google.cloud.video.stitcher.v1.[VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html);
    import com.google.cloud.video.stitcher.v1.[VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig.html);
    import com.google.cloud.video.stitcher.v1.[VodConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfigName.html);
    import java.io.IOException;
    
    public class GetVodConfig {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String vodConfigId = "my-vod-config-id";
    
        getVodConfig(projectId, location, vodConfigId);
      }
    
      // Gets a video on demand (VOD) config.
      public static [VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig.html) getVodConfig(String projectId, String location, String vodConfigId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html) videoStitcherServiceClient =
            [VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html).create()) {
          [GetVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetVodConfigRequest.html) getVodConfigRequest =
              [GetVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetVodConfigRequest.html).newBuilder()
                  .setName([VodConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfigName.html).of(projectId, location, vodConfigId).toString())
                  .build();
    
          [VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig.html) response = videoStitcherServiceClient.getVodConfig(getVodConfigRequest);
          System.out.println("VOD config: " + response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig.html#com_google_cloud_video_stitcher_v1_VodConfig_getName__)());
          return response;
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // projectId = 'my-project-id';
    // location = 'us-central1';
    // vodConfigId = 'my-vod-config-id';
    
    // Imports the Video Stitcher library
    const {VideoStitcherServiceClient} =
      require('[@google-cloud/video-stitcher](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)').v1;
    // Instantiates a client
    const stitcherClient = new [VideoStitcherServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)();
    
    async function getVodConfig() {
      // Construct request
      const request = {
        name: stitcherClient.[vodConfigPath](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/v1.videostitcherserviceclient.html)(projectId, location, vodConfigId),
      };
      const [vodConfig] = await stitcherClient.getVodConfig(request);
      console.log(`VOD config: ${vodConfig.name}`);
    }
    
    getVodConfig().catch(err => {
      console.error(err.message);
      process.exitCode = 1;
    });

### PHP

Before trying this sample, follow the PHP setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/videostitcher/readme). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Stitcher\V1\Client\VideoStitcherServiceClient;
    use Google\Cloud\Video\Stitcher\V1\GetVodConfigRequest;
    
    /**
     * Gets a VOD config.
     *
     * @param string $callingProjectId     The project ID to run the API call under
     * @param string $location             The location of the VOD config
     * @param string $vodConfigId         The ID of the VOD config
     */
    function get_vod_config(
        string $callingProjectId,
        string $location,
        string $vodConfigId
    ): void {
        // Instantiate a client.
        $stitcherClient = new VideoStitcherServiceClient();
    
        $formattedName = $stitcherClient->vodConfigName($callingProjectId, $location, $vodConfigId);
        $request = (new GetVodConfigRequest())
            ->setName($formattedName);
        $vodConfig = $stitcherClient->getVodConfig($request);
    
        // Print results
        printf('VOD config: %s' . PHP_EOL, $vodConfig->getName());
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud.video import stitcher_v1
    from google.cloud.video.stitcher_v1.services.video_stitcher_service import (
        VideoStitcherServiceClient,
    )
    
    
    def get_vod_config(
        project_id: str, location: str, vod_config_id: str
    ) -> stitcher_v1.types.VodConfig:
        """Gets a VOD config.
        Args:
            project_id: The GCP project ID.
            location: The location of the VOD config.
            vod_config_id: The user-defined VOD config ID.
    
        Returns:
            The VOD config resource.
        """
    
        client = VideoStitcherServiceClient()
    
        name = f"projects/{project_id}/locations/{location}/vodConfigs/{vod_config_id}"
        response = client.get_vod_config(name=name)
        print(f"VOD config: {response.name}")
        return response
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/video/stitcher"
    
    ##
    # Get a VOD config
    #
    # @param project_id [String] Your Google Cloud project (e.g. `my-project`)
    # @param location [String] The location (e.g. `us-central1`)
    # @param vod_config_id [String] Your VOD config name (e.g. `my-vod-config`)
    #
    def get_vod_config project_id:, location:, vod_config_id:
      # Create a Video Stitcher client.
      client = Google::Cloud::Video::Stitcher.video_stitcher_service
    
      # Build the resource name of the VOD config.
      name = client.vod_config_path project: project_id, location: location,
                                    vod_config: vod_config_id
    
      # Get the VOD config.
      vod_config = client.get_vod_config name: name
    
      # Print the vod config name.
      puts "VOD config: #{vod_config.name}"
    end

Check that the state is set to `READY`. If not, wait for a few seconds and send the request again.

## Create a session

To create a session for an ad-stitched video, use the [`projects.locations.vodSessions.create`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodSessions/create) method.

### REST

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number located in the **Project number** field on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page
  * `LOCATION`: the location in which to create your session; use one of the [supported regions](https://docs.cloud.google.com/video-stitcher/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `us-west1`
    * `asia-east1`
    * `asia-south1`
    * `asia-southeast1`
    * `europe-west1`
    * `southamerica-east1`
  * `VOD_CONFIG_ID`: the user-defined identifier for the VOD config 



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "vodConfig": "projects/PROJECT_NUMBER/locations/LOCATION/vodConfigs/VOD_CONFIG_ID",
      "adTracking": "SERVER"
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/vodSessions"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "vodConfig": "projects/PROJECT_NUMBER/locations/LOCATION/vodConfigs/VOD_CONFIG_ID",
      "adTracking": "SERVER"
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/vodSessions" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/vodSessions/SESSION_ID",
      "interstitials": {
        "sessionContent": {
          "duration": "60s"
        }
      },
      "playUri": "PLAY_URI", # This is the ad-stitched VOD URI
      "sourceUri": "VOD_URI",
      "adTagUri": "AD_TAG_URI",
      "assetId": "ASSET_ID",
      "adTracking": "SERVER",
      "vodConfig": "projects/PROJECT_NUMBER/locations/LOCATION/vodConfigs/VOD_CONFIG_ID"
    }
    

### C#

Before trying this sample, follow the C# setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Video.Stitcher.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.html);
    
    public class CreateVodSessionSample
    {
        public VodSession CreateVodSession(
            string projectId, string location, string vodConfigId)
        {
            // Create the client.
            [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html) client = [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_Create)();
    
            [CreateVodSessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CreateVodSessionRequest.html) request = new [CreateVodSessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CreateVodSessionRequest.html)
            {
                ParentAsLocationName = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html#Google_Api_Gax_ResourceNames_LocationName_FromProjectLocation_System_String_System_String_)(projectId, location),
                VodSession = new [VodSession](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodSession.html)
                {
                    VodConfig = [VodConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodConfigName.html).[FormatProjectLocationVodConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodConfigName.html#Google_Cloud_Video_Stitcher_V1_VodConfigName_FormatProjectLocationVodConfig_System_String_System_String_System_String_)(projectId, location, vodConfigId),
                    AdTracking = [AdTracking](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.AdTracking.html).[Server](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.AdTracking.html#Google_Cloud_Video_Stitcher_V1_AdTracking_Server)
                }
            };
    
            // Call the API.
            [VodSession](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodSession.html) session = client.[CreateVodSession](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_CreateVodSession_Google_Api_Gax_ResourceNames_LocationName_Google_Cloud_Video_Stitcher_V1_VodSession_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Return the result.
            return session;
        }
    }
    

### Go

Before trying this sample, follow the Go setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/video/stitcher). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	stitcher "cloud.google.com/go/video/stitcher/apiv1"
    	stitcherstreampb "cloud.google.com/go/video/stitcher/apiv1/stitcherpb"
    )
    
    // createVodSession creates a video on demand (VOD) session in which to insert ads.
    // VOD sessions are ephemeral resources that expire after a few hours.
    func createVodSession(w io.Writer, projectID, vodConfigID string) error {
    	// projectID := "my-project-id"
    	// vodConfigID := "my-vod-config-id"
    	location := "us-central1"
    	ctx := context.Background()
    	client, err := stitcher.[NewVideoStitcherClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_NewVideoStitcherClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("stitcher.NewVideoStitcherClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_Close)()
    
    	req := &stitcherstreampb.CreateVodSessionRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    		VodSession: &stitcherstreampb.VodSession{
    			VodConfig:  fmt.Sprintf("projects/%s/locations/%s/vodConfigs/%s", projectID, location, vodConfigID),
    			AdTracking: stitcherstreampb.AdTracking_SERVER,
    		},
    	}
    	// Creates the VOD session.
    	response, err := client.CreateVodSession(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.CreateVodSession: %w", err)
    	}
    
    	fmt.Fprintf(w, "VOD session: %v", response.GetName())
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/overview). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.stitcher.v1.[AdTracking](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.AdTracking.html);
    import com.google.cloud.video.stitcher.v1.[CreateVodSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateVodSessionRequest.html);
    import com.google.cloud.video.stitcher.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LocationName.html);
    import com.google.cloud.video.stitcher.v1.[VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html);
    import com.google.cloud.video.stitcher.v1.[VodConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfigName.html);
    import com.google.cloud.video.stitcher.v1.[VodSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodSession.html);
    import java.io.IOException;
    
    public class CreateVodSession {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String vodConfigId = "my-vod-config-id";
    
        createVodSession(projectId, location, vodConfigId);
      }
    
      // Creates a video on demand (VOD) session using the parameters in the designated VOD config.
      // For more information, see
      // https://cloud.google.com/video-stitcher/docs/how-to/creating-vod-sessions.
      public static [VodSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodSession.html) createVodSession(String projectId, String location, String vodConfigId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html) videoStitcherServiceClient =
            [VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html).create()) {
          [CreateVodSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateVodSessionRequest.html) createVodSessionRequest =
              [CreateVodSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateVodSessionRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LocationName.html).of(projectId, location).toString())
                  .setVodSession(
                      [VodSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodSession.html).newBuilder()
                          .setVodConfig([VodConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfigName.html).format(projectId, location, vodConfigId))
                          .setAdTracking([AdTracking](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.AdTracking.html).SERVER)
                          .build())
                  .build();
    
          [VodSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodSession.html) response = videoStitcherServiceClient.createVodSession(createVodSessionRequest);
          System.out.println("Created VOD session: " + response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodSession.html#com_google_cloud_video_stitcher_v1_VodSession_getName__)());
          return response;
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // projectId = 'my-project-id';
    // location = 'us-central1';
    // vodConfigId = 'my-vod-config-id';
    
    // Imports the Video Stitcher library
    const {VideoStitcherServiceClient} =
      require('[@google-cloud/video-stitcher](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)').v1;
    // Instantiates a client
    const stitcherClient = new [VideoStitcherServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)();
    
    async function createVodSession() {
      // Construct request
      const request = {
        parent: stitcherClient.[locationPath](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/v1.videostitcherserviceclient.html)(projectId, location),
        vodSession: {
          vodConfig: stitcherClient.[vodConfigPath](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/v1.videostitcherserviceclient.html)(
            projectId,
            location,
            vodConfigId
          ),
          adTracking: '[SERVER](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/protos.google.cloud.video.stitcher.v1.adtracking.html)',
        },
      };
      const [session] = await stitcherClient.createVodSession(request);
      console.log(`VOD session: ${session.name}`);
    }
    
    createVodSession().catch(err => {
      console.error(err.message);
      process.exitCode = 1;
    });

### PHP

Before trying this sample, follow the PHP setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/videostitcher/readme). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Stitcher\V1\AdTracking;
    use Google\Cloud\Video\Stitcher\V1\Client\VideoStitcherServiceClient;
    use Google\Cloud\Video\Stitcher\V1\CreateVodSessionRequest;
    use Google\Cloud\Video\Stitcher\V1\VodSession;
    
    /**
     * Creates a VOD session. VOD sessions are ephemeral resources that expire
     * after a few hours.
     *
     * @param string $callingProjectId     The project ID to run the API call under
     * @param string $location             The location of the session
     * @param string $vodConfigId          The name of the VOD config to use for the session
     */
    function create_vod_session(
        string $callingProjectId,
        string $location,
        string $vodConfigId
    ): void {
        // Instantiate a client.
        $stitcherClient = new VideoStitcherServiceClient();
    
        $parent = $stitcherClient->locationName($callingProjectId, $location);
        $vodConfig = $stitcherClient->vodConfigName($callingProjectId, $location, $vodConfigId);
        $vodSession = new VodSession();
        $vodSession->setVodConfig($vodConfig);
        $vodSession->setAdTracking(AdTracking::SERVER);
    
        // Run VOD session creation request
        $request = (new CreateVodSessionRequest())
            ->setParent($parent)
            ->setVodSession($vodSession);
        $response = $stitcherClient->createVodSession($request);
    
        // Print results
        printf('VOD session: %s' . PHP_EOL, $response->getName());
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud.video import stitcher_v1
    from google.cloud.video.stitcher_v1.services.video_stitcher_service import (
        VideoStitcherServiceClient,
    )
    
    
    def create_vod_session(
        project_id: str, location: str, vod_config_id: str
    ) -> stitcher_v1.types.VodSession:
        """Creates a VOD session. VOD sessions are ephemeral resources that expire
        after a few hours.
        Args:
            project_id: The GCP project ID.
            location: The location in which to create the session.
            vod_config_id: The user-defined VOD config ID to use to create the
                            session.
    
        Returns:
            The VOD session resource.
        """
    
        client = VideoStitcherServiceClient()
    
        parent = f"projects/{project_id}/locations/{location}"
        vod_config_name = (
            f"projects/{project_id}/locations/{location}/vodConfigs/{vod_config_id}"
        )
    
        vod_session = stitcher_v1.types.VodSession(
            vod_config=vod_config_name, ad_tracking="SERVER"
        )
    
        response = client.create_vod_session(parent=parent, vod_session=vod_session)
        print(f"VOD session: {response.name}")
        return response
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/video/stitcher"
    
    ##
    # Create a video on demand (VOD) session. VOD sessions are ephemeral resources
    # that expire after a few hours.
    #
    # @param project_id [String] Your Google Cloud project (e.g. `my-project`)
    # @param location [String] The location (e.g. `us-central1`)
    # @param vod_config_id [String] The VOD config ID (e.g. `my-vod-config`) to use
    #
    def create_vod_session project_id:, location:, vod_config_id:
      # Create a Video Stitcher client.
      client = Google::Cloud::Video::Stitcher.video_stitcher_service
    
      # Build the resource name of the parent.
      parent = client.location_path project: project_id, location: location
    
      # Build the resource name of the VOD config.
      vod_config_name = client.vod_config_path project: project_id,
                                               location: location,
                                               vod_config: vod_config_id
    
      # Set the session fields.
      new_vod_session = {
        vod_config: vod_config_name,
        ad_tracking: Google::Cloud::Video::Stitcher::V1::AdTracking::SERVER
      }
    
      response = client.create_vod_session parent: parent,
                                           vod_session: new_vod_session
    
      # Print the VOD session name.
      puts "VOD session: #{response.name}"
    end

The Video Stitcher API generates a unique session ID for each request. A session expires after 4 hours.

## Confirm that the ad was stitched

An ad must be encoded before it can be stitched into a VOD session.

If the ad you specified in the `vodSessions.create` command has already been encoded from a previous session, the Video Stitcher API includes `adBreaks` events in the JSON response. The Video Stitcher API only looks for encoded ads created by sessions associated with your Google Cloud project.

If the ad has not yet been encoded, the JSON response doesn't include `adBreaks` events. If you receive a JSON response similar to the one in the previous section, wait for ad encoding and re-run the `vodSessions.create` command.

When the encoded ad has been successfully stitched into the session, the response should look like the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/vodSessions/SESSION_ID",
      "interstitials": {
        "adBreaks": [
          {
            "progressEvents": [
              {
                "timeOffset": "0s",
                "events": [
                  {
                    "type": "IMPRESSION",
                    "uri": "https://securepubads.g.doubleclick.net/pcs/view..."
                  },
                  {
                    "type": "START",
                    "uri": "https://pubads.g.doubleclick.net/pagead/interaction/..."
                  },
                  ...
                ]
              },
              ...
            ],
            "ads": [
              {
                "duration": "10s",
                "activityEvents": [
                  {
                    "type": "ERROR",
                    "uri": "https://pubads.g.doubleclick.net/pagead/interaction/..."
                  },
                  {
                    "type": "CLICK_THROUGH",
                    "uri": "https://pubads.g.doubleclick.net/pcs/click...",
                    "id": "GDFP"
                  },
                  ...
                ]
              }
            ],
            "endTimeOffset": "10s",
            "startTimeOffset": "0s"
          }
        ],
        "sessionContent": {
          "duration": "70s"
        }
      },
      "playUri": "PLAY_URI",
      "sourceUri": "VOD_URI",
      "adTagUri": "AD_TAG_URI",
      "assetId": "ASSET_ID",
      "adTracking": "SERVER",
      "vodConfig": "projects/PROJECT_NUMBER/locations/LOCATION/vodConfigs/VOD_CONFIG_ID"
    }

You can play the ad-stitched VOD stream by referencing the URI from the `playUri` field of the response object.

**Note:** A single VOD asset may be transcoded into different variants based on bandwidth, resolution, and frame rate. The Video Stitcher API may need to encode the same ad multiple times to match the source VOD variant. For example, suppose you create a session for a 720p VOD asset and a given ad. The same ad must be encoded again if you create a session for the same VOD asset content at 1080p.

## Play the ad-stitched VOD stream

Play the ad-stitched VOD stream using the URI from the `playUri` field of the response object. To play this VOD session in [Shaka Player](https://shaka-player-demo.appspot.com/demo/), complete the following steps:

  1. Navigate to [Shaka Player](https://shaka-player-demo.appspot.com/demo/), an online media player.
  2. Click **Custom Content** in the top navigation bar.
  3. Click the **+** button.
  4. Paste the value of the `playUri` field (PLAY_URI) into the **Manifest URL** box.

![](https://docs.cloud.google.com/static/video-stitcher/images/shaka-player.png)

  5. Type a name in the **Name** box.

  6. Click **Save**.

  7. Click **Play**.




If your video is located in a Cloud Storage bucket, make sure that the [bucket is public and CORS is enabled](https://docs.cloud.google.com/transcoder/docs/transcode-video#play_video) on the bucket.

See an example [ad-stitched video](https://docs.cloud.google.com/static/video-stitcher/images/quickstart.mp4) that uses the [Transcoder API sample video](https://docs.cloud.google.com/transcoder/docs/transcode-video#transcode_video) and a [VMAP Pre-roll](https://developers.google.com/interactive-media-ads/docs/sdks/html5/client-side/tags#vmap-pre-roll) ad tag URL.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

**Note:** You must manually delete all user-generated content from your project (for example, [slates](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-slates#delete_slate) and [CDN keys](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-cdn-keys#delete_cdn_key)). The Video Stitcher API does not automatically delete this content, even if you remove the service or delete the project. 

### Delete the VOD config

To delete the VOD config, do the following:

### REST

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number; this is located in the **Project number** field on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page
  * `LOCATION`: the location of the VOD config; use one of the [supported regions](https://docs.cloud.google.com/video-stitcher/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `us-west1`
    * `asia-east1`
    * `asia-south1`
    * `asia-southeast1`
    * `europe-west1`
    * `southamerica-east1`
  * `VOD_CONFIG_ID`: the user-defined identifier for the VOD config



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/vodConfigs/VOD_CONFIG_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/vodConfigs/VOD_CONFIG_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.common.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_NUMBER/locations/LOCATION/vodConfigs/VOD_CONFIG_ID",
        "verb": "delete"
      },
      "done": false
    }
    

This command creates a [long-running operation (LRO)](https://docs.cloud.google.com/video-stitcher/docs/how-to/manage-long-running-operations) that you can query to track progress. For more information, see Check for the result. 

### C#

Before trying this sample, follow the C# setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Video.Stitcher.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System.Threading.Tasks;
    
    public class DeleteVodConfigSample
    {
        public async Task DeleteVodConfigAsync(
            string projectId, string location, string vodConfigId)
        {
            // Create the client.
            [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html) client = [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_Create)();
    
            [DeleteVodConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.DeleteVodConfigRequest.html) request = new [DeleteVodConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.DeleteVodConfigRequest.html)
            {
                VodConfigName = [VodConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodConfigName.html).[FromProjectLocationVodConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodConfigName.html#Google_Cloud_Video_Stitcher_V1_VodConfigName_FromProjectLocationVodConfig_System_String_System_String_System_String_)(projectId, location, vodConfigId)
            };
    
            // Make the request.
            Operation<Empty, OperationMetadata> response = await client.[DeleteVodConfigAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_DeleteVodConfigAsync_Google_Cloud_Video_Stitcher_V1_DeleteVodConfigRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete.
            await response.PollUntilCompletedAsync();
        }
    }
    

### Go

Before trying this sample, follow the Go setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/video/stitcher). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	stitcher "cloud.google.com/go/video/stitcher/apiv1"
    	stitcherstreampb "cloud.google.com/go/video/stitcher/apiv1/stitcherpb"
    )
    
    // deleteVodConfig deletes a previously-created VOD config.
    func deleteVodConfig(w io.Writer, projectID, vodConfigID string) error {
    	// projectID := "my-project-id"
    	// vodConfigID := "my-vod-config-id"
    	location := "us-central1"
    	ctx := context.Background()
    	client, err := stitcher.[NewVideoStitcherClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_NewVideoStitcherClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("stitcher.NewVideoStitcherClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_Close)()
    
    	req := &stitcherstreampb.DeleteVodConfigRequest{
    		Name: fmt.Sprintf("projects/%s/locations/%s/vodConfigs/%s", projectID, location, vodConfigID),
    	}
    	// Deletes the VOD config.
    	op, err := client.DeleteVodConfig(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.DeleteVodConfig: %w", err)
    	}
    	err = op.Wait(ctx)
    	if err != nil {
    		return err
    	}
    
    	fmt.Fprintf(w, "Deleted VOD config")
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/overview). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.stitcher.v1.[DeleteVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteVodConfigRequest.html);
    import com.google.cloud.video.stitcher.v1.[VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html);
    import com.google.cloud.video.stitcher.v1.[VodConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfigName.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class DeleteVodConfig {
    
      private static final int TIMEOUT_IN_MINUTES = 2;
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String vodConfigId = "my-vod-config-id";
    
        deleteVodConfig(projectId, location, vodConfigId);
      }
    
      // Deletes a video on demand (VOD) config.
      public static void deleteVodConfig(String projectId, String location, String vodConfigId)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html) videoStitcherServiceClient =
            [VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html).create()) {
          [DeleteVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteVodConfigRequest.html) deleteVodConfigRequest =
              [DeleteVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteVodConfigRequest.html).newBuilder()
                  .setName([VodConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfigName.html).of(projectId, location, vodConfigId).toString())
                  .build();
    
          videoStitcherServiceClient
              .[deleteVodConfigAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html#com_google_cloud_video_stitcher_v1_VideoStitcherServiceClient_deleteVodConfigAsync__org_jspecify_annotations_Nullable_com_google_cloud_video_stitcher_v1_VodConfigName_)(deleteVodConfigRequest)
              .get(TIMEOUT_IN_MINUTES, TimeUnit.MINUTES);
          System.out.println("Deleted VOD config");
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // projectId = 'my-project-id';
    // location = 'us-central1';
    // vodConfigId = 'my-vod-config-id';
    
    // Imports the Video Stitcher library
    const {VideoStitcherServiceClient} =
      require('[@google-cloud/video-stitcher](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)').v1;
    // Instantiates a client
    const stitcherClient = new [VideoStitcherServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)();
    
    async function deleteVodConfig() {
      // Construct request
      const request = {
        name: stitcherClient.[vodConfigPath](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/v1.videostitcherserviceclient.html)(projectId, location, vodConfigId),
      };
      const [operation] = await stitcherClient.deleteVodConfig(request);
      await operation.promise();
      console.log('Deleted VOD config');
    }
    
    deleteVodConfig().catch(err => {
      console.error(err.message);
      process.exitCode = 1;
    });

### PHP

Before trying this sample, follow the PHP setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/videostitcher/readme). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Stitcher\V1\Client\VideoStitcherServiceClient;
    use Google\Cloud\Video\Stitcher\V1\DeleteVodConfigRequest;
    
    /**
     * Deletes a VOD config.
     *
     * @param string $callingProjectId     The project ID to run the API call under
     * @param string $location             The location of the VOD config
     * @param string $vodConfigId         The ID of the VOD config
     */
    function delete_vod_config(
        string $callingProjectId,
        string $location,
        string $vodConfigId
    ): void {
        // Instantiate a client.
        $stitcherClient = new VideoStitcherServiceClient();
    
        $formattedName = $stitcherClient->vodConfigName($callingProjectId, $location, $vodConfigId);
        $request = (new DeleteVodConfigRequest())
            ->setName($formattedName);
        $operationResponse = $stitcherClient->deleteVodConfig($request);
        $operationResponse->pollUntilComplete();
        if ($operationResponse->operationSucceeded()) {
            // Print status
            printf('Deleted VOD config %s' . PHP_EOL, $vodConfigId);
        } else {
            $error = $operationResponse->getError();
            // handleError($error)
        }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud.video.stitcher_v1.services.video_stitcher_service import (
        VideoStitcherServiceClient,
    )
    from google.protobuf import empty_pb2 as empty
    
    
    def delete_vod_config(
        project_id: str, location: str, vod_config_id: str
    ) -> empty.Empty:
        """Deletes a VOD config.
        Args:
            project_id: The GCP project ID.
            location: The location of the VOD config.
            vod_config_id: The user-defined VOD config ID."""
    
        client = VideoStitcherServiceClient()
    
        name = f"projects/{project_id}/locations/{location}/vodConfigs/{vod_config_id}"
        operation = client.delete_vod_config(name=name)
        response = operation.result()
        print("Deleted VOD config")
        return response
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/video/stitcher"
    
    ##
    # Delete a VOD config
    #
    # @param project_id [String] Your Google Cloud project (e.g. `my-project`)
    # @param location [String] The location (e.g. `us-central1`)
    # @param vod_config_id [String] Your VOD config name (e.g. `my-vod-config`)
    #
    def delete_vod_config project_id:, location:, vod_config_id:
      # Create a Video Stitcher client.
      client = Google::Cloud::Video::Stitcher.video_stitcher_service
    
      # Build the resource name of the VOD config.
      name = client.vod_config_path project: project_id, location: location,
                                    vod_config: vod_config_id
    
      # Delete the VOD config.
      operation = client.delete_vod_config name: name
    
      # The returned object is of type Gapic::Operation. You can use this
      # object to check the status of an operation, cancel it, or wait
      # for results. Here is how to block until completion:
      operation.wait_until_done!
    
      # Print a success message.
      puts "Deleted VOD config"
    end

### Delete the CDN key

To delete the CDN key, do the following:

### REST

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number; this is located in the **Project number** field on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page
  * `LOCATION`: the location where your CDN key is located; use one of the [supported regions](https://docs.cloud.google.com/video-stitcher/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `us-west1`
    * `asia-east1`
    * `asia-south1`
    * `asia-southeast1`
    * `europe-west1`
    * `southamerica-east1`
  * `CDN_KEY_ID`: a user-defined identifier for the CDN key



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/cdnKeys/CDN_KEY_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/cdnKeys/CDN_KEY_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.common.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_NUMBER/locations/LOCATION/cdnKeys/CDN_KEY_ID",
        "verb": "delete",
        "cancelRequested": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

This command creates a [long-running operation (LRO)](https://docs.cloud.google.com/video-stitcher/docs/how-to/manage-long-running-operations) that you can query to track progress. For more information, see Check for the result. 

### C#

Before trying this sample, follow the C# setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Video.Stitcher.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System.Threading.Tasks;
    
    public class DeleteCdnKeySample
    {
        public async Task DeleteCdnKeyAsync(
            string projectId, string location, string cdnKeyId)
        {
            // Create the client.
            [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html) client = [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_Create)();
    
            [DeleteCdnKeyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.DeleteCdnKeyRequest.html) request = new [DeleteCdnKeyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.DeleteCdnKeyRequest.html)
            {
                CdnKeyName = [CdnKeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CdnKeyName.html).[FromProjectLocationCdnKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CdnKeyName.html#Google_Cloud_Video_Stitcher_V1_CdnKeyName_FromProjectLocationCdnKey_System_String_System_String_System_String_)(projectId, location, cdnKeyId)
            };
    
            // Make the request.
            Operation<Empty, OperationMetadata> response = await client.[DeleteCdnKeyAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_DeleteCdnKeyAsync_Google_Cloud_Video_Stitcher_V1_CdnKeyName_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete.
            await response.PollUntilCompletedAsync();
        }
    }
    

### Go

Before trying this sample, follow the Go setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/video/stitcher). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	stitcher "cloud.google.com/go/video/stitcher/apiv1"
    	stitcherstreampb "cloud.google.com/go/video/stitcher/apiv1/stitcherpb"
    )
    
    // deleteCDNKey deletes a CDN key.
    func deleteCDNKey(w io.Writer, projectID, keyID string) error {
    	// projectID := "my-project-id"
    	// keyID := "my-cdn-key"
    	location := "us-central1"
    	ctx := context.Background()
    	client, err := stitcher.[NewVideoStitcherClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_NewVideoStitcherClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("stitcher.NewVideoStitcherClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_Close)()
    
    	name := fmt.Sprintf("projects/%s/locations/%s/cdnKeys/%s", projectID, location, keyID)
    
    	req := &stitcherstreampb.DeleteCdnKeyRequest{
    		Name: name,
    	}
    	// Deletes the CDN key.
    	op, err := client.DeleteCdnKey(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.DeleteCdnKey: %w", err)
    	}
    	err = op.Wait(ctx)
    	if err != nil {
    		return err
    	}
    
    	fmt.Fprintf(w, "Deleted CDN key")
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/overview). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.stitcher.v1.[CdnKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKeyName.html);
    import com.google.cloud.video.stitcher.v1.[DeleteCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteCdnKeyRequest.html);
    import com.google.cloud.video.stitcher.v1.[VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class DeleteCdnKey {
    
      private static final int TIMEOUT_IN_MINUTES = 2;
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String cdnKeyId = "my-cdn-key-id";
    
        deleteCdnKey(projectId, location, cdnKeyId);
      }
    
      // Deletes a CDN key.
      public static void deleteCdnKey(String projectId, String location, String cdnKeyId)
          throws InterruptedException, ExecutionException, TimeoutException, IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html) videoStitcherServiceClient =
            [VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html).create()) {
          [DeleteCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteCdnKeyRequest.html) deleteCdnKeyRequest =
              [DeleteCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteCdnKeyRequest.html).newBuilder()
                  .setName([CdnKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKeyName.html).of(projectId, location, cdnKeyId).toString())
                  .build();
    
          videoStitcherServiceClient
              .[deleteCdnKeyAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html#com_google_cloud_video_stitcher_v1_VideoStitcherServiceClient_deleteCdnKeyAsync__org_jspecify_annotations_Nullable_com_google_cloud_video_stitcher_v1_CdnKeyName_)(deleteCdnKeyRequest)
              .get(TIMEOUT_IN_MINUTES, TimeUnit.MINUTES);
          System.out.println("Deleted CDN key");
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // projectId = 'my-project-id';
    // location = 'us-central1';
    // cdnKeyId = 'my-cdn-key';
    
    // Imports the Video Stitcher library
    const {VideoStitcherServiceClient} =
      require('[@google-cloud/video-stitcher](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)').v1;
    // Instantiates a client
    const stitcherClient = new [VideoStitcherServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)();
    
    async function deleteCdnKey() {
      // Construct request
      const request = {
        name: stitcherClient.[cdnKeyPath](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/v1.videostitcherserviceclient.html)(projectId, location, cdnKeyId),
      };
      const [operation] = await stitcherClient.deleteCdnKey(request);
      await operation.promise();
      console.log('Deleted CDN key');
    }
    
    deleteCdnKey().catch(err => {
      console.error(err.message);
      process.exitCode = 1;
    });

### PHP

Before trying this sample, follow the PHP setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/videostitcher/readme). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Stitcher\V1\Client\VideoStitcherServiceClient;
    use Google\Cloud\Video\Stitcher\V1\DeleteCdnKeyRequest;
    
    /**
     * Deletes a CDN key.
     *
     * @param string $callingProjectId     The project ID to run the API call under
     * @param string $location             The location of the CDN key
     * @param string $cdnKeyId             The ID of the CDN key
     */
    function delete_cdn_key(
        string $callingProjectId,
        string $location,
        string $cdnKeyId
    ): void {
        // Instantiate a client.
        $stitcherClient = new VideoStitcherServiceClient();
    
        $formattedName = $stitcherClient->cdnKeyName($callingProjectId, $location, $cdnKeyId);
        $request = (new DeleteCdnKeyRequest())
            ->setName($formattedName);
        $operationResponse = $stitcherClient->deleteCdnKey($request);
        $operationResponse->pollUntilComplete();
        if ($operationResponse->operationSucceeded()) {
            // Print status
            printf('Deleted CDN key %s' . PHP_EOL, $cdnKeyId);
        } else {
            $error = $operationResponse->getError();
            // handleError($error)
        }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud.video.stitcher_v1.services.video_stitcher_service import (
        VideoStitcherServiceClient,
    )
    from google.protobuf import empty_pb2 as empty
    
    
    def delete_cdn_key(project_id: str, location: str, cdn_key_id: str) -> empty.Empty:
        """Deletes a CDN key.
        Args:
            project_id: The GCP project ID.
            location: The location of the CDN key.
            cdn_key_id: The user-defined CDN key ID."""
    
        client = VideoStitcherServiceClient()
    
        name = f"projects/{project_id}/locations/{location}/cdnKeys/{cdn_key_id}"
        operation = client.delete_cdn_key(name=name)
        response = operation.result()
        print("Deleted CDN key")
        return response
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/video/stitcher"
    
    ##
    # Delete a CDN key
    #
    # @param project_id [String] Your Google Cloud project (e.g. `my-project`)
    # @param location [String] The location (e.g. `us-central1`)
    # @param cdn_key_id [String] Your CDN key name (e.g. `my-cdn-key`)
    #
    def delete_cdn_key project_id:, location:, cdn_key_id:
      # Create a Video Stitcher client.
      client = Google::Cloud::Video::Stitcher.video_stitcher_service
    
      # Build the resource name of the CDN key.
      name = client.cdn_key_path project: project_id, location: location,
                                 cdn_key: cdn_key_id
    
      # Delete the CDN key.
      operation = client.delete_cdn_key name: name
    
      # The returned object is of type Gapic::Operation. You can use this
      # object to check the status of an operation, cancel it, or wait
      # for results. Here is how to block until completion:
      operation.wait_until_done!
    
      # Print a success message.
      puts "Deleted CDN key"
    end

### Revoke your credentials

  1. Optional: Revoke the authentication credentials that you created, and delete the local credential file. 
         
         gcloud auth application-default revoke

  2. Optional: Revoke credentials from the gcloud CLI. 
         
         gcloud auth revoke




## What's next

Review the [Video Stitcher API reference documentation](https://docs.cloud.google.com/video-stitcher/docs/reference).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
