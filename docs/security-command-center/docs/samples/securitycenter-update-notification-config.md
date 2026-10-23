---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-update-notification-config/
title: Update a NotificationConfig \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:31:39.712916+00:00
---

# Update a NotificationConfig  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-update-notification-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  Update a NotificationConfig Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to update a NotificationConfig

## Code sample

### C#

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.SecurityCenter.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.html);
    using static Google.Cloud.SecurityCenter.V1.NotificationConfig.Types;
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System;
    
    /// <summary>Snippet for UpdateNotificationConfig</summary>
    public class UpdateNotificationConfigSnippets
    {
        public static NotificationConfig UpdateNotificationConfig(
            string organizationId, string notificationConfigId, string projectId, string topicName)
        {
            // You can also use 'projectId' or 'folderId' instead of the 'organizationId'.
            [NotificationConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.NotificationConfigName.html) notificationConfigName = new [NotificationConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.NotificationConfigName.html)(organizationId, notificationConfigId);
            [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.TopicName.html) pubsubTopic = new [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.TopicName.html)(projectId, topicName);
    
            [NotificationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.NotificationConfig.html) configToUpdate = new [NotificationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.NotificationConfig.html)
            {
                NotificationConfigName = notificationConfigName,
                Description = "updated description",
                PubsubTopicAsTopicName = pubsubTopic,
                StreamingConfig = new StreamingConfig { Filter = "state = \"INACTIVE\"" }
            };
    
            [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html) fieldMask = new [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html) { Paths = { "description", "pubsub_topic", "streaming_config.filter" } };
            [SecurityCenterClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.SecurityCenterClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.SecurityCenterClient.html#Google_Cloud_SecurityCenter_V1_SecurityCenterClient_Create)();
            [NotificationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.NotificationConfig.html) updatedConfig = client.[UpdateNotificationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.SecurityCenterClient.html#Google_Cloud_SecurityCenter_V1_SecurityCenterClient_UpdateNotificationConfig_Google_Cloud_SecurityCenter_V1_NotificationConfig_Google_Api_Gax_Grpc_CallSettings_)(configToUpdate, fieldMask);
    
            Console.WriteLine($"Notification config updated: {updatedConfig}");
            return updatedConfig;
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
    	"google.golang.org/genproto/protobuf/field_mask"
    )
    
    func updateNotificationConfig(w io.Writer, orgID string, notificationConfigID string, updatedPubsubTopic string) error {
    	// orgID := "your-org-id"
    	// notificationConfigID := "your-config-id"
    	// updatedPubsubTopic := "projects/{new-project}/topics/{new-topic}"
    
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_NewClient)(ctx)
    
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_Close)()
    
    	updatedDescription := "Updated sample config"
    	updatedFilter := `state = "INACTIVE"`
    	// Parent must be in one of the following formats:
    	//		"organizations/{orgId}"
    	//		"projects/{projectId}"
    	//		"folders/{folderId}"
    	parent := fmt.Sprintf("organizations/%s", orgID)
    	req := &securitycenterpb.UpdateNotificationConfigRequest{
    		NotificationConfig: &securitycenterpb.NotificationConfig{
    			Name:        fmt.Sprintf("%s/notificationConfigs/%s", parent, notificationConfigID),
    			Description: updatedDescription,
    			PubsubTopic: updatedPubsubTopic,
    			NotifyConfig: &securitycenterpb.NotificationConfig_StreamingConfig_{
    				StreamingConfig: &securitycenterpb.NotificationConfig_StreamingConfig{
    					Filter: updatedFilter,
    				},
    			},
    		},
    		UpdateMask: &field_mask.FieldMask{
    			Paths: []string{"description", "pubsub_topic", "streaming_config.filter"},
    		},
    	}
    
    	notificationConfig, err := client.UpdateNotificationConfig(ctx, req)
    	if err != nil {
    		return fmt.Errorf("Failed to update notification config: %w", err)
    	}
    
    	fmt.Fprintln(w, "Updated NotificationConfig: ", notificationConfig)
    
    	return nil
    }
    

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.securitycenter.v1.[NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.NotificationConfig.html);
    import com.google.cloud.securitycenter.v1.[NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.NotificationConfig.html).[StreamingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.NotificationConfig.StreamingConfig.html);
    import com.google.cloud.securitycenter.v1.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.io.IOException;
    
    public class UpdateNotificationConfigSnippets {
    
      public static void main(String[] args) throws IOException {
        // parentId: must be in one of the following formats:
        //    "organizations/{organization_id}"
        //    "projects/{project_id}"
        //    "folders/{folder_id}"
        String parentId = String.format("organizations/%s", "ORG_ID");
        String notificationConfigId = "{config-id}";
        String projectId = "{your-project}";
        String topicName = "{your-topic}";
    
        updateNotificationConfig(parentId, notificationConfigId, projectId, topicName);
      }
    
      // Update an existing notification config.
      // If updating a Pubsub Topic, ensure the ServiceAccount has the
      // "pubsub.topics.setIamPolicy" permission on the new topic.
      public static [NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.NotificationConfig.html) updateNotificationConfig(
          String parentId, String notificationConfigId, String projectId, String topicName)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html).create()) {
    
          String notificationConfigName =
              String.format(
                  "%s/notificationConfigs/%s", parentId, notificationConfigId);
    
          // Ensure this ServiceAccount has the "pubsub.topics.setIamPolicy" permission on the topic.
          String pubsubTopic = String.format("projects/%s/topics/%s", projectId, topicName);
    
          [NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.NotificationConfig.html) configToUpdate =
              [NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.NotificationConfig.html).newBuilder()
                  .setName(notificationConfigName)
                  .setDescription("updated description")
                  .[setPubsubTopic](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.NotificationConfig.Builder.html#com_google_cloud_securitycenter_v1_NotificationConfig_Builder_setPubsubTopic_java_lang_String_)(pubsubTopic)
                  .[setStreamingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.NotificationConfig.Builder.html#com_google_cloud_securitycenter_v1_NotificationConfig_Builder_setStreamingConfig_com_google_cloud_securitycenter_v1_NotificationConfig_StreamingConfig_)([StreamingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.NotificationConfig.StreamingConfig.html).newBuilder().setFilter("state = \"ACTIVE\""))
                  .build();
    
          [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) fieldMask =
              [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder()
                  .[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("description")
                  .[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("pubsub_topic")
                  .[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("streaming_config.filter")
                  .build();
    
          [NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.NotificationConfig.html) updatedConfig = client.updateNotificationConfig(configToUpdate, fieldMask);
    
          System.out.printf("Notification config: %s%n", updatedConfig);
          return updatedConfig;
        }
      }
    }

### Node.js

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // npm install @google-cloud/security-center/
    const {SecurityCenterClient} = require('[@google-cloud/security-center](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)');
    
    const client = new [SecurityCenterClient](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)();
    
    const formattedConfigName = `organizations/${organizationId}/notificationConfigs/${configId}`;
    
    // pubsubTopic = "projects/{your-project}/topics/{your-topic}";
    // Ensure this Service Account has the "pubsub.topics.setIamPolicy" permission on this topic.
    
    async function updateNotificationConfig() {
      const [response] = await client.updateNotificationConfig({
        updateMask: {
          paths: ['description', 'pubsub_topic', 'streaming_config.filter'],
        },
        notificationConfig: {
          name: formattedConfigName,
          description: 'Updated config description',
          pubsubTopic: pubsubTopic,
          streamingConfig: {filter: 'state = "INACTIVE"'},
        },
      });
      console.log('notification config update succeeded: ', response);
    }
    
    updateNotificationConfig();

### PHP

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\SecurityCenter\V1\Client\SecurityCenterClient;
    use Google\Cloud\SecurityCenter\V1\NotificationConfig;
    use Google\Cloud\SecurityCenter\V1\NotificationConfig\StreamingConfig;
    use Google\Cloud\SecurityCenter\V1\UpdateNotificationConfigRequest;
    use Google\Protobuf\FieldMask;
    
    /**
     * @param string $organizationId        Your org ID
     * @param string $notificationConfigId  A unique identifier
     * @param string $projectId             Your Cloud Project ID
     * @param string $topicName             Your topic name
     */
    function update_notification(
        string $organizationId,
        string $notificationConfigId,
        string $projectId,
        string $topicName
    ): void {
        $securityCenterClient = new SecurityCenterClient();
    
        // Ensure this ServiceAccount has the 'pubsub.topics.setIamPolicy' permission on the topic.
        // https://cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics/setIamPolicy
        $pubsubTopic = $securityCenterClient::topicName($projectId, $topicName);
        // You can also use 'projectId' or 'folderId' instead of the 'organizationId'.
        $notificationConfigName = $securityCenterClient::notificationConfigName($organizationId, $notificationConfigId);
    
        $streamingConfig = (new StreamingConfig())->setFilter('state = "ACTIVE"');
        $fieldMask = (new FieldMask())->setPaths(['description', 'pubsub_topic', 'streaming_config.filter']);
        $notificationConfig = (new NotificationConfig())
            ->setName($notificationConfigName)
            ->setDescription('Updated description.')
            ->setPubsubTopic($pubsubTopic)
            ->setStreamingConfig($streamingConfig);
        $updateNotificationConfigRequest = (new UpdateNotificationConfigRequest())
            ->setNotificationConfig($notificationConfig);
    
        $response = $securityCenterClient->updateNotificationConfig($updateNotificationConfigRequest);
        printf('Notification config was updated: %s' . PHP_EOL, $response->getName());
    }

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def update_notification_config(parent_id, notification_config_id, pubsub_topic):
        """
        Args:
            parent_id: must be in one of the following formats:
                "organizations/{organization_id}"
                "projects/{project_id}"
                "folders/{folder_id}"
            notification_config_id: "config-id-to-update"
            pubsub_topic: "projects/{new-project}/topics/{new-topic}"
    
        If updating a pubsub_topic, ensure this ServiceAccount has the
        "pubsub.topics.setIamPolicy" permission on the new topic.
        """
        from google.cloud import securitycenter as securitycenter
        from google.protobuf import field_mask_pb2
    
        client = securitycenter.SecurityCenterClient()
    
        notification_config_name = (
            f"{parent_id}/notificationConfigs/{notification_config_id}"
        )
    
        updated_description = "New updated description"
        updated_filter = 'state = "INACTIVE"'
    
        # Only description and pubsub_topic can be updated.
        field_mask = field_mask_pb2.FieldMask(
            paths=["description", "pubsub_topic", "streaming_config.filter"]
        )
    
        updated_notification_config = client.update_notification_config(
            request={
                "notification_config": {
                    "name": notification_config_name,
                    "description": updated_description,
                    "pubsub_topic": pubsub_topic,
                    "streaming_config": {"filter": updated_filter},
                },
                "update_mask": field_mask,
            }
        )
    
        print(updated_notification_config)

### Ruby

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/security_center"
    
    # Your organization id. e.g. for "organizations/123", this would be "123".
    # org_id = "YOUR_ORGANZATION_ID"
    
    # Your location. e.g. "global" or "us".
    # location = "global"
    
    # Your notification config id. e.g. for
    # "organizations/123/notificationConfigs/my-config" this would be "my-config".
    # config_id = "YOUR_CONFIG_ID"
    
    # Updated description of the notification config.
    # description = "YOUR_DESCRIPTION"
    
    # The PubSub topic where notifications will be published.
    # pubsub_topic = "YOUR_TOPIC"
    
    # Updated filter string for Notification config.
    # filter = "UPDATED_FILTER"
    
    client = Google::Cloud::[SecurityCenter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center/latest/Google-Cloud-SecurityCenter.html).[security_center](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center/latest/Google-Cloud-SecurityCenter.html)
    
    # You can also use a project or folder as a parent.
    config_path = client.notification_config_path organization:        org_id,
                                                  location:            location,
                                                  notification_config: config_id
    notification_config = { name: config_path }
    notification_config[:description] = description unless description.nil?
    notification_config[:pubsub_topic] = pubsub_topic unless pubsub_topic.nil?
    notification_config[:streaming_config][:filter] = filter unless filter.nil?
    
    paths = []
    paths.push "description" unless description.nil?
    paths.push "pubsub_topic" unless pubsub_topic.nil?
    paths.push "streaming_config.filter" unless filter.nil?
    update_mask = { paths: paths }
    
    response = client.update_notification_config(
      notification_config: notification_config,
      update_mask:         update_mask
    )
    puts response

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
