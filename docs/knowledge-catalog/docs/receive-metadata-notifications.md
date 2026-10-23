---
url: https://docs.cloud.google.com/knowledge-catalog/docs/receive-metadata-notifications/
title: Receive notifications with metadata change feeds \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:50:52.179529+00:00
---

# Receive notifications with metadata change feeds  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/receive-metadata-notifications/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Receive notifications with metadata change feeds Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure Knowledge Catalog (formerly Dataplex Universal Catalog) metadata change feeds to receive notifications through Pub/Sub when metadata within Knowledge Catalog is created, updated, or deleted.

For more information about metadata change feeds, see [Metadata change feeds overview](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-change-feeds-overview).

## Before you begin

Familiarize yourself with [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview) and the [Dataplex API](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest).

  1. Enable the Dataplex API and Pub/Sub APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com,pubsub.googleapis.com)

  2. Create a Pub/Sub topic to receive notifications. For more information, see [Create a topic](https://docs.cloud.google.com/pubsub/docs/create-topic).

  3. [Install `gcloud`](https://docs.cloud.google.com/sdk/docs/install). Make sure the short alias of `gcloud` is set.

  4. Set an alias of `gcurl`. This creates a shortcut that includes your authentication token and sets the JSON content-type for API requests:
         
         alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
         

  5. Set the `DATAPLEX_API` variable:
         
         DATAPLEX_API="dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION"
         

Replace the following:

     * `PROJECT_ID`: your project ID where the Dataplex API is enabled
     * `LOCATION`: the location where the job runs—for example, `us-central1`, `europe-west3`, or `asia-south1`



## Required roles and permissions

To configure metadata change feeds, ensure that you and the [Knowledge Catalog service account](https://docs.cloud.google.com/knowledge-catalog/docs/iam-and-access-control#service-agent) have the required IAM roles and permissions.

### User roles and permissions

To get the permissions that you need to export metadata and access metadata change feeds messages, ask your administrator to grant you the following IAM roles on the project or organization: 

  * Export metadata: [Dataplex Entry Group Exporter ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupExporter) (`roles/dataplex.entryGroupExporter`) 
  * Access metadata change feeds messages: [Pub/Sub Subscriber ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.subscriber) (`roles/pubsub.subscriber`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to export metadata and access metadata change feeds messages. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to export metadata and access metadata change feeds messages:

  * Export metadata: 
    * `dataplex.metadataFeeds.create` on the project
    * `dataplex.entryGroups.export` on the resource defining the scope of the feed (Organization, Project, or Entry Group)
    * `resourcemanager.projects.get` on the project
    * `resourcemanager.projects.list` on the project
  * Access metadata change feeds messages: 
    * `pubsub.subscriptions.consume` on the subscription
    * `pubsub.topics.attachSubscription` on the topic



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Knowledge Catalog service account roles and permissions

To ensure that the Knowledge Catalog service account has the necessary permission to publish metadata change feeds messages, ask your administrator to grant the Pub/Sub Publisher (`roles/pubsub.publisher`) and Pub/Sub Viewer (`roles/pubsub.viewer`) IAM role to the Knowledge Catalog service account on the Pub/Sub topic. **Important:** You must grant this role to the Knowledge Catalog service account, _not_ to your user account. Failure to grant the role to the correct principal might result in permission errors.  For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `pubsub.topics.publish` and `pubsub.topics.get` permission, which is required to publish metadata change feeds messages. 

Your administrator might also be able to give the Knowledge Catalog service account this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Grant permissions to the Knowledge Catalog service account

The service agent in Knowledge Catalog is created when you enable the Dataplex API. You can identify the service agent by its email ID:

`service-PROJECT_NUMBER@gcp-sa-dataplex.iam.gserviceaccount.com`

Here, `PROJECT_NUMBER` is the project number of the project where you enabled the Dataplex API.

The Knowledge Catalog service account requires the ability to publish messages to your Pub/Sub topic and retrieve topic metadata. To grant these permissions, give the service account the [Pub/Sub Publisher role](https://docs.cloud.google.com/iam/docs/understanding-roles#pubsub.publisher) (`roles/pubsub.publisher`) and the [Pub/Sub Viewer role](https://docs.cloud.google.com/iam/docs/understanding-roles#pubsub.viewer) (`roles/pubsub.viewer`) on the Pub/Sub topic:

### gcloud

Run the [`gcloud pubsub topics add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/add-iam-policy-binding) command:
    
    
    gcloud pubsub topics add-iam-policy-binding TOPIC_ID \
        --member="serviceAccount:service-PROJECT_NUMBER@gcp-sa-dataplex.iam.gserviceaccount.com" \
        --role="roles/pubsub.publisher"
    
    gcloud pubsub topics add-iam-policy-binding TOPIC_ID \
        --member="serviceAccount:service-PROJECT_NUMBER@gcp-sa-dataplex.iam.gserviceaccount.com" \
        --role="roles/pubsub.viewer"
    

Replace the following:

  * `TOPIC_ID`: the ID of your Pub/Sub topic to which the metadata change feed messages are published.
  * `PROJECT_NUMBER`: the project number of your Knowledge Catalog project where the service account is located.



### Console

  1. In the Google Cloud console, go to the Pub/Sub **Topics** page.

[Go to topics](https://console.cloud.google.com/cloudpubsub/topic/list)

  2. Select the topic you're using for metadata feed notifications and if required click **Show info panel**.

  3. In the **Permissions** tab, click **Add principal**.

  4. In the **New principals** field, enter the Knowledge Catalog service account: `service-PROJECT_NUMBER@gcp-sa-dataplex.iam.gserviceaccount.com`.

  5. In the **Assign roles** field, select **Pub/Sub Publisher**.

  6. Click **Add another role** and select **Pub/Sub Viewer**.

  7. Click **Save**.




## Create a metadata change feed

To control which changes generate notifications, you can configure a metadata change feed to monitor specific resources. You do this by specifying a scope, such as your entire organization, specific projects, or specific entry groups. While scope lets you define _which_ resources to monitor, you can use filters to further refine _when_ Knowledge Catalog sends notifications.

For more information, see [Metadata change feed](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-change-feeds-overview#terminology).

### C#

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    
    public sealed partial class GeneratedCatalogServiceClientSnippets
    {
        /// <summary>Snippet for CreateMetadataFeed</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void CreateMetadataFeedRequestObject()
        {
            // Create client
            [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_Create)();
            // Initialize request argument(s)
            [CreateMetadataFeedRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CreateMetadataFeedRequest.html) request = new [CreateMetadataFeedRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CreateMetadataFeedRequest.html)
            {
                ParentAsLocationName = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html#Google_Api_Gax_ResourceNames_LocationName_FromProjectLocation_System_String_System_String_)("[PROJECT]", "[LOCATION]"),
                MetadataFeed = new [MetadataFeed](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.MetadataFeed.html)(),
                MetadataFeedId = "",
                ValidateOnly = false,
            };
            // Make the request
            Operation<MetadataFeed, OperationMetadata> response = catalogServiceClient.[CreateMetadataFeed](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_CreateMetadataFeed_Google_Api_Gax_ResourceNames_LocationName_Google_Cloud_Dataplex_V1_MetadataFeed_System_String_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete
            Operation<MetadataFeed, OperationMetadata> completedResponse = response.PollUntilCompleted();
            // Retrieve the operation result
            [MetadataFeed](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.MetadataFeed.html) result = completedResponse.Result;
    
            // Or get the name of the operation
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name
            Operation<MetadataFeed, OperationMetadata> retrievedResponse = catalogServiceClient.[PollOnceCreateMetadataFeed](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_PollOnceCreateMetadataFeed_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
            // Check if the retrieved long-running operation has completed
            if (retrievedResponse.IsCompleted)
            {
                // If it has completed, then access the result
                [MetadataFeed](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.MetadataFeed.html) retrievedResult = retrievedResponse.Result;
            }
        }
    }

### Go

### Go

Before trying this sample, follow the Go setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataplex). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	dataplex "cloud.google.com/go/dataplex/apiv1"
    	dataplexpb "cloud.google.com/go/dataplex/apiv1/dataplexpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataplex.[NewCatalogClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataplex/latest/apiv1.html#cloud_google_com_go_dataplex_apiv1_CatalogClient_NewCatalogClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataplexpb.CreateMetadataFeedRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataplex/apiv1/dataplexpb#CreateMetadataFeedRequest.
    	}
    	op, err := c.CreateMetadataFeed(ctx, req)
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

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html);
    import com.google.cloud.dataplex.v1.[CreateMetadataFeedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateMetadataFeedRequest.html);
    import com.google.cloud.dataplex.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LocationName.html);
    import com.google.cloud.dataplex.v1.[MetadataFeed](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataFeed.html);
    
    public class SyncCreateMetadataFeed {
    
      public static void main(String[] args) throws Exception {
        syncCreateMetadataFeed();
      }
    
      public static void syncCreateMetadataFeed() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html).create()) {
          [CreateMetadataFeedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateMetadataFeedRequest.html) request =
              [CreateMetadataFeedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateMetadataFeedRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LocationName.html).of("[PROJECT]", "[LOCATION]").toString())
                  .setMetadataFeed([MetadataFeed](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataFeed.html).newBuilder().build())
                  .[setMetadataFeedId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateMetadataFeedRequest.Builder.html#com_google_cloud_dataplex_v1_CreateMetadataFeedRequest_Builder_setMetadataFeedId_java_lang_String_)("metadataFeedId1633421160")
                  .setValidateOnly(true)
                  .build();
          [MetadataFeed](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataFeed.html) response = catalogServiceClient.[createMetadataFeedAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html#com_google_cloud_dataplex_v1_CatalogServiceClient_createMetadataFeedAsync__org_jspecify_annotations_Nullable_com_google_cloud_dataplex_v1_LocationName_com_google_cloud_dataplex_v1_MetadataFeed_java_lang_String_)(request).get();
        }
      }
    }

### Node.js

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. The resource name of the parent location, in the format
     *  `projects/{project_id_or_number}/locations/{location_id}`
     */
    // const parent = 'abc123'
    /**
     *  Required. The metadata job resource.
     */
    // const metadataFeed = {}
    /**
     *  Optional. The metadata job ID. If not provided, a unique ID is generated
     *  with the prefix `metadata-job-`.
     */
    // const metadataFeedId = 'abc123'
    /**
     *  Optional. The service validates the request without performing any
     *  mutations. The default is false.
     */
    // const validateOnly = true
    
    // Imports the Dataplex library
    const {CatalogServiceClient} = require('[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)').v1;
    
    // Instantiates a client
    const dataplexClient = new [CatalogServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)();
    
    async function callCreateMetadataFeed() {
      // Construct request
      const request = {
        parent,
        metadataFeed,
      };
    
      // Run request
      const [operation] = await dataplexClient.createMetadataFeed(request);
      const [response] = await operation.promise();
      console.log(response);
    }
    
    callCreateMetadataFeed();

### Python

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
    
    def sample_create_metadata_feed():
        # Create a client
        client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html)()
    
        # Initialize request argument(s)
        metadata_feed = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[MetadataFeed](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.MetadataFeed.html)()
        metadata_feed.pubsub_topic = "pubsub_topic_value"
    
        request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CreateMetadataFeedRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.CreateMetadataFeedRequest.html)(
            parent="parent_value",
            metadata_feed=metadata_feed,
        )
    
        # Make the request
        operation = client.[create_metadata_feed](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html#google_cloud_dataplex_v1_services_catalog_service_CatalogServiceClient_create_metadata_feed)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    
    

### REST

To create a metadata change feed, use the [`projects.locations.metadataFeeds.create`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.metadataFeeds/create) method.

**Organization scope**

Run the following command to create a metadata change feed that monitors the entire organization:
    
    
    gcurl -X POST -d "$(cat <<EOF
    {
      "scope": {
        "organizationLevel": true
      },
      "pubsubTopic": "projects/PROJECT_ID_PUBSUB/topics/TOPIC_ID"
    }
    EOF
    )" "https://${DATAPLEX_API}/metadataFeeds?metadataFeedId=FEED_ID"
    

Replace the following:

  * `PROJECT_ID_PUBSUB`: the project ID where the Pub/Sub topic is located—for example, `example-project`
  * `TOPIC_ID`: the Pub/Sub topic ID to which the metadata change feed messages are published—for example, `example-topic`
  * `FEED_ID`: the metadata change feed ID that you want to create—for example, `example-feed`



**Project scope**

Run the following command to create a metadata change feed that monitors specific projects:
    
    
    gcurl -X POST -d "$(cat <<EOF
    {
      "scope": {
        "projects": [
          "projects/PROJECT_ID_1",
          "projects/PROJECT_ID_2"
        ]
      },
      "pubsubTopic": "projects/PROJECT_ID_PUBSUB/topics/TOPIC_ID"
    }
    EOF
    )" "https://${DATAPLEX_API}/metadataFeeds?metadataFeedId=FEED_ID"
    

Replace the following:

  * `PROJECT_ID_PUBSUB`: the project ID where the Pub/Sub topic is located—for example, `example-project`
  * `TOPIC_ID`: the Pub/Sub topic ID to which the metadata change feed messages are published—for example, `example-topic`
  * `FEED_ID`: the metadata change feed ID that you want to create—for example, `example-feed`



**Entry group scope**

Run the following command to create a metadata change feed that monitors specific entry groups:
    
    
    gcurl -X POST -d "$(cat <<EOF
    {
      "scope": {
        "entryGroups": [
          "projects/PROJECT_ID/locations/LOCATION/entryGroups/ENTRY_GROUP_ID_1",
          "projects/PROJECT_ID/locations/LOCATION/entryGroups/ENTRY_GROUP_ID_2"
        ]
      },
      "pubsubTopic": "projects/PROJECT_ID_PUBSUB/topics/TOPIC_ID"
    }
    EOF
    )" "https://${DATAPLEX_API}/metadataFeeds?metadataFeedId=FEED_ID"
    

Replace the following:

  * `PROJECT_ID_PUBSUB`: the project ID where the Pub/Sub topic is located—for example, `example-project`
  * `LOCATION`: the location where you want to create the feed—for example, `us-central1`
  * `ENTRY_GROUP_ID`: the entry group ID to monitor—for example, `example-entry-group`
  * `TOPIC_ID`: the Pub/Sub topic ID to which the metadata change feed messages are published—for example, `example-topic`
  * `FEED_ID`: the metadata change feed ID that you want to create—for example, `example-feed`



**With filters**

Run the following command to create a metadata change feed with filters (filtering by entry type):
    
    
    gcurl -X POST -d "$(cat <<EOF
    {
      "scope": {
        "projects": [
          "projects/PROJECT_ID_1",
          "projects/PROJECT_ID_2"
        ]
      },
      "filter": {
        "entryTypes": [
          "projects/PROJECT_ID/locations/global/entryTypes/bigquery-table"
        ]
      },
      "pubsubTopic": "projects/PROJECT_ID_PUBSUB/topics/TOPIC_ID"
    }
    EOF
    )" "https://${DATAPLEX_API}/metadataFeeds?metadataFeedId=FEED_ID"
    

Replace the following:

  * `PROJECT_ID_PUBSUB`: the project ID where the Pub/Sub topic is located—for example, `example-project`
  * `TOPIC_ID`: the Pub/Sub topic ID to which the metadata change feed messages are published—for example, `example-topic`
  * `FEED_ID`: the metadata change feed ID that you want to create—for example, `example-feed`



Response:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.dataplex.v1.OperationMetadata",
        "createTime": "2023-10-02T15:01:23Z",
        "target": "projects/PROJECT_ID/locations/LOCATION/metadataFeeds/FEED_ID",
        "verb": "create",
        "apiVersion": "v1"
      },
      "done": false
    }
    

## View a metadata change feed

You can view the details of a metadata change feed.

### C#

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.html);
    
    public sealed partial class GeneratedCatalogServiceClientSnippets
    {
        /// <summary>Snippet for GetMetadataFeed</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void GetMetadataFeedRequestObject()
        {
            // Create client
            [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_Create)();
            // Initialize request argument(s)
            [GetMetadataFeedRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.GetMetadataFeedRequest.html) request = new [GetMetadataFeedRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.GetMetadataFeedRequest.html)
            {
                MetadataFeedName = [MetadataFeedName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.MetadataFeedName.html).[FromProjectLocationMetadataFeed](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.MetadataFeedName.html#Google_Cloud_Dataplex_V1_MetadataFeedName_FromProjectLocationMetadataFeed_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[METADATA_FEED]"),
            };
            // Make the request
            [MetadataFeed](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.MetadataFeed.html) response = catalogServiceClient.[GetMetadataFeed](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_GetMetadataFeed_Google_Cloud_Dataplex_V1_GetMetadataFeedRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
        }
    }

### Go

### Go

Before trying this sample, follow the Go setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataplex). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	dataplex "cloud.google.com/go/dataplex/apiv1"
    	dataplexpb "cloud.google.com/go/dataplex/apiv1/dataplexpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataplex.[NewCatalogClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataplex/latest/apiv1.html#cloud_google_com_go_dataplex_apiv1_CatalogClient_NewCatalogClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataplexpb.GetMetadataFeedRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataplex/apiv1/dataplexpb#GetMetadataFeedRequest.
    	}
    	resp, err := c.GetMetadataFeed(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### Java

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html);
    import com.google.cloud.dataplex.v1.[GetMetadataFeedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetMetadataFeedRequest.html);
    import com.google.cloud.dataplex.v1.[MetadataFeed](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataFeed.html);
    import com.google.cloud.dataplex.v1.[MetadataFeedName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataFeedName.html);
    
    public class SyncGetMetadataFeed {
    
      public static void main(String[] args) throws Exception {
        syncGetMetadataFeed();
      }
    
      public static void syncGetMetadataFeed() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html).create()) {
          [GetMetadataFeedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetMetadataFeedRequest.html) request =
              [GetMetadataFeedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetMetadataFeedRequest.html).newBuilder()
                  .setName([MetadataFeedName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataFeedName.html).of("[PROJECT]", "[LOCATION]", "[METADATA_FEED]").toString())
                  .build();
          [MetadataFeed](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataFeed.html) response = catalogServiceClient.getMetadataFeed(request);
        }
      }
    }

### Node.js

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. The resource name of the metadata feed, in the format
     *  `projects/{project_id_or_number}/locations/{location_id}/MetadataFeeds/{metadata_feed_id}`.
     */
    // const name = 'abc123'
    
    // Imports the Dataplex library
    const {CatalogServiceClient} = require('[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)').v1;
    
    // Instantiates a client
    const dataplexClient = new [CatalogServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)();
    
    async function callGetMetadataFeed() {
      // Construct request
      const request = {
        name,
      };
    
      // Run request
      const response = await dataplexClient.getMetadataFeed(request);
      console.log(response);
    }
    
    callGetMetadataFeed();

### Python

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
    
    def sample_get_metadata_feed():
        # Create a client
        client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html)()
    
        # Initialize request argument(s)
        request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[GetMetadataFeedRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.GetMetadataFeedRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_metadata_feed](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html#google_cloud_dataplex_v1_services_catalog_service_CatalogServiceClient_get_metadata_feed)(request=request)
    
        # Handle the response
        print(response)
    
    

### REST

To view a metadata change feed, use the [`projects.locations.metadataFeeds.get`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.metadataFeeds/get) method.

Run the following command:
    
    
    gcurl "https://${DATAPLEX_API}/metadataFeeds/FEED_ID"
    

Replace the following:

  * `FEED_ID`: the metadata change feed ID that you want to view—for example, `example-feed`



## List metadata change feeds

You can list the metadata change feeds in a project and location.

### C#

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.html);
    using System;
    
    public sealed partial class GeneratedCatalogServiceClientSnippets
    {
        /// <summary>Snippet for ListMetadataFeeds</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void ListMetadataFeedsRequestObject()
        {
            // Create client
            [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_Create)();
            // Initialize request argument(s)
            [ListMetadataFeedsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListMetadataFeedsRequest.html) request = new [ListMetadataFeedsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListMetadataFeedsRequest.html)
            {
                ParentAsLocationName = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html#Google_Api_Gax_ResourceNames_LocationName_FromProjectLocation_System_String_System_String_)("[PROJECT]", "[LOCATION]"),
                Filter = "",
                OrderBy = "",
            };
            // Make the request
            PagedEnumerable<ListMetadataFeedsResponse, MetadataFeed> response = catalogServiceClient.[ListMetadataFeeds](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_ListMetadataFeeds_Google_Api_Gax_ResourceNames_LocationName_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Iterate over all response items, lazily performing RPCs as required
            foreach ([MetadataFeed](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.MetadataFeed.html) item in response)
            {
                // Do something with each item
                Console.WriteLine(item);
            }
    
            // Or iterate over pages (of server-defined size), performing one RPC per page
            foreach ([ListMetadataFeedsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListMetadataFeedsResponse.html) page in response.AsRawResponses())
            {
                // Do something with each page of items
                Console.WriteLine("A page of results:");
                foreach ([MetadataFeed](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.MetadataFeed.html) item in page)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
            }
    
            // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
            int pageSize = 10;
            Page<MetadataFeed> singlePage = response.ReadPage(pageSize);
            // Do something with the page of items
            Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
            foreach ([MetadataFeed](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.MetadataFeed.html) item in singlePage)
            {
                // Do something with each item
                Console.WriteLine(item);
            }
            // Store the pageToken, for when the next page is required.
            string nextPageToken = singlePage.NextPageToken;
        }
    }

### Go

### Go

Before trying this sample, follow the Go setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataplex). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	dataplex "cloud.google.com/go/dataplex/apiv1"
    	dataplexpb "cloud.google.com/go/dataplex/apiv1/dataplexpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataplex.[NewCatalogClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataplex/latest/apiv1.html#cloud_google_com_go_dataplex_apiv1_CatalogClient_NewCatalogClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataplexpb.ListMetadataFeedsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataplex/apiv1/dataplexpb#ListMetadataFeedsRequest.
    	}
    	it := c.ListMetadataFeeds(ctx, req)
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
    		_ = it.Response.(*dataplexpb.ListMetadataFeedsResponse)
    	}
    }
    

### Java

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html);
    import com.google.cloud.dataplex.v1.[ListMetadataFeedsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListMetadataFeedsRequest.html);
    import com.google.cloud.dataplex.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LocationName.html);
    import com.google.cloud.dataplex.v1.[MetadataFeed](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataFeed.html);
    
    public class SyncListMetadataFeeds {
    
      public static void main(String[] args) throws Exception {
        syncListMetadataFeeds();
      }
    
      public static void syncListMetadataFeeds() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html).create()) {
          [ListMetadataFeedsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListMetadataFeedsRequest.html) request =
              [ListMetadataFeedsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListMetadataFeedsRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LocationName.html).of("[PROJECT]", "[LOCATION]").toString())
                  .setPageSize(883849137)
                  .setPageToken("pageToken873572522")
                  .setFilter("filter-1274492040")
                  .setOrderBy("orderBy-1207110587")
                  .build();
          for ([MetadataFeed](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataFeed.html) element : catalogServiceClient.listMetadataFeeds(request).iterateAll()) {
            // doThingsWith(element);
          }
        }
      }
    }

### Node.js

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. The resource name of the parent location, in the format
     *  `projects/{project_id_or_number}/locations/{location_id}`
     */
    // const parent = 'abc123'
    /**
     *  Optional. The maximum number of metadata feeds to return. The service
     *  might return fewer feeds than this value. If unspecified, at most 10 feeds
     *  are returned. The maximum value is 1,000.
     */
    // const pageSize = 1234
    /**
     *  Optional. The page token received from a previous `ListMetadataFeeds` call.
     *  Provide this token to retrieve the subsequent page of results. When
     *  paginating, all other parameters that are provided to the
     *  `ListMetadataFeeds` request must match the call that provided the
     *  page token.
     */
    // const pageToken = 'abc123'
    /**
     *  Optional. Filter request. Filters are case-sensitive.
     *  The service supports the following formats:
     *  * `labels.key1 = "value1"`
     *  * `labels:key1`
     *  * `name = "value"`
     *  You can combine filters with `AND`, `OR`, and `NOT` operators.
     */
    // const filter = 'abc123'
    /**
     *  Optional. The field to sort the results by, either `name` or `create_time`.
     *  If not specified, the ordering is undefined.
     */
    // const orderBy = 'abc123'
    
    // Imports the Dataplex library
    const {CatalogServiceClient} = require('[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)').v1;
    
    // Instantiates a client
    const dataplexClient = new [CatalogServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)();
    
    async function callListMetadataFeeds() {
      // Construct request
      const request = {
        parent,
      };
    
      // Run request
      const iterable = dataplexClient.[listMetadataFeedsAsync](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/v1.catalogserviceclient.html)(request);
      for await (const response of iterable) {
          console.log(response);
      }
    }
    
    callListMetadataFeeds();

### Python

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
    
    def sample_list_metadata_feeds():
        # Create a client
        client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html)()
    
        # Initialize request argument(s)
        request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[ListMetadataFeedsRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListMetadataFeedsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_metadata_feeds](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html#google_cloud_dataplex_v1_services_catalog_service_CatalogServiceClient_list_metadata_feeds)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    
    

### REST

To list metadata change feeds, use the [`projects.locations.metadataFeeds.list`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.metadataFeeds/list) method.

Run the following command:
    
    
    gcurl "https://${DATAPLEX_API}/metadataFeeds"
    

## Update a metadata change feed

You can update the scope or filters of an existing metadata change feed.

### C#

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    
    public sealed partial class GeneratedCatalogServiceClientSnippets
    {
        /// <summary>Snippet for UpdateMetadataFeed</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void UpdateMetadataFeedRequestObject()
        {
            // Create client
            [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_Create)();
            // Initialize request argument(s)
            [UpdateMetadataFeedRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.UpdateMetadataFeedRequest.html) request = new [UpdateMetadataFeedRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.UpdateMetadataFeedRequest.html)
            {
                MetadataFeed = new [MetadataFeed](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.MetadataFeed.html)(),
                UpdateMask = new [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)(),
                ValidateOnly = false,
            };
            // Make the request
            Operation<MetadataFeed, OperationMetadata> response = catalogServiceClient.[UpdateMetadataFeed](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_UpdateMetadataFeed_Google_Cloud_Dataplex_V1_MetadataFeed_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete
            Operation<MetadataFeed, OperationMetadata> completedResponse = response.PollUntilCompleted();
            // Retrieve the operation result
            [MetadataFeed](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.MetadataFeed.html) result = completedResponse.Result;
    
            // Or get the name of the operation
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name
            Operation<MetadataFeed, OperationMetadata> retrievedResponse = catalogServiceClient.[PollOnceUpdateMetadataFeed](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_PollOnceUpdateMetadataFeed_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
            // Check if the retrieved long-running operation has completed
            if (retrievedResponse.IsCompleted)
            {
                // If it has completed, then access the result
                [MetadataFeed](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.MetadataFeed.html) retrievedResult = retrievedResponse.Result;
            }
        }
    }

### Go

### Go

Before trying this sample, follow the Go setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataplex). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	dataplex "cloud.google.com/go/dataplex/apiv1"
    	dataplexpb "cloud.google.com/go/dataplex/apiv1/dataplexpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataplex.[NewCatalogClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataplex/latest/apiv1.html#cloud_google_com_go_dataplex_apiv1_CatalogClient_NewCatalogClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataplexpb.UpdateMetadataFeedRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataplex/apiv1/dataplexpb#UpdateMetadataFeedRequest.
    	}
    	op, err := c.UpdateMetadataFeed(ctx, req)
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

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html);
    import com.google.cloud.dataplex.v1.[MetadataFeed](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataFeed.html);
    import com.google.cloud.dataplex.v1.[UpdateMetadataFeedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateMetadataFeedRequest.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    
    public class SyncUpdateMetadataFeed {
    
      public static void main(String[] args) throws Exception {
        syncUpdateMetadataFeed();
      }
    
      public static void syncUpdateMetadataFeed() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html).create()) {
          [UpdateMetadataFeedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateMetadataFeedRequest.html) request =
              [UpdateMetadataFeedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateMetadataFeedRequest.html).newBuilder()
                  .setMetadataFeed([MetadataFeed](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataFeed.html).newBuilder().build())
                  .setUpdateMask([FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().build())
                  .setValidateOnly(true)
                  .build();
          [MetadataFeed](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataFeed.html) response = catalogServiceClient.[updateMetadataFeedAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html#com_google_cloud_dataplex_v1_CatalogServiceClient_updateMetadataFeedAsync_com_google_cloud_dataplex_v1_MetadataFeed_com_google_protobuf_FieldMask_)(request).get();
        }
      }
    }

### Node.js

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. Update description.
     *  Only fields specified in `update_mask` are updated.
     */
    // const metadataFeed = {}
    /**
     *  Optional. Mask of fields to update.
     */
    // const updateMask = {}
    /**
     *  Optional. Only validate the request, but do not perform mutations.
     *  The default is false.
     */
    // const validateOnly = true
    
    // Imports the Dataplex library
    const {CatalogServiceClient} = require('[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)').v1;
    
    // Instantiates a client
    const dataplexClient = new [CatalogServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)();
    
    async function callUpdateMetadataFeed() {
      // Construct request
      const request = {
        metadataFeed,
      };
    
      // Run request
      const [operation] = await dataplexClient.updateMetadataFeed(request);
      const [response] = await operation.promise();
      console.log(response);
    }
    
    callUpdateMetadataFeed();

### Python

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
    
    def sample_update_metadata_feed():
        # Create a client
        client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html)()
    
        # Initialize request argument(s)
        metadata_feed = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[MetadataFeed](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.MetadataFeed.html)()
        metadata_feed.pubsub_topic = "pubsub_topic_value"
    
        request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[UpdateMetadataFeedRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.UpdateMetadataFeedRequest.html)(
            metadata_feed=metadata_feed,
        )
    
        # Make the request
        operation = client.[update_metadata_feed](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html#google_cloud_dataplex_v1_services_catalog_service_CatalogServiceClient_update_metadata_feed)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    
    

### REST

To update a metadata change feed, use the [`projects.locations.metadataFeeds.patch`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.metadataFeeds/patch) method.

Run the following command to update the metadata change feed to remove the entry type filters:
    
    
    gcurl -X PATCH -d "$(cat <<EOF
    {
      "filter": {
        "entryTypes": []
      }
    }
    EOF
    )" "https://${DATAPLEX_API}/metadataFeeds/FEED_ID?updateMask=filter"
    

Replace the following:

  * `FEED_ID`: the metadata change feed ID that you want to update—for example, `example-feed`



## Delete a metadata change feed

You can delete a metadata change feed if you no longer need to receive notifications.

Deleting a metadata change feed stops the feed from publishing new metadata changes to your Pub/Sub topic. However, it doesn't delete the topic or the subscription associated with the feed. You must delete them manually if they're no longer needed.

Before you delete the feed or the subscription, ensure that your subscriber applications have processed all outstanding messages in the Pub/Sub subscription.

### C#

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    
    public sealed partial class GeneratedCatalogServiceClientSnippets
    {
        /// <summary>Snippet for DeleteMetadataFeed</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void DeleteMetadataFeedRequestObject()
        {
            // Create client
            [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_Create)();
            // Initialize request argument(s)
            [DeleteMetadataFeedRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DeleteMetadataFeedRequest.html) request = new [DeleteMetadataFeedRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DeleteMetadataFeedRequest.html)
            {
                MetadataFeedName = [MetadataFeedName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.MetadataFeedName.html).[FromProjectLocationMetadataFeed](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.MetadataFeedName.html#Google_Cloud_Dataplex_V1_MetadataFeedName_FromProjectLocationMetadataFeed_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[METADATA_FEED]"),
            };
            // Make the request
            Operation<Empty, OperationMetadata> response = catalogServiceClient.[DeleteMetadataFeed](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_DeleteMetadataFeed_Google_Cloud_Dataplex_V1_DeleteMetadataFeedRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete
            Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
            // Retrieve the operation result
            [Empty](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html) result = completedResponse.Result;
    
            // Or get the name of the operation
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name
            Operation<Empty, OperationMetadata> retrievedResponse = catalogServiceClient.[PollOnceDeleteMetadataFeed](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_PollOnceDeleteMetadataFeed_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
            // Check if the retrieved long-running operation has completed
            if (retrievedResponse.IsCompleted)
            {
                // If it has completed, then access the result
                [Empty](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html) retrievedResult = retrievedResponse.Result;
            }
        }
    }

### Go

### Go

Before trying this sample, follow the Go setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataplex). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	dataplex "cloud.google.com/go/dataplex/apiv1"
    	dataplexpb "cloud.google.com/go/dataplex/apiv1/dataplexpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataplex.[NewCatalogClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataplex/latest/apiv1.html#cloud_google_com_go_dataplex_apiv1_CatalogClient_NewCatalogClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataplexpb.DeleteMetadataFeedRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataplex/apiv1/dataplexpb#DeleteMetadataFeedRequest.
    	}
    	op, err := c.DeleteMetadataFeed(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### Java

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html);
    import com.google.cloud.dataplex.v1.[DeleteMetadataFeedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteMetadataFeedRequest.html);
    import com.google.cloud.dataplex.v1.[MetadataFeedName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataFeedName.html);
    import com.google.protobuf.[Empty](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html);
    
    public class SyncDeleteMetadataFeed {
    
      public static void main(String[] args) throws Exception {
        syncDeleteMetadataFeed();
      }
    
      public static void syncDeleteMetadataFeed() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html).create()) {
          [DeleteMetadataFeedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteMetadataFeedRequest.html) request =
              [DeleteMetadataFeedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteMetadataFeedRequest.html).newBuilder()
                  .setName([MetadataFeedName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataFeedName.html).of("[PROJECT]", "[LOCATION]", "[METADATA_FEED]").toString())
                  .build();
          catalogServiceClient.[deleteMetadataFeedAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html#com_google_cloud_dataplex_v1_CatalogServiceClient_deleteMetadataFeedAsync__org_jspecify_annotations_Nullable_com_google_cloud_dataplex_v1_MetadataFeedName_)(request).get();
        }
      }
    }

### Node.js

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. The resource name of the metadata feed, in the format
     *  `projects/{project_id_or_number}/locations/{location_id}/MetadataFeeds/{metadata_feed_id}`.
     */
    // const name = 'abc123'
    
    // Imports the Dataplex library
    const {CatalogServiceClient} = require('[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)').v1;
    
    // Instantiates a client
    const dataplexClient = new [CatalogServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)();
    
    async function callDeleteMetadataFeed() {
      // Construct request
      const request = {
        name,
      };
    
      // Run request
      const [operation] = await dataplexClient.deleteMetadataFeed(request);
      const [response] = await operation.promise();
      console.log(response);
    }
    
    callDeleteMetadataFeed();

### Python

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
    
    def sample_delete_metadata_feed():
        # Create a client
        client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html)()
    
        # Initialize request argument(s)
        request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[DeleteMetadataFeedRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.DeleteMetadataFeedRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = client.[delete_metadata_feed](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html#google_cloud_dataplex_v1_services_catalog_service_CatalogServiceClient_delete_metadata_feed)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    
    

### REST

To delete a metadata change feed, use the [`projects.locations.metadataFeeds.delete`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.metadataFeeds/delete) method.

Run the following command:
    
    
    gcurl -X DELETE \
    "https://${DATAPLEX_API}/metadataFeeds/FEED_ID"
    

Replace the following:

  * `FEED_ID`: the metadata change feed ID that you want to delete—for example, `example-feed`



## Consume notification messages

After you configure a metadata change feed, Knowledge Catalog publishes messages to the specified Pub/Sub topic when metadata changes occur. To consume these messages, create a Pub/Sub subscription to the topic.

For example, you can create a pull subscription and use the Google Cloud CLI to view messages:

  1. Create a subscription:
         
         gcloud pubsub subscriptions create SUBSCRIPTION_ID --topic=TOPIC_ID
         

Replace the following:

     * `SUBSCRIPTION_ID`: the subscription ID that you want to create
     * `TOPIC_ID`: the Pub/Sub topic ID to which the metadata change feed messages are published.
  2. Pull messages from the subscription:
         
         gcloud pubsub subscriptions pull SUBSCRIPTION_ID --auto-ack --limit=10
         

Replace the following:

     * `SUBSCRIPTION_ID`: the subscription ID from which you want to pull messages



For more information about processing Pub/Sub messages, see [Receive messages from a pull subscription](https://docs.cloud.google.com/pubsub/docs/pull-messages). For information about the message format, see [Data payload](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-change-feeds-overview#data-payload).

## What's next

  * Read the [Metadata change feeds overview](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-change-feeds-overview).
  * Learn about [Knowledge Catalog IAM and access control](https://docs.cloud.google.com/knowledge-catalog/docs/iam-and-access-control).
  * [Troubleshoot metadata change feeds](https://docs.cloud.google.com/knowledge-catalog/docs/troubleshoot-metadata-change-feeds).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
