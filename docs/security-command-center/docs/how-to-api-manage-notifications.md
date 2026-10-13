---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-api-manage-notifications/
title: Creating and managing Notification Configs \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:01:39.241094+00:00
---

# Creating and managing Notification Configs  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-api-manage-notifications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Creating and managing Notification Configs Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page describes how to use the Security Command Center API notifications feature, including the following examples:

  * Create a `NotificationConfig`
  * Get a `NotificationConfig`
  * Update a `NotificationConfig`
  * Delete a `NotificationConfig`
  * List `NotificationConfig`
  * Receive Pub/Sub notifications



Alternatively, you can [set up continuous exports](https://docs.cloud.google.com/security-command-center/docs/how-to-export-data#continuous_exports) for Pub/Sub in Security Command Center.

## Before you begin

To use the examples on this page, you need to complete the guide to [set up finding notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications).

To execute the following examples, you need an Identity and Access Management (IAM) role with appropriate permissions:

  * Create `NotificationConfig`: Security Center Notification Configurations Editor (`roles/securitycenter.notificationConfigEditor`)
  * Get and List `NotificationConfig`: Security Center Notification Configurations Viewer (`roles/securitycenter.notificationConfigViewer`) or Security Center Notification Configurations Editor (`roles/securitycenter.notificationConfigEditor`)
  * Update and Delete `NotificationConfig`: Security Center Notification Configurations Editor (`roles/securitycenter.notificationConfigEditor`)



To grant appropriate roles to a principal that accesses a `notificationConfig`, you must have one of the following IAM roles:

  * Organization Administrator (`roles/resourcemanager.organizationAdmin`)
  * Folder IAM Admin (`roles/resourcemanager.folderIamAdmin`)
  * Project IAM Admin (`roles/resourcemanager.projectIamAdmin`)



The IAM roles for Security Command Center can be granted at the organization, folder, or project level. Your ability to view, edit, create, or update findings, assets, and security sources depends on the level that you're granted access for. To learn more about Security Command Center roles, see [Access control](https://docs.cloud.google.com/security-command-center/docs/access-control). 

### Data residency and notifications

If [data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support) is enabled for Security Command Center, the configurations that define continuous exports to Pub/Sub—`notificationConfig` resources—are subject to data residency control and are stored in your [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations).

To export findings in a Security Command Center location to Pub/Sub, you must configure the continuous export in the same Security Command Center location as the findings.

Because the filters that are used in continuous exports can contain data that is subject to residency controls, make sure you specify the correct location before you create them. Security Command Center does not restrict which location you create exports in.

Continuous exports are stored only in the location in which they are created and cannot be viewed or edited in other locations.

After you create a continuous export, you can't change its location. To change the location, you need to delete the continuous export and recreate it in the new location.

To learn how to use Security Command Center when data residency is enabled, see [Security Command Center regional endpoints](https://docs.cloud.google.com/security-command-center/docs/regional-endpoints). 

## Creating a NotificationConfig

To create a `NotificationConfig`, you must have:

  * An existing Pub/Sub topic that you want to send notifications to.
  * Required IAM roles for the principal that creates the `notificationConfig`.



For more information, see the step to [set up a Pub/Sub topic](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications#set-up-pubsub-topic) in the guide to [set up finding notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications).

Before you create a `NotificationConfig`, note that each organization can have a limited number of `NotificationConfig` resources. For more information, see [Quotas and limits](https://docs.cloud.google.com/security-command-center/quotas).

The `NotificationConfig` includes a `filter` field that limits notifications to useful events. This field accepts all of the filters that are available in the Security Command Center API [`findings.list`](https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-findings) method.

When you create a `NotificationConfig`, you specify a parent for the `NotificationConfig` from the Google Cloud resource hierarchy, either an organization, a folder, or a project. If you need to retrieve, update, or delete the `NotificationConfig` later, you need to include the numerical ID of the parent organization, folder, or project when you reference it.

**Note:** If you migrate to the v2 Security Command Center API, keep in mind that `NotificationConfig` resources created with the v1 API are not visible in the v2 API. For more information, see [Notification configurations and BigQuery export configurations](https://docs.cloud.google.com/security-command-center/docs/migrate-v2-api#export-config). 

To manage `NotificationConfig` resources created with the v1 API, don't specify a location when you run gcloud CLI commands. The v1 API doesn't support data residency. 

To create the `NotificationConfig` using the language or platform of your choice:

### gcloud
    
    
    gcloud scc notifications create NOTIFICATION_NAME \
      --PARENT=PARENT_ID \
      --location=LOCATION \
      --description="NOTIFICATION_DESCRIPTION" \
      --pubsub-topic=PUBSUB_TOPIC \
      --filter="FILTER" \
      --deletion-notifications-enabled
    

Replace the following:

  * `NOTIFICATION_NAME`: the name of the notification. Must be between 1 and 128 characters and contain alphanumeric characters, underscores, or hyphens only.
  * `PARENT`: the scope in the resource hierarchy to which the notification applies, `organization`, `folder`, or `project`.
  * `PARENT_ID`: the ID of the parent organization, folder, or project, specified in the format of `organizations/123`, `folders/456`, or `projects/789`.
  * `LOCATION`: the [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations) in which to create a `NotificationConfig`; if data residency is enabled, use `eu`, `sa`, or `us`; otherwise, use the value `global`.
  * `NOTIFICATION_DESCRIPTION`: a description of the notification of no more than 1,024 characters.
  * `PUBSUB_TOPIC`: The Pub/Sub topic that will receive notifications. Its format is `projects/PROJECT_ID/topics/TOPIC`.
  * `FILTER`: the expression you define to select which findings get sent to Pub/Sub. For example, `state=\"ACTIVE\"`.



Use the following flags to configure whether to receive notifications for deleted findings. By default, deleted findings are not exported.

  * `--deletion-notifications-enabled`: enables notifications for findings that are deleted due to data retention policies. When set, notifications are triggered when a finding is deleted. The notification includes the `deletedFinding` attribute set to `true`.
  * `--no-deletion-notifications-enabled`: disables notifications for findings that are deleted due to data retention policies.



### Terraform

Create a `NotificationConfig` for an organization:
    
    
    resource "google_pubsub_topic" "scc_v2_organization_notification_config" {
      name = "my-topic"
    }
    
    resource "google_scc_v2_organization_notification_config" "custom_organization_notification_config" {
      config_id    = "my-config"
      organization = "123456789"
      location     = "global"
      description  = "My custom Cloud Security Command Center Finding Organization Notification Configuration"
      pubsub_topic = google_pubsub_topic.scc_v2_organization_notification_config.id
    
      streaming_config {
        filter = "category = \"OPEN_FIREWALL\" AND state = \"ACTIVE\""
      }
    }
    

Create a `NotificationConfig` for a folder:
    
    
    resource "google_folder" "folder" {
      parent       = "organizations/123456789"
      display_name = "folder-name"
    }
    
    resource "google_pubsub_topic" "scc_v2_folder_notification_config" {
      name = "my-topic"
    }
    
    resource "google_scc_v2_folder_notification_config" "custom_notification_config" {
      config_id    = "my-config"
      folder       = google_folder.folder.folder_id
      location     = "global"
      description  = "My custom Cloud Security Command Center Finding Notification Configuration"
      pubsub_topic =  google_pubsub_topic.scc_v2_folder_notification_config.id
    
      streaming_config {
        filter = "category = \"OPEN_FIREWALL\" AND state = \"ACTIVE\""
      }
    }
    

Create a `NotificationConfig` for a project:
    
    
    resource "google_pubsub_topic" "scc_v2_project_notification" {
      name = "my-topic"
    }
    
    resource "google_scc_v2_project_notification_config" "custom_notification_config" {
      config_id    = "my-config"
      project      = "my-project-name"
      description  = "My custom Cloud Security Command Center Finding Notification Configuration"
      pubsub_topic =  google_pubsub_topic.scc_v2_project_notification.id
    
      streaming_config {
        filter = "category = \"OPEN_FIREWALL\" AND state = \"ACTIVE\""
      }
    }
    

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	securitycenter "cloud.google.com/go/securitycenter/apiv2"
    	"cloud.google.com/go/securitycenter/apiv2/securitycenterpb"
    )
    
    func createNotificationConfig(w io.Writer, orgID string, pubsubTopic string, notificationConfigID string) error {
    	// orgID := "your-org-id"
    	// pubsubTopic := "projects/{your-project}/topics/{your-topic}"
    	// notificationConfigID := "your-config-id"
    
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_NewClient)(ctx)
    
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_Close)()
    
    	req := &securitycenterpb.CreateNotificationConfigRequest{
    		// Parent must be in one of the following formats:
    		//		"organizations/{orgId}/locations/global"
    		//		"projects/{projectId}/locations/global"
    		//		"folders/{folderId}/locations/global"
    		Parent:   fmt.Sprintf("organizations/%s/locations/global", orgID),
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
    
    
    // npm install '@google-cloud/security-center'
    const {SecurityCenterClient} = require('[@google-cloud/security-center](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)').v2;
    const uuidv1 = require('uuid').v1;
    
    const client = new [SecurityCenterClient](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)();
    /*
     *  Required. Resource name of the new notification config's parent. Its format
     *  is "organizations/[organization_id]/locations/[location_id]",
     *  "folders/[folder_id]/locations/[location_id]", or
     *  "projects/[project_id]/locations/[location_id]".
     */
    const parent = `projects/${projectId}/locations/${location}`;
    
    /**
     *  Required.
     *  Unique identifier provided by the client within the parent scope.
     *  It must be between 1 and 128 characters and contain alphanumeric
     *  characters, underscores, or hyphens only.
     */
    const configId = 'notif-config-test-node-create-' + uuidv1();
    
    // pubsubTopic = "projects/{your-project}/topics/{your-topic}";
    const pubsubTopic = `projects/${projectId}/topics/${topicName}`;
    
    /**
     *  Required. The notification config being created. The name and the service
     *  account will be ignored as they are both output only fields on this
     *  resource.
     */
    const notificationConfig = {
      description: 'Sample config for node v2',
      pubsubTopic: pubsubTopic,
      streamingConfig: {filter: 'state = "ACTIVE"'},
    };
    
    // Build the request.
    const createNotificationRequest = {
      parent: parent,
      configId: configId,
      notificationConfig: notificationConfig,
    };
    
    async function createNotificationConfig() {
      const [response] = await client.createNotificationConfig(
        createNotificationRequest
      );
      console.log('Notification configuration creation successful: %j', response);
    }
    
    await createNotificationConfig();

### Python
    
    
    def create_notification_config(
        parent_id, location_id, pubsub_topic, notification_config_id
    ) -> NotificationConfig:
        """
        This method is used to create the Notification Config.
        Args:
            parent_id: must be in one of the following formats:
                "organizations/{organization_id}"
                "projects/{project_id}"
                "folders/{folder_id}"
            location_id: "global"
            pubsub_topic: "projects/{your-project-id}/topics/{your-topic-id}"
            notification_config_id: "your-config-id"
    
    
        Ensure this ServiceAccount has the "pubsub.topics.setIamPolicy" permission on the new topic.
        """
        from google.cloud import securitycenter_v2 as securitycenter_v2
    
        client = securitycenter_v2.SecurityCenterClient()
        parent_id = parent_id + "/locations/" + location_id
        response = client.create_notification_config(
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
        print(f"create notification config response:{response}")
        return response
    
    

Notifications are now published to the Pub/Sub topic you specified.

To publish notifications, a service account is created for you in the form of `service-org-ORGANIZATION_ID@gcp-sa-scc-notification.iam.gserviceaccount.com`. This service account is created when you create your first `NotificationConfig` and is automatically granted the `securitycenter.notificationServiceAgent` role on the IAM policy for PUBSUB_TOPIC when creating the notification config. This service account role is required for notifications to function.

## Getting a NotificationConfig

To get a `NotificationConfig`, you must have an IAM role that includes the `securitycenter.notification.get` permission.

### gcloud
    
    
    gcloud scc notifications describe NOTIFICATION_NAME \
      --PARENT_TYPE=PARENT_ID \
      --location=LOCATION
    

Replace the following:

  * `NOTIFICATION_NAME`: the name of the notification configuration.
  * `PARENT_TYPE`: the level of the resource hierarchy where the configuration is specified; use `organization`, `folder`, or `project`.
  * `PARENT_ID`: the numeric ID of the parent resource.
  * `LOCATION`: the [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations) in which to get the `NotificationConfig`; if data residency is enabled, use `eu`, `sa`, or `us`; otherwise, use the value `global`.



## Updating a NotificationConfig

To update a `NotificationConfig`, you must have an IAM role that includes the `securitycenter.notification.update` permission.

When you update using a field mask, only the fields you specify are updated. If you don't use a field mask, all mutable fields in the `NotificationConfig` are replaced by the new values. You can use a field mask to update the Pub/Sub topic and description.

To complete this example, you must be subscribed to the new topic, and your notifications service account must have the `pubsub.topics.setIamPolicy` permission on the topic.

After you grant the necessary permissions, update the `NotificationConfig` description, Pub/Sub topic and filter:

### gcloud
    
    
    gcloud scc notifications update NOTIFICATION_NAME \
      --PARENT_TYPE=PARENT_ID \
      --location=LOCATION \
      --description="NOTIFICATION_DESCRIPTION" \
      --pubsub-topic=PUBSUB_TOPIC \
      --filter="FILTER" \
      --deletion-notifications-enabled
    
    

Replace the following:

  * `NOTIFICATION_NAME`: the name of the notification configuration.
  * `PARENT_TYPE` the level of the resource hierarchy where the configuration is specified; use `organization`, `folder`, or `project`.
  * `PARENT_ID`: the numeric ID of the parent resource.
  * `LOCATION`: the [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations) in which to update the `NotificationConfig`; if data residency is enabled, use `eu`, `sa`, or `us`; otherwise, use the value `global`.
  * `NOTIFICATION_DESCRIPTION`: a description of the notification of no more than 1,024 characters.
  * `PUBSUB_TOPIC`: the Pub/Sub topic which will receive notifications. Its format is `projects/PROJECT_ID/topics/TOPIC`.
  * `FILTER`: the expression you define to select which findings get sent to Pub/Sub. For example, `state="ACTIVE"`.



Use the following flags to configure whether to receive notifications for deleted findings. If you don't specify either flag, the default behavior is to not export deleted findings.

  * `--deletion-notifications-enabled`: enable notifications for findings deleted due to retention policies. When enabled, deleted findings are exported to Pub/Sub with `deleted_finding = true`. This flag applies to future deletion events only. Findings deleted before enabling this flag aren't retroactively exported.

  * `--no-deletion-notifications-enabled`: disable notifications for deleted findings.




## Deleting a NotificationConfig

To delete a `NotificationConfig`, you must have an IAM role that includes the `securitycenter.notification.delete` permission.

When you delete a `NotificationConfig`, the `securitycenter.notificationServiceAgent` role stays on the Pub/Sub topic. If you aren't using the Pub/Sub topic in any other `NotificationConfig`, remove the role from the topic. For more information, see [access control](https://docs.cloud.google.com/security-command-center/docs/access-control).

### gcloud
    
    
    gcloud scc notifications delete NOTIFICATION_NAME \
      --PARENT_TYPE=PARENT_ID \
      --location=LOCATION
    

Replace the following:

  * `NOTIFICATION_NAME`: the name of the notification configuration.
  * `PARENT_TYPE` the level of the resource hierarchy where the configuration is specified; use `organization`, `folder`, or `project`.
  * `PARENT_ID`: the numeric ID of the parent resource.
  * `LOCATION`: the [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations) in which to delete the `NotificationConfig`; if data residency is enabled, use `eu`, `sa`, or `us`; otherwise, use the value `global`.



## Listing NotificationConfigs

To list `NotificationConfigs`, you must have an IAM role that includes the `securitycenter.notification.list` permission.

All Security Command Center API lists are paginated. Each response returns a page of results and a token to return the next page. The default `pageSize` is 10. You can configure page size to a minimum of 1, and a maximum of 1000.

### gcloud
    
    
    gcloud scc notifications list PARENT_TYPE/PARENT_ID \
      --location=LOCATION
    

Replace the following:

  * `PARENT_TYPE` the level of the resource hierarchy where the configuration is specified; use `organizations`, `folders`, or `projects`.
  * `PARENT_ID`: the numeric ID of the parent resource.
  * `LOCATION`: the [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations) in which to list `NotificationConfig` resources; if data residency is enabled, use `eu`, `sa`, or `us`; otherwise, use the value `global`.



## Receiving Pub/Sub notifications

This section provides a sample notification message and examples that show how to convert a Pub/Sub message into a `NotificationMessage` that contains a finding.

Notifications are published to Pub/Sub in the `JSON` format. Following is an example of a notification message:
    
    
    {
       "notificationConfigName": "organizations/ORGANIZATION_ID/notificationConfigs/CONFIG_ID",
       "finding": {
         "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
         "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
         "state": "ACTIVE",
         "category": "TEST-CATEGORY",
         "securityMarks": {
           "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID/securityMarks"
         },
         "eventTime": "2019-07-26T07:32:37Z",
         "createTime": "2019-07-29T18:45:27.243Z"
       },
       "deletedFinding": true
     }
    

Security Command Center deletes findings periodically based on [data retention](https://docs.cloud.google.com/security-command-center/docs/concepts-data-security-overview#data_retention) policies. You can configure whether Security Command Center exports a snapshot of deleted findings to Pub/Sub.

You enable deletion notifications when you create or update an export configuration. When deletion notifications are enabled on the export configuration, Security Command Center sends snapshot of deleted findings to Pub/Sub. The notification has the `"deletedFinding": true` field set in the payload. The finding's pre-deletion state (for example, `"state": "ACTIVE"`) is preserved in the payload and `eventTime` is set to the time the finding was deleted in Security Command Center.

When you modify the deletion notification option on an export configuration, the change applies to future deletions of findings only. Findings deleted prior to enabling the option aren't retroactively exported.

Convert a Pub/Sub message into a `NotificationMessage` using the language of your choice:

### gcloud

The gcloud CLI doesn't support converting a Pub/Sub message into a `NotificationMessage`. You can use the gcloud CLI to get a `NotificationMessage` and print the `JSON` directly in your terminal:
    
    
      # The subscription used to receive published messages from a topic
      PUBSUB_SUBSCRIPTION="projects/PROJECT_ID/subscriptions/SUBSCRIPTION_ID"
    
      gcloud pubsub subscriptions pull $PUBSUB_SUBSCRIPTION
    

Replace the following:

  * PROJECT_ID with your project ID.
  * SUBSCRIPTION_ID with your subscription ID.



### Go
    
    
    import (
    	"bytes"
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/pubsub"
    	"cloud.google.com/go/securitycenter/apiv2/securitycenterpb"
    	"github.com/golang/protobuf/jsonpb"
    )
    
    func receiveMessages(w io.Writer, projectID string, subscriptionName string) error {
    	// projectID := "your-project-id"
    	// subsriptionName := "your-subscription-name"
    
    	ctx := context.Background()
    
    	client, err := pubsub.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_Client_NewClient)(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	sub := client.Subscription(subscriptionName)
    	cctx, cancel := context.WithCancel(ctx)
    	err = sub.Receive(cctx, func(ctx context.Context, msg *pubsub.Message) {
    		var notificationMessage = new(securitycenterpb.[NotificationMessage](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2/securitycenterpb.html#cloud_google_com_go_securitycenter_apiv2_securitycenterpb_NotificationMessage))
    		jsonpb.Unmarshal(bytes.NewReader(msg.Data), notificationMessage)
    
    		fmt.Fprintln(w, "Got finding: ", notificationMessage.GetFinding())
    		msg.Ack()
    		cancel()
    	})
    	if err != nil {
    		return fmt.Errorf("Receive: %w", err)
    	}
    
    	return nil
    }
    

## What's next

  * Learn about [filtering notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-api-filter-notifications).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
