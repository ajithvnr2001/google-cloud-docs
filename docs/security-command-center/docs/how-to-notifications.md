---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-notifications/
title: Enable finding notifications for Pub/Sub \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:48:24.457973+00:00
---

# Enable finding notifications for Pub/Sub  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-notifications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Enable finding notifications for Pub/Sub Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page explains how to use the Security Command Center API to enable finding notifications for Pub/Sub.

You can configure notifications to automatically send new findings, finding updates, and findings deleted due to data retention policies to a Pub/Sub topic in near-real time. You can use these notifications to trigger automated actions, such as invoking [Cloud Run functions](https://docs.cloud.google.com/functions/docs/concepts/overview) for response, enrichment, or remediation. For example solutions, see the Security Command Center open-source repository of [Cloud Run functions code](https://github.com/GoogleCloudPlatform/security-response-automation).

If you prefer a simplified setup experience using the Google Cloud console instead of the API, see [Continuous exports](https://docs.cloud.google.com/security-command-center/docs/how-to-export-data#continuous_exports). Continuous exports provide the same functionality as API notifications.

Alternatively, you can [export findings to BigQuery](https://docs.cloud.google.com/security-command-center/docs/how-to-analyze-findings-in-big-query) for analysis.

## Before you begin

Before you enable finding notifications, you must obtain specific Identity and Access Management (IAM) roles and permissions, enable the Security Command Center API, and familiarize yourself with data residency limitations.

### Required roles

To get the permissions that you need to set up and configure Security Command Center API notifications, ask your administrator to grant you the following IAM roles: 

  * [Security Center Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`) on the organization or project where Security Command Center is activated
  * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) on the project where you will create your Pub/Sub topic



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Enable the Security Command Center API

Enable the Security Command Center API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
    
    
    gcloud services enable securitycenter.googleapis.com

### Data residency and notifications

If [data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support) is enabled for Security Command Center, the configurations that define continuous exports to Pub/Sub—`notificationConfig` resources—are subject to data residency control and are stored in your [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations).

To export findings in a Security Command Center location to Pub/Sub, you must configure the continuous export in the same Security Command Center location as the findings.

Because the filters that are used in continuous exports can contain data that is subject to residency controls, make sure you specify the correct location before you create them. Security Command Center does not restrict which location you create exports in.

Continuous exports are stored only in the location in which they are created and cannot be viewed or edited in other locations.

After you create a continuous export, you can't change its location. To change the location, you need to delete the continuous export and recreate it in the new location.

To learn how to use Security Command Center when data residency is enabled, see [Security Command Center regional endpoints](https://docs.cloud.google.com/security-command-center/docs/regional-endpoints). 

## Set up a Pub/Sub topic

In this task, you create and subscribe to the Pub/Sub topic that you want to send notifications to.

### Step 1: Set up Pub/Sub

To set up and subscribe to a Pub/Sub topic, do the following:

  1. Go to the Google Cloud console.

[Go to the Google Cloud console](https://console.cloud.google.com/projectselector2)

  2. Select the project where you enabled the Security Command Center API.

  3. Click **Activate Cloud Shell**. ![](https://docs.cloud.google.com/static/security-command-center/images/activate-cloud-shell.svg)

  4. Optional: To create a new Pub/Sub topic, run the following command:
         
         gcloud pubsub topics create TOPIC_ID
         

Replace `TOPIC_ID` with a topic name.

  5. Create a subscription to the topic:
         
         gcloud pubsub subscriptions create SUBSCRIPTION_ID --topic=TOPIC_ID
         

Replace the following:

     * `SUBSCRIPTION_ID`: the subscription ID
     * `TOPIC_ID`: the topic ID
**Note:** By default, Pub/Sub subscriptions expire after 31 days of inactivity, defined by the absence of active connections, pull requests, or push successes. To keep subscriptions longer, set the `--expiration-period` flag to a higher value or the special value `never`, indicating the subscription never expires. For details, see [Using subscription properties](https://docs.cloud.google.com/pubsub/docs/admin#using_subscription_properties).



To learn more about setting up Pub/Sub, see [Managing topics and subscriptions](https://docs.cloud.google.com/pubsub/docs/admin).

### Step 2: Grant role on Pub/Sub topic

To create a `NotificationConfig`, you need the Pub/Sub Admin role (`roles/pubsub.admin`) on the Pub/Sub topic for which you created a subscription.

To grant this role, do the following:

  1. Go to the Google Cloud console.

[Go to the Google Cloud console](https://console.cloud.google.com/projectselector2)

  2. Select the project for which you enabled the Security Command Center API.

  3. Click **Activate Cloud Shell**. ![](https://docs.cloud.google.com/static/security-command-center/images/activate-cloud-shell.svg)

  4. Grant the required role to your Google Account on the Pub/Sub topic:
         
         gcloud pubsub topics add-iam-policy-binding \
             projects/PUBSUB_PROJECT/topics/TOPIC_ID \
             --member="user:GOOGLE_ACCOUNT" \
             --role="roles/pubsub.admin"
         

Replace the following:

     * `PUBSUB_PROJECT`: the Google Cloud project that contains your Pub/Sub topic
     * `TOPIC_ID`: the topic ID
     * `GOOGLE_ACCOUNT`: the email address for your Google Account



## Create a NotificationConfig

**Note:** If you use VPC Service Controls, you might need to grant access to protected project resources before creating a `NotificationConfig` and in order for notifications to work. For more information, see Granting perimeter access in VPC Service Controls.

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
  * `LOCATION`: the [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations) in which to set up and configure Security Command Center API notifications; if data residency is enabled, use `eu`, `sa`, or `us`; otherwise, use the value `global`.
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

To receive notifications when findings are deleted from due to data retention, specify the `--deletion-notifications-enabled` flag in gcloud CLI or set the `deletion_notifications_enabled` field to `false` when calling the REST API or using the client libraries. Changes to the configuration apply to future deletion events. Findings that were deleted prior to enabling are not retroactively sent as deletion notifications. To disable deletion notifications, update the `NotificationConfig` and set the `--no-deletion-notifications-enabled` flag.

If you don't enable deletion notifications when you create a `NotificationConfig`, they are disabled by default.

## Grant perimeter access in VPC Service Controls

If you use [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) and your Pub/Sub topic is part of a project inside a service perimeter, you must grant access to projects in order to create notifications.

To grant access to projects, create [ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) for the principals and projects that are used to create notifications. The rules allow access to protected resources and let Pub/Sub verify that users have the `setIamPolicy` permission on the Pub/Sub topic.

### Before creating a NotificationConfig

Before completing the steps in Creating a NotificationConfig, complete the following steps.

### Console

#### Navigate to the service perimeter

  1. In the Google Cloud console, go to the **VPC Service Controls** page.

[Go to VPC Service Controls](https://console.cloud.google.com/projectselector2/security/service-perimeter?supportedpurview=organizationId)

  2. Select your organization.
  3. In the drop-down list, select the access policy that contains the service perimeter that you want to grant access to.

The service perimeters associated with the access policy appear in the list.

  4. Click the name of the service perimeter that you want to update.

To find the service perimeter you need to modify, you can check your logs for entries that show `RESOURCES_NOT_IN_SAME_SERVICE_PERIMETER` violations. In those entries, check the `servicePerimeterName` field: 
         
         accessPolicies/ACCESS_POLICY_ID/servicePerimeters/SERVICE_PERIMETER_NAME

  5. Click edit **Edit**.



#### Add an egress rule

  1. Click **Egress policy**.
  2. Click **Add an egress rule**.
  3. In the **From** section, set the following details:

     1. For **Identities > Identity**, select **Select identities & groups**.
     2. Click **Add identities**.
     3. Enter the email address that identifies the principal used to call the Security Command Center API.
     4. Select the principal or press `ENTER`, and then click **Add identities**. 
  4. In the **To** section, set the following details:

     1. For **Resources > Projects**, select **Select projects**.
     2. Click **Add projects** , and then add the project that contains the Pub/Sub topic. 
     3. For **Operations or IAM roles** , select **Select operations**. 
     4. Click **Add operations** , and then add the following operations:

        * Add the **pubsub.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.



#### Add an ingress rule

  1. Click **Ingress policy**.
  2. Click **Add an ingress rule**.
  3. In the **From** section, set the following details:

     1. For **Identities > Identity**, select **Select identities & groups**.
     2. Click **Add identities**.
     3. Enter the email address that identifies the principal used to call the Security Command Center API.
     4. Select the principal or press `ENTER`, and then click **Add identities**. 
  4. In the **To** section, set the following details:

     1. For **Resources > Projects**, select **Select projects**.
     2. Click **Add projects** , and then add the project that contains the Pub/Sub topic. 
     3. For **Operations or IAM roles** , select **Select operations**. 
     4. Click **Add operations** , and then add the following operations:

        * Add the **pubsub.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
  5. Click **Save**.



### gcloud

**Warning:** The `--set-ingress-policies` and `--set-egress-policies` flags replace all existing ingress or egress policies in the perimeter. If you have existing policies, you must retrieve them first, add the new policy to the appropriate ingress or egress YAML file, and then run the update command. 

  1. If a quota project isn't already set, then set it. Choose a project that has the Access Context Manager API enabled. 
         
         gcloud config set billing/quota_project QUOTA_PROJECT_ID

Replace `QUOTA_PROJECT_ID` with the ID of the project that you want to use for billing and quota. 

  2. Create a file named `egress-rule.yaml` with the following contents:
         
         - egressFrom:
             identities:
             - PRINCIPAL_ID
           egressTo:
             operations:
             - serviceName: pubsub.googleapis.com
               methodSelectors:
               - method: '*'
             resources:
             - projects/PROJECT_ID

Replace `PRINCIPAL_ID` with the identifier for the principal used to call the Security Command Center API. 

Replace `PROJECT_ID` with the ID of the project that contains the Pub/Sub topic. 

  3. Create a file named `ingress-rule.yaml` with the following contents:
         
         - ingressFrom:
             identities:
             - PRINCIPAL_ID
             sources:
             - accessLevel: '*'
           ingressTo:
             operations:
             - serviceName: pubsub.googleapis.com
               methodSelectors:
               - method: '*'
             resources:
             - projects/PROJECT_ID

Replace `PRINCIPAL_ID` with the identifier for the principal used to call the Security Command Center API. 

Replace `PROJECT_ID` with the ID of the project that contains the Pub/Sub topic. 

  4. Add the egress rule to the perimeter:
         
         gcloud access-context-manager perimeters update PERIMETER_NAME \
             --set-egress-policies=egress-rule.yaml

Replace the following:

     * `PERIMETER_NAME`: the name of the perimeter. For example, `accessPolicies/1234567890/servicePerimeters/example_perimeter`. 

To find the service perimeter you need to modify, you can check your logs for entries that show `RESOURCES_NOT_IN_SAME_SERVICE_PERIMETER` violations. In those entries, check the `servicePerimeterName` field: 
           
           accessPolicies/ACCESS_POLICY_ID/servicePerimeters/SERVICE_PERIMETER_NAME

  5. Add the ingress rule to the perimeter:
         
         gcloud access-context-manager perimeters update PERIMETER_NAME \
             --set-ingress-policies=ingress-rule.yaml

Replace the following:

     * `PERIMETER_NAME`: the name of the perimeter. For example, `accessPolicies/1234567890/servicePerimeters/example_perimeter`. 

To find the service perimeter you need to modify, you can check your logs for entries that show `RESOURCES_NOT_IN_SAME_SERVICE_PERIMETER` violations. In those entries, check the `servicePerimeterName` field: 
           
           accessPolicies/ACCESS_POLICY_ID/servicePerimeters/SERVICE_PERIMETER_NAME




For more information, see [Ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules). 

### Create an ingress rule for the NotificationConfig

To create an ingress rule for a `NotificationConfig`, complete the instructions in Creating a NotificationConfig, and then complete the following steps.

### Console

#### Navigate to the service perimeter

  1. Re-open the service perimeter from the previous section.

[Go to VPC Service Controls](https://console.cloud.google.com/projectselector2/security/service-perimeter?supportedpurview=organizationId)




#### Add an ingress rule

  1. Click **Ingress policy**.
  2. Click **Add an ingress rule**.
  3. In the **From** section, set the following details:

     1. For **Identities > Identity**, select **Select identities & groups**.
     2. Click **Add identities**.
     3. Enter the email address that identifies the `NotificationConfig` service agent. This address has the following format: 
            
            service-org-ORGANIZATION_ID@gcp-sa-scc-notification.iam.gserviceaccount.com

Replace `ORGANIZATION_ID` with your organization ID.

     4. Select the service agent or press `ENTER`, and then click **Add identities**. 
  4. In the **To** section, set the following details:

     1. For **Resources > Projects**, select **Select projects**.
     2. Click **Add projects** , and then add the project that contains the Pub/Sub topic. 
     3. For **Operations or IAM roles** , select **Select operations**. 
     4. Click **Add operations** , and then add the following operations:

        * Add the **pubsub.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
  5. Click **Save**.



### gcloud

**Warning:** The `--set-ingress-policies` and `--set-egress-policies` flags replace all existing ingress or egress policies in the perimeter. If you have existing policies, you must retrieve them first, add the new policy to the appropriate ingress or egress YAML file, and then run the update command. 

  1. If a quota project isn't already set, then set it. Choose a project that has the Access Context Manager API enabled. 
         
         gcloud config set billing/quota_project QUOTA_PROJECT_ID

Replace `QUOTA_PROJECT_ID` with the ID of the project that you want to use for billing and quota. 

  2. Create a file named `ingress-rule.yaml` with the following contents:
         
         - ingressFrom:
             identities:
             - serviceAccount:service-org-ORGANIZATION_ID@gcp-sa-scc-notification.iam.gserviceaccount.com
             sources:
             - accessLevel: '*'
           ingressTo:
             operations:
             - serviceName: pubsub.googleapis.com
               methodSelectors:
               - method: '*'
             resources:
             - projects/PROJECT_ID

Replace `ORGANIZATION_ID` with your organization ID.

Replace `PROJECT_ID` with the ID of the project that contains the Pub/Sub topic. 

  3. Add the ingress rule to the perimeter:
         
         gcloud access-context-manager perimeters update PERIMETER_NAME \
             --set-ingress-policies=ingress-rule.yaml

Replace the following:

     * `PERIMETER_NAME`: the name of the perimeter. For example, `accessPolicies/1234567890/servicePerimeters/example_perimeter`. 

To find the service perimeter you need to modify, you can check your logs for entries that show `RESOURCES_NOT_IN_SAME_SERVICE_PERIMETER` violations. In those entries, check the `servicePerimeterName` field: 
           
           accessPolicies/ACCESS_POLICY_ID/servicePerimeters/SERVICE_PERIMETER_NAME




### Terraform

To configure the perimeter using Terraform, see the following sample:
    
    
    locals {
      access_policy_id    = "123456789012"
      perimeter_name      = "my_service_perimeter"
      project_number      = "123456789012"
      scc_service_account = "service-{project_number}@gcp-sa-scc-notification.iam.gserviceaccount.com"
    }
    
    resource "google_access_context_manager_service_perimeter_ingress_policy" "scc_notification_ingress" {
      perimeter = "accessPolicies/${local.access_policy_id}/servicePerimeters/${local.perimeter_name}"
    
      ingress_from {
        identities = [
          "serviceAccount:${local.scc_service_account}"
        ]
        sources {
          access_level = "*"
        }
      }
    
      ingress_to {
        resources = [
          "projects/${local.project_number}"
        ]
        operations {
          service_name = "pubsub.googleapis.com"
          method_selectors {
            # Limit to publishing messages rather than allowing topic deletion
            method = "google.pubsub.v1.Publisher.Publish"
          }
        }
      }
    }

For more information, see [Ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules). 

The selected projects, users, and services accounts can now access the protected resources and create notifications.

If you followed all of the steps in this guide, and notifications are working properly, you can now delete the following:

  * The ingress rule for the principal
  * The egress rule for the principal



Those rules were only needed to configure the `NotificationConfig`. However, for notifications to continue working, you must keep the ingress rule for the `NotificationConfig`, which lets it publish notifications to your Pub/Sub topic behind the service perimeter.

## What's next

  * Learn about [enabling real-time chat notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-enable-real-time-notifications).
  * Learn how to [manage the notifications API](https://docs.cloud.google.com/security-command-center/docs/how-to-api-manage-notifications).
  * Learn about [filtering notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-api-filter-notifications).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
