---
url: https://cloud.google.com/asset-inventory/docs/monitoring-asset-changes-with-condition/
title: Monitor asset changes with Pub/Sub \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:20.634068+00:00
---

# Monitor asset changes with Pub/Sub  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://cloud.google.com/asset-inventory/docs/monitoring-asset-changes-with-condition/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Guides ](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview)



Send feedback 

#  Monitor asset changes with Pub/Sub Stay organized with collections  Save and categorize content based on your preferences. 

You can receive real-time notifications about resource and policy changes by creating and subscribing to a feed.

When you create the feed, you can specify that you want to monitor changes of supported resource types, IAM policies, access policies, and organization policies in an organization, folder, project. Additionally, you can add conditions to your feed so that you only receive notifications for certain types of changes to an asset.

After creating a feed, you receive notifications through [Pub/Sub](https://cloud.google.com/pubsub/docs) whenever the specified assets change. The first message published to the Pub/Sub topic is a welcome message in the format of a string, and all following messages are in the format of a [TemporalAsset](https://cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/batchGetAssetsHistory#temporalasset).

Here's a sample Pub/Sub message for the `RESOURCE` content type.
    
    
    {
      "asset":{
        "ancestors":[
          "projects/000000000000",
          "folders/000000000000",
          "organizations/000000000000"
        ],
        "assetType":"storage.googleapis.com/Bucket",
        "name":"//storage.googleapis.com/my-bucket",
        "resource":{
          "data":{
            LATEST_ASSET_METADATA
          },
          "discoveryDocumentUri":"https://www.googleapis.com/discovery/v1/apis/storage/v1/rest",
          "discoveryName":"Bucket",
          "location":"us",
          "parent":"//cloudresourcemanager.googleapis.com/projects/000000000000",
          "version":"v1"
        },
        "updateTime":"2024-01-30T00:00:00.000000Z"
      },
      "priorAsset":{
        "ancestors":[
          "projects/000000000000",
          "folders/000000000000",
          "organizations/000000000000"
        ],
        "assetType":"storage.googleapis.com/Bucket",
        "name":"//storage.googleapis.com/my-bucket",
        "resource":{
          "data":{
            PREVIOUS_ASSET_METADATA
          },
          "discoveryDocumentUri":"https://www.googleapis.com/discovery/v1/apis/storage/v1/rest",
          "discoveryName":"Bucket",
          "location":"us",
          "parent":"//cloudresourcemanager.googleapis.com/projects/000000000000",
          "version":"v1"
        },
        "updateTime":"2024-01-29T00:00:00.000000Z"
      },
      "priorAssetState":"PRESENT",
      "window":{
        "startTime":"2024-01-30T00:00:00.000000Z"
      }
    }
    

To learn more about Pub/Sub or how to set up subscriptions, see the [Pub/Sub documentation](https://cloud.google.com/pubsub/docs).

**Tip:** You can connect real-time notifications to your workloads. For example, you could run a Cloud Run function to reverse a resource change after it has been detected.

## Before you begin

  1. Enable the Cloud Asset Inventory API in the project you're running Cloud Asset Inventory commands from.

[Enable the Cloud Asset Inventory API](https://console.cloud.google.com/apis/library/cloudasset.googleapis.com)

  2. Make sure your account has the [correct role to call the Cloud Asset Inventory API](https://cloud.google.com/asset-inventory/docs/roles-permissions#roles). For individual permissions for each call type, see [Permissions](https://cloud.google.com/asset-inventory/docs/roles-permissions#permissions).

  3. [Create a Pub/Sub topic](https://cloud.google.com/pubsub/docs/create-topic), if you don't have one already.




## Limitations

  * It can take up to 10 minutes for any feed creation, update, or deletion to take effect.

  * The project where a feed is created must outlive the feed. This is because the service account used to publish to the destination Pub/Sub topic is located in that project. A feed no longer functions and is deleted as soon as project deletion is permanent.

  * You can create up to 200 feeds on a parent. This limit only applies to feeds directly following a parent and does not count the feeds of its children. For example, if you have 10 projects in an organization, each project can have up to 200 feeds, and the organization can also have up to 200 feeds.




## Create feeds

#### gcloud
    
    
    gcloud asset feeds create FEED_ID \
        --SCOPE \
        --billing-project=BILLING_PROJECT_ID \
        --pubsub-topic=projects/TOPIC_PROJECT_ID/topics/TOPIC_ID \
        --asset-names=ASSET_NAME_1,ASSET_NAME_2,... \
        --asset-types=ASSET_TYPE_1,ASSET_TYPE_2,... \
        --content-type=CONTENT_TYPE \
        --relationship-types=RELATIONSHIP_TYPE_1,RELATIONSHIP_TYPE_2,... \
        --condition-title="CONDITION_TITLE" \
        --condition-description="CONDITION_DESCRIPTION" \
        --condition-expression="CONDITION_EXPRESSION"

Provide the following values:

  * `SCOPE`: Use one of the following values:

    * `project=PROJECT_ID`, where `PROJECT_ID` is the ID of the project to create the feed in. 
    * `folder=FOLDER_ID`, where `FOLDER_ID` is the ID of the folder to create the feed in. 

How to find the ID of a Google Cloud folder

### Google Cloud console

To find the ID of a Google Cloud folder, complete the following steps:

      1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box.
      4. Search for your folder name. The folder ID is shown next to the folder name.

### gcloud CLI

You can retrieve the ID of a Google Cloud folder that's located at the organization level with the following command:
    
    gcloud resource-manager folders list \
        --organization=$(gcloud organizations describe ORGANIZATION_NAME \
          --format="value(name.segment(1))") \
        --filter='"DISPLAY_NAME":"TOP_LEVEL_FOLDER_NAME"' \
        --format="value(ID)"

Where TOP_LEVEL_FOLDER_NAME is a partial or full string match for the folder's name. Remove the `--format` flag to see more information about the found folders.

The previous command doesn't return the IDs of subfolders within folders. To do so, run the following command using a top level folder's ID:
    
    gcloud resource-manager folders list --folder=FOLDER_ID

    * `organization=ORGANIZATION_ID`, where `ORGANIZATION_ID` is the ID of the organization to create the feed in. 

How to find the ID of a Google Cloud organization

### Google Cloud console

To find the ID of a Google Cloud organization, complete the following steps:

      1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box.
      4. Click the **All** tab. The organization ID is shown next to the organization name.

### gcloud CLI

You can retrieve the ID of a Google Cloud organization with the following command:
    
    gcloud organizations describe ORGANIZATION_NAME --format="value(name.segment(1))"

  * `FEED_ID`: A unique asset feed identifier.
  * `BILLING_PROJECT_ID`: Optional. The project ID that the default Cloud Asset Inventory service agent is in that has permissions to manage your Pub/Sub topic. [ Read more about setting the billing project](https://cloud.google.com/asset-inventory/docs/multiple-projects#orchestrator). 
  * `TOPIC_PROJECT_ID`: The ID of the project where the Pub/Sub topic is located. 
  * `TOPIC_ID`: The ID of the Pub/Sub topic to publish notifications to. 
  * At least one of the following asset definitions:

    * `ASSET_NAME_#`: Optional. A comma-separated list of [asset full names](https://cloud.google.com/asset-inventory/docs/asset-names). 
    * `ASSET_TYPE_#`: Optional. A comma-separated list of [searchable asset types](https://cloud.google.com/asset-inventory/docs/asset-types). [RE2-compatible regular expressions](https://github.com/google/re2/wiki/Syntax) are supported. If the regular expression doesn't match any supported asset type, an `INVALID_ARGUMENT` error is returned. When `--asset-types` isn't specified, all asset types are returned. 
  * `CONTENT_TYPE`: Optional. The [content type](https://cloud.google.com/asset-inventory/docs/asset-inventory-overview#content_types) of the metadata that you want to retrieve. When `--content-type` isn't specified, only basic information is returned, such as asset names, the last time the assets were updated, and what projects, folders, and organizations that they belong to. 
  * `RELATIONSHIP_TYPE_#`: Optional. Requires access to the [ Security Command Center Premium or Enterprise tier](https://cloud.google.com/security-command-center/pricing#tier-pricing). A comma-separated list of [asset relationship types](https://cloud.google.com/asset-inventory/docs/relationship-types) that you want to retrieve. You must set `CONTENT_TYPE` to `RELATIONSHIP` for this to work. 
  * If adding an optional feed condition, include the following details in your command: 

    * `CONDITION_TITLE`: A title to assign to the feed condition.
    * `CONDITION_DESCRIPTION`: A description to assign to the feed condition. 
    * `CONDITION_EXPRESSION`: The condition expression to apply to the feed. 



See the [gcloud CLI reference](https://cloud.google.com/sdk/gcloud/reference/asset/feeds/create) for all options. 

### Example

Run the following command to create a feed in the `my-topic` Pub/Sub topic that notifies when changes are made to the following resources in the `my-project` project. 

  * The `my-bucket` Cloud Storage bucket
  * Any BigQuery table


    
    
    gcloud asset feeds create **my-feed** \
        --project=**my-project** \
        --pubsub-topic=projects/**my-project** /topics/**my-topic** \
        --asset-names=//storage.googleapis.com/**my-bucket** \
        --asset-types=bigquery.googleapis.com/Table \
        --content-type=resource

#### Example response
    
    
    assetNames:
    - //storage.googleapis.com/my-bucket
    assetTypes:
    - bigquery.googleapis.com/Table
    condition: {}
    contentType: RESOURCE
    feedOutputConfig:
      pubsubDestination:
        topic: projects/my-project/topics/my-topic
    name: projects/000000000000/feeds/my-feed
    

#### REST

HTTP method and URL:
    
    
    POST https://cloudasset.googleapis.com/v1/SCOPE_PATH/feeds
    

Headers:
    
    
    X-Goog-User-Project: BILLING_PROJECT_ID

Request JSON body:
    
    
    {
      "feedId": "FEED_ID",
      "feed": {
        "assetNames": [
          "ASSET_NAME_1",
          "ASSET_NAME_2",
          "..."
        ],
        "assetTypes": [
          "ASSET_TYPE_1",
          "ASSET_TYPE_2",
          "..."
        ],
        "contentType": "CONTENT_TYPE",
        "relationshipTypes": [
          "RELATIONSHIP_TYPE_1",
          "RELATIONSHIP_TYPE_2",
          "..."
        ],
        "feedOutputConfig": {
          "pubsubDestination": {
            "topic": "projects/TOPIC_PROJECT_ID/topics/TOPIC_ID"
          }
        },
        "condition": {
          "title": "CONDITION_TITLE",
          "description": "CONDITION_DESCRIPTION",
          "expression": "CONDITION_EXPRESSION"
        }
      }
    }

Provide the following values:

  * `SCOPE_PATH`: Use one of the following values:

    * `projects/PROJECT_ID`, where `PROJECT_ID` is the ID of the project to create the feed in. 
    * `projects/PROJECT_NUMBER`, where `PROJECT_NUMBER` is the number of the project to create the feed in. 

How to find a Google Cloud project number

### Google Cloud console

To find a Google Cloud project number, complete the following steps:

      1. Go to the **Welcome** page in the Google Cloud console.

[ Go to Welcome](https://console.cloud.google.com/welcome)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box, and then search for your project name. The project name, project number, and project ID are shown near the **Welcome** heading. 

Up to 4,000 resources are displayed. If you don't see the project you're looking for, go to the [**Manage resources**](https://console.cloud.google.com//cloud-resource-manager) page and filter the list using the name of that project. 

### gcloud CLI

You can retrieve a Google Cloud project number with the following command:
    
    gcloud projects describe PROJECT_ID --format="value(projectNumber)"

    * `folders/FOLDER_ID`, where `FOLDER_ID` is the ID of the folder to create the feed in. 

How to find the ID of a Google Cloud folder

### Google Cloud console

To find the ID of a Google Cloud folder, complete the following steps:

      1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box.
      4. Search for your folder name. The folder ID is shown next to the folder name.

### gcloud CLI

You can retrieve the ID of a Google Cloud folder that's located at the organization level with the following command:
    
    gcloud resource-manager folders list \
        --organization=$(gcloud organizations describe ORGANIZATION_NAME \
          --format="value(name.segment(1))") \
        --filter='"DISPLAY_NAME":"TOP_LEVEL_FOLDER_NAME"' \
        --format="value(ID)"

Where TOP_LEVEL_FOLDER_NAME is a partial or full string match for the folder's name. Remove the `--format` flag to see more information about the found folders.

The previous command doesn't return the IDs of subfolders within folders. To do so, run the following command using a top level folder's ID:
    
    gcloud resource-manager folders list --folder=FOLDER_ID

    * `organizations/ORGANIZATION_ID`, where `ORGANIZATION_ID` is the ID of the organization to create the feed in. 

How to find the ID of a Google Cloud organization

### Google Cloud console

To find the ID of a Google Cloud organization, complete the following steps:

      1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box.
      4. Click the **All** tab. The organization ID is shown next to the organization name.

### gcloud CLI

You can retrieve the ID of a Google Cloud organization with the following command:
    
    gcloud organizations describe ORGANIZATION_NAME --format="value(name.segment(1))"

  * `BILLING_PROJECT_ID`: The project ID that the default Cloud Asset Inventory service agent is in that has permissions to manage your Pub/Sub topic. [ Read more about setting the billing project](https://cloud.google.com/asset-inventory/docs/multiple-projects#orchestrator). 
  * `FEED_ID`: A unique asset feed identifier.
  * At least one of the following asset definitions:

    * `ASSET_NAME_#`: Optional. An array of [asset full names](https://cloud.google.com/asset-inventory/docs/asset-names). 
    * `ASSET_TYPE_#`: Optional. An array of [searchable asset types](https://cloud.google.com/asset-inventory/docs/asset-types). [RE2-compatible regular expressions](https://github.com/google/re2/wiki/Syntax) are supported. If the regular expression doesn't match any supported asset type, an `INVALID_ARGUMENT` error is returned. When `assetTypes` isn't specified, all asset types are returned. 
  * `CONTENT_TYPE`: Optional. The [content type](https://cloud.google.com/asset-inventory/docs/asset-inventory-overview#content_types) of the metadata that you want to retrieve. When `contentType` isn't specified, only basic information is returned, such as asset names, the last time the assets were updated, and what projects, folders, and organizations that they belong to. 
  * `RELATIONSHIP_TYPE_#`: Optional. Requires access to the [ Security Command Center Premium or Enterprise tier](https://cloud.google.com/security-command-center/pricing#tier-pricing). A comma-separated list of [asset relationship types](https://cloud.google.com/asset-inventory/docs/relationship-types) that you want to retrieve. You must set `CONTENT_TYPE` to `RELATIONSHIP` for this to work. 
  * `TOPIC_PROJECT_ID`: The ID of the project where the Pub/Sub topic is located. 
  * `TOPIC_ID`: The ID of the Pub/Sub topic to publish notifications to. 
  * If adding an optional feed condition, include the following details in your command: 

    * `CONDITION_TITLE`: A title to assign to the feed condition.
    * `CONDITION_DESCRIPTION`: A description to assign to the feed condition. 
    * `CONDITION_EXPRESSION`: The condition expression to apply to the feed. 



See the [REST reference](https://cloud.google.com/asset-inventory/docs/reference/rest/v1/feeds/create) for all options.

### Command examples

Run one of the following commands to create a feed in the `my-topic` Pub/Sub topic that notifies when changes are made to the following resources in the `my-project` project. 

  * The `my-bucket` Cloud Storage bucket
  * Any BigQuery table



#### curl (Linux, macOS, or Cloud Shell)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://cloud.google.com/shell/docs), which automatically logs you into the gcloud CLI. You can check the active account by running [`gcloud auth list`](https://cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    curl -X POST \
         -H "X-Goog-User-Project: BILLING_PROJECT_ID" \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d '{
                "feedId": "**my-feed** ",
                "feed": {
                  "assetNames": [
                    "//storage.googleapis.com/**my-bucket** "
                  ],
                  "assetTypes": [
                    "bigquery.googleapis.com/Table"
                  ],
                  "contentType": "RESOURCE",
                  "feedOutputConfig": {
                    "pubsubDestination": {
                      "topic": "projects/**my-project** /topics/**my-topic** "
                    }
                  }
                }
              }' \
         https://cloudasset.googleapis.com/v1/projects/**my-project** /feeds

#### PowerShell (Windows)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://cloud.google.com/sdk/gcloud/reference/init) or [ `gcloud auth login`](https://cloud.google.com/sdk/gcloud/reference/auth/login). You can check the active account by running [ `gcloud auth list`](https://cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    $cred = gcloud auth print-access-token
    
    $headers = @{ 
      "X-Goog-User-Project" = "BILLING_PROJECT_ID";
      "Authorization" = "Bearer $cred"
    }
    
    
    $body = @"
    {
      "feedId": "**my-feed** ",
      "feed": {
        "assetNames": [
          "//storage.googleapis.com/**my-bucket** "
        ],
        "assetTypes": [
          "bigquery.googleapis.com/Table"
        ],
        "contentType": "RESOURCE",
        "feedOutputConfig": {
          "pubsubDestination": {
            "topic": "projects/**my-project** /topics/**my-topic** "
          }
        }
      }
    }
    "@
    
    Invoke-WebRequest `
      -Method POST `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body $body `
      -Uri "https://cloudasset.googleapis.com/v1/projects/**my-project** /feeds" | Select-Object -Expand Content

#### Example response
    
    
    {
      "name": "projects/000000000000/feeds/my-feed",
      "assetNames": [
        "//storage.googleapis.com/my-bucket"
      ],
      "assetTypes": [
        "bigquery.googleapis.com/Table"
      ],
      "contentType": "RESOURCE",
      "feedOutputConfig": {
        "pubsubDestination": {
          "topic": "projects/my-project/topics/my-topic"
        }
      }
    }

#### Go

To learn how to install and use the client library for Cloud Asset Inventory, see [Cloud Asset Inventory client libraries](https://cloud.google.com/asset-inventory/docs/client-libraries). 

To authenticate to Cloud Asset Inventory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Sample create-feed create feed.
    package main
    
    import (
    	"context"
    	"flag"
    	"fmt"
    	"log"
    	"os"
    
    	asset "cloud.google.com/go/asset/apiv1"
    	"cloud.google.com/go/asset/apiv1/assetpb"
    )
    
    // Command-line flags.
    var (
    	feedID = flag.String("feed_id", "YOUR_FEED_ID", "Identifier of Feed.")
    )
    
    func main() {
    	flag.Parse()
    	ctx := context.Background()
    	client, err := asset.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/asset/latest/apiv1.html#cloud_google_com_go_asset_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		log.Fatalf("asset.NewClient: %v", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/asset/latest/apiv1.html#cloud_google_com_go_asset_apiv1_Client_Close)()
    
    	projectID := os.Getenv("GOOGLE_CLOUD_PROJECT")
    	feedParent := fmt.Sprintf("projects/%s", projectID)
    	assetNames := []string{"YOUR_ASSET_NAME"}
    	topic := fmt.Sprintf("projects/%s/topics/%s", projectID, "YOUR_TOPIC_NAME")
    
    	req := &assetpb.CreateFeedRequest{
    		Parent: feedParent,
    		FeedId: *feedID,
    		Feed: &assetpb.Feed{
    			AssetNames: assetNames,
    			FeedOutputConfig: &assetpb.FeedOutputConfig{
    				Destination: &assetpb.FeedOutputConfig_PubsubDestination{
    					PubsubDestination: &assetpb.PubsubDestination{
    						Topic: topic,
    					},
    				},
    			},
    		}}
    	response, err := client.CreateFeed(ctx, req)
    	if err != nil {
    		log.Fatalf("client.CreateFeed: %v", err)
    	}
    	fmt.Print(response)
    }
    

#### Java

To learn how to install and use the client library for Cloud Asset Inventory, see [Cloud Asset Inventory client libraries](https://cloud.google.com/asset-inventory/docs/client-libraries). 

To authenticate to Cloud Asset Inventory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.asset.v1.[AssetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetServiceClient.html);
    import com.google.cloud.asset.v1.[ContentType](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ContentType.html);
    import com.google.cloud.asset.v1.[CreateFeedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.CreateFeedRequest.html);
    import com.google.cloud.asset.v1.[Feed](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.Feed.html);
    import com.google.cloud.asset.v1.[FeedOutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.FeedOutputConfig.html);
    import com.google.cloud.asset.v1.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ProjectName.html);
    import com.google.cloud.asset.v1.[PubsubDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.PubsubDestination.html);
    import java.io.IOException;
    import java.util.Arrays;
    
    public class CreateFeedExample {
      // Create a feed
      public static void createFeed(
          String[] assetNames, String feedId, String topic, String projectId, [ContentType](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ContentType.html) contentType)
          throws IOException, IllegalArgumentException {
        // String[] assetNames = {"MY_ASSET_NAME"}
        // ContentType contentType = contentType
        // String FeedId = "MY_FEED_ID"
        // String topic = "projects/[PROJECT_ID]/topics/[TOPIC_NAME]"
        // String projectID = "MY_PROJECT_ID"
        [Feed](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.Feed.html) feed =
            [Feed](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.Feed.html).newBuilder()
                .addAllAssetNames(Arrays.asList(assetNames))
                .setContentType(contentType)
                .[setFeedOutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.Feed.Builder.html#com_google_cloud_asset_v1_Feed_Builder_setFeedOutputConfig_com_google_cloud_asset_v1_FeedOutputConfig_)(
                    [FeedOutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.FeedOutputConfig.html).newBuilder()
                        .[setPubsubDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.FeedOutputConfig.Builder.html#com_google_cloud_asset_v1_FeedOutputConfig_Builder_setPubsubDestination_com_google_cloud_asset_v1_PubsubDestination_)([PubsubDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.PubsubDestination.html).newBuilder().[setTopic](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.PubsubDestination.Builder.html#com_google_cloud_asset_v1_PubsubDestination_Builder_setTopic_java_lang_String_)(topic).build())
                        .build())
                .build();
        [CreateFeedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.CreateFeedRequest.html) request =
            [CreateFeedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.CreateFeedRequest.html).newBuilder()
                .setParent(String.format([ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ProjectName.html).of(projectId).toString()))
                .[setFeedId](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.CreateFeedRequest.Builder.html#com_google_cloud_asset_v1_CreateFeedRequest_Builder_setFeedId_java_lang_String_)(feedId)
                .setFeed(feed)
                .build();
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([AssetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetServiceClient.html) client = [AssetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetServiceClient.html).create()) {
          [Feed](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.Feed.html) response = client.createFeed(request);
          System.out.println("Feed created successfully: " + response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.Feed.html#com_google_cloud_asset_v1_Feed_getName__)());
        } catch (IOException | IllegalArgumentException e) {
          System.out.println("Error during CreateFeed: \n" + e.toString());
        }
      }
    }

#### Node.js

To learn how to install and use the client library for Cloud Asset Inventory, see [Cloud Asset Inventory client libraries](https://cloud.google.com/asset-inventory/docs/client-libraries). 

To authenticate to Cloud Asset Inventory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const feedId = 'my feed';
    // const assetNames = '//storage.googleapis.com/<BUCKET_NAME1>,//storage.googleapis.com/<BUCKET_NAME2>';
    // const topicName = 'projects/<PROJECT_ID>/topics/<TOPIC_ID>'
    // const contentType = 'RESOURCE';
    
    const util = require('util');
    const {AssetServiceClient} = require('[@google-cloud/asset](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/overview.html)');
    
    const client = new [AssetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/overview.html)();
    
    async function createFeed() {
      const projectId = await client.getProjectId();
      // TODO(developer): Choose asset names, such as //storage.googleapis.com/[YOUR_BUCKET_NAME].
      // const assetNames = ['ASSET_NAME1', 'ASSET_NAME2', ...];
    
      const request = {
        parent: `projects/${projectId}`,
        feedId: feedId,
        feed: {
          assetNames: assetNames.split(','),
          contentType: contentType,
          feedOutputConfig: {
            pubsubDestination: {
              topic: topicName,
            },
          },
        },
      };
    
      // Handle the operation using the promise pattern.
      const result = await client.createFeed(request);
      // Do things with with the response.
      console.log(util.inspect(result, {depth: null}));

#### Python

To learn how to install and use the client library for Cloud Asset Inventory, see [Cloud Asset Inventory client libraries](https://cloud.google.com/asset-inventory/docs/client-libraries). 

To authenticate to Cloud Asset Inventory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest)
    
    # TODO project_id = 'Your Google Cloud Project ID'
    # TODO feed_id = 'Feed ID you want to create'
    # TODO asset_names = 'List of asset names the feed listen to'
    # TODO topic = "Topic name of the feed"
    # TODO content_type ="Content type of the feed"
    
    client = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[AssetServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient.html)()
    parent = f"projects/{project_id}"
    feed = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[Feed](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.Feed.html)()
    feed.asset_names.extend(asset_names)
    feed.feed_output_config.pubsub_destination.topic = topic
    feed.content_type = content_type
    response = client.[create_feed](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient.html#google_cloud_asset_v1_services_asset_service_AssetServiceClient_create_feed)(
        request={"parent": parent, "feed_id": feed_id, "feed": feed}
    )
    print(f"feed: {response}")

#### Ruby

To learn how to install and use the client library for Cloud Asset Inventory, see [Cloud Asset Inventory client libraries](https://cloud.google.com/asset-inventory/docs/client-libraries). 

To authenticate to Cloud Asset Inventory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/asset"
    
    # project_id = 'YOUR_PROJECT_ID'
    # feed_id = 'NAME_OF_FEED'
    # pubsub_topic = 'YOUR_PUBSUB_TOPIC'
    # asset names, e.g.: //storage.googleapis.com/[YOUR_BUCKET_NAME]
    # asset_names = [ASSET_NAMES, COMMMA_DELIMTTED]
    asset_service = Google::Cloud::[Asset](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset/latest/Google-Cloud-Asset.html).[asset_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset/latest/Google-Cloud-Asset.html)
    
    formatted_parent = asset_service.[project_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AssetService-Paths.html) project: project_id
    
    feed = {
      asset_names:        asset_names,
      feed_output_config: {
        pubsub_destination: {
          topic: pubsub_topic
        }
      }
    }
    response = asset_service.create_feed(
      parent:  formatted_parent,
      feed_id: feed_id,
      feed:    feed
    )
    puts "Created feed: #{response.name}"

## Get feeds

#### gcloud
    
    
    gcloud asset feeds describe FEED_ID \
        --SCOPE \
        --billing-project=BILLING_PROJECT_ID

Provide the following values:

  * `SCOPE`: Use one of the following values:

    * `project=PROJECT_ID`, where `PROJECT_ID` is the ID of the project that the feed is in. 
    * `folder=FOLDER_ID`, where `FOLDER_ID` is the ID of the folder that the feed is in. 

How to find the ID of a Google Cloud folder

### Google Cloud console

To find the ID of a Google Cloud folder, complete the following steps:

      1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box.
      4. Search for your folder name. The folder ID is shown next to the folder name.

### gcloud CLI

You can retrieve the ID of a Google Cloud folder that's located at the organization level with the following command:
    
    gcloud resource-manager folders list \
        --organization=$(gcloud organizations describe ORGANIZATION_NAME \
          --format="value(name.segment(1))") \
        --filter='"DISPLAY_NAME":"TOP_LEVEL_FOLDER_NAME"' \
        --format="value(ID)"

Where TOP_LEVEL_FOLDER_NAME is a partial or full string match for the folder's name. Remove the `--format` flag to see more information about the found folders.

The previous command doesn't return the IDs of subfolders within folders. To do so, run the following command using a top level folder's ID:
    
    gcloud resource-manager folders list --folder=FOLDER_ID

    * `organization=ORGANIZATION_ID`, where `ORGANIZATION_ID` is the ID of the organization that the feed is in. 

How to find the ID of a Google Cloud organization

### Google Cloud console

To find the ID of a Google Cloud organization, complete the following steps:

      1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box.
      4. Click the **All** tab. The organization ID is shown next to the organization name.

### gcloud CLI

You can retrieve the ID of a Google Cloud organization with the following command:
    
    gcloud organizations describe ORGANIZATION_NAME --format="value(name.segment(1))"

  * `BILLING_PROJECT_ID`: The project ID that the default Cloud Asset Inventory service agent is in that has permissions to manage your Pub/Sub topic. [ Read more about setting the billing project](https://cloud.google.com/asset-inventory/docs/multiple-projects#orchestrator). 
  * `FEED_ID`: A unique asset feed identifier.



See the [gcloud CLI reference](https://cloud.google.com/sdk/gcloud/reference/asset/feeds/describe) for all options. 

#### Example response
    
    
    assetNames:
    - //storage.googleapis.com/my-bucket
    assetTypes:
    - bigquery.googleapis.com/Table
    condition: {}
    contentType: RESOURCE
    feedOutputConfig:
      pubsubDestination:
        topic: projects/my-project/topics/my-topic
    name: projects/000000000000/feeds/my-feed
    

#### REST

HTTP method and URL:
    
    
    GET https://cloudasset.googleapis.com/v1/SCOPE_PATH/feeds/FEED_ID
    

Headers:
    
    
    X-Goog-User-Project: BILLING_PROJECT_ID

Provide the following values:

  * `SCOPE_PATH`: Use one of the following values:

    * `projects/PROJECT_ID`, where `PROJECT_ID` is the ID of the project that the feed is in. 
    * `projects/PROJECT_NUMBER`, where `PROJECT_NUMBER` is the number of the project that the feed is in. 

How to find a Google Cloud project number

### Google Cloud console

To find a Google Cloud project number, complete the following steps:

      1. Go to the **Welcome** page in the Google Cloud console.

[ Go to Welcome](https://console.cloud.google.com/welcome)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box, and then search for your project name. The project name, project number, and project ID are shown near the **Welcome** heading. 

Up to 4,000 resources are displayed. If you don't see the project you're looking for, go to the [**Manage resources**](https://console.cloud.google.com//cloud-resource-manager) page and filter the list using the name of that project. 

### gcloud CLI

You can retrieve a Google Cloud project number with the following command:
    
    gcloud projects describe PROJECT_ID --format="value(projectNumber)"

    * `folders/FOLDER_ID`, where `FOLDER_ID` is the ID of the folder that the feed is in. 

How to find the ID of a Google Cloud folder

### Google Cloud console

To find the ID of a Google Cloud folder, complete the following steps:

      1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box.
      4. Search for your folder name. The folder ID is shown next to the folder name.

### gcloud CLI

You can retrieve the ID of a Google Cloud folder that's located at the organization level with the following command:
    
    gcloud resource-manager folders list \
        --organization=$(gcloud organizations describe ORGANIZATION_NAME \
          --format="value(name.segment(1))") \
        --filter='"DISPLAY_NAME":"TOP_LEVEL_FOLDER_NAME"' \
        --format="value(ID)"

Where TOP_LEVEL_FOLDER_NAME is a partial or full string match for the folder's name. Remove the `--format` flag to see more information about the found folders.

The previous command doesn't return the IDs of subfolders within folders. To do so, run the following command using a top level folder's ID:
    
    gcloud resource-manager folders list --folder=FOLDER_ID

    * `organizations/ORGANIZATION_ID`, where `ORGANIZATION_ID` is the ID of the organization that the feed is in. 

How to find the ID of a Google Cloud organization

### Google Cloud console

To find the ID of a Google Cloud organization, complete the following steps:

      1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box.
      4. Click the **All** tab. The organization ID is shown next to the organization name.

### gcloud CLI

You can retrieve the ID of a Google Cloud organization with the following command:
    
    gcloud organizations describe ORGANIZATION_NAME --format="value(name.segment(1))"

  * `BILLING_PROJECT_ID`: The project ID that the default Cloud Asset Inventory service agent is in that has permissions to publish to your Pub/Sub topic. [ Read more about setting the billing project](https://cloud.google.com/asset-inventory/docs/multiple-projects#orchestrator). 

  * `FEED_ID`: A unique asset feed identifier.



See the [REST reference](https://cloud.google.com/asset-inventory/docs/reference/rest/v1/feeds/get) for all options.

### Command examples

Run one of the following commands to get a specific feed.

#### curl (Linux, macOS, or Cloud Shell)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://cloud.google.com/shell/docs), which automatically logs you into the gcloud CLI. You can check the active account by running [`gcloud auth list`](https://cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    curl -X GET \
         -H "X-Goog-User-Project: BILLING_PROJECT_ID" \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         https://cloudasset.googleapis.com/v1/projects/**my-project** /feeds/**my-feed**

#### PowerShell (Windows)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://cloud.google.com/sdk/gcloud/reference/init) or [ `gcloud auth login`](https://cloud.google.com/sdk/gcloud/reference/auth/login). You can check the active account by running [ `gcloud auth list`](https://cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    $cred = gcloud auth print-access-token
    
    $headers = @{ 
      "X-Goog-User-Project" = "BILLING_PROJECT_ID";
      "Authorization" = "Bearer $cred"
    }
    
    
    Invoke-WebRequest `
      -Method GET `
      -Headers $headers `
      -Uri "https://cloudasset.googleapis.com/v1/projects/**my-project** /feeds/**my-feed** " | Select-Object -Expand Content

#### Example response
    
    
    {
      "name": "projects/000000000000/feeds/my-feed",
      "assetNames": [
        "//storage.googleapis.com/my-bucket"
      ],
      "assetTypes": [
        "bigquery.googleapis.com/Table"
      ],
      "contentType": "RESOURCE",
      "feedOutputConfig": {
        "pubsubDestination": {
          "topic": "projects/my-project/topics/my-topic"
        }
      }
    }

#### Go

To learn how to install and use the client library for Cloud Asset Inventory, see [Cloud Asset Inventory client libraries](https://cloud.google.com/asset-inventory/docs/client-libraries). 

To authenticate to Cloud Asset Inventory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Sample get-feed get feed.
    package main
    
    import (
    	"context"
    	"flag"
    	"fmt"
    	"log"
    	"os"
    	"strconv"
    
    	asset "cloud.google.com/go/asset/apiv1"
    	"cloud.google.com/go/asset/apiv1/assetpb"
    	cloudresourcemanager "google.golang.org/api/cloudresourcemanager/v1"
    )
    
    // Command-line flags.
    var (
    	feedID = flag.String("feed_id", "YOUR_FEED_ID", "Identifier of Feed.")
    )
    
    func main() {
    	flag.Parse()
    	ctx := context.Background()
    	client, err := asset.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/asset/latest/apiv1.html#cloud_google_com_go_asset_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		log.Fatalf("asset.NewClient: %v", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/asset/latest/apiv1.html#cloud_google_com_go_asset_apiv1_Client_Close)()
    
    	projectID := os.Getenv("GOOGLE_CLOUD_PROJECT")
    	cloudresourcemanagerClient, err := cloudresourcemanager.NewService(ctx)
    	if err != nil {
    		log.Fatalf("cloudresourcemanager.NewService: %v", err)
    	}
    
    	project, err := cloudresourcemanagerClient.Projects.Get(projectID).Do()
    	if err != nil {
    		log.Fatalf("cloudresourcemanagerClient.Projects.Get.Do: %v", err)
    	}
    	projectNumber := strconv.FormatInt(project.ProjectNumber, 10)
    	feedName := fmt.Sprintf("projects/%s/feeds/%s", projectNumber, *feedID)
    	req := &assetpb.GetFeedRequest{
    		Name: feedName}
    	response, err := client.GetFeed(ctx, req)
    	if err != nil {
    		log.Fatalf("client.GetFeed: %v", err)
    	}
    	fmt.Print(response)
    }
    

#### Java

To learn how to install and use the client library for Cloud Asset Inventory, see [Cloud Asset Inventory client libraries](https://cloud.google.com/asset-inventory/docs/client-libraries). 

To authenticate to Cloud Asset Inventory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.asset.v1.[AssetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetServiceClient.html);
    import com.google.cloud.asset.v1.[Feed](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.Feed.html);
    
    public class GetFeedExample {
    
      // Get a feed with full feed name
      public static void getFeed(String feedName) throws Exception {
        // String feedName = "MY_FEED_NAME"
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([AssetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetServiceClient.html) client = [AssetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetServiceClient.html).create()) {
          [Feed](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.Feed.html) feed = client.getFeed(feedName);
          System.out.println("Get a feed: " + feedName);
        } catch (Exception e) {
          System.out.println("Error during GetFeed: \n" + e.toString());
        }
      }
    }

#### Node.js

To learn how to install and use the client library for Cloud Asset Inventory, see [Cloud Asset Inventory client libraries](https://cloud.google.com/asset-inventory/docs/client-libraries). 

To authenticate to Cloud Asset Inventory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const util = require('util');
    const {AssetServiceClient} = require('[@google-cloud/asset](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/overview.html)');
    
    const client = new [AssetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/overview.html)();
    
    async function getFeed() {
      const request = {
        name: feedName,
      };
    
      // Handle the operation using the promise pattern.
      const result = await client.getFeed(request);
      // Do things with with the response.
      console.log(util.inspect(result, {depth: null}));
    }
    getFeed();

#### Python

To learn how to install and use the client library for Cloud Asset Inventory, see [Cloud Asset Inventory client libraries](https://cloud.google.com/asset-inventory/docs/client-libraries). 

To authenticate to Cloud Asset Inventory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest)
    
    # TODO feed_name = 'Feed Name you want to get'
    
    client = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[AssetServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient.html)()
    response = client.[get_feed](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient.html#google_cloud_asset_v1_services_asset_service_AssetServiceClient_get_feed)(request={"name": feed_name})
    print(f"gotten_feed: {response}")

## List feeds

To list all the feeds for a project, folder, or organization, make one of the following requests.

#### gcloud
    
    
    gcloud asset feeds list \
        --SCOPE \
        --billing-project=BILLING_PROJECT_ID

Provide the following values:

  * `SCOPE`: Use one of the following values:

    * `project=PROJECT_ID`, where `PROJECT_ID` is the ID of the project that the feeds are in. 
    * `folder=FOLDER_ID`, where `FOLDER_ID` is the ID of the folder that the feeds are in. 

How to find the ID of a Google Cloud folder

### Google Cloud console

To find the ID of a Google Cloud folder, complete the following steps:

      1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box.
      4. Search for your folder name. The folder ID is shown next to the folder name.

### gcloud CLI

You can retrieve the ID of a Google Cloud folder that's located at the organization level with the following command:
    
    gcloud resource-manager folders list \
        --organization=$(gcloud organizations describe ORGANIZATION_NAME \
          --format="value(name.segment(1))") \
        --filter='"DISPLAY_NAME":"TOP_LEVEL_FOLDER_NAME"' \
        --format="value(ID)"

Where TOP_LEVEL_FOLDER_NAME is a partial or full string match for the folder's name. Remove the `--format` flag to see more information about the found folders.

The previous command doesn't return the IDs of subfolders within folders. To do so, run the following command using a top level folder's ID:
    
    gcloud resource-manager folders list --folder=FOLDER_ID

    * `organization=ORGANIZATION_ID`, where `ORGANIZATION_ID` is the ID of the organization that the feeds are in. 

How to find the ID of a Google Cloud organization

### Google Cloud console

To find the ID of a Google Cloud organization, complete the following steps:

      1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box.
      4. Click the **All** tab. The organization ID is shown next to the organization name.

### gcloud CLI

You can retrieve the ID of a Google Cloud organization with the following command:
    
    gcloud organizations describe ORGANIZATION_NAME --format="value(name.segment(1))"

  * `BILLING_PROJECT_ID`: The project ID that the default Cloud Asset Inventory service agent is in that has permissions to manage your Pub/Sub topic. [ Read more about setting the billing project](https://cloud.google.com/asset-inventory/docs/multiple-projects#orchestrator). 



See the [gcloud CLI reference](https://cloud.google.com/sdk/gcloud/reference/asset/feeds/list) for all options. 

#### Example response
    
    
    - assetNames:
      - //storage.googleapis.com/my-bucket
      assetTypes:
      - bigquery.googleapis.com/Table
      condition: {}
      contentType: RESOURCE
      feedOutputConfig:
        pubsubDestination:
          topic: projects/my-project/topics/my-topic
      name: projects/000000000000/feeds/my-feed
    

#### REST

HTTP method and URL:
    
    
    GET https://cloudasset.googleapis.com/v1/SCOPE_PATH/feeds
    

Headers:
    
    
    X-Goog-User-Project: BILLING_PROJECT_ID

Provide the following values:

  * `SCOPE_PATH`: Use one of the following values:

    * `projects/PROJECT_ID`, where `PROJECT_ID` is the ID of the project that the feeds are in. 
    * `projects/PROJECT_NUMBER`, where `PROJECT_NUMBER` is the number of the project that the feeds are in. 

How to find a Google Cloud project number

### Google Cloud console

To find a Google Cloud project number, complete the following steps:

      1. Go to the **Welcome** page in the Google Cloud console.

[ Go to Welcome](https://console.cloud.google.com/welcome)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box, and then search for your project name. The project name, project number, and project ID are shown near the **Welcome** heading. 

Up to 4,000 resources are displayed. If you don't see the project you're looking for, go to the [**Manage resources**](https://console.cloud.google.com//cloud-resource-manager) page and filter the list using the name of that project. 

### gcloud CLI

You can retrieve a Google Cloud project number with the following command:
    
    gcloud projects describe PROJECT_ID --format="value(projectNumber)"

    * `folders/FOLDER_ID`, where `FOLDER_ID` is the ID of the folder that the feeds are in. 

How to find the ID of a Google Cloud folder

### Google Cloud console

To find the ID of a Google Cloud folder, complete the following steps:

      1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box.
      4. Search for your folder name. The folder ID is shown next to the folder name.

### gcloud CLI

You can retrieve the ID of a Google Cloud folder that's located at the organization level with the following command:
    
    gcloud resource-manager folders list \
        --organization=$(gcloud organizations describe ORGANIZATION_NAME \
          --format="value(name.segment(1))") \
        --filter='"DISPLAY_NAME":"TOP_LEVEL_FOLDER_NAME"' \
        --format="value(ID)"

Where TOP_LEVEL_FOLDER_NAME is a partial or full string match for the folder's name. Remove the `--format` flag to see more information about the found folders.

The previous command doesn't return the IDs of subfolders within folders. To do so, run the following command using a top level folder's ID:
    
    gcloud resource-manager folders list --folder=FOLDER_ID

    * `organizations/ORGANIZATION_ID`, where `ORGANIZATION_ID` is the ID of the organization that the feeds are in. 

How to find the ID of a Google Cloud organization

### Google Cloud console

To find the ID of a Google Cloud organization, complete the following steps:

      1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box.
      4. Click the **All** tab. The organization ID is shown next to the organization name.

### gcloud CLI

You can retrieve the ID of a Google Cloud organization with the following command:
    
    gcloud organizations describe ORGANIZATION_NAME --format="value(name.segment(1))"

  * `BILLING_PROJECT_ID`: The project ID that the default Cloud Asset Inventory service agent is in that has permissions to manage your Pub/Sub topic. [ Read more about setting the billing project](https://cloud.google.com/asset-inventory/docs/multiple-projects#orchestrator). 



See the [REST reference](https://cloud.google.com/asset-inventory/docs/reference/rest/v1/feeds/list) for all options.

### Command examples

Run one of the following commands to list all feeds in the `my-project` project.

#### curl (Linux, macOS, or Cloud Shell)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://cloud.google.com/shell/docs), which automatically logs you into the gcloud CLI. You can check the active account by running [`gcloud auth list`](https://cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    curl -X GET \
         -H "X-Goog-User-Project: BILLING_PROJECT_ID" \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         https://cloudasset.googleapis.com/v1/projects/**my-project** /feeds

#### PowerShell (Windows)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://cloud.google.com/sdk/gcloud/reference/init) or [ `gcloud auth login`](https://cloud.google.com/sdk/gcloud/reference/auth/login). You can check the active account by running [ `gcloud auth list`](https://cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    $cred = gcloud auth print-access-token
    
    $headers = @{ 
      "X-Goog-User-Project" = "BILLING_PROJECT_ID";
      "Authorization" = "Bearer $cred"
    }
    
    
    Invoke-WebRequest `
      -Method GET `
      -Headers $headers `
      -Uri "https://cloudasset.googleapis.com/v1/projects/**my-project** /feeds" | Select-Object -Expand Content

#### Example response
    
    
    {
      "feeds": [
        {
          "name": "projects/000000000000/feeds/my-feed",
          "assetNames": [
            "//storage.googleapis.com/my-bucket"
          ],
          "assetTypes": [
            "bigquery.googleapis.com/Table"
          ],
          "contentType": "RESOURCE",
          "feedOutputConfig": {
            "pubsubDestination": {
              "topic": "projects/my-project/topics/my-topic"
            }
          }
        }
      ]
    }

#### Go

To learn how to install and use the client library for Cloud Asset Inventory, see [Cloud Asset Inventory client libraries](https://cloud.google.com/asset-inventory/docs/client-libraries). 

To authenticate to Cloud Asset Inventory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Sample list-feeds list feeds.
    package main
    
    import (
    	"context"
    	"fmt"
    	"log"
    	"os"
    	"strconv"
    
    	asset "cloud.google.com/go/asset/apiv1"
    	"cloud.google.com/go/asset/apiv1/assetpb"
    	cloudresourcemanager "google.golang.org/api/cloudresourcemanager/v1"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := asset.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/asset/latest/apiv1.html#cloud_google_com_go_asset_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		log.Fatalf("asset.NewClient: %v", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/asset/latest/apiv1.html#cloud_google_com_go_asset_apiv1_Client_Close)()
    
    	projectID := os.Getenv("GOOGLE_CLOUD_PROJECT")
    	cloudresourcemanagerClient, err := cloudresourcemanager.NewService(ctx)
    	if err != nil {
    		log.Fatalf("cloudresourcemanager.NewService: %v", err)
    	}
    
    	project, err := cloudresourcemanagerClient.Projects.Get(projectID).Do()
    	if err != nil {
    		log.Fatalf("cloudresourcemanagerClient.Projects.Get.Do: %v", err)
    	}
    	projectNumber := strconv.FormatInt(project.ProjectNumber, 10)
    	parent := fmt.Sprintf("projects/%s", projectNumber)
    	req := &assetpb.ListFeedsRequest{
    		Parent: parent}
    	response, err := client.ListFeeds(ctx, req)
    	if err != nil {
    		log.Fatalf("client.ListFeeds: %v", err)
    	}
    	fmt.Print(response)
    }
    

#### Java

To learn how to install and use the client library for Cloud Asset Inventory, see [Cloud Asset Inventory client libraries](https://cloud.google.com/asset-inventory/docs/client-libraries). 

To authenticate to Cloud Asset Inventory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.asset.v1.[AssetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetServiceClient.html);
    import com.google.cloud.asset.v1.[ListFeedsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ListFeedsResponse.html);
    import com.google.cloud.asset.v1.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ProjectName.html);
    
    public class ListFeedsExample {
      // List feeds in a project.
      public static void listFeeds(String projectId) throws Exception {
        // String projectId = "MY_PROJECT_ID"
        // String topic = "projects/[PROJECT_ID]/topics/[TOPIC_NAME]"
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([AssetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetServiceClient.html) client = [AssetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetServiceClient.html).create()) {
          [ListFeedsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ListFeedsResponse.html) response = client.listFeeds([ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.ProjectName.html).of(projectId).toString());
          System.out.println("Listed feeds under: " + projectId);
        } catch (Exception e) {
          System.out.println("Error during ListFeeds: \n" + e.toString());
        }
      }
    }

#### Node.js

To learn how to install and use the client library for Cloud Asset Inventory, see [Cloud Asset Inventory client libraries](https://cloud.google.com/asset-inventory/docs/client-libraries). 

To authenticate to Cloud Asset Inventory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const util = require('util');
    const {AssetServiceClient} = require('[@google-cloud/asset](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/overview.html)');
    
    const client = new [AssetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/overview.html)();
    
    async function listFeeds() {
      const projectId = await client.getProjectId();
    
      const request = {
        parent: `projects/${projectId}`,
      };
    
      // Handle the operation using the promise pattern.
      const result = await client.listFeeds(request);
      // Do things with with the response.
      console.log(util.inspect(result, {depth: null}));

#### Python

To learn how to install and use the client library for Cloud Asset Inventory, see [Cloud Asset Inventory client libraries](https://cloud.google.com/asset-inventory/docs/client-libraries). 

To authenticate to Cloud Asset Inventory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest)
    
    # TODO parent_resource = 'Parent resource you want to list all feeds'
    
    client = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[AssetServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient.html)()
    response = client.[list_feeds](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient.html#google_cloud_asset_v1_services_asset_service_AssetServiceClient_list_feeds)(request={"parent": parent_resource})
    print(f"feeds: {response.feeds}")

## Update feeds

You can update the attributes of an existing feed in the following ways:

  * Adding and removing specific asset names, or clearing all of them from the feed.

  * Adding and removing specific asset types, or clearing all of them from the feed.

  * Overwriting conditions or clearing them from the feed.




#### gcloud
    
    
    gcloud asset feeds update FEED_ID \
        --SCOPE \
        --billing-project=BILLING_PROJECT_ID \
        --pubsub-topic=projects/TOPIC_PROJECT_ID/topics/TOPIC_ID \
        --clear-asset-names \
        --add-asset-names=ASSET_NAME_1,ASSET_NAME_2,... \
        --remove-asset-names=ASSET_NAME_3,ASSET_NAME_4,... \
        --clear-asset-types \
        --add-asset-types=ASSET_TYPE_1,ASSET_TYPE_2,... \
        --remove-asset-types=ASSET_TYPE_3,ASSET_TYPE_4,... \
        --clear-content-type \
        --content-type=CONTENT_TYPE \
        --clear-relationship-types \
        --remove-relationship-types=RELATIONSHIP_TYPE_1,RELATIONSHIP_TYPE_2,... \
        --add-relationship-types=RELATIONSHIP_TYPE_1,RELATIONSHIP_TYPE_2,... \
        --clear-condition-title \
        --condition-title="CONDITION_TITLE" \
        --clear-condition-description \
        --condition-description="CONDITION_DESCRIPTION" \
        --clear-condition-expression
        --condition-expression="CONDITION_EXPRESSION"

Provide the following values:

  * `SCOPE`: Use one of the following values:

    * `project=PROJECT_ID`, where `PROJECT_ID` is the ID of the project to update the feed in. 
    * `folder=FOLDER_ID`, where `FOLDER_ID` is the ID of the folder to update the feed in. 

How to find the ID of a Google Cloud folder

### Google Cloud console

To find the ID of a Google Cloud folder, complete the following steps:

      1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box.
      4. Search for your folder name. The folder ID is shown next to the folder name.

### gcloud CLI

You can retrieve the ID of a Google Cloud folder that's located at the organization level with the following command:
    
    gcloud resource-manager folders list \
        --organization=$(gcloud organizations describe ORGANIZATION_NAME \
          --format="value(name.segment(1))") \
        --filter='"DISPLAY_NAME":"TOP_LEVEL_FOLDER_NAME"' \
        --format="value(ID)"

Where TOP_LEVEL_FOLDER_NAME is a partial or full string match for the folder's name. Remove the `--format` flag to see more information about the found folders.

The previous command doesn't return the IDs of subfolders within folders. To do so, run the following command using a top level folder's ID:
    
    gcloud resource-manager folders list --folder=FOLDER_ID

    * `organization=ORGANIZATION_ID`, where `ORGANIZATION_ID` is the ID of the organization to update the feed in. 

How to find the ID of a Google Cloud organization

### Google Cloud console

To find the ID of a Google Cloud organization, complete the following steps:

      1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box.
      4. Click the **All** tab. The organization ID is shown next to the organization name.

### gcloud CLI

You can retrieve the ID of a Google Cloud organization with the following command:
    
    gcloud organizations describe ORGANIZATION_NAME --format="value(name.segment(1))"

  * `FEED_ID`: A unique asset feed identifier.
  * `BILLING_PROJECT_ID`: Optional. The project ID that the default Cloud Asset Inventory service agent is in that has permissions to manage your Pub/Sub topic. [ Read more about setting the billing project](https://cloud.google.com/asset-inventory/docs/multiple-projects#orchestrator). 
  * `TOPIC_PROJECT_ID`: The ID of the project where the Pub/Sub topic is located. 
  * `TOPIC_ID`: The ID of the Pub/Sub topic to publish notifications to. 
  * At least one of the following asset definitions:

    * `ASSET_NAME_#`: Optional. A comma-separated list of [asset full names](https://cloud.google.com/asset-inventory/docs/asset-names). 
    * `ASSET_TYPE_#`: Optional. A comma-separated list of [searchable asset types](https://cloud.google.com/asset-inventory/docs/asset-types). [RE2-compatible regular expressions](https://github.com/google/re2/wiki/Syntax) are supported. If the regular expression doesn't match any supported asset type, an `INVALID_ARGUMENT` error is returned. When `--asset-types` isn't specified, all asset types are returned. 
  * `CONTENT_TYPE`: Optional. The [content type](https://cloud.google.com/asset-inventory/docs/asset-inventory-overview#content_types) of the metadata that you want to retrieve. When `--content-type` isn't specified, only basic information is returned, such as asset names, the last time the assets were updated, and what projects, folders, and organizations that they belong to. 
  * `RELATIONSHIP_TYPE_#`: Optional. Requires access to the [ Security Command Center Premium or Enterprise tier](https://cloud.google.com/security-command-center/pricing#tier-pricing). A comma-separated list of [asset relationship types](https://cloud.google.com/asset-inventory/docs/relationship-types) that you want to retrieve. You must set `CONTENT_TYPE` to `RELATIONSHIP` for this to work. 
  * If adding an optional feed condition, include the following details in your command: 

    * `CONDITION_TITLE`: A title to assign to the feed condition.
    * `CONDITION_DESCRIPTION`: A description to assign to the feed condition. 
    * `CONDITION_EXPRESSION`: The condition expression to apply to the feed. 



See the [gcloud CLI reference](https://cloud.google.com/sdk/gcloud/reference/asset/feeds/update) for all options. 

### Example

Run the following command to update the `my-topic` Pub/Sub topic in the `my-project` project. This request removes all asset names from monitoring, and adds the asset type `gkemulticloud.googleapis.com/AttachedCluster`. 
    
    
    gcloud asset feeds update **my-feed** \
        --project=**my-project** \
        --pubsub-topic=projects/**my-project** /topics/**my-topic** \
        --clear-asset-names \
        --add-asset-types=gkemulticloud.googleapis.com/AttachedCluster

#### Example response
    
    
    assetTypes:
    - bigquery.googleapis.com/Table
    - gkemulticloud.googleapis.com/AttachedCluster
    condition: {}
    contentType: RESOURCE
    feedOutputConfig:
      pubsubDestination:
        topic: projects/my-project/topics/my-topic
    name: projects/000000000000/feeds/my-feed
    

To update the attributes of a feed, you need to specify the attribute path in the `update_mask` and the value of that attribute.

#### REST

HTTP method and URL:
    
    
    PATCH https://cloudasset.googleapis.com/v1/SCOPE_PATH/feeds/FEED_ID
    

Headers:
    
    
    X-Goog-User-Project: BILLING_PROJECT_ID

Request JSON body:
    
    
    {
      "feed": {
        "assetNames": [
          "ASSET_NAME_1",
          "ASSET_NAME_2",
          "..."
        ],
        "assetTypes": [
          "ASSET_TYPE_1",
          "ASSET_TYPE_2",
          "..."
        ],
        "contentType": "CONTENT_TYPE",
        "relationshipTypes": [
          "RELATIONSHIP_TYPE_1",
          "RELATIONSHIP_TYPE_2",
          "..."
        ],
        "feedOutputConfig": {
          "pubsubDestination": {
            "topic": "projects/TOPIC_PROJECT_ID/topics/TOPIC_ID"
          }
        }
      },
      "condition": {
        "title": "CONDITION_TITLE",
        "description": "CONDITION_DESCRIPTION",
        "expression": "CONDITION_EXPRESSION"
      },
      "update_mask": {
        "paths": [
          "feed_output_config.pubsub_destination.topic",
          ATTRIBUTE_PATH_1,
          ATTRIBUTE_PATH_2,
          ...
        ]
      }
    }

Provide the following values:

  * `SCOPE_PATH`: Use one of the following values:

    * `projects/PROJECT_ID`, where `PROJECT_ID` is the ID of the project to update the feed in. 
    * `projects/PROJECT_NUMBER`, where `PROJECT_NUMBER` is the number of the project to update the feed in. 

How to find a Google Cloud project number

### Google Cloud console

To find a Google Cloud project number, complete the following steps:

      1. Go to the **Welcome** page in the Google Cloud console.

[ Go to Welcome](https://console.cloud.google.com/welcome)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box, and then search for your project name. The project name, project number, and project ID are shown near the **Welcome** heading. 

Up to 4,000 resources are displayed. If you don't see the project you're looking for, go to the [**Manage resources**](https://console.cloud.google.com//cloud-resource-manager) page and filter the list using the name of that project. 

### gcloud CLI

You can retrieve a Google Cloud project number with the following command:
    
    gcloud projects describe PROJECT_ID --format="value(projectNumber)"

    * `folders/FOLDER_ID`, where `FOLDER_ID` is the ID of the folder to update the feed in. 

How to find the ID of a Google Cloud folder

### Google Cloud console

To find the ID of a Google Cloud folder, complete the following steps:

      1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box.
      4. Search for your folder name. The folder ID is shown next to the folder name.

### gcloud CLI

You can retrieve the ID of a Google Cloud folder that's located at the organization level with the following command:
    
    gcloud resource-manager folders list \
        --organization=$(gcloud organizations describe ORGANIZATION_NAME \
          --format="value(name.segment(1))") \
        --filter='"DISPLAY_NAME":"TOP_LEVEL_FOLDER_NAME"' \
        --format="value(ID)"

Where TOP_LEVEL_FOLDER_NAME is a partial or full string match for the folder's name. Remove the `--format` flag to see more information about the found folders.

The previous command doesn't return the IDs of subfolders within folders. To do so, run the following command using a top level folder's ID:
    
    gcloud resource-manager folders list --folder=FOLDER_ID

    * `organizations/ORGANIZATION_ID`, where `ORGANIZATION_ID` is the ID of the organization to update the feed in. 

How to find the ID of a Google Cloud organization

### Google Cloud console

To find the ID of a Google Cloud organization, complete the following steps:

      1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box.
      4. Click the **All** tab. The organization ID is shown next to the organization name.

### gcloud CLI

You can retrieve the ID of a Google Cloud organization with the following command:
    
    gcloud organizations describe ORGANIZATION_NAME --format="value(name.segment(1))"

  * `BILLING_PROJECT_ID`: The project ID that the default Cloud Asset Inventory service agent is in that has permissions to manage your Pub/Sub topic. [ Read more about setting the billing project](https://cloud.google.com/asset-inventory/docs/multiple-projects#orchestrator). 
  * `FEED_ID`: A unique asset feed identifier.
  * At least one of the following asset definitions:

    * `ASSET_NAME_#`: Optional. An array of [asset full names](https://cloud.google.com/asset-inventory/docs/asset-names). 
    * `ASSET_TYPE_#`: Optional. An array of [searchable asset types](https://cloud.google.com/asset-inventory/docs/asset-types). [RE2-compatible regular expressions](https://github.com/google/re2/wiki/Syntax) are supported. If the regular expression doesn't match any supported asset type, an `INVALID_ARGUMENT` error is returned. When `assetTypes` isn't specified, all asset types are returned. 
  * `CONTENT_TYPE`: Optional. The [content type](https://cloud.google.com/asset-inventory/docs/asset-inventory-overview#content_types) of the metadata that you want to retrieve. When `contentType` isn't specified, only basic information is returned, such as asset names, the last time the assets were updated, and what projects, folders, and organizations that they belong to. 
  * `RELATIONSHIP_TYPE_#`: Optional. Requires access to the [ Security Command Center Premium or Enterprise tier](https://cloud.google.com/security-command-center/pricing#tier-pricing). A comma-separated list of [asset relationship types](https://cloud.google.com/asset-inventory/docs/relationship-types) that you want to retrieve. You must set `CONTENT_TYPE` to `RELATIONSHIP` for this to work. 
  * `TOPIC_PROJECT_ID`: The ID of the project where the Pub/Sub topic is located. 
  * `TOPIC_ID`: The ID of the Pub/Sub topic to publish notifications to. 
  * If adding an optional feed condition, include the following details in your command: 

    * `CONDITION_TITLE`: A title to assign to the feed condition.
    * `CONDITION_DESCRIPTION`: A description to assign to the feed condition. 
    * `CONDITION_EXPRESSION`: The condition expression to apply to the feed. 



See the [REST reference](https://cloud.google.com/asset-inventory/docs/reference/rest/v1/feeds/patch) for all options.

### Command examples

Run one of the following commands to update the `my-topic` Pub/Sub topic in the `my-project` project. This request removes all asset names from monitoring, and adds the asset type `gkemulticloud.googleapis.com/AttachedCluster`. 

#### curl (Linux, macOS, or Cloud Shell)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://cloud.google.com/shell/docs), which automatically logs you into the gcloud CLI. You can check the active account by running [`gcloud auth list`](https://cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    curl -X PATCH \
         -H "X-Goog-User-Project: BILLING_PROJECT_ID" \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d '{
                "feed": {
                  "assetNames": [],
                  "assetTypes": [
                    "gkemulticloud.googleapis.com/AttachedCluster"
                  ],
                  "feedOutputConfig": {
                    "pubsubDestination": {
                      "topic": "projects/my-project/topics/my-topic"
                    }
                  }
                },
                "update_mask": {
                  "paths": ["feed_output_config.pubsub_destination.topic", "asset_names", "asset_types"]
                }
              }' \
         https://cloudasset.googleapis.com/v1/projects/**my-project** /feeds/**my-feed**

#### PowerShell (Windows)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://cloud.google.com/sdk/gcloud/reference/init) or [ `gcloud auth login`](https://cloud.google.com/sdk/gcloud/reference/auth/login). You can check the active account by running [ `gcloud auth list`](https://cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    $cred = gcloud auth print-access-token
    
    $headers = @{ 
      "X-Goog-User-Project" = "BILLING_PROJECT_ID";
      "Authorization" = "Bearer $cred"
    }
    
    
    $body = @"
    {
      "feed": {
        "assetNames": [],
        "assetTypes": [
          "gkemulticloud.googleapis.com/AttachedCluster"
        ],
        "feedOutputConfig": {
          "pubsubDestination": {
            "topic": "projects/my-project/topics/my-topic"
          }
        }
      },
      "update_mask": {
        "paths": ["feed_output_config.pubsub_destination.topic", "asset_names", "asset_types"]
      }
    }
    "@
    
    Invoke-WebRequest `
      -Method PATCH `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body $body `
      -Uri "https://cloudasset.googleapis.com/v1/projects/**my-project** /feeds/**my-feed** " | Select-Object -Expand Content

#### Example response
    
    
    {
      "feeds": [
        {
          "name": "projects/000000000000/feeds/my-feed",
          "assetTypes": [
            "bigquery.googleapis.com/Table",
            "gkemulticloud.googleapis.com/AttachedCluster"
          ],
          "contentType": "RESOURCE",
          "feedOutputConfig": {
            "pubsubDestination": {
              "topic": "projects/my-project/topics/my-topic"
            }
          }
        }
      ]
    }

#### Go

To learn how to install and use the client library for Cloud Asset Inventory, see [Cloud Asset Inventory client libraries](https://cloud.google.com/asset-inventory/docs/client-libraries). 

To authenticate to Cloud Asset Inventory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Sample update-feed update feed.
    package main
    
    import (
    	"context"
    	"flag"
    	"fmt"
    	"log"
    	"os"
    	"strconv"
    
    	asset "cloud.google.com/go/asset/apiv1"
    	"cloud.google.com/go/asset/apiv1/assetpb"
    	cloudresourcemanager "google.golang.org/api/cloudresourcemanager/v1"
    	field_mask "google.golang.org/genproto/protobuf/field_mask"
    )
    
    // Command-line flags.
    var (
    	feedID = flag.String("feed_id", "YOUR_FEED_ID", "Identifier of Feed.")
    )
    
    func main() {
    	flag.Parse()
    	ctx := context.Background()
    	client, err := asset.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/asset/latest/apiv1.html#cloud_google_com_go_asset_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		log.Fatalf("asset.NewClient: %v", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/asset/latest/apiv1.html#cloud_google_com_go_asset_apiv1_Client_Close)()
    
    	projectID := os.Getenv("GOOGLE_CLOUD_PROJECT")
    	cloudresourcemanagerClient, err := cloudresourcemanager.NewService(ctx)
    	if err != nil {
    		log.Fatalf("cloudresourcemanager.NewService: %v", err)
    	}
    
    	project, err := cloudresourcemanagerClient.Projects.Get(projectID).Do()
    	if err != nil {
    		log.Fatalf("cloudresourcemanagerClient.Projects.Get.Do: %v", err)
    	}
    	projectNumber := strconv.FormatInt(project.ProjectNumber, 10)
    	feedName := fmt.Sprintf("projects/%s/feeds/%s", projectNumber, *feedID)
    	topic := fmt.Sprintf("projects/%s/topics/%s", projectID, "TOPIC_TO_UPDATE")
    
    	req := &assetpb.UpdateFeedRequest{
    		Feed: &assetpb.Feed{
    			Name: feedName,
    			FeedOutputConfig: &assetpb.FeedOutputConfig{
    				Destination: &assetpb.FeedOutputConfig_PubsubDestination{
    					PubsubDestination: &assetpb.PubsubDestination{
    						Topic: topic,
    					},
    				},
    			},
    		},
    		UpdateMask: &field_mask.FieldMask{
    			Paths: []string{"feed_output_config.pubsub_destination.topic"},
    		},
    	}
    	response, err := client.UpdateFeed(ctx, req)
    	if err != nil {
    		log.Fatalf("client.UpdateFeed: %v", err)
    	}
    	fmt.Print(response)
    }
    

#### Java

To learn how to install and use the client library for Cloud Asset Inventory, see [Cloud Asset Inventory client libraries](https://cloud.google.com/asset-inventory/docs/client-libraries). 

To authenticate to Cloud Asset Inventory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.asset.v1.[AssetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetServiceClient.html);
    import com.google.cloud.asset.v1.[Feed](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.Feed.html);
    import com.google.cloud.asset.v1.[FeedOutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.FeedOutputConfig.html);
    import com.google.cloud.asset.v1.[PubsubDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.PubsubDestination.html);
    import com.google.cloud.asset.v1.[UpdateFeedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.UpdateFeedRequest.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    
    public class UpdateFeedExample {
    
      // Update a feed
      public static void updateFeed(String feedName, String topic) throws Exception {
        // String feedName = "MY_FEED_NAME"
        // String topic = "projects/[PROJECT_ID]/topics/[TOPIC_NAME]"
        [Feed](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.Feed.html) feed =
            [Feed](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.Feed.html).newBuilder()
                .setName(feedName)
                .[setFeedOutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.Feed.Builder.html#com_google_cloud_asset_v1_Feed_Builder_setFeedOutputConfig_com_google_cloud_asset_v1_FeedOutputConfig_)(
                    [FeedOutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.FeedOutputConfig.html).newBuilder()
                        .[setPubsubDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.FeedOutputConfig.Builder.html#com_google_cloud_asset_v1_FeedOutputConfig_Builder_setPubsubDestination_com_google_cloud_asset_v1_PubsubDestination_)([PubsubDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.PubsubDestination.html).newBuilder().[setTopic](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.PubsubDestination.Builder.html#com_google_cloud_asset_v1_PubsubDestination_Builder_setTopic_java_lang_String_)(topic).build())
                        .build())
                .build();
        [UpdateFeedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.UpdateFeedRequest.html) request =
            [UpdateFeedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.UpdateFeedRequest.html).newBuilder()
                .setFeed(feed)
                .setUpdateMask(
                    [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder()
                        .[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("feed_output_config.pubsub_destination.topic")
                        .build())
                .build();
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([AssetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetServiceClient.html) client = [AssetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetServiceClient.html).create()) {
          [Feed](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.Feed.html) response = client.updateFeed(request);
          System.out.println("Feed updated successfully: " + response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.Feed.html#com_google_cloud_asset_v1_Feed_getName__)());
        } catch (Exception e) {
          System.out.println("Error during UpdateFeed: \n" + e.toString());
        }
      }
    }

#### Node.js

To learn how to install and use the client library for Cloud Asset Inventory, see [Cloud Asset Inventory client libraries](https://cloud.google.com/asset-inventory/docs/client-libraries). 

To authenticate to Cloud Asset Inventory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const {AssetServiceClient} = require('[@google-cloud/asset](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/overview.html)');
    
    const client = new [AssetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/overview.html)();
    // example inputs:
    // const fullQueryName = 'folders/<FOLDER_NUMBER>/savedQueries/<QUERY_ID>';
    // const description = 'a new description';
    async function updateSavedQuery() {
      const request = {
        savedQuery: {
          name: fullQueryName,
          description: description,
        },
        updateMask: {
          paths: ['description'],
        },
      };
    
      // Handle the operation using the promise pattern.
      const [query] = await client.updateSavedQuery(request);
      // Do things with with the response.
      console.log('Query name:', query.name);
      console.log('Query description:', query.description);
      console.log('Created time:', query.createTime);
      console.log('Updated time:', query.lastUpdateTime);
      console.log('Query type:', query.content.[queryContent](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1.savedquery.querycontent.html));
      console.log('Query content:', JSON.stringify(query.content, null, 4));

#### Python

To learn how to install and use the client library for Cloud Asset Inventory, see [Cloud Asset Inventory client libraries](https://cloud.google.com/asset-inventory/docs/client-libraries). 

To authenticate to Cloud Asset Inventory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest)
    from google.protobuf import field_mask_pb2
    
    # TODO feed_name = 'Feed Name you want to update'
    # TODO topic = "Topic name you want to update with"
    
    client = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[AssetServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient.html)()
    feed = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[Feed](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.Feed.html)()
    feed.name = feed_name
    feed.feed_output_config.pubsub_destination.topic = topic
    update_mask = field_mask_pb2.FieldMask()
    # In this example, we update topic of the feed
    update_mask.paths.append("feed_output_config.pubsub_destination.topic")
    response = client.[update_feed](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient.html#google_cloud_asset_v1_services_asset_service_AssetServiceClient_update_feed)(request={"feed": feed, "update_mask": update_mask})
    print(f"updated_feed: {response}")

## Delete feeds

If you no longer want to be notified of asset changes, make one of the following requests to delete a feed.

#### gcloud
    
    
    gcloud asset feeds delete FEED_ID \
        --SCOPE \
        --billing-project=BILLING_PROJECT_ID

Provide the following values:

  * `SCOPE`: Use one of the following values:

    * `project=PROJECT_ID`, where `PROJECT_ID` is the ID of the project that the feed is in. 
    * `folder=FOLDER_ID`, where `FOLDER_ID` is the ID of the folder that the feed is in. 

How to find the ID of a Google Cloud folder

### Google Cloud console

To find the ID of a Google Cloud folder, complete the following steps:

      1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box.
      4. Search for your folder name. The folder ID is shown next to the folder name.

### gcloud CLI

You can retrieve the ID of a Google Cloud folder that's located at the organization level with the following command:
    
    gcloud resource-manager folders list \
        --organization=$(gcloud organizations describe ORGANIZATION_NAME \
          --format="value(name.segment(1))") \
        --filter='"DISPLAY_NAME":"TOP_LEVEL_FOLDER_NAME"' \
        --format="value(ID)"

Where TOP_LEVEL_FOLDER_NAME is a partial or full string match for the folder's name. Remove the `--format` flag to see more information about the found folders.

The previous command doesn't return the IDs of subfolders within folders. To do so, run the following command using a top level folder's ID:
    
    gcloud resource-manager folders list --folder=FOLDER_ID

    * `organization=ORGANIZATION_ID`, where `ORGANIZATION_ID` is the ID of the organization that the feed is in. 

How to find the ID of a Google Cloud organization

### Google Cloud console

To find the ID of a Google Cloud organization, complete the following steps:

      1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box.
      4. Click the **All** tab. The organization ID is shown next to the organization name.

### gcloud CLI

You can retrieve the ID of a Google Cloud organization with the following command:
    
    gcloud organizations describe ORGANIZATION_NAME --format="value(name.segment(1))"

  * `BILLING_PROJECT_ID`: The project ID that the default Cloud Asset Inventory service agent is in that has permissions to manage your Pub/Sub topic. [ Read more about setting the billing project](https://cloud.google.com/asset-inventory/docs/multiple-projects#orchestrator). 



See the [gcloud CLI reference](https://cloud.google.com/sdk/gcloud/reference/asset/feeds/delete) for all options. 

#### Example response

A successful deletion returns no response.

#### REST

HTTP method and URL:
    
    
    DELETE https://cloudasset.googleapis.com/v1/SCOPE_PATH/feeds/FEED_ID
    

Headers:
    
    
    X-Goog-User-Project: BILLING_PROJECT_ID

Provide the following values:

  * `SCOPE_PATH`: Use one of the following values:

    * `projects/PROJECT_NUMBER`, where `PROJECT_NUMBER` is the number of the project that the feed is in. 

How to find a Google Cloud project number

### Google Cloud console

To find a Google Cloud project number, complete the following steps:

      1. Go to the **Welcome** page in the Google Cloud console.

[ Go to Welcome](https://console.cloud.google.com/welcome)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box, and then search for your project name. The project name, project number, and project ID are shown near the **Welcome** heading. 

Up to 4,000 resources are displayed. If you don't see the project you're looking for, go to the [**Manage resources**](https://console.cloud.google.com//cloud-resource-manager) page and filter the list using the name of that project. 

### gcloud CLI

You can retrieve a Google Cloud project number with the following command:
    
    gcloud projects describe PROJECT_ID --format="value(projectNumber)"

    * `folders/FOLDER_ID`, where `FOLDER_ID` is the ID of the folder that the feed is in. 

How to find the ID of a Google Cloud folder

### Google Cloud console

To find the ID of a Google Cloud folder, complete the following steps:

      1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box.
      4. Search for your folder name. The folder ID is shown next to the folder name.

### gcloud CLI

You can retrieve the ID of a Google Cloud folder that's located at the organization level with the following command:
    
    gcloud resource-manager folders list \
        --organization=$(gcloud organizations describe ORGANIZATION_NAME \
          --format="value(name.segment(1))") \
        --filter='"DISPLAY_NAME":"TOP_LEVEL_FOLDER_NAME"' \
        --format="value(ID)"

Where TOP_LEVEL_FOLDER_NAME is a partial or full string match for the folder's name. Remove the `--format` flag to see more information about the found folders.

The previous command doesn't return the IDs of subfolders within folders. To do so, run the following command using a top level folder's ID:
    
    gcloud resource-manager folders list --folder=FOLDER_ID

    * `organizations/ORGANIZATION_ID`, where `ORGANIZATION_ID` is the ID of the organization that the feed is in. 

How to find the ID of a Google Cloud organization

### Google Cloud console

To find the ID of a Google Cloud organization, complete the following steps:

      1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box.
      4. Click the **All** tab. The organization ID is shown next to the organization name.

### gcloud CLI

You can retrieve the ID of a Google Cloud organization with the following command:
    
    gcloud organizations describe ORGANIZATION_NAME --format="value(name.segment(1))"

  * `BILLING_PROJECT_ID`: The project ID that the default Cloud Asset Inventory service agent is in that has permissions to manage your Pub/Sub topic. [ Read more about setting the billing project](https://cloud.google.com/asset-inventory/docs/multiple-projects#orchestrator). 



See the [REST reference](https://cloud.google.com/asset-inventory/docs/reference/rest/v1/feeds/delete) for all options.

### Command examples

Run one of the following commands to delete a specific feed.

#### curl (Linux, macOS, or Cloud Shell)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://cloud.google.com/shell/docs), which automatically logs you into the gcloud CLI. You can check the active account by running [`gcloud auth list`](https://cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    curl -X DELETE \
         -H "X-Goog-User-Project: BILLING_PROJECT_ID" \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         https://cloudasset.googleapis.com/v1/projects/**000000000000** /feeds/**my-feed**

#### PowerShell (Windows)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://cloud.google.com/sdk/gcloud/reference/init) or [ `gcloud auth login`](https://cloud.google.com/sdk/gcloud/reference/auth/login). You can check the active account by running [ `gcloud auth list`](https://cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    $cred = gcloud auth print-access-token
    
    $headers = @{ 
      "X-Goog-User-Project" = "BILLING_PROJECT_ID";
      "Authorization" = "Bearer $cred"
    }
    
    
    Invoke-WebRequest `
      -Method DELETE `
      -Headers $headers `
      -Uri "https://cloudasset.googleapis.com/v1/projects/**000000000000** /feeds/**my-feed** " | Select-Object -Expand Content

#### Example response
    
    
    {}

#### Go

To learn how to install and use the client library for Cloud Asset Inventory, see [Cloud Asset Inventory client libraries](https://cloud.google.com/asset-inventory/docs/client-libraries). 

To authenticate to Cloud Asset Inventory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Sample delete-feed delete feed.
    package main
    
    import (
    	"context"
    	"flag"
    	"fmt"
    	"log"
    	"os"
    	"strconv"
    
    	asset "cloud.google.com/go/asset/apiv1"
    	"cloud.google.com/go/asset/apiv1/assetpb"
    	cloudresourcemanager "google.golang.org/api/cloudresourcemanager/v1"
    )
    
    // Command-line flags.
    var (
    	feedID = flag.String("feed_id", "YOUR_FEED_ID", "Identifier of Feed.")
    )
    
    func main() {
    	flag.Parse()
    	ctx := context.Background()
    	client, err := asset.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/asset/latest/apiv1.html#cloud_google_com_go_asset_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		log.Fatalf("asset.NewClient: %v", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/asset/latest/apiv1.html#cloud_google_com_go_asset_apiv1_Client_Close)()
    
    	projectID := os.Getenv("GOOGLE_CLOUD_PROJECT")
    	cloudresourcemanagerClient, err := cloudresourcemanager.NewService(ctx)
    	if err != nil {
    		log.Fatalf("cloudresourcemanager.NewService: %v", err)
    	}
    
    	project, err := cloudresourcemanagerClient.Projects.Get(projectID).Do()
    	if err != nil {
    		log.Fatalf("cloudresourcemanagerClient.Projects.Get.Do: %v", err)
    	}
    	projectNumber := strconv.FormatInt(project.ProjectNumber, 10)
    	feedName := fmt.Sprintf("projects/%s/feeds/%s", projectNumber, *feedID)
    	req := &assetpb.DeleteFeedRequest{
    		Name: feedName,
    	}
    	if err = client.DeleteFeed(ctx, req); err != nil {
    		log.Fatalf("client.DeleteFeed: %v", err)
    	}
    	fmt.Print("Deleted Feed")
    }
    

#### Java

To learn how to install and use the client library for Cloud Asset Inventory, see [Cloud Asset Inventory client libraries](https://cloud.google.com/asset-inventory/docs/client-libraries). 

To authenticate to Cloud Asset Inventory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.asset.v1.[AssetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetServiceClient.html);
    
    public class DeleteFeedExample {
    
      // Delete a feed with full feed name
      public static void deleteFeed(String feedName) throws Exception {
        // String feedName = "MY_FEED_NAME"
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([AssetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetServiceClient.html) client = [AssetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetServiceClient.html).create()) {
          client.deleteFeed(feedName);
          System.out.println("Feed deleted");
        } catch (Exception e) {
          System.out.println("Error during DeleteFeed: \n" + e.toString());
        }
      }
    }

#### Node.js

To learn how to install and use the client library for Cloud Asset Inventory, see [Cloud Asset Inventory client libraries](https://cloud.google.com/asset-inventory/docs/client-libraries). 

To authenticate to Cloud Asset Inventory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const util = require('util');
    const {AssetServiceClient} = require('[@google-cloud/asset](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/overview.html)');
    
    const client = new [AssetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/overview.html)();
    
    async function deleteFeed() {
      const request = {
        name: feedName,
      };
    
      // Handle the operation using the promise pattern.
      const result = await client.deleteFeed(request);
      // Do things with with the response.
      console.log(util.inspect(result, {depth: null}));

#### Python

To learn how to install and use the client library for Cloud Asset Inventory, see [Cloud Asset Inventory client libraries](https://cloud.google.com/asset-inventory/docs/client-libraries). 

To authenticate to Cloud Asset Inventory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest)
    
    # TODO feed_name = 'Feed name you want to delete'
    
    client = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[AssetServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient.html)()
    client.[delete_feed](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient.html#google_cloud_asset_v1_services_asset_service_AssetServiceClient_delete_feed)(request={"name": feed_name})
    print("deleted_feed")

## Feed conditions

To view only certain types of changes for a given asset, you can add a condition to your feed. Conditions are written in [Common Expression Language (CEL)](https://github.com/google/cel-spec).

Support for conditions is limited. In some cases, creating or updating feeds with conditions might result in a delay.

### Limitations

  * Condition expressions have a length limit of 3,000 characters.

  * Most variable names in condition expressions are represented in lowercase with underscores between each word. For example, `example_variable`.

The exception is the variable names of the sub-fields of `data` in the [Resource](https://cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.Resource) object. These don't have word separators, and the first character of each word after the first is capitalized. For example, `exampleVariable`.

  * Some validations on condition expressions are performed during feed creation or feed update time. However, such validations are not comprehensive, especially for conditions set on the `temporal_asset.asset.resource.data` field, which has a dynamic type. Where possible, filter your feed by using the appropriate gcloud CLI or REST API parameters instead.

  * Notifications aren't sent if errors happen during evaluation time, however the errors are logged.

  * For dynamic types in `temporal_asset.asset.resource.data`, conditions specified on absent fields trigger runtime errors and notifications aren't published. For example, for the condition `temporal_asset.asset.resource.data.name != "my_name"`, if the `name` field is missing in an update, the evaluation fails and you don't receive notifications. If your condition only works in the presence of certain fields, add an existence check to the condition to ensure it is properly evaluated.

  * Static enum types can be represented as either fully qualified path names or raw integers. For example, the following expressions are valid for `prior_asset_state`:
        
        temporal_asset.prior_asset_state == google.cloud.asset.v1.TemporalAsset.PriorAssetState.DOES_NOT_EXIST
        

and
        
        temporal_asset.prior_asset_state == 3
        

Dynamic enum types in `temporal_asset.asset.resource.data` are represented as raw strings. For example, the following expression is valid for the asset type `cloudresourcemanager.googleapis.com/Project`:
        
        temporal_asset.asset.resource.data.lifecycleState == "ACTIVE"
        




### Create a condition expression with CEL

In a feed condition, [Common Expression Language (CEL)](https://github.com/google/cel-spec) is used to make boolean decisions based on attribute data. A condition expression consists of one or more statements that are joined using logic operators. Each statement expresses an attribute-based control rule that applies to the `TemporalAsset` to determine whether a notification is sent.

The following CEL features are the most important for feed conditions:

  * **Variables** : Conditions use variables to express a given attribute, such as `temporal_asset.deleted` (`Boolean`) or `temporal_asset.asset.name` (`String`). These variables are populated with values based on the context at runtime.

  * **Operators** : Every data type, such as `String`, supports a set of operators that can be used to create a logic expression. Most commonly, operators are used to compare the value contained in a variable with a literal value, such as `temporal_asset.asset.name == "//cloudresourcemanager.googleapis.com/projects/12345"`. In this example, if the input value of `temporal_asset.asset.name` is `//cloudresourcemanager.googleapis.com/projects/12345`, then the expression evaluates to `true`.

  * **Functions** : A function is a compound operator for data types that support more complex operations. In condition expressions, there are predefined functions that can be used in conjunction with a given data type. For example, `temporal_asset.asset.name.contains("keyword")` uses a function called `contains` to check if the value of `temporal_asset.asset.name` contains `"keyword"`. If so, it evaluates to `true`.

  * **Logical operators** : Conditions support logical operators that can be used to build complex logic expressions from basic expression statements: `&&` (AND) and `||` (OR). These logical operators make it possible to use multiple input variables in a condition expression. For example: `temporal_asset.deleted && temporal_asset.window.start_time.getFullYear() > 2020` joins two basic statements, and requires both statements to be met in order to produce a `true` evaluation result.




For more information about CEL features, see the [language definition](https://github.com/google/cel-spec/blob/master/doc/langdef.md).

#### Handle unset properties

When accessing fields in the `temporal_asset.asset.resource.data` payload, it's important to safely handle potentially unset fields, keys, or parent messages to avoid errors or unexpected behavior.

For example, for an expression that monitors Compute Engine instance updates and excludes instances with the label `xyz`, you might write something similar to the following:
    
    
    (has(temporal_asset.asset.resource.data) && !('xyz' in temporal_asset.asset.resource.data.labels))
    

The `!('xyz' in temporal_asset.asset.resource.data.labels)` part of this expression, however, filters out both assets with the `xyz` label _and_ assets with no labels at all. This is because unlabeled assets don't have a label that contains `xyz`.

A correct expression to include unlabeled assets might look like the following:
    
    
    (has(temporal_asset.asset.resource.data) && (!has(temporal_asset.asset.resource.data.labels) || !('xyz' in temporal_asset.asset.resource.data.labels)))
    

### Using condition variables

Condition variables allow you to create conditions on different attributes. Supported condition variables are:

  * **temporal_asset** : The most recent asset change in [TemporalAsset](https://cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#temporalasset) format. If the condition evaluates to true, the `TemporalAsset` is sent to the configured destination.



### Example condition expressions

The following condition expression sends notifications on creation events:
    
    
    temporal_asset.deleted == false &&
    temporal_asset.prior_asset_state == google.cloud.asset.v1.TemporalAsset.PriorAssetState.DOES_NOT_EXIST
    

The following condition expression sends notifications for resources that are located in folders `12345` and `23456`:
    
    
    "folders/12345" in temporal_asset.asset.ancestors ||
    "folders/23456" in temporal_asset.asset.ancestors
    

The following condition expression sends notifications when new allowed rules are added to firewalls, assuming the asset type is already set to `compute.googleapis.com/Firewall` in the feed:
    
    
    size(temporal_asset.asset.resource.data.allowed) >
    size(temporal_asset.prior_asset.resource.data.allowed)
    

The following condition expression sends notifications for VM instances with `n1-standard-1` machine type, assuming the asset type is already set to `compute.googleapis.com/Instance` in the feed:
    
    
    temporal_asset.asset.resource.data.machineType.endsWith('/machineTypes/n1-standard-1')
    

The following condition expression sends notifications for storage buckets with any IAM policies for `allUsers`, assuming the asset type is set to `storage.googleapis.com/Bucket`, and the content type is set to `IAM_POLICY` in the feed:
    
    
    temporal_asset.asset.iam_policy.bindings.exists(b, b.members.exists(m, m == "allUsers"))
    

The following condition expression sends a notification when a storage bucket with the `test` key in its label is deleted:
    
    
    temporal_asset.deleted == true && temporal_asset.prior_asset_state == google.cloud.asset.v1.TemporalAsset.PriorAssetState.PRESENT && "test" in temporal_asset.prior_asset.resource.data.labels
    

## Troubleshooting

If you're not receiving notifications for resource or IAM policy updates, the following steps can help you to troubleshoot:

  * Make sure that the metadata has changed on your assets. The real-time feed only sends updates when the metadata of the supported [resource types](https://cloud.google.com/asset-inventory/docs/asset-types#resource-types) has changed. Operations such as uploading a new file to your Cloud Storage bucket does not trigger a metadata change.

  * Make sure your assets match one of the asset names or types you specified in the feed.

  * For project deletions, keep in mind that when you [shut down a project](https://cloud.google.com/resource-manager/docs/creating-managing-projects#shut_down_a_project) you have 30 days to undo the operation. Because of this, the `deleted` field in the asset metadata is not set until the project is permanently deleted. To monitor projects that are pending deletion, you can set a condition on the project's `lifecycleState` field instead. For example: `temporal_asset.asset.resource.data.lifecycleState == "DELETE_REQUESTED"`.

  * Check the logs to see if there are errors when publishing updates to your topic.




## Cloud Logging

When real-time feeds fail to send resources or IAM policy updates through Pub/Sub, Cloud Asset Inventory logs the error status and message in Logging. Logging is enabled by default, and belongs to Google Cloud Observability. Learn about [Google Cloud Observability pricing](https://cloud.google.com/stackdriver/pricing).

### Viewing real-time feed logs

The real-time feed log is indexed by a Pub/Sub topic. To see all logs:

  1. Go to the **Logs Explorer** page in the Google Cloud console.

[Go to Logs Explorer](https://console.cloud.google.com/logs)

  2. Click the **Resource** list, which is near to the **Search all fields** box.

  3. Search for `Cloud Pub/Sub Topic`, and then click the **Cloud Pub/Sub Topic** resource type.

  4. Click the topic ID you want to view.

  5. Click **Apply**.




UTF-8 encoding is enforced for log fields. Characters that are not UTF-8 characters are replaced with question marks.

### Logged information

Real-time feed log entries contain following types of information:

  * General information shown in most Google Cloud logs, such as severity, project ID, project number, or timestamp.

  * Real-time feed log fields in `jsonPayload`, which contains asset name, feed output config, and error status when publishing resource or IAM policy updates.




The following table shows what kind of information each field contains.

Field | Type and description  
---|---  
`name` |  `string` Full Name of the feed. The format is one of the following:

  * ` projects/PROJECT_ID/feeds/FEED_ID `
  * ` folders/FOLDER_ID/feeds/FEED_ID `
  * ` organizations/ORGANIZATION_ID/feeds/FEED_ID `

  
`asset_name` |  `string` Full name of the asset to receive updates. For example: ` //compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1 ` See [ Resource names ](https://cloud.google.com/apis/design/resource_names#full_resource_name) for more info.   
`condition` |  ` [ Expr ](https://cloud.google.com/asset-inventory/docs/reference/rpc/google.type#expr) ` Feed condition which determines whether an asset update should be published.   
`error_status` |  ` [ Status ](https://cloud.google.com/tasks/docs/reference/rpc/google.rpc#google.rpc.Status) ` Status when there's a failure to publish asset updates to a feed.  
`feed_output_config` |  ` [ FeedOutputConfig ](https://cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.FeedOutputConfig) ` Feed output configuration defining where the asset updates are published to.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
