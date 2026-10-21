---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-recommendations/
title: Get recommendations \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:28:07.602208+00:00
---

# Get recommendations  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-recommendations/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Get recommendations Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to preview recommendations using the Google Cloud console and get recommendations results using the API. See the REST tab for examples of API calls that can help you integrate recommendations into your app.

The procedure that you use depends on whether you have media data or custom data:

  * Get media recommendations
  * Get custom recommendations for an app with structured data

**Note:** Depending on the amount of data, it can take hours after data ingestion until the preview feature works.

## Get media recommendations

### Console

To use the Google Cloud console to preview media recommendations, follow these steps:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/start)

  2. Click the name of the app for which you want to preview recommendations.

  3. Click **Configurations** > **Training**. If **Ready to query** is Yes, then the app is ready for preview.

  4. Click **Preview**.

  5. Click the **Document ID** field. A list of document IDs appears.

  6. Click the document ID for the document that you want recommendations for. Alternatively, enter a document ID into the **Document ID** field.

  7. Click **Select serving config** and select the serving config to preview.

  8. Optional: Enter the visitor ID (also called the pseudo user ID) of a user for whom you have collected user events. If you leave this field blank or enter a non-existent visitor ID, you'll preview recommendations as a new user.

  9. Click **Get recommendations**. A list of recommended documents appears.

  10. Click a document to get document details.




### REST

To use the API to get media recommendations, use the [`servingConfigs.recommend`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.dataStores.servingConfigs/recommend) method:

  1. Find your engine ID and serving config ID. If you already have your engine ID and serving config IDs, skip to step 2.

     1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/engines)

     2. Click the name of the app.

     3. In the navigation pane, click **Configurations**.

     4. If you have only one serving config, get the serving config ID that is displayed in the **Control** tab.

If you have multiple serving configs listed in the **Control** tab, find the serving config that you want to get recommendations from. Your serving config ID is the value in the **ID** column.

     5. Click the **Training** tab. Your engine ID is the value in the **App ID** row.

  2. Make sure the app is ready for previewing:

     1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/)

     2. Click the name of the app.

     3. Click **Configurations** > **Training**. If **Ready to query** is Yes, then the app is ready for preview.

  3. Get recommendations.

**Note:** If your recommendation is not yet active or you want to test your method call, you can call this method with the `validateOnly` flag set to `true`. This call returns a placeholder result, and does not incur charges.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d  '{
                 "validateOnly": false,
                 "userEvent": {
                     "eventType": "view-item",
                     "userPseudoId": "USER_PSEUDO_ID",
                     "documents": [{
                       "id": "DOCUMENT_ID"
                     }],
                 "filter": "FILTER_STRING"            }
             }' \
           "https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/servingConfigs/SERVING_CONFIG_ID:recommend"

Replace the following:

     * `PROJECT_ID`: the ID of your project.
     * `DATA_STORE_ID`: the ID of your data store.
     * `DOCUMENT_ID`: the ID of document that you want to preview recommendations for. Use the ID that you used for this document at the time you ingested your data.
     * `USER_PSEUDO_ID`: a UTF-8 encoded string, which acts as a unique pseudonymized identifier that tracks the users. It can have a maximum length of 128 characters. Google strongly recommends using this field because it improves model performance and personalization quality. You can use an HTTP cookie for this field, which uniquely identifies a visitor on a single device. Some important considerations are as follows:



  * This identifier doesn't change when the visitor signs in or out of a website.
  * This field must not be set to the same identifier for multiple users. Otherwise, same user ID can combine event histories of different users and degrade model quality.
  * This field must not include personally identifiable information (PII).



For more information, see [`userPseudoId`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents#UserEvent.FIELDS.user_pseudo_id). 

* `SERVING_CONFIG_ID`: the ID of your serving config.
* `FILTER`: optional. A text field that lets you to filter on a specified set of fields, using filter expression syntax. The default value is an empty string, which means no filter is applied. For more information, see [Filter recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-recommendations).

You should see results similar to the following:
    
    
    {
      "results": [{"id": "sample-id-1"}, {"id": "sample-id-2"}],
      "attributionToken": "abc123"
    }

Google recommends associating attribution tokens, which we include with each search response and recommendation, with actions that a user takes in response to those search responses and recommendations. This can improve the quality of your search responses and recommendations over time. To do this, append `attributionToken` values to the URLs for each of the links that you display on your website for search responses or recommendations—for example, `https://www.example.com/54321/?rtoken=abc123`. When a user clicks one of these links, include the `attributionToken` value in the user event that you record.

## Get recommendations for an app with custom structured data

**Preview — Recommendations (custom)**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

### Console

To use the Google Cloud console to preview custom recommendations for your structured app, follow these steps:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/start)

  2. Click the name of the app for which you want to preview recommendations.

  3. Click **Preview**.

  4. Click the **Document ID** field. A list of document IDs appears.

  5. Click the document ID for the document that you want recommendations for. Alternatively, enter a document ID into the **Document ID** field.

  6. Click **Get recommendations**. A list of recommended documents appears.

  7. Click a document to get document details.




### REST

To use the API to get custom recommendations for an app with structured data, use the [`servingConfigs.recommend`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.dataStores.servingConfigs/recommend) method:

  1. Find your engine ID. If you already have your engine ID, skip to step 2.

     1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/engines)

     2. Click the name of the app.

     3. Get the engine ID from the URL of the Google Cloud console. It is the text between `engines/` and `/data`. For example, if the URL contains
            
            gen-app-builder/engines/demo_1234567890123/data/records
            

then the engine ID is `demo_1234567890123`.

  2. Find your data store ID. If you already have your data store ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page and in the navigation menu, click **Data Stores**.

[Go to the Data Stores page](https://console.cloud.google.com/gen-app-builder/data-stores)

     2. Click the name of your data store.

     3. On the **Data** page for your data store, get the data store ID.

  3. Make sure your engine is ready to previewing by polling the `GetEngine` method until it returns `"servingState":"ACTIVE"`. At that point the engine is ready for previewing.
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/ENGINE_ID
         

Replace the following:

     * `PROJECT_ID`: the ID of your project.
     * `ENGINE_ID`: the ID of your engine.
  4. Get recommendations.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         -H "Content-Type: application/json" \
         -d '{
           "userEvent": { "eventType":"view-item", "userPseudoId":"USER_PSEUDO_ID", "documents":[{"id":"DOCUMENT_ID"}]}}' \
           "https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/servingConfigs/SERVING_CONFIG_ID:recommend"
         

Replace the following:

     * `PROJECT_ID`: the ID of your project.
     * `DATA_STORE_ID`: the ID of your data store.
     * `DOCUMENT_ID`: the ID of document that you want to preview recommendations for. Use the ID that you used for this document at the time you ingested your data.
     * `USER_PSEUDO_ID`: a UTF-8 encoded string, which acts as a unique pseudonymized identifier that tracks the users. It can have a maximum length of 128 characters. Google strongly recommends using this field because it improves model performance and personalization quality. You can use an HTTP cookie for this field, which uniquely identifies a visitor on a single device. Some important considerations are as follows: 

       * This identifier doesn't change when the visitor signs in or out of a website.
       * This field must not be set to the same identifier for multiple users. Otherwise, same user ID can combine event histories of different users and degrade model quality.
       * This field must not include personally identifiable information (PII).

For more information, see [`userPseudoId`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents#UserEvent.FIELDS.user_pseudo_id). 

     * `SERVING_CONFIG_ID`: the ID of your serving config. Your serving config ID is the same as your engine ID, so use your engine ID here.
**Note:** You don't need to have user events in your data store to get custom recommendations. However, you do need to provide the user event object, including an event type and a value for the user pseudo ID. 



### C#

For more information, see the [Agent Search C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.DiscoveryEngine.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    
    public sealed partial class GeneratedRecommendationServiceClientSnippets
    {
        /// <summary>Snippet for Recommend</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void RecommendRequestObject()
        {
            // Create client
            [RecommendationServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.RecommendationServiceClient.html) recommendationServiceClient = [RecommendationServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.RecommendationServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.RecommendationServiceClient.html#Google_Cloud_DiscoveryEngine_V1Beta_RecommendationServiceClient_Create)();
            // Initialize request argument(s)
            [RecommendRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.RecommendRequest.html) request = new [RecommendRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.RecommendRequest.html)
            {
                ServingConfigAsServingConfigName = [ServingConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ServingConfigName.html).[FromProjectLocationDataStoreServingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ServingConfigName.html#Google_Cloud_DiscoveryEngine_V1Beta_ServingConfigName_FromProjectLocationDataStoreServingConfig_System_String_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SERVING_CONFIG]"),
                UserEvent = new [UserEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.UserEvent.html)(),
                PageSize = 0,
                Filter = "",
                ValidateOnly = false,
                Params = { { "", new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Value.html)() }, },
                UserLabels = { { "", "" }, },
            };
            // Make the request
            [RecommendResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.RecommendResponse.html) response = recommendationServiceClient.[Recommend](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.RecommendationServiceClient.html#Google_Cloud_DiscoveryEngine_V1Beta_RecommendationServiceClient_Recommend_Google_Cloud_DiscoveryEngine_V1Beta_RecommendRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
        }
    }

### Go

For more information, see the [Agent Search Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/discoveryengine/latest/apiv1). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	discoveryengine "cloud.google.com/go/discoveryengine/apiv1beta"
    	discoveryenginepb "cloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := discoveryengine.[NewRecommendationClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/discoveryengine/latest/apiv1beta.html#cloud_google_com_go_discoveryengine_apiv1beta_RecommendationClient_NewRecommendationClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &discoveryenginepb.RecommendRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb#RecommendRequest.
    	}
    	resp, err := c.Recommend(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### Java

For more information, see the [Agent Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/overview). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.discoveryengine.v1beta.RecommendRequest;
    import com.google.cloud.discoveryengine.v1beta.RecommendResponse;
    import com.google.cloud.discoveryengine.v1beta.RecommendationServiceClient;
    import com.google.cloud.discoveryengine.v1beta.ServingConfigName;
    import com.google.cloud.discoveryengine.v1beta.UserEvent;
    import com.google.protobuf.[Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html);
    import java.util.HashMap;
    
    public class SyncRecommend {
    
      public static void main(String[] args) throws Exception {
        syncRecommend();
      }
    
      public static void syncRecommend() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (RecommendationServiceClient recommendationServiceClient =
            RecommendationServiceClient.create()) {
          RecommendRequest request =
              RecommendRequest.newBuilder()
                  .setServingConfig(
                      ServingConfigName.ofProjectLocationDataStoreServingConfigName(
                              "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SERVING_CONFIG]")
                          .toString())
                  .setUserEvent(UserEvent.newBuilder().build())
                  .setPageSize(883849137)
                  .setFilter("filter-1274492040")
                  .setValidateOnly(true)
                  .putAllParams(new HashMap<String, Value>())
                  .putAllUserLabels(new HashMap<String, String>())
                  .build();
          RecommendResponse response = recommendationServiceClient.recommend(request);
        }
      }
    }

### Node.js

For more information, see the [Agent Search Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. Full resource name of a
     *  ServingConfig google.cloud.discoveryengine.v1beta.ServingConfig:
     *  `projects/* /locations/global/collections/* /engines/* /servingConfigs/*`, or
     *  `projects/* /locations/global/collections/* /dataStores/* /servingConfigs/*`
     *  One default serving config is created along with your recommendation engine
     *  creation. The engine ID is used as the ID of the default serving
     *  config. For example, for Engine
     *  `projects/* /locations/global/collections/* /engines/my-engine`, you can use
     *  `projects/* /locations/global/collections/* /engines/my-engine/servingConfigs/my-engine`
     *  for your
     *  RecommendationService.Recommend google.cloud.discoveryengine.v1beta.RecommendationService.Recommend 
     *  requests.
     */
    // const servingConfig = 'abc123'
    /**
     *  Required. Context about the user, what they are looking at and what action
     *  they took to trigger the Recommend request. Note that this user event
     *  detail won't be ingested to userEvent logs. Thus, a separate userEvent
     *  write request is required for event logging.
     *  Don't set
     *  UserEvent.user_pseudo_id google.cloud.discoveryengine.v1beta.UserEvent.user_pseudo_id 
     *  or
     *  UserEvent.user_info.user_id google.cloud.discoveryengine.v1beta.UserInfo.user_id 
     *  to the same fixed ID for different users. If you are trying to receive
     *  non-personalized recommendations (not recommended; this can negatively
     *  impact model performance), instead set
     *  UserEvent.user_pseudo_id google.cloud.discoveryengine.v1beta.UserEvent.user_pseudo_id 
     *  to a random unique ID and leave
     *  UserEvent.user_info.user_id google.cloud.discoveryengine.v1beta.UserInfo.user_id 
     *  unset.
     */
    // const userEvent = {}
    /**
     *  Maximum number of results to return. Set this property
     *  to the number of recommendation results needed. If zero, the service
     *  chooses a reasonable default. The maximum allowed value is 100. Values
     *  above 100 are set to 100.
     */
    // const pageSize = 1234
    /**
     *  Filter for restricting recommendation results with a length limit of 5,000
     *  characters. Currently, only filter expressions on the `filter_tags`
     *  attribute is supported.
     *  Examples:
     *   * `(filter_tags: ANY("Red", "Blue") OR filter_tags: ANY("Hot", "Cold"))`
     *   * `(filter_tags: ANY("Red", "Blue")) AND NOT (filter_tags: ANY("Green"))`
     *  If `attributeFilteringSyntax` is set to true under the `params` field, then
     *  attribute-based expressions are expected instead of the above described
     *  tag-based syntax. Examples:
     *   * (language: ANY("en", "es")) AND NOT (categories: ANY("Movie"))
     *   * (available: true) AND
     *     (language: ANY("en", "es")) OR (categories: ANY("Movie"))
     *  If your filter blocks all results, the API returns generic
     *  (unfiltered) popular Documents. If you only want results strictly matching
     *  the filters, set `strictFiltering` to `true` in
     *  RecommendRequest.params google.cloud.discoveryengine.v1beta.RecommendRequest.params 
     *  to receive empty results instead.
     *  Note that the API never returns
     *  Document google.cloud.discoveryengine.v1beta.Document s with
     *  `storageStatus` as `EXPIRED` or `DELETED` regardless of filter choices.
     */
    // const filter = 'abc123'
    /**
     *  Use validate only mode for this recommendation query. If set to `true`, a
     *  fake model is used that returns arbitrary Document IDs.
     *  Note that the validate only mode should only be used for testing the API,
     *  or if the model is not ready.
     */
    // const validateOnly = true
    /**
     *  Additional domain specific parameters for the recommendations.
     *  Allowed values:
     *  * `returnDocument`: Boolean. If set to `true`, the associated Document
     *     object is returned in
     *     RecommendResponse.RecommendationResult.document google.cloud.discoveryengine.v1beta.RecommendResponse.RecommendationResult.document.
     *  * `returnScore`: Boolean. If set to true, the recommendation score
     *     corresponding to each returned Document is set in
     *     RecommendResponse.RecommendationResult.metadata google.cloud.discoveryengine.v1beta.RecommendResponse.RecommendationResult.metadata.
     *     The given score indicates the probability of a Document conversion given
     *     the user's context and history.
     *  * `strictFiltering`: Boolean. True by default. If set to `false`, the
     *  service
     *     returns generic (unfiltered) popular Documents instead of empty if
     *     your filter blocks all recommendation results.
     *  * `diversityLevel`: String. Default empty. If set to be non-empty, then
     *     it needs to be one of:
     *      *  `no-diversity`
     *      *  `low-diversity`
     *      *  `medium-diversity`
     *      *  `high-diversity`
     *      *  `auto-diversity`
     *     This gives request-level control and adjusts recommendation results
     *     based on Document category.
     *  * `attributeFilteringSyntax`: Boolean. False by default. If set to true,
     *     the `filter` field is interpreted according to the new,
     *     attribute-based syntax.
     */
    // const params = [1,2,3,4]
    /**
     *  The user labels applied to a resource must meet the following requirements:
     *  * Each resource can have multiple labels, up to a maximum of 64.
     *  * Each label must be a key-value pair.
     *  * Keys have a minimum length of 1 character and a maximum length of 63
     *    characters and cannot be empty. Values can be empty and have a maximum
     *    length of 63 characters.
     *  * Keys and values can contain only lowercase letters, numeric characters,
     *    underscores, and dashes. All characters must use UTF-8 encoding, and
     *    international characters are allowed.
     *  * The key portion of a label must be unique. However, you can use the same
     *    key with multiple resources.
     *  * Keys must start with a lowercase letter or international character.
     *  See Requirements for
     *  labels (https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements)
     *  for more details.
     */
    // const userLabels = [1,2,3,4]
    
    // Imports the Discoveryengine library
    const {RecommendationServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1beta;
    
    // Instantiates a client
    const discoveryengineClient = new [RecommendationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
    async function callRecommend() {
      // Construct request
      const request = {
        servingConfig,
        userEvent,
      };
    
      // Run request
      const response = await discoveryengineClient.recommend(request);
      console.log(response);
    }
    
    callRecommend();

### PHP

For more information, see the [Agent Search PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\DiscoveryEngine\V1beta\Client\RecommendationServiceClient;
    use Google\Cloud\DiscoveryEngine\V1beta\RecommendRequest;
    use Google\Cloud\DiscoveryEngine\V1beta\RecommendResponse;
    use Google\Cloud\DiscoveryEngine\V1beta\UserEvent;
    
    /**
     * Makes a recommendation, which requires a contextual user event.
     *
     * @param string $formattedServingConfig Full resource name of a
     *                                       [ServingConfig][google.cloud.discoveryengine.v1beta.ServingConfig]:
     *                                       `projects/&#42;/locations/global/collections/&#42;/engines/&#42;/servingConfigs/*`, or
     *                                       `projects/&#42;/locations/global/collections/&#42;/dataStores/&#42;/servingConfigs/*`
     *
     *                                       One default serving config is created along with your recommendation engine
     *                                       creation. The engine ID is used as the ID of the default serving
     *                                       config. For example, for Engine
     *                                       `projects/&#42;/locations/global/collections/&#42;/engines/my-engine`, you can use
     *                                       `projects/&#42;/locations/global/collections/&#42;/engines/my-engine/servingConfigs/my-engine`
     *                                       for your
     *                                       [RecommendationService.Recommend][google.cloud.discoveryengine.v1beta.RecommendationService.Recommend]
     *                                       requests. Please see
     *                                       {@see RecommendationServiceClient::servingConfigName()} for help formatting this field.
     * @param string $userEventEventType     User event type. Allowed values are:
     *
     *                                       Generic values:
     *
     *                                       * `search`: Search for Documents.
     *                                       * `view-item`: Detailed page view of a Document.
     *                                       * `view-item-list`: View of a panel or ordered list of Documents.
     *                                       * `view-home-page`: View of the home page.
     *                                       * `view-category-page`: View of a category page, e.g. Home > Men > Jeans
     *
     *                                       Retail-related values:
     *
     *                                       * `add-to-cart`: Add an item(s) to cart, e.g. in Retail online shopping
     *                                       * `purchase`: Purchase an item(s)
     *
     *                                       Media-related values:
     *
     *                                       * `media-play`: Start/resume watching a video, playing a song, etc.
     *                                       * `media-complete`: Finished or stopped midway through a video, song, etc.
     * @param string $userEventUserPseudoId  A unique identifier for tracking visitors.
     *
     *                                       For example, this could be implemented with an HTTP cookie, which should be
     *                                       able to uniquely identify a visitor on a single device. This unique
     *                                       identifier should not change if the visitor log in/out of the website.
     *
     *                                       Do not set the field to the same fixed ID for different users. This mixes
     *                                       the event history of those users together, which results in degraded model
     *                                       quality.
     *
     *                                       The field must be a UTF-8 encoded string with a length limit of 128
     *                                       characters. Otherwise, an `INVALID_ARGUMENT` error is returned.
     *
     *                                       The field should not contain PII or user-data. We recommend to use Google
     *                                       Analytics [Client
     *                                       ID](https://developers.google.com/analytics/devguides/collection/analyticsjs/field-reference#clientId)
     *                                       for this field.
     */
    function recommend_sample(
        string $formattedServingConfig,
        string $userEventEventType,
        string $userEventUserPseudoId
    ): void {
        // Create a client.
        $recommendationServiceClient = new RecommendationServiceClient();
    
        // Prepare the request message.
        $userEvent = (new UserEvent())
            ->setEventType($userEventEventType)
            ->setUserPseudoId($userEventUserPseudoId);
        $request = (new RecommendRequest())
            ->setServingConfig($formattedServingConfig)
            ->setUserEvent($userEvent);
    
        // Call the API and handle any network failures.
        try {
            /** @var RecommendResponse $response */
            $response = $recommendationServiceClient->recommend($request);
            printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
        } catch (ApiException $ex) {
            printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
        }
    }
    
    /**
     * Helper to execute the sample.
     *
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function callSample(): void
    {
        $formattedServingConfig = RecommendationServiceClient::servingConfigName(
            '[PROJECT]',
            '[LOCATION]',
            '[DATA_STORE]',
            '[SERVING_CONFIG]'
        );
        $userEventEventType = '[EVENT_TYPE]';
        $userEventUserPseudoId = '[USER_PSEUDO_ID]';
    
        recommend_sample($formattedServingConfig, $userEventEventType, $userEventUserPseudoId);
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
    from google.cloud import discoveryengine_v1beta
    
    
    def sample_recommend():
        # Create a client
        client = discoveryengine_v1beta.[RecommendationServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.recommendation_service.RecommendationServiceClient.html)()
    
        # Initialize request argument(s)
        user_event = discoveryengine_v1beta.[UserEvent](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.UserEvent.html)()
        user_event.event_type = "event_type_value"
        user_event.user_pseudo_id = "user_pseudo_id_value"
    
        request = discoveryengine_v1beta.[RecommendRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.RecommendRequest.html)(
            serving_config="serving_config_value",
            user_event=user_event,
        )
    
        # Make the request
        response = client.[recommend](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.recommendation_service.RecommendationServiceClient.html)(request=request)
    
        # Handle the response
        print(response)
    
    

### Ruby

For more information, see the [Agent Search Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/discovery_engine/v1beta"
    
    ##
    # Snippet for the recommend call in the RecommendationService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::DiscoveryEngine::V1beta::RecommendationService::Client#recommend.
    #
    def recommend
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::DiscoveryEngine::V1beta::RecommendationService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::DiscoveryEngine::V1beta::RecommendRequest.new
    
      # Call the recommend method.
      result = client.recommend request
    
      # The returned object is of type Google::Cloud::DiscoveryEngine::V1beta::RecommendResponse.
      p result
    end

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
