---
url: https://docs.cloud.google.com/contact-center/insights/docs/pub-sub/
title: Enable Pub/Sub notifications for Conversational Insights events \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:10:13.585868+00:00
---

# Enable Pub/Sub notifications for Conversational Insights events  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/insights/docs/pub-sub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Enable Pub/Sub notifications for Conversational Insights events Stay organized with collections  Save and categorize content based on your preferences. 

Enabling [Pub/Sub](https://docs.cloud.google.com/pubsub) notifications lets you receive a notification each time a CX Insights event completes. You can configure CX Insights to send a notification for all events or only specified events. To learn more about the events that can trigger Pub/Sub notifications, see the [reference documentation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1#settings).

## Prerequisites

  1. Follow the instructions to [create a Pub/Sub topic and a pull subscription](https://docs.cloud.google.com/pubsub/docs/create-topic-console).



## Enable Pub/Sub notifications

You can configure CX Insights to send a notification for **specific events only** or for **all events**. The following code sample configures CX Insights to only send a notification each time a conversation or an analysis is created.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `contactcenterinsights.settings.update`



### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID.
  * TOPIC_ID: the ID for the notification topic (for example, notify each time a conversation is created). Each notification topic should have a unique ID.

**Note:** All the examples are using the global Customer Experience Insights instance. Refer to [Regionalization](https://docs.cloud.google.com/gemini-enterprise-cx/insights/docs/regionalization) for instructions on using regional instances. 

HTTP method and URL: 
    
    
    PATCH https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/settings?updateMask=pubsub_notification_settings

Request JSON body: 
    
    
    {
      "pubsub_notification_settings": {
        "create-conversation": "projects/PROJECT_ID/topics/TOPIC_ID_1",
        "create-analysis": "projects/PROJECT_ID/topics/TOPIC_ID_2"
      },
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/settings?updateMask=pubsub_notification_settings"

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
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/settings?updateMask=pubsub_notification_settings" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/us-central1/settings",
      "createTime": "2021-01-20T10:10:10.123000Z",
      "updateTime": "2021-01-20T11:11:11.456000Z",
      "pubsubNotificationSettings": {
        "create-conversation": "projects/PROJECT_ID/topics/TOPIC_ID_1",
        "create-analysis": "projects/PROJECT_ID/topics/TOPIC_ID_2"
      }
    }
    

### Python

To authenticate to CX Insights, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core import protobuf_helpers
    from google.cloud import [contact_center_insights_v1](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest)
    
    
    def enable_pubsub_notifications(
        project_id: str, topic_create_conversation: str, topic_create_analysis: str
    ) -> None:
        """Enables Cloud Pub/Sub notifications for specified events.
    
        Args:
            project_id:
                The project identifier. For example, 'my-project'.
            topic_create_conversation:
                The Cloud Pub/Sub topic to notify of conversation creation events.
                Format is 'projects/{project_id}/topics/{topic_id}'.
                For example, 'projects/my-project/topics/my-topic'.
            topic_create_analysis:
                The Cloud Pub/Sub topic to notify of analysis creation events.
                Format is 'projects/{project_id}/topics/{topic_id}'.
                For example, 'projects/my-project/topics/my-topic'.
    
        Returns:
            None.
        """
        # Construct a settings resource.
        settings = [contact_center_insights_v1](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest).[Settings](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.Settings.html)()
        settings.name = (
            [contact_center_insights_v1](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest).[ContactCenterInsightsClient](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.services.contact_center_insights.ContactCenterInsightsClient.html).settings_path(
                project_id, "us-central1"
            )
        )
        settings.pubsub_notification_settings = {
            "create-conversation": topic_create_conversation,
            "create-analysis": topic_create_analysis,
        }
    
        update_mask = protobuf_helpers.field_mask(None, type(settings).pb(settings))
    
        # Call the Insights client to enable Pub/Sub notifications.
        insights_client = [contact_center_insights_v1](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest).[ContactCenterInsightsClient](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.services.contact_center_insights.ContactCenterInsightsClient.html)()
        insights_client.[update_settings](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.services.contact_center_insights.ContactCenterInsightsClient.html#google_cloud_contact_center_insights_v1_services_contact_center_insights_ContactCenterInsightsClient_update_settings)(settings=settings, update_mask=update_mask)
        print("Enabled Pub/Sub notifications")
    
    

### Java

To authenticate to CX Insights, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.contactcenterinsights.v1.[ContactCenterInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsClient.html);
    import com.google.cloud.contactcenterinsights.v1.[Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.Settings.html);
    import com.google.cloud.contactcenterinsights.v1.[SettingsName](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.SettingsName.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.io.IOException;
    
    public class EnablePubSubNotifications {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my_project_id";
        String topicCreateConversation = "projects/my_project_id/topics/my_topic_id";
        String topicCreateAnalysis = "projects/my_project_id/topics/my_other_topic_id";
    
        enablePubSubNotifications(projectId, topicCreateConversation, topicCreateAnalysis);
      }
    
      public static void enablePubSubNotifications(
          String projectId, String topicCreateConversation, String topicCreateAnalysis)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([ContactCenterInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsClient.html) client = [ContactCenterInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsClient.html).create()) {
          // Construct a settings resource.
          [SettingsName](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.SettingsName.html) name = [SettingsName](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.SettingsName.html).of(projectId, "us-central1");
          [Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.Settings.html) settings =
              [Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.Settings.html).newBuilder()
                  .setName(name.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.SettingsName.html#com_google_cloud_contactcenterinsights_v1_SettingsName_toString__)())
                  .[putPubsubNotificationSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.Settings.Builder.html#com_google_cloud_contactcenterinsights_v1_Settings_Builder_putPubsubNotificationSettings_java_lang_String_java_lang_String_)("create-conversation", topicCreateConversation)
                  .[putPubsubNotificationSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.Settings.Builder.html#com_google_cloud_contactcenterinsights_v1_Settings_Builder_putPubsubNotificationSettings_java_lang_String_java_lang_String_)("create-analysis", topicCreateAnalysis)
                  .build();
    
          // Construct an update mask.
          [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) updateMask =
              [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("pubsub_notification_settings").build();
    
          // Call the Insights client to enable Pub/Sub notifications.
          [Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.Settings.html) response = client.updateSettings(settings, updateMask);
          System.out.printf("Enabled Pub/Sub notifications");
        }
      }
    }
    

### Node.js

To authenticate to CX Insights, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'my_project_id';
    // const topicCreateConversation = 'projects/my_project_id/topics/my_topic_id';
    // const topicCreateAnalysis = 'projects/my_project_id/topics/my_other_topic_id';
    
    // Imports the Contact Center Insights client.
    const {
      ContactCenterInsightsClient,
    } = require('[@google-cloud/contact-center-insights](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/overview.html)');
    
    // Instantiates a client.
    const client = new [ContactCenterInsightsClient](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/overview.html)();
    
    async function enablePubSubNotifications() {
      const [settings] = await client.updateSettings({
        settings: {
          name: client.[settingsPath](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/v1.contactcenterinsightsclient.html)(projectId, 'us-central1'),
          pubsubNotificationSettings: {
            'create-conversation': topicCreateConversation,
            'create-analysis': topicCreateAnalysis,
          },
        },
        updateMask: {
          paths: ['pubsub_notification_settings'],
        },
      });
      console.info(`Enabled Pub/Sub notifications for ${settings.name}`);
    }
    enablePubSubNotifications();

## Content of the Pub/Sub message

The content of the [Pub/Sub message](https://docs.cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#pubsubmessage) depends on the event that triggers that Pub/Sub notification.

Trigger | Message Data | Message Attributes  
---|---|---  
create-analysis | [Long-running operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.longrunning#google.longrunning.Operation) whose response is an [analysis](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.Analysis) | `{"operation_name": "projects/{project}/locations/{location}/operations/{operation}"}`  
create-conversation | [Conversation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.Conversation) | `{"conversation_name": "projects/{project}/locations/{location}/conversations/{conversation}"}`  
export-insights-data | [Long-running operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.longrunning#google.longrunning.Operation) whose response is empty | `{"operation_name": "projects/{project}/locations/{location}/operations/{operation}"}`  
ingest-conversations | [Long-running operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.longrunning#google.longrunning.Operation) whose response is empty | `{"operation_name": "projects/{project}/locations/{location}/operations/{operation}"}`  
update-conversation | [Conversation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.Conversation) | `{"conversation_name": "projects/{project}/locations/{location}/conversations/{conversation}"}`  
upload-conversation | [Long-running operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.longrunning#google.longrunning.Operation) whose response is empty | `{"operation_name": "projects/{project}/locations/{location}/operations/{operation}"}`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
