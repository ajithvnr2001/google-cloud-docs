---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-create-notification-config/
title: Create a NotificationConfig \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:48:09.767997+00:00
---

# Create a NotificationConfig  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-create-notification-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  Create a NotificationConfig Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to create a NotificationConfig

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Creating and managing Notification Configs](https://docs.cloud.google.com/security-command-center/docs/how-to-api-manage-notifications)
  * [Enable finding notifications for Pub/Sub](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications)



## Code sample

### C#

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.SecurityCenter.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.html);
    using System;
    
    ///<summary> Create NotificationConfig Snippet. </summary>
    public class CreateNotificationConfigSnippets
    {
        public static NotificationConfig CreateNotificationConfig(
            string organizationId, string notificationConfigId, string projectId, string topicName)
        {
            // You can also use 'projectId' or 'folderId' instead of the 'organizationId'.
            //      ProjectName projectName = new ProjectName(projectId);
            //      FolderName folderName = new FolderName(folderId);
            [OrganizationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.OrganizationName.html) orgName = new [OrganizationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.OrganizationName.html)(organizationId);
            [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.TopicName.html) pubsubTopic = new [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.TopicName.html)(projectId, topicName);
    
            [SecurityCenterClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.SecurityCenterClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.SecurityCenterClient.html#Google_Cloud_SecurityCenter_V1_SecurityCenterClient_Create)();
            [CreateNotificationConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.CreateNotificationConfigRequest.html) request = new [CreateNotificationConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.CreateNotificationConfigRequest.html)
            {
                ParentAsOrganizationName = orgName,
                ConfigId = notificationConfigId,
                NotificationConfig = new [NotificationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.NotificationConfig.html)
                {
                    Description = ".Net notification config",
                    PubsubTopicAsTopicName = pubsubTopic,
                    StreamingConfig = new NotificationConfig.Types.StreamingConfig { Filter = "state = \"ACTIVE\"" }
                }
            };
    
            [NotificationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.NotificationConfig.html) response = client.[CreateNotificationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.SecurityCenterClient.html#Google_Cloud_SecurityCenter_V1_SecurityCenterClient_CreateNotificationConfig_Google_Api_Gax_ResourceNames_FolderName_Google_Cloud_SecurityCenter_V1_NotificationConfig_Google_Api_Gax_Grpc_CallSettings_)(request);
            Console.WriteLine($"Notification config was created: {response}");
            return response;
        }
    }

### Go

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	securitycenter "cloud.google.com/go/securitycenter/apiv1"
    	"cloud.google.com/go/securitycenter/apiv1/securitycenterpb"
    )
    
    func createNotificationConfig(w io.Writer, orgID string, pubsubTopic string, notificationConfigID string) error {
    	// orgID := "your-org-id"
    	// pubsubTopic := "projects/{your-project}/topics/{your-topic}"
    	// notificationConfigID := "your-config-id"
    
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_NewClient)(ctx)
    
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_Close)()
    
    	req := &securitycenterpb.CreateNotificationConfigRequest{
    		// Parent must be in one of the following formats:
    		//		"organizations/{orgId}"
    		//		"projects/{projectId}"
    		//		"folders/{folderId}"
    		Parent:   fmt.Sprintf("organizations/%s", orgID),
    		ConfigId: notificationConfigID,
    		NotificationConfig: &securitycenterpb.NotificationConfig{
    			Description: "Go sample config",
    			PubsubTopic: pubsubTopic,
    			NotifyConfig: &securitycenterpb.NotificationConfig_StreamingConfig_{
    				StreamingConfig: &securitycenterpb.NotificationConfig_StreamingConfig{
    					Filter: `state = "ACTIVE"`,
    				},
    			},
    		},
    	}
    
    	notificationConfig, err := client.CreateNotificationConfig(ctx, req)
    	if err != nil {
    		return fmt.Errorf("Failed to create notification config: %w", err)
    	}
    	fmt.Fprintln(w, "New NotificationConfig created: ", notificationConfig)
    
    	return nil
    }
    

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    package vtwo.notifications;
    
    import com.google.cloud.securitycenter.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.LocationName.html);
    import com.google.cloud.securitycenter.v2.[NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.NotificationConfig.html);
    import com.google.cloud.securitycenter.v2.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html);
    import java.io.IOException;
    
    public class CreateNotification {
    
      public static void main(String[] args) throws IOException {
        // parentId: must be in one of the following formats:
        //    "organizations/{organization_id}"
        //    "projects/{project_id}"
        //    "folders/{folder_id}"
        String parentId = "{parent-id}";
        String topicName = "{your-topic}";
        String notificationConfigId = "{your-notification-id}";
        // Specify the location of the notification config.
        String location = "global";
    
        createNotificationConfig(parentId, location, topicName, notificationConfigId);
      }
    
      // Crete a notification config.
      // Ensure the ServiceAccount has the "pubsub.topics.setIamPolicy" permission on the new topic.
      public static [NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.NotificationConfig.html) createNotificationConfig(
          String parentId, String location, String topicName, String notificationConfigId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html).create()) {
    
          String pubsubTopic = String.format("projects/%s/topics/%s", parentId, topicName);
    
          [NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.NotificationConfig.html) notificationConfig = [NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.NotificationConfig.html).newBuilder()
              .setDescription("Java notification config")
              .[setPubsubTopic](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.NotificationConfig.Builder.html#com_google_cloud_securitycenter_v2_NotificationConfig_Builder_setPubsubTopic_java_lang_String_)(pubsubTopic)
              .[setStreamingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.NotificationConfig.Builder.html#com_google_cloud_securitycenter_v2_NotificationConfig_Builder_setStreamingConfig_com_google_cloud_securitycenter_v2_NotificationConfig_StreamingConfig_)(
                  [NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.NotificationConfig.html).StreamingConfig.newBuilder().setFilter("state = \"ACTIVE\"")
                      .build())
              .build();
    
          [NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.NotificationConfig.html) response = client.createNotificationConfig(
              [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.LocationName.html).of(parentId, location), notificationConfig, notificationConfigId);
    
          System.out.printf("Notification config was created: %s%n", response);
          return response;
        }
      }
    }

### Node.js

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // npm install '@google-cloud/security-center'
    const {SecurityCenterClient} = require('[@google-cloud/security-center](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)');
    
    const client = new [SecurityCenterClient](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)();
    
    // parent: must be in one of the following formats:
    //    `organizations/${organization_id}`
    //    `projects/${project_id}`
    //    `folders/${folder_id}`
    // configId = "your-config-name";
    // pubsubTopic = "projects/{your-project}/topics/{your-topic}";
    // Ensure this Service Account has the "pubsub.topics.setIamPolicy" permission on this topic.
    const parent = `organizations/${organizationId}`;
    
    async function createNotificationConfig() {
      const [response] = await client.createNotificationConfig({
        parent: parent,
        configId: configId,
        notificationConfig: {
          description: 'Sample config for node.js',
          pubsubTopic: pubsubTopic,
          streamingConfig: {filter: 'state = "ACTIVE"'},
        },
      });
      console.log('Notification config creation succeeded: ', response);
    }
    
    createNotificationConfig();

### PHP

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\SecurityCenter\V1\Client\SecurityCenterClient;
    use Google\Cloud\SecurityCenter\V1\CreateNotificationConfigRequest;
    use Google\Cloud\SecurityCenter\V1\NotificationConfig;
    use Google\Cloud\SecurityCenter\V1\NotificationConfig\StreamingConfig;
    
    /**
     * @param string $organizationId        Your org ID
     * @param string $notificationConfigId  A unique identifier
     * @param string $projectId             Your Cloud Project ID
     * @param string $topicName             Your topic name
     */
    function create_notification(
        string $organizationId,
        string $notificationConfigId,
        string $projectId,
        string $topicName
    ): void {
        $securityCenterClient = new SecurityCenterClient();
        // 'parent' must be in one of the following formats:
        //		"organizations/{orgId}"
        //		"projects/{projectId}"
        //		"folders/{folderId}"
        $parent = $securityCenterClient::organizationName($organizationId);
        $pubsubTopic = $securityCenterClient::topicName($projectId, $topicName);
    
        $streamingConfig = (new StreamingConfig())->setFilter('state = "ACTIVE"');
        $notificationConfig = (new NotificationConfig())
            ->setDescription('A sample notification config')
            ->setPubsubTopic($pubsubTopic)
            ->setStreamingConfig($streamingConfig);
        $createNotificationConfigRequest = (new CreateNotificationConfigRequest())
            ->setParent($parent)
            ->setConfigId($notificationConfigId)
            ->setNotificationConfig($notificationConfig);
    
        $response = $securityCenterClient->createNotificationConfig($createNotificationConfigRequest);
        printf('Notification config was created: %s' . PHP_EOL, $response->getName());
    }

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def create_notification_config(parent_id, notification_config_id, pubsub_topic):
        """
        Args:
            parent_id: must be in one of the following formats:
                "organizations/{organization_id}"
                "projects/{project_id}"
                "folders/{folder_id}"
            notification_config_id: "your-config-id"
            pubsub_topic: "projects/{your-project-id}/topics/{your-topic-ic}"
    
        Ensure this ServiceAccount has the "pubsub.topics.setIamPolicy" permission on the new topic.
        """
        from google.cloud import securitycenter as securitycenter
    
        client = securitycenter.SecurityCenterClient()
    
        created_notification_config = client.create_notification_config(
            request={
                "parent": parent_id,
                "config_id": notification_config_id,
                "notification_config": {
                    "description": "Notification for active findings",
                    "pubsub_topic": pubsub_topic,
                    "streaming_config": {"filter": 'state = "ACTIVE"'},
                },
            }
        )
    
        print(created_notification_config)

### Ruby

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/security_center"
    
    # Your organization id. e.g. for "organizations/123", this would be "123".
    # org_id = "YOUR_ORGANZATION_ID"
    
    # Your location. e.g. "global" or "us".
    # location = "global"
    
    # Your notification config id within its parent scope. e.g. for
    # "organizations/123/locations/global/notificationConfigs/my-config" this would be "my-config".
    # config_id = "YOUR_CONFIG_ID"
    
    # The PubSub topic where notifications will be published.
    # pubsub_topic = "YOUR_TOPIC"
    
    client = Google::Cloud::[SecurityCenter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter.html).[security_center](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center/latest/Google-Cloud-SecurityCenter.html)
    
    # You can also use a project or folder path as a parent.
    parent = client.organization_location_path organization: org_id, location: location
    
    notification_config = {
      description:      "Sample config for Ruby",
      pubsub_topic:     pubsub_topic,
      streaming_config: { filter: 'state = "ACTIVE"' }
    }
    
    response = client.create_notification_config(
      parent:              parent,
      config_id:           config_id,
      notification_config: notification_config
    )
    puts "Created notification config #{config_id}: #{response}."

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
