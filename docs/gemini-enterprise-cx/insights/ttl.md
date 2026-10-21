---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/ttl/
title: Set a TTL (time-to-live) on conversation data \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:45:55.598922+00:00
---

# Set a TTL (time-to-live) on conversation data  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/ttl/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Set a TTL (time-to-live) on conversation data Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

There are two ways to set a conversation's expiration time in CX Insights: using the `expire_time` field, or using the `ttl` field. You can use the `expire_time` field set a timestamp indicating when the conversation will expire, or the `ttl` field to set a time duration (in seconds) until the conversation will expire. If a conversation has both an `expire_time` and `ttl` value, CX Insights uses the `expire_time` value.

Conversations set to expire using either the `expire_time` or `ttl` field will be deleted 24 hours after the specified expiration time is reached. See the [Conversation resource documentation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations#Conversation) for complete details. This page demonstrates how to set a TTL, both for individual conversations and for all conversations in a given project.

If a conversation is not set to expire, it will remain in CX Insights indefinitely, though conversations can always be manually deleted.

**Warning:** Conversations that are deleted due to expiration are not recoverable.

## Create a conversation with a TTL value

The following sample illustrates how to set a TTL value for a single, newly-created conversation using the `ttl` field in a [Conversation resource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations#Conversation).

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `contactcenterinsights.conversations.create`



### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID.
  * TRANSCRIPT_URI: the Cloud Storage URI that points to a file containing the conversation transcript.
  * MEDIUM: set to either `PHONE_CALL` or `CHAT` depending on the data type. If unspecified the default value is `PHONE_CALL`.
  * SECONDS: the time-to-live (time until the conversation expires) in seconds and fractions of a second.

**Note:** All the examples are using the global Customer Experience Insights instance. Refer to [Regionalization](https://docs.cloud.google.com/gemini-enterprise-cx/insights/docs/regionalization) for instructions on using regional instances. 

HTTP method and URL: 
    
    
    POST https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/conversations

Request JSON body: 
    
    
    {
      "data_source": {
        "gcs_source": {
          "transcript_uri": "TRANSCRIPT_URI"
        }
      },
      "medium": "MEDIUM",
      "ttl": {
        "seconds": "SECONDS"
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/conversations"

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
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/conversations" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/us-central1/conversations/CONVERSATION_ID",
      "dataSource": {
        "gcsSource": {
          "transcriptUri": "gs://cloud-samples-data/ccai/chat_sample.json"
        }
      },
      "createTime": "2021-01-20T10:10:10.123000Z",
      "transcript": {
        "transcriptSegments": [
          ...
          {
            "text": "Thanks for confirming",
            "words": [
              {
                "word": "Thanks"
              },
              {
                "word": "for"
              },
              {
                "word": "confirming"
              }
            ],
            "languageCode": "en-US",
            "channelTag": 2,
            "messageTime": "2021-01-10T10:10:15.123000Z",
            "segmentParticipant": {
              "role": "HUMAN_AGENT",
              "userId": "555"
            }
          },
          ...
        ]
      },
      "medium": "CHAT",
      "duration": "5.00s",
      "turnCount": 10,
      "startTime": "2021-01-10T10:10:10.123000Z"
      "expireTime":"2021-01-21T10:10:10.123000Z",
    }
    

### Python

To authenticate to CX Insights, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [contact_center_insights_v1](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest)
    from google.protobuf import duration_pb2
    
    
    def create_conversation_with_ttl(
        project_id: str,
        transcript_uri: str = "gs://cloud-samples-data/ccai/chat_sample.json",
        audio_uri: str = "gs://cloud-samples-data/ccai/voice_6912.txt",
    ) -> contact_center_insights_v1.Conversation:
        """Creates a conversation with a TTL value.
    
        Args:
            project_id:
                The project identifier. For example, 'my-project'.
            transcript_uri:
                The Cloud Storage URI that points to a file that contains the
                conversation transcript. Format is 'gs://{bucket_name}/{file.json}'.
                For example, 'gs://cloud-samples-data/ccai/chat_sample.json'.
            audio_uri:
                The Cloud Storage URI that points to a file that contains the
                conversation audio. Format is 'gs://{bucket_name}/{file.json}'.
                For example, 'gs://cloud-samples-data/ccai/voice_6912.txt'.
    
        Returns:
            A conversation.
        """
        # Construct a parent resource.
        parent = (
            [contact_center_insights_v1](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest).[ContactCenterInsightsClient](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.services.contact_center_insights.ContactCenterInsightsClient.html).common_location_path(
                project_id, "us-central1"
            )
        )
    
        # Construct a conversation.
        conversation = [contact_center_insights_v1](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest).[Conversation](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.Conversation.html)()
        conversation.data_source.gcs_source.transcript_uri = transcript_uri
        conversation.data_source.gcs_source.audio_uri = audio_uri
        conversation.medium = [contact_center_insights_v1](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest).[Conversation](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.Conversation.html).[Medium](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.Conversation.Medium.html).CHAT
    
        # Construct a TTL.
        ttl = duration_pb2.Duration()
        ttl.seconds = 86400
        conversation.ttl = ttl
    
        # Call the Insights client to create a conversation.
        insights_client = [contact_center_insights_v1](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest).[ContactCenterInsightsClient](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.services.contact_center_insights.ContactCenterInsightsClient.html)()
        conversation = insights_client.[create_conversation](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.services.contact_center_insights.ContactCenterInsightsClient.html#google_cloud_contact_center_insights_v1_services_contact_center_insights_ContactCenterInsightsClient_create_conversation)(
            parent=parent, conversation=conversation
        )
    
        print(f"Created {conversation.name}")
        return conversation
    
    

### Java

To authenticate to CX Insights, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.contactcenterinsights.v1.[ContactCenterInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsClient.html);
    import com.google.cloud.contactcenterinsights.v1.[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.Conversation.html);
    import com.google.cloud.contactcenterinsights.v1.[ConversationDataSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ConversationDataSource.html);
    import com.google.cloud.contactcenterinsights.v1.[CreateConversationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.CreateConversationRequest.html);
    import com.google.cloud.contactcenterinsights.v1.[GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.GcsSource.html);
    import com.google.cloud.contactcenterinsights.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.LocationName.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.io.IOException;
    
    public class CreateConversationWithTtl {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my_project_id";
        String transcriptUri = "gs://cloud-samples-data/ccai/chat_sample.json";
        String audioUri = "gs://cloud-samples-data/ccai/voice_6912.txt";
    
        createConversationWithTtl(projectId, transcriptUri, audioUri);
      }
    
      public static [Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.Conversation.html) createConversationWithTtl(
          String projectId, String transcriptUri, String audioUri) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([ContactCenterInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsClient.html) client = [ContactCenterInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsClient.html).create()) {
          // Construct a parent resource.
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.LocationName.html).of(projectId, "us-central1");
    
          // Construct a conversation.
          [Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.Conversation.html) conversation =
              [Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.Conversation.html).newBuilder()
                  .[setDataSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.Conversation.Builder.html#com_google_cloud_contactcenterinsights_v1_Conversation_Builder_setDataSource_com_google_cloud_contactcenterinsights_v1_ConversationDataSource_)(
                      [ConversationDataSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ConversationDataSource.html).newBuilder()
                          .setGcsSource(
                              [GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.GcsSource.html).newBuilder()
                                  .[setTranscriptUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.GcsSource.Builder.html#com_google_cloud_contactcenterinsights_v1_GcsSource_Builder_setTranscriptUri_java_lang_String_)(transcriptUri)
                                  .setAudioUri(audioUri)
                                  .build())
                          .build())
                  .setMedium([Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.Conversation.html).Medium.CHAT)
                  .[setTtl](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.Conversation.Builder.html#com_google_cloud_contactcenterinsights_v1_Conversation_Builder_setTtl_com_google_protobuf_Duration_)([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(86400).build())
                  .build();
    
          // Construct a request.
          [CreateConversationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.CreateConversationRequest.html) request =
              [CreateConversationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.CreateConversationRequest.html).newBuilder()
                  .setParent(parent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.LocationName.html#com_google_cloud_contactcenterinsights_v1_LocationName_toString__)())
                  .setConversation(conversation)
                  .build();
    
          // Call the Insights client to create a conversation.
          [Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.Conversation.html) response = client.createConversation(request);
          System.out.printf("Created %s%n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.Conversation.html#com_google_cloud_contactcenterinsights_v1_Conversation_getName__)());
          return response;
        }
      }
    }
    

### Node.js

To authenticate to CX Insights, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'my_project_id';
    // const transcriptUri = 'gs://cloud-samples-data/ccai/chat_sample.json';
    // const audioUri = 'gs://cloud-samples-data/ccai/voice_6912.txt';
    
    // Imports the Contact Center Insights client.
    const {
      ContactCenterInsightsClient,
    } = require('[@google-cloud/contact-center-insights](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/overview.html)');
    
    // Instantiates a client.
    const client = new [ContactCenterInsightsClient](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/overview.html)();
    
    async function createConversationWithTtl() {
      const [conversation] = await client.createConversation({
        parent: client.[locationPath](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/v1.contactcenterinsightsclient.html)(projectId, 'us-central1'),
        conversation: {
          dataSource: {
            gcsSource: {
              transcriptUri: transcriptUri,
              audioUri: audioUri,
            },
          },
          medium: '[CHAT](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.conversation.medium.html)',
          ttl: {
            seconds: 86400,
          },
        },
      });
      console.info(`Created ${conversation.name}`);
    }
    createConversationWithTtl();

## Set a project-level TTL for all incoming conversations

The following code sample demonstrates how to set a project-level TTL using the `conversation_ttl` field in a [Settings resource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1#settings). This TTL will be applied to all incoming conversations that don't specify a separate expiration time or a different TTL value.

**Note:** Project-level TTL only applies to conversations that are created after this TTL is set. Changing the TTL does not retroactively change the expiration time of any existing conversations.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `contactcenterinsights.settings.update`



### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID.
  * SECONDS: the time-to-live (time until the conversation expires) in seconds and fractions of a second.

**Note:** All the examples are using the global Customer Experience Insights instance. Refer to [Regionalization](https://docs.cloud.google.com/gemini-enterprise-cx/insights/docs/regionalization) for instructions on using regional instances. 

HTTP method and URL: 
    
    
    POST https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/settings?updateMask=conversation_ttl

Request JSON body: 
    
    
    {
      "conversation_ttl": {
        "seconds": "SECONDS"
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/settings?updateMask=conversation_ttl"

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
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/settings?updateMask=conversation_ttl" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/$PROJECT/locations/us-central1/settings",
      "createTime": "2021-01-20T10:10:10.123000Z",
      "updateTime": "2021-01-20T11:11:11.456000Z",
      "conversationTtl": "86400s"
    }
    

### Python

To authenticate to CX Insights, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core import protobuf_helpers
    from google.cloud import [contact_center_insights_v1](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest)
    from google.protobuf import duration_pb2
    
    
    def set_project_ttl(project_id: str) -> None:
        """Sets a project-level TTL for all incoming conversations.
    
        Args:
            project_id:
                The project identifier. For example, 'my-project'.
    
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
    
        conversation_ttl = duration_pb2.Duration()
        conversation_ttl.seconds = 86400
        settings.conversation_ttl = conversation_ttl
    
        # Construct an update mask to only update the fields that are set on the settings resource.
        update_mask = protobuf_helpers.field_mask(None, type(settings).pb(settings))
    
        # Construct an Insights client that will authenticate via Application Default Credentials.
        # See authentication details at https://cloud.google.com/docs/authentication/production.
        insights_client = [contact_center_insights_v1](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest).[ContactCenterInsightsClient](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.services.contact_center_insights.ContactCenterInsightsClient.html)()
    
        # Call the Insights client to set a project-level TTL.
        insights_client.[update_settings](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.services.contact_center_insights.ContactCenterInsightsClient.html#google_cloud_contact_center_insights_v1_services_contact_center_insights_ContactCenterInsightsClient_update_settings)(settings=settings, update_mask=update_mask)
    
        # Call the Insights client to get the project-level TTL to confirm that it was set.
        new_conversation_ttl = insights_client.[get_settings](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.services.contact_center_insights.ContactCenterInsightsClient.html#google_cloud_contact_center_insights_v1_services_contact_center_insights_ContactCenterInsightsClient_get_settings)(
            name=settings.name
        ).conversation_ttl
        print(
            "Set TTL for all incoming conversations to {} day".format(
                new_conversation_ttl.days
            )
        )
    
    

### Java

To authenticate to CX Insights, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.contactcenterinsights.v1.[ContactCenterInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsClient.html);
    import com.google.cloud.contactcenterinsights.v1.[Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.Settings.html);
    import com.google.cloud.contactcenterinsights.v1.[SettingsName](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.SettingsName.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.io.IOException;
    
    public class SetProjectTtl {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace this variable before running the sample.
        String projectId = "my_project_id";
    
        setProjectTtl(projectId);
      }
    
      public static void setProjectTtl(String projectId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([ContactCenterInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsClient.html) client = [ContactCenterInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsClient.html).create()) {
          // Construct a settings resource.
          [SettingsName](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.SettingsName.html) name = [SettingsName](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.SettingsName.html).of(projectId, "us-central1");
          [Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.Settings.html) settings =
              [Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.Settings.html).newBuilder()
                  .setName(name.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.SettingsName.html#com_google_cloud_contactcenterinsights_v1_SettingsName_toString__)())
                  .[setConversationTtl](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.Settings.Builder.html#com_google_cloud_contactcenterinsights_v1_Settings_Builder_setConversationTtl_com_google_protobuf_Duration_)([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(86400).build())
                  .build();
    
          // Construct an update mask.
          [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) updateMask = [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("conversation_ttl").build();
    
          // Call the Insights client to set a project-level TTL.
          [Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.Settings.html) response = client.updateSettings(settings, updateMask);
          System.out.printf("Set TTL for all incoming conversations to 1 day");
        }
      }
    }
    

### Node.js

To authenticate to CX Insights, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment this variable before running the sample.
     */
    // const projectId = 'my_project_id';
    
    // Imports the Contact Center Insights client.
    const {
      ContactCenterInsightsClient,
    } = require('[@google-cloud/contact-center-insights](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/overview.html)');
    
    // Instantiates a client.
    const client = new [ContactCenterInsightsClient](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/overview.html)();
    
    async function setProjectTtl() {
      await client.updateSettings({
        settings: {
          name: client.[settingsPath](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/v1.contactcenterinsightsclient.html)(projectId, 'us-central1'),
          conversationTtl: {
            seconds: 86400,
          },
        },
        updateMask: {
          paths: ['conversation_ttl'],
        },
      });
      console.info('Set TTL for all incoming conversations to 1 day');
    }
    setProjectTtl();

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
