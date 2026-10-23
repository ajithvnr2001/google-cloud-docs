---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/record-user-events/
title: Record real-time user events \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:47.351093+00:00
---

# Record real-time user events  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/record-user-events/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Record real-time user events Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to record user events in real time. User events are required for media apps. If you don't use media apps, importing user events isn't required. However, recording user events is recommended for custom search and recommendations apps.

To see an example of record user events, run the "Record user events" notebook in one of the following environments: 

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/search/vais-building-blocks/record_user_events.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/search/vais-building-blocks/record_user_events.ipynb)

For the user event types that you can record, see the `eventType` field of the [`userEvents`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents#resource:-userevent) object. By ingesting user events, you can improve the quality of your results. For example, user events affect the ranking of search results. Results with higher click-through rates are boosted, while results with lower click-through rates are buried. Don't record user events for documents that you have not yet imported.

If you are using an app with multiple data stores attached, ingest user events at the location level instead of the data-store level. This allows a given user event to be sent to the data store that it's associated with. When recording user events at a location level, you must include the `engine` field in the user events to associate the event with the correct app. For examples of user events that include the `engine` field, see the following:

  * [Custom apps user event type examples and schemas ](https://docs.cloud.google.com/generative-ai-app-builder/docs/user-events#formats)
  * [Media apps user event type examples and schemas ](https://docs.cloud.google.com/generative-ai-app-builder/docs/media-user-events)



To import historical user events in bulk, see [Import historical user events](https://docs.cloud.google.com/generative-ai-app-builder/docs/import-user-events).

You can record user events in the following ways:

  * With a JavaScript pixel.
  * With the `userEvents.write` method.



For the JSON representation for user events, see [`userEvents`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents#resource:-userevent) in the API reference.

**Note:** The search widget also records user events. If you [add the widget](https://docs.cloud.google.com/generative-ai-app-builder/docs/add-widget) to a web page and the user clicks a search result, the widget records a `view-item` user event for that click.

## Before you begin

Before you import user events:

  * Create a data store and an app.
  * Review [About media user events](https://docs.cloud.google.com/generative-ai-app-builder/docs/media-user-events) or [About user events for custom apps](https://docs.cloud.google.com/generative-ai-app-builder/docs/user-events) for user event requirements.



## Record real-time user events with a JavaScript pixel

To record user events with a JavaScript pixel:

  1. Create an API key for calls to the [`userEvents.collect`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.userEvents/collect) method.
  2. See the JavaScript pixel example for an example of a JavaScript tag that collects user events.



### Create an API key

An API key is required if you use a JavaScript pixel to collect user events from users' browsers.

To create an API key for calls to the [`userEvents.collect`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.userEvents/collect) method, complete the following steps:

  1. In the Google Cloud console, go to the **Credentials** page.

[Credentials](https://console.cloud.google.com/apis/credentials)

  2. In the project list at the top of the Google Cloud console page, select your project (the project might already be selected).

  3. Click **Create credentials** and then select **API key**. _Don't add any referrer restrictions_. Some user privacy settings don't pass the referrer URL.

     * Take note of the generated API key, which you will use when calling user event logging.
  4. For increased security, add an [HTTP restriction](https://docs.cloud.google.com/docs/authentication/api-keys#api_key_restrictions) to your API Key to restrict access to the Agent Search service at `https://discoveryengine.googleapis.com/*`.


**Note:** The API key is only for authenticating the [`userEvents.collect`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.userEvents/collect) method and the [`servingConfigs.searchLite`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/searchLite) method. Other Agent Search methods require OAuth 2.0 through a service account or a user account.

### JavaScript pixel example

The following example records a `view-item` user event using a JavaScript pixel.

For the JSON representation for user events, see [`userEvents`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents#resource:-userevent) in the API reference.
    
    
    <script type="text/javascript">
    var user_event = {
      "eventType" : "view-item",
      "userPseudoId": "USER_PSEUDO_ID",
      "engine": "projects/PROJECT_ID/locations/LOCATION_ID/collections/default_collection/engines/APP_ID",
      "userInfo": {
          "userId": "USER_ID"
      },
      "attributionToken": "ATTRIBUTION_TOKEN",
      "tagIds": "TAG_ID",
      "documents": [
          {
            "id": "DOCUMENT_ID"
          }
      ]
    };
    
    var _gre = _gre || {};
    // Credentials for project.
    _gre.apiKey = '[API_KEY]';
    _gre.logEvent = user_event;
    _gre.projectId = 'PROJECT_ID';
    _gre.locationId = 'LOCATION_ID';
    _gre.dataStoreId = 'DATA_STORE_ID';
    
    (function() {
      var gre = document.createElement('script'); gre.type = 'text/javascript'; gre.async = true;
      gre.src = 'https://www.gstatic.com/discoveryengine/v1beta_event.js';
      var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(gre, s);
    })();
    
    </script>
    

## Record real-time user events with the `userEvents.write` method

### REST

You can use the [`userEvents.write`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.userEvents/write) method to send user events directly to the API from your backend server.

To record user events, send a POST request to the `userEvents.write` method and provide the appropriate request body. For the JSON representation for user events, see [`userEvents`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents#resource:-userevent) in the API reference.

If you are recording user events at the location level, use the endpoint `https://discoveryengine.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/userEvents:write`.
    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_NUMBER/locations/global/userEvents:write" \
         -d '{
             "eventType": "view-item",
             "userPseudoId": "visitor0",
             "engine": "projects/PROJECT_NUMBER/locations/global/collections/default_collection/engines/APP_ID",
             "eventTime": "2020-01-01T03:33:33.000001Z",
             "tagIds": ["321"],
             "attributionToken": "ABC",
             "attributes": {
                "example_text_attribute": {
                  "text": ["text_1", "text_2"]
                },
                "example_number_attribute": {
                   "numbers": [3.14, 42, 1.2345]
                }
              },
             "documents": [{
                "id": "abc"
              }],
             "userInfo": {
               "userId": "abc",
               "userAgent": "Mozilla/5.0"
             },
             "pageInfo": {
              "uri": "http://example",
              "referrerUri": "http://example",
              "pageViewId": "currentPageUri"
             }
            }'
    

### C#

For more information, see the [Agent Search C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.DiscoveryEngine.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.html);
    
    public sealed partial class GeneratedUserEventServiceClientSnippets
    {
        /// <summary>Snippet for WriteUserEvent</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void WriteUserEventRequestObject()
        {
            // Create client
            [UserEventServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.UserEventServiceClient.html) userEventServiceClient = [UserEventServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.UserEventServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.UserEventServiceClient.html#Google_Cloud_DiscoveryEngine_V1_UserEventServiceClient_Create)();
            // Initialize request argument(s)
            [WriteUserEventRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.WriteUserEventRequest.html) request = new [WriteUserEventRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.WriteUserEventRequest.html)
            {
                ParentAsDataStoreName = [DataStoreName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DataStoreName.html).[FromProjectLocationDataStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DataStoreName.html#Google_Cloud_DiscoveryEngine_V1_DataStoreName_FromProjectLocationDataStore_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[DATA_STORE]"),
                UserEvent = new [UserEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.UserEvent.html)(),
                WriteAsync = false,
            };
            // Make the request
            [UserEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.UserEvent.html) response = userEventServiceClient.[WriteUserEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.UserEventServiceClient.html#Google_Cloud_DiscoveryEngine_V1_UserEventServiceClient_WriteUserEvent_Google_Cloud_DiscoveryEngine_V1_WriteUserEventRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
        }
    }

### Go

For more information, see the [Agent Search Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/discoveryengine/latest/apiv1). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	discoveryengine "cloud.google.com/go/discoveryengine/apiv1"
    	discoveryenginepb "cloud.google.com/go/discoveryengine/apiv1/discoveryenginepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := discoveryengine.[NewUserEventClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/discoveryengine/latest/apiv1.html#cloud_google_com_go_discoveryengine_apiv1_UserEventClient_NewUserEventClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &discoveryenginepb.WriteUserEventRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/discoveryengine/apiv1/discoveryenginepb#WriteUserEventRequest.
    	}
    	resp, err := c.WriteUserEvent(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### Java

For more information, see the [Agent Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/overview). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.discoveryengine.v1.[DataStoreName](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStoreName.html);
    import com.google.cloud.discoveryengine.v1.[UserEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UserEvent.html);
    import com.google.cloud.discoveryengine.v1.[UserEventServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UserEventServiceClient.html);
    import com.google.cloud.discoveryengine.v1.[WriteUserEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.WriteUserEventRequest.html);
    
    public class SyncWriteUserEvent {
    
      public static void main(String[] args) throws Exception {
        syncWriteUserEvent();
      }
    
      public static void syncWriteUserEvent() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([UserEventServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UserEventServiceClient.html) userEventServiceClient = [UserEventServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UserEventServiceClient.html).create()) {
          [WriteUserEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.WriteUserEventRequest.html) request =
              [WriteUserEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.WriteUserEventRequest.html).newBuilder()
                  .setParent(
                      [DataStoreName](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStoreName.html).ofProjectLocationDataStoreName(
                              "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                          .toString())
                  .setUserEvent([UserEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UserEvent.html).newBuilder().build())
                  .[setWriteAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.WriteUserEventRequest.Builder.html#com_google_cloud_discoveryengine_v1_WriteUserEventRequest_Builder_setWriteAsync_boolean_)(true)
                  .build();
          [UserEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UserEvent.html) response = userEventServiceClient.writeUserEvent(request);
        }
      }
    }

### Python

For more information, see the [Agent Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [discoveryengine_v1](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest)
    
    
    def sample_write_user_event():
        # Create a client
        client = [discoveryengine_v1](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest).[UserEventServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.user_event_service.UserEventServiceClient.html)()
    
        # Initialize request argument(s)
        request = [discoveryengine_v1](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest).[WriteUserEventRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.WriteUserEventRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = client.[write_user_event](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.user_event_service.UserEventServiceClient.html#google_cloud_discoveryengine_v1_services_user_event_service_UserEventServiceClient_write_user_event)(request=request)
    
        # Handle the response
        print(response)
    
    

### Ruby

For more information, see the [Agent Search Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/discovery_engine/v1"
    
    ##
    # Snippet for the write_user_event call in the UserEventService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::DiscoveryEngine::V1::UserEventService::Client#write_user_event.
    #
    def write_user_event
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::DiscoveryEngine::V1::UserEventService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::DiscoveryEngine::V1::WriteUserEventRequest.new
    
      # Call the write_user_event method.
      result = client.write_user_event request
    
      # The returned object is of type Google::Cloud::DiscoveryEngine::V1::UserEvent.
      p result
    end

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
