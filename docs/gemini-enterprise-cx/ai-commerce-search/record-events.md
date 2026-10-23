---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/record-events/
title: Record real-time user events \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:51.235142+00:00
---

# Record real-time user events  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/record-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Record real-time user events Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how you record real-time user events. AI Commerce Search uses real-time user events to generate recommendations and search results. Recording as many types of user events as possible with valid product information increases the quality of your results.

The recording procedures on this page apply to both recommendations and search. After you record data, both services are able to use those events, so you don't need to upload the same data twice if you use both services.

## Before you begin

Before recording user events, you should have:

  * A Google Cloud project created, with authentication set up.

  * A valid API key (for JavaScript Pixel or Tag Manager), or a valid service account with the Retail Editor Role assigned if using the API to write directly.




### Required components

  * **Attribution token** : Enables [performance metrics](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/performance) for recorded user events to capture first-time user interactions with a product based on previously provided recommendations or search result. Read more about [including attribution tokens](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/attribution-tokens).

  * **Visitor IDs** : Required when recording user events. For information, see [About user information](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/implement-user-events#user-information).




### Get started recording

  * Follow best practices such as rejoining events, keeping your catalog up to date, and providing as much information as possible.

  * You can find sample JSON for [user event type examples and schema](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/user-events#formats) in the [About user events](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/user-events) page.


**Caution:** Use a secure form of a unique identifier to keep users anonymous to AI Commerce Search and protect your users' privacy. You are responsible for redacting PII (personally identifiable information), such as email or home addresses, from your data. 

## Stream live user events

While both bulk import and real-time streaming offer effective mechanisms for user event ingestion in AI Commerce Search, real-time streaming presents several nuanced advantages:

  * **Immediate scalability** : Real-time streaming often negates the need for additional extract, transform, load (ETL) pipelines, facilitating scalability as event volumes increase. The infrastructure can typically handle growth organically without major adjustments.

  * **Integration with Google Analytics (GA4)** : Websites instrumented with GA4 can use Google Tag Manager to capture and stream real-time events into AI Commerce Search, eliminating the need for custom event tracking implementations.

  * **Direct API calls** : Real-time events can be transmitted directly from the frontend or through a proxy server using REST APIs, integrating the entire process and reducing potential points of failure.

  * **Up-to-date KPI measurement and error reporting** : Faster processing of real-time events translates to more current KPI measurements and error reporting. This allows for quicker identification and resolution of issues.

  * **Real-time personalization** : By capturing and processing user events in real time, AI Commerce Search can deliver personalized search results based on recent browsing and purchase behavior.




### Live user event streaming methods

You can record a user event in multiple ways:

  * Use JavaScript pixel.

  * Google Analytics (GA4) with Tag Manager is recommended.

  * Send events directly to the API from your backend server through the `user.Events.write` method.

  * Tag Manager, on its own or in conjunction with Google Analytics 4.

  * With server-side tagging, record events by deploying a single server-side container with many downstream clients.




### Potential downsides of real-time streaming

The potential downsides of real-time streaming can present themselves in the following ways:

  * **Limited reingestion** : Unlike bulk imports, where data can be staged in BigQuery or Cloud Storage, real-time events are difficult to reingest in case of errors or malformed data. This necessitates robust validation mechanisms at the ingestion point to ensure data integrity.

  * **Challenges with custom analysis** : If custom analysis of event data is required, it often necessitates exporting events to BigQuery for further processing. This can become a bottleneck for high-volume event streams, potentially slowing down analysis and reporting.

  * **Limited retrospective debugging and event data transfer** : Sending the event directly without staging limits the ability to do any retrospective forensics on the events that are already ingested. Another potential limitation is that training the models in a lower environment might not have sufficient events. Having a staging area for the events data (BigQuery or Cloud Storage) builds the ability to also import or transfer the events in other environments after minor data transformations.




Understanding these nuances can help you make informed decisions about the most suitable user event ingestion strategy for your specific needs and priorities within the AI Commerce Search ecosystem.

## Best practices for recording user events

AI Commerce Search requires high-quality data to generate high-quality results. If your data is incomplete or incorrect, the quality of your results suffers.

When you record user events, ensure that you implement the following best practices:

  * If you record user events before or while importing your catalog, [rejoin any events](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-user-events#rejoin-event) recorded before the catalog import completed.

You can [import the catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/upload-catalog) before, after, or at the same time you record user events. Doing these tasks in parallel can save time if the catalog is large and there are many user events. Once the catalog import is complete, you must use the API to rejoin events that were uploaded before the import completed.

AI Commerce Search attempts to join recorded user events with metadata from the product catalog when the user event is created. Only successfully joined events are used for training, so make sure to rejoin any events recorded before the catalog was completely imported. If an event refers to an item that doesn't exist in the catalog, it is discarded or not associated with the correct products. Similarly, if you import user events from the past, the catalog must include any products they reference; you can mark older products as `OUT_OF_STOCK` rather than removing them from the catalog.

  * [Keep your catalog up to date](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/upload-catalog#current).

When you record user events, the product included in the user event is connected with your current catalog. If you record an event for a product that is not in the current catalog, it cannot be used for training your models. This is called an "unjoined" event. If you recorded events before your catalog was completely imported, you must [rejoin the events](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-user-events#rejoin-event) that were recorded during the import. Having a few unjoined events is expected. However, if the percentage of unjoined events reaches 5% or more of your total user events, make sure your catalog is up to date, rejoin events that were recorded before the catalog was fully updated, and investigate why the unjoined events are being created.

You can see your unjoined events by using event filtering. [Learn more](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-user-events#filter).

  * Provide as much information with your user events as possible.

Each user event type has different information that is required and accepted. For more information, see [About user events](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/user-events).

  * [Set up Cloud Monitoring alerts](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/monitor) so that you will know if your user event recording processes experience any outages.

  * For a bulk user event import, limit the size of the data you are importing.

A bulk user event import can take up to 24 hours to complete.

The size of each file must be 2 GB or smaller. You can include at most 100 files in a single import request. One approach is import only the user events for one day at a time.

  * After a bulk import, review your [error reporting](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/error-reporting) to ensure that your data was imported correctly.

  * When importing user event data, include an accurate timestamp for each user event and avoid importing sequential user events with identical timestamps.

Provide the timestamp in the [`eventTime`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents#UserEvent.FIELDS.event_time) field in the format specified by [RFC 3339](https://tools.ietf.org/html/rfc3339).

  * If you have imported user events that are incorrect, talk to your AI Commerce Search contact about how to correct the problem.

  * When possible, keep your user event data continuous.

Gaps in user event data can reduce model quality.

  * Use a secure form of a unique identifier to keep users anonymous to AI Commerce Search and protect your users' privacy. You are responsible for redacting PII (personally identifiable information), such as email or home addresses, from your data. 




## Write user events tutorial

This tutorial shows how to record user events using the [`userEvents.write`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents/write) method.

* * *

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_write_user_events_select_language&show=ide&environment_deployment=ide)

* * *

## Record user events with a JavaScript pixel

For standard web pages (multi-page applications or MPAs), the following example records a `detail-page-view` [UserEvent](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents) using a JavaScript pixel.
    
    
      var user_event = {
        "eventType" : "detail-page-view",
        "visitorId": "visitor-id",
        "userInfo": {
            "userId": "user-id"
        },
        "experimentIds": "experiment-id",
        "productDetails": [
            {
              "product": {"id": "123"}
            }
        ]
      };
      var _gre = _gre || [];
      // Credentials for project.
      _gre.push(['apiKey', 'api-key']);
      _gre.push(['logEvent', user_event]);
      _gre.push(['projectId', 'project-id']);
      _gre.push(['locationId', 'global']);
      _gre.push(['catalogId', 'default_catalog']);
      (function() {
        var gre = document.createElement('script'); gre.type = 'text/javascript'; gre.async = true;
        gre.src = 'https://www.gstatic.com/retail/v2_event.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(gre, s);
      })();
      

If you [imported user events with Google Analytics 360](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/import-user-events#bq-ga), set `visitorID` to the Google Analytics client ID. Note that the Google Analytics client ID is only part of the full _ga cookie name (for example, client ID `123456789.123456789` is part of _ga cookie `GA1.3.123456789.123456789`).

The following is an abbreviated example that shows the format for setting the client ID in a user event. Replace "G-XXXXXX" with your [Google Analytics tracking ID](https://support.google.com/analytics/answer/9539598).
    
    
        var tracker = ga.getByName('G-XXXXXX');
        var user_event = {
              "visitorId": tracker.get('clientId')
        };
      

### Advanced example: Single-page applications and multiple events

While single-page-applications aren't officially supported with the JavaScript pixel, it is possible to send events directly. This requires calling the cloud_retail.logEvent() directly with the appropriate parameters.
    
    
    <html>
      <body>
        <p>This is a great product.</p>
        <button id="addToCartBtn">Add to Cart (Product ID: item123)</button>
    
        <script type="text/javascript">
          // Initialize the Google Retail Events array for the initial load
          var _gre = _gre || [];
    
          // --- RETAIL API CONFIGURATION ---
          const API_KEY = 'api-key';
          const PROJECT_NUMBER = 'project-number';
          const LOCATION_ID = 'global';
          const CATALOG_ID = 'default_catalog';
          const VISITOR_ID = 'visitor-id';
    
          _gre.push(['apiKey', API_KEY]);
          _gre.push(['projectId', PROJECT_NUMBER]);
          _gre.push(['locationId', LOCATION_ID]);
          _gre.push(['catalogId', CATALOG_ID]);
    
          // --- LOAD THE RETAIL EVENT TRACKING SCRIPT ---
          (function () {
            if (document.querySelector('script[src="https://www.gstatic.com/retail/v2_event.js"]')) return;
            var gre = document.createElement('script');
            gre.type = 'text/javascript';
            gre.async = true;
            gre.src = 'https://www.gstatic.com/retail/v2_event.js';
            var s = document.getElementsByTagName('script')[0];
            s.parentNode.insertBefore(gre, s);
          })();
    
          // --- SEND HOME PAGE VIEW EVENT ON LOAD ---
          document.addEventListener('DOMContentLoaded', function() {
            const homePageViewEvent = {
              "eventType": "home-page-view",
              "visitorId": VISITOR_ID,
              "eventTime": new Date().toISOString(),
              "uri": window.location.href,
              "referrerUri": document.referrer,
              "pageViewId": window.location.pathname,
              "userInfo": {
                "directUserRequest": true
              }
            };
            _gre.push(['logEvent', homePageViewEvent]);
          });
    
          // --- FUNCTION TO SEND ADD-TO-CART EVENT ---
          function sendAddToCartEvent(productId, quantity) {
            const addToCartEvent = {
              "eventType": "add-to-cart",
              "visitorId": VISITOR_ID,
              "eventTime": new Date().toISOString(),
              "uri": window.location.href,
              "userInfo": {
                "directUserRequest": true
              },
              "productDetails": [
                {
                  "product": {
                    "id": productId
                  },
                  "quantity": quantity
                }
              ]
            };
    
            if (typeof cloud_retail !== 'undefined' && cloud_retail.logEvent) {
              cloud_retail.logEvent([
                ['apiKey', API_KEY],
                ['projectId', PROJECT_NUMBER],
                ['locationId', LOCATION_ID],
                ['catalogId', CATALOG_ID],
                ['logEvent', addToCartEvent]
              ]);
            }
          }
    
          document.getElementById('addToCartBtn').addEventListener('click', function() {
            const mockProductId = 'item123';
            const mockQuantity = 1;
            sendAddToCartEvent(mockProductId, mockQuantity);
          });
        </script>
      </body>
    </html>

## Record user events with the `userEvents.write` method

You can use the [`userEvents.write`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents/write) method to send user events directly to the API from your backend server.

To record user events, send a `POST` request to the `userEvents.write` method and provide the appropriate request body.

### curl
    
    
    export GOOGLE_APPLICATION_CREDENTIALS=/tmp/my-key.json
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         --data "{
             'eventType': 'detail-page-view',
             'visitorId': 'visitor0',
             'eventTime': '2020-01-01T03:33:33.000001Z',
             'experimentIds': ['321'],
             'attributionToken': 'ABC',
             'attributes': {
                'example_text_attribute': {
                  'text': ['text_1', 'text_2']
                },
                'example_number_attribute': {
                   'numbers': [3.14, 42, 1.2345]
                }
             },
             'productDetails': [{
               'product': {
                 'id': 'abc'
               }
              }],
             'userInfo': {
               'userId': 'abc',
               'ipAddress': '8.8.8.8',
               'userAgent': 'Mozilla/5.0',
               'directUserRequest': true
             },
             'uri': 'http://example',
             'referrerUri': 'http://example',
             'pageViewId': 'currentPageUri'
    }" \
    "https://retail.googleapis.com/v2/projects/PROJECT_ID/locations/global/catalogs/default_catalog/userEvents:write"
    

### Java
    
    
    public static UserEvent writeUserEvents(UserEvent eventToWrite)
        throws IOException, InterruptedException {
      UserEventServiceClient userEventsClient = getUserEventServiceClient();
    
      WriteUserEventRequest request = WriteUserEventRequest.newBuilder()
          .setParent(DEFAULT_CATALOG_NAME)
          .setUserEvent(eventToWrite)
          .build();
    
      UserEvent writtenUserEvent = userEventsClient.writeUserEvent(request);
    
      userEventsClient.shutdownNow();
      userEventsClient.awaitTermination(2, TimeUnit.SECONDS);
    
      return writtenUserEvent;
    }

### Send real-time user events to recommendations from Android or iOS applications

There are no specific Swift or Kotlin client libraries provided in the sources for direct connection from mobile apps. However, two primary architectural approaches are recommended to send real-time user events to recommendations:

  1. **Backend proxy (Recommended)** : Set up an intermediary endpoint (like a Google Cloud function or your own backend server) to receive events from your mobile app. Then, write them to the AI Commerce Search API using the `userEvents.write` method. This procedure keeps API credentials off the mobile device.

  2. **Server-side tagging (Google Tag Manager)** : Use Google Analytics 4 (GA4) on your mobile app to stream events to a server-side Google Tag Manager container, which then forwards them to the AI Commerce Search API.




If you choose the backend proxy method, your mobile app would send data to your server. Your server would use the following code to send the event to AI Commerce Search.

## Record user events with Google Analytics 4

You can record Google Analytics 4 user event data to AI Commerce Search.

### Check your data source

Make sure that the user event data that you want to import is correctly formatted.

For a table of Google Analytics 4 fields that AI Commerce Search uses and which AI Commerce Search fields they map to, see [Google Analytics 4 user event fields](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/user-events#ga4-mapping).

For all Google Analytics event parameters, see the [Google Analytics Events reference documentation](https://developers.google.com/analytics/devguides/collection/protocol/ga4/reference/events).

Check that:

  1. If you're importing purchase events, which some AI Commerce Search models require, your event reporting includes currency codes. See the [`purchase`](https://developers.google.com/analytics/devguides/collection/protocol/ga4/reference/events#purchase) event parameters in the Google Analytics documentation.

  2. If you plan to import `search` events, your event reporting includes search queries.

Importing `search` events is supported, but `search` events don't map from Google Analytics 4 in the same way that other event types do because Google Analytics 4 doesn't natively support the AI Commerce Search `search` event type. During import, `search` events are constructed from Google Analytics 4 by combining information from the `view_item_list` and the `search_term` event parameters.

See the [`search`](https://developers.google.com/analytics/devguides/collection/protocol/ga4/reference/events#search) event parameters in the Google Analytics documentation.




### Record your Google Analytics 4 events

Record a user event by including URL-encoded raw JSON data for the event in your call to the [`userEvents.collect`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents/collect) method.

For the `prebuilt_rule` parameter, use the value `ga4_bq`.

For readability, the following example of using the `userEvents.collect` call first sets `GA4_EVENT` as a variable containing the raw JSON data for an example event. The `userEvents.collect` call in the example then URL-encodes the event data using the `GA4_EVENT` variable.

  1. For easier URL-encoding later, you can set the `GA4_EVENT` as a variable containing event data. This example shows an `add-to-cart` event.
         
         GA4_EVENT='{
           "event_timestamp": 1622994083878241,
           "event_name": "add_to_cart",
           "user_pseudo_id": "352499268.1622993559",
           "items": [
             {
               "item_id": "11",
               "price": 29.99,
               "quantity": 3
             }
           ],
           "event_params": [
             {
               "key": "currency",
               "value": {
                 "string_value": "CAD"
               }
             }
           ],
           "user_id": "Alice"
         }'

  2. Make a `userEvents.collect` call that includes the URL-encoded raw JSON data of a user event:
         
         curl \
         -G \
         --data-urlencode "raw_json=${GA4_EVENT}" \
         -i \
         "https://retail.googleapis.com/v2/projects/PROJECT_ID/locations/global/catalogs/default_catalog/userEvents:collect?key=EXAMPLEKEY1&prebuilt_rule=ga4_bq'"




## Record user events with Google Tag Manager

**Note:** Tag Manager is required for Google Analytics 4 to work on the AI Commerce Search frontend.

Tag Manager provides a way to manage and test multiple tags without many server-side code changes to your site.

Some decisions you make during setup depend on whether you are using Google Analytics and Google Analytics Ecommerce. Google Analytics Ecommerce can be implemented using Google Analytics 4 or Enhanced Ecommerce. The Cloud Retail tag supports both.

Neither Google Analytics nor Google Analytics Ecommerce is required. If you don't use them, you can either configure **Variable > Ecommerce** (for using the GA4 ecommerce schema) or **Variable > Cloud Retail** (for using the AI Commerce Search schema) when creating the Cloud Retail tag. Manually populate your site's data layer code after creating the tag.

Google Analytics Ecommerce is an additional configuration for Google Analytics that passes product titles, IDs, prices, transaction details, and other structured ecommerce data to Google Analytics. AI Commerce Search can automatically use the Google Analytics Ecommerce data layer, so if you have that set up already, configuration can be easier. If you don't have Google Analytics Ecommerce configured for Google Analytics but want to use it, see more details and setup instructions in the [GA4 developer guide](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm).

Use this one-time procedure to set up a Cloud Retail tag in Tag Manager for recording user events.

### Create a visitor ID variable

The value `visitorId` is for tracking users. `visitorId` is typically a session ID and is required for all events. Set up a variable that sets session IDs as `visitorId`.

If you're using Google Analytics, you can use the Google Analytics visitor ID. To configure this, use the following procedure to override the visitor ID value for the Cloud Retail tag. This maps the first-party cookie "_ga" to a Tag Manager variable called "GA visitorId". You can do the same for any session ID cookie; it doesn't have to be from Google Analytics.

This procedure assumes you are using Google Analytics. If you aren't, you can use another cookie or variable, or get the visitor ID from the `cloud_retail` data layer.

**Note:** Getting the `visitorID` field correct is important. It should be consistent when recording user events, importing user events, and sending prediction requests. Using inconsistent visitor IDs does not return an error, but results in an incomplete history of user events, which can degrade the quality of model personalization. 

To set the `visitorID` value to a variable for the Cloud Retail tag:

  1. In [Tag Manager](https://tagmanager.google.com/), go to the **Variables** tab and click **New** to create a new user-defined variable.

  2. Give the variable a name at the top of the dialog, such as "GA visitorId".

  3. Enter your variable settings.

You can use the client ID or the cookie ID to set as the source of visitor IDs. Always use a consistent visitor ID source when ingesting historical and real-time user events.

###  Client ID 

In Google Analytics 4, this variable maps to the `user_pseudo_id` field in the [Google Analytics 4 BigQuery export schema](https://support.google.com/firebase/answer/7029846).

     1. Set **Variable Type** to **Custom JavaScript**.

     2. Enter the following script in the **Custom JavaScript** field.

Replace "G-XXXXXX" with your [Google Analytics tracking ID](https://support.google.com/analytics/answer/9539598). To find your tracking ID, see [What happened to my Tracking ID?](https://support.google.com/analytics/answer/9539598).
            
            function() {
             var tracker = ga.getByName('G-XXXXXX');
             return tracker.get('clientID');
            }

     3. Click **Save** to save the variable.

###  Cookie ID 

     1. Choose **1st Party Cookie** as the variable type.

     2. In the **Cookie Name** field, enter **_ga**.

     3. Click **Format Value** , select **Convert undefined to..** , and enter **""** (an empty string).

     4. Click **Save** to save the variable.

This maps the first party cookie "_ga" to a Tag Manager variable called "GA visitorId".




Next, create a Cloud Retail tag in Tag Manager. This tag will use the visitor ID variable you just created.

### Create a Google Tag Manager tag

Set up a tag in Tag Manager to send user event information to AI Commerce Search.

  1. Sign in to [Tag Manager](https://tagmanager.google.com/) and select the container for your site.

  2. Go to the **Tags** tab and click **New** to add a new tag.

  3. Give your tag a name at the top of the panel (the placeholder is **Untitled Variable**), such as "AI Commerce Search".

  4. Click **Tag Configuration** and choose the **Cloud Retail** tag to open the tag configuration panel.

  5. Enter your API key.

Use the [key you created](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/setting-up#create-key) when setting up AI Commerce Search.

Your API keys are available from the **APIs & Services > Credentials** page in Google Cloud console.

  6. Enter the project number of the Google Cloud project where AI Commerce Search is enabled.

The project number is available from your Google Cloud console dashboard.

  7. For the **User Event Data Source** field:

     * **Data Layer** (recommended): Select if your implementation will be one of the following:

       * You have Google Analytics Ecommerce implemented through Tag Manager. Reuse the data layer as your events data source instead of populating a new one. This uses the Google Analytics 4 schema if present. Otherwise, it uses UA Enhanced Ecommerce. With this data source, you can only record `add-to-cart`, `purchase-complete`, `detail-page-view`, and `search` events. `search` events are recorded using ecommerce impressions combined with search queries (see Create a search query variable). 

       * You are using Google Analytics Ecommerce, and can manually populate data layer code. See the [Tag Manager Developer Guide](https://developers.google.com/tag-platform/tag-manager/datalayer).

     * **Variable > Cloud Retail**: Select to populate a Tag Manager variable with the required fields for AI Commerce Search. You might choose this option if you aren't using Google Analytics Ecommerce, or if Google Analytics Ecommerce doesn't have the data needed for AI Commerce Search. If you are switching to this source from the legacy **Data Layer > Cloud Retail** option, also create a **Data Layer > Variable** with key `cloud_retail` and associate it with this **Variable > Cloud Retail** option.

     * **Variable > Ecommerce**: Select if you aren't using Google Analytics Ecommerce in your data layer, and can't manually populate the data layer code, but still want to use the Google Analytics Ecommerce schema. This is also useful if have Google Analytics Ecommerce implemented, but want to augment or change the values in the datalayer. You can then pull those values together into a custom variable in the Google Analytics Ecommerce schema format that can be used by the Cloud Retail tag.

In the **Read Ecommerce Data from User Variable** field that appears, choose a variable. This enables AI Commerce Search to read Google Analytics Ecommerce user event data from a custom variable that you create.

The variable should match the format documented in the [GA4 Developer Guide](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm). To construct a variable in the correct format, you can use [Enhanced Ecommerce Object Builder](https://tagmanager.google.com/gallery/#/owners/gtm-templates-simo-ahava/templates/enhanced-ecommerce-object-builder), a [custom variable template](https://developers.google.com/tag-platform/tag-manager/templates/) from the [Tag Manager community template gallery](https://tagmanager.google.com/gallery). Community templates are not maintained by Google. To use this template, see the Enhanced Ecommerce Object Builder gallery page for documentation and other resources.

  8. Click the **\+ Overwrite a value on the UserEvent message** button.

  9. For **Field Selector** , select `visitorId` as the field, and for **Field Value** , select the new visitor ID variable you created in Create a visitor ID variable.

  10. Click **Save**.

Your Cloud Retail tag is created.




#### Legacy data source options

Previously, **Data Layer > Ecommerce** and **Data Layer > Cloud Retail** were available as data source options. These legacy options aren't available in new tags. If you switch an existing tag to a new data source, preview it with Tag Manager to verify it before deployment. When switching:

  * If you used **Data Layer > Ecommerce**, you can switch to **Data Layer**. This uses the Google Analytics 4 schema if present. Otherwise, it uses UA Enhanced Ecommerce.

  * If you used **Data Layer > Cloud Retail**, switch to option **Variable > Cloud Retail**. Create a **Data Layer > Variable** with key `cloud_retail` and associate it with the **Variable > Cloud Retail** option.




Next:

  * If you're using search, create a variable for search queries and attach it to your new tag.
  * Create event triggers for your tag.



### Create a search query variable

If you're using search, you can create a variable in Tag Manager for search queries and attach it to your Cloud Retail tag. This allows AI Commerce Search to get search queries from Analytics.

The types of variables you create depend on your user event data source.

  * **Variable > Ecommerce**, or the data layer with the Google Analytics Ecommerce schema: Create a URL or DOM element variable in Tag Manager and attach it to your Cloud Retail tag. In addition, enable the option for your tag to use Google Analytics Ecommerce impressions to construct search events.
  * **Variable > Cloud Retail**, or a manually populated data layer: Create a URL or DOM element variable in Tag Manager and attach it to your Cloud Retail tag. In order to determine if a user event's type is `search`, you must also either: 
    * Create a constant type variable for the search event types and attach it to your tag.
    * Set the search event type in your data layer or Cloud Retail variable.



#### Create and attach a Tag Manager variable for search queries

If you use search, you can create a URL, DOM element, or custom JavaScript variable that will be populated with search queries entered on your site.

As an alternative to this procedure, you can configure the data layer to provide search query information. However, you might choose to use Tag Manager variables if you don't have access to the data layer, or prefer not to configure the data layer.

You can create a URL type variable, a DOM element type variable, or a custom JavaScript (page) variable. Which one you create and how you configure it, depends on your site's implementation:

  * A **URL variable** gets search queries from your site's search result URLs. Use this variable if your site includes the query string in the URL of its search results.
  * A **DOM element** variable gets the search query information from your site's Document Object Model (DOM). You don't need to edit the DOM to use this variable. However, you should be able to read and understand the DOM to configure this variable correctly.
  * A **Custom JavaScript** variable returns data formatted by a JavaScript function. This is useful if you have existing data that you want to format in the Cloud Retail or Ecommerce schema.



First, create a Tag Manager variable of type URL, DOM element, or Custom JavaScript:

  1. In [Tag Manager](https://tagmanager.google.com/), go to the **Variables** tab and click **New** to create a new user-defined variable.

  2. Give the variable a name at the top of the dialog, such as "search_variable".

  3. Enter your variable settings:

###  URL type 

     1. Set **Variable Type** to **URL**.

     2. Set **Component Type** to **Query**.

     3. If you specify a query key, set it to the key that precedes the search query in your URL.

For example, if the URL is `http://example.com/?q=shoes`, the query key is `q`. In this example, the variable's value would get set to `shoes`.

###  DOM element type 

     1. Set **Variable Type** to **DOM Element**.

     2. Set **Selection Method** and enter the search query's element ID or element selector.

This setting depends on whether your site uses an element ID or a CSS selector to identify the search query.

     3. If you specify an attribute, set it to the attribute that contains the search query term.

For example, if the search query in your DOM is `<id="search" value="shoes">`, the attribute would be `value`. In this example, your variable's value would be set to `shoes`.

###  Custom JavaScript type 

     1. Set **Variable Type** to **Custom JavaScript**.

     2. Replace the variables in the following code and paste it into the Custom JavaScript pane.

     3. In the Custom JavaScript pane, add JavaScript code that returns a search event in the [Retail Schema](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents).

The following sample code transforms data in an existing `Ecommerce Items` variable into the [productDetails array](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents#UserEvent.FIELDS.product_details) used by the AI Commerce Search schema and returns a complete event. To use this code, replace `Ecommerce Items`, `Search Query`, and `Search Filter` with variables in your Tag Manager implementation.
            
            function () {
            
              var retail;
              var items = [];
            
              for (var i = 0; i < {{Ecommerce Items}}.length; i++) {
                var item = {'product':
                            {
                              'id': {{Ecommerce Items}}[i].item_id
                            }
                           };
            
                items.push(item);
              }
            
              retail = {
                'eventType': 'search',
                'searchQuery': '{{Search Query}}',
                'filter': '{{Search Filter}}',
                'productDetails': items
              }
            
              return retail;
            }
            

  4. Click **Save** to save the variable.




Next, attach the variable to your Cloud Retail tag:

  1. On the [Tag Manager](https://tagmanager.google.com/), **Tags** page, click your Cloud Retail tag to edit it.

  2. If your tag's user event data source is **Variable > Ecommerce** or you use the data layer with Google Analytics Ecommerce schema, select the checkbox **Use enhanced ecommerce impressions to construct search events**.

This allows AI Commerce Search to determine if a user event's type is `search` based on search data it gets from this tag.

  3. In the **User Events Data** section, click the **\+ Overwrite a value on the UserEvent message** button.

  4. Select `searchQuery` from **Field Selector** and set your search query variable as the **Field Value**.

  5. Save your tag.




Next:

  * If you chose use a Cloud Retail variable or a manually populated data layer as the user event source for your Cloud Retail tag, see Create and attach a constant variable.
  * Create event triggers for your tag.



#### Create and attach a constant variable

You can use this procedure if you chose **Variable > Cloud Retail** or a manually populated data layer as the user event source for your Cloud Retail tag.

Creating a constant type variable for search events and setting it as a user event override on your Cloud Retail tag allows AI Commerce Search to determine if a user event's type is `search`.

As an alternative to this procedure, you can specify the `search` user event type using the data layer or Cloud Retail variable that serves as your tag's event source. Otherwise, use the following steps to set the event type.

First, create a constant type variable:

  1. In [Tag Manager](https://tagmanager.google.com/), go to the **Variables** tab and click **New** to create a new user-defined variable.

  2. Give the variable a name at the top of the dialog, such as "search_constant".

  3. Set **Variable Type** to **Constant**.

  4. Enter `search` in the **Value** field

  5. Click **Save** to save the variable.




Next, attach the variable to your Cloud Retail tag:

  1. On the [Tag Manager](https://tagmanager.google.com/), **Tags** page, click your Cloud Retail tag to edit it.

  2. In the **User Events Data** section, click the **\+ Overwrite a value on the UserEvent message** button.

  3. Select `eventType` from **Field Selector** and set your search query variable as the **Field Value**.

  4. Save your tag.




Next, create event triggers for your tag.

### Create event triggers for your Tag Manager tag

Create triggers for all user event types your AI Commerce Search models will use.

Tag Manager tags must have triggers that control when the tag should be "fired" on the site. Triggers listen for when events occur (such as a user viewing the home page or adding an item to their cart) and prompts your tag to send that user event information to AI Commerce Search.

Tag Manager provides some standard triggers. For example, **Window Loaded** is a trigger for `detail-page-view` events. For details about each type, see [Trigger types](https://support.google.com/tagmanager/topic/7679108) in the Tag Manager documentation.

You'll usually set the tag to trigger when a user views any page that has the events needed for AI Commerce Search (such as the home page, product detail pages, cart pages, or checkout complete page). In these cases, the tag should fire after the page has loaded, so that cookies are available and all data layer variables are populated. To accomplish this, set your triggers to fire on **Window Loaded** or **DOM Ready**.

You might need to fire the tag when an action is performed rather than at page load (such as if a user adding an item to a cart doesn't force a page to reload). In these cases, you can configure that click action on your site to simultaneously push updates to the data layer and associate the trigger with that action.

For example, if you created a trigger for `add-to-cart` events, you could choose the trigger type to **Click > Just Links** and set it to fire on the click ID (in this example, `addtocart`). You would then configure the `addtocart` link on your site to also update the data layer with new values when clicked:
    
    
        <a id="addtocart" href="javascript:void(0);"
              onclick="dataLayer.push({
                        'cloud_retail': {
                        'eventType': 'add-to-cart',
                        'visitorId': '456',
                        'cartId': 'mobile',
                        'productDetails': [{
                        'product': {
                        'id': '54321'
                        },
                        'quantity': 1
                        }]}});">Add to Cart</a>
      
      

For some user events, you must create a custom trigger. Generally, you create a custom trigger in Tag Manager using the user event name. If you can't modify your frontend code, you can create a custom trigger using JavaScript macros. For more information about custom triggers, see [Custom event trigger](https://support.google.com/tagmanager/answer/7679219).

Use the following procedures to create triggers in Tag Manager:

  * **If you don't have existing triggers configured** : Create new triggers for your Tag Manager tag
  * **If you've already set up Google Analytics Ecommerce triggers** : You can reuse the triggers you configured for Google Analytics Ecommerce instead of creating new ones. See Reuse Google Analytics Ecommerce triggers.



#### Create new triggers for your Tag Manager tag

If you don't use Google Analytics Ecommerce, create new event triggers for any user events your AI Commerce Search models need. Then, associate your new triggers with the Cloud Retail tag you created in Tag Manager.

Before you start the following steps, make sure you have created a Cloud Retail tag in Tag Manager. See Create a Tag Manager tag.

First, create the triggers. Repeat this procedure for all user events your AI Commerce Search models require:

  1. On the [Tag Manager](https://tagmanager.google.com/), **Triggers** page, click **New > Trigger Configuration**.

  2. Choose the [trigger type](https://support.google.com/tagmanager/topic/7679108) that applies to the user event you're creating a trigger for.

  3. Save your trigger.




Next, associate your new triggers with your Cloud Retail tag. This is a one-time procedure:

  1. On the [Tag Manager](https://tagmanager.google.com/), **Tags** page, click your Cloud Retail tag to edit it.

  2. Click **Triggering** , select your new triggers, and click **Add**.

  3. Save your tag.




Next, preview your tag, and [set up monitoring of event recording errors](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/monitor) and other issues to make sure that data continues to be received successfully.

If you're using `cloud_retail` data layer as your user event source, make sure to also set up your data layer.

#### Reuse Google Analytics Ecommerce triggers

If you have implemented Google Analytics Ecommerce using Tag Manager, reuse event triggers from your Google Analytics Ecommerce for AI Commerce Search.

With this data source, you can only record `add-to-cart`, `purchase-complete`, `detail-page-view`, and `search` events. `search` events are recorded using ecommerce impressions combined with search queries (see Create a search query variable). 

The following table shows how Google Analytics Ecommerce and Enhanced Ecommerce events map to AI Commerce Search events.

Google Analytics 4 | Enhanced Ecommerce  | AI Commerce Search  
---|---|---  
`add_to_cart` | `add` | `add-to-cart`  
`purchase` | `purchase` | `purchase-complete`  
`view_item` | `detail` | `detail-page-view`  
`view_item_list` or `view_search_results` | `impressions` | `search` (if combined with field `searchQuery`)  
  
Before you start these steps, make sure you have first:

  * Set up a tag in Tag Manager of tag type **Google Analytics (GA4) Event** , and enabled Enhanced Ecommerce or GA4 on it. See [the Tag Manager documentation](https://support.google.com/tagmanager/answer/6107169#enhanced-ecommerce), and the [GA4 Developer Guide](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm) for details.
  * Configured your Enhanced Ecommerce or GA4 tag in Tag Manager to trigger on the user events you plan to record for AI Commerce Search.
  * Created a Cloud Retail tag in Tag Manager, with **Data Layer** or **Variable > Ecommerce** as the user event data source (see Create a Tag Manager tag.



To reuse Google Analytics Ecommerce triggers:

  1. On the [Tag Manager](https://tagmanager.google.com/), **Tags** page, click your Google Analytics Ecommerce tag by typing **Google Analytics (GA4) Event** to edit it.

  2. Under **Advanced Settings > Tag Sequencing**, select **Fire a tag after <_Enhanced Ecommerce or GA4 tag name_ > fires**. 

  3. Select your Cloud Retail tag as the **Cleanup Tag**.

Select **Don't fire <_Cloud Retail tag name_ > if <_Enhanced Ecommerce or GA4 tag name_ > fails or is paused**.

  4. Save your tag.




Next, preview your tag, and [set up monitoring of event recording errors](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/monitor) and other issues to make sure that data continues to be received successfully.

If you're using `cloud_retail` data layer as your user event source, make sure to also set up your data layer.

### Use the `cloud_retail` data layer with Tag Manager

If you created your Cloud Retail tag in Tag Manager to use the `cloud_retail` data layer as the user event source, set up the `dataLayer` variable in your source HTML as described in the [Tag Manager Developer Guide](https://developers.google.com/tag-platform/tag-manager/datalayer).

#### About the data layer

Most Tag Manager tags require data that changes depending on the user or the page (such as user IDs or product IDs). For the Cloud Retail tag, that data must be exposed in a structured way using a data layer so that Tag Manager can use it.

The data layer is a JavaScript object that is typically added to a page using server-side code or, in the frontend, using HTML or a template. If a page is configured with the data layer, it will contain some code like the following:
    
    
      dataLayer = dataLayer || [];
      dataLayer.push({
        'cloud_retail': {
          'eventType': 'home-page-view',
          'visitorId': 'visitor_a',
          'userInfo': {
            'userId': '789'
          },
        }
      });
      

This code creates a `dataLayer` object and assigns the `cloud_retail` structure to it as an array element.

#### Required fields in the `cloud_retail` data layer

[About user events](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/user-events) lists all required fields and examples for event types that should be passed to the `cloud_retail` data layer.

Your server-side code or templates should have the correct script tags on each page that you want to send events from. After the `dataLayer` object is populated correctly on each page, you should be able to test the Cloud Retail tag.

Some fields like `visitorId` are required for the [`UserEvent`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents) message, but might not be available when populating the data layer. For example, `visitorId` might be derived from the user's cookie, or `experimentIds` from the A/B experimentation framework. In this case, use a variable to overwrite the field on the Tag Manager tag.

You can overwrite the following fields:

  * `visitorId`
  * `userInfo.userId`
  * `attributionToken`
  * `experimentIds`



For how to overwrite a `UserEvent` field in Tag Manager, see Setting the `visitorID` field in Tag Manager, which walks through overwriting the `visitorId` field value with a user-defined variable.

**Note:** Getting the `visitorID` field correct is important. It should be consistent when recording user events, importing user events, and sending prediction requests. Using inconsistent visitor IDs does not return an error, but results in an incomplete history of user events, which can degrade the quality of model personalization. 

The following example shows the data layer that needs to be included in your page for a `detail-page-view` [UserEvent](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents) using Tag Manager:
    
    
        dataLayer = dataLayer || [];
        dataLayer.push({
          'cloud_retail': {
            'eventType' : 'detail-page-view',
            'visitorId': 'visitor_a',
            'userInfo': {
                // The user and visitor ID fields can typically be
                // be populated from a client-side JavaScript
                // variable such as a cookie. If you set the user
                // and/or visitor ID values from the server,
                // populate the userID.
                'userId': 'user_a'
            },
            // In most cases, the experiment ID field is populated from a
            // client side JavaScript variable as defined by the experiment
            // manager.
            // If you set the experiment ID value from the server,
            // populate the experimentIds field here.
            'productDetails': [
                  {
                    'product': {'id': '123'}
                  }
            ],
          // You can use the 'cloud_retail' data layer element along with other
          // data layer elements.
          'ecommerce': {
            ...
          },
        }];
      

### Preview your Tag Manager tag

Tag Manager's preview mode lets you test new tags before publishing them to your live site.

For more details about preview mode, see the Tag Manager documentation for [preview mode](https://support.google.com/tagmanager/answer/6107056).

Use the following procedure to confirm that your tag is firing correctly.

  1. On the Tag Manager overview page, click **Preview**.

Tag Manager preview mode opens in a new browser tab.

  2. Enter your site information and click **Start** to start Tag Assistant.

In the current browser tab, Tag Assistant starts, and your site opens in a new tab.

  3. On your site, visit any page where the Cloud Retail tag should be triggered.

  4. Confirm that the Tag Assistant lists the Cloud Retail tag in the **Tags** tab under the **Tags Fired** section.

  5. In the Tag Assistant, go to the **Data Layer** tab and check that the correct values from the `cloud_retail` or ecommerce data layer are displayed.




#### Check for tag errors

If some fields are incorrect or missing when you preview your tag, the tag typically also returns an error, unless it isn't firing at all.

You can check the [**Monitoring**](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/monitoring/) page in the AI Commerce Search in Gemini Enterprise for Customer Experience console for errors. This page logs most errors except for syntax errors, which typically only appear in request results.

You can use the following steps to use Chrome DevTools to check for any errors generated, including syntax errors.

  1. Turn on preview mode in Tag Manager for your site in a Chrome browser and visit any page where the Cloud Retail tag should be triggered.

  2. With preview mode open, open DevTools and click the **Network** tab.

  3. Reload the page.

  4. In DevTools, search for `userEvent`.

The Network tab displays the `userEvent:collect` event and its status code.

     * A `200` response indicates your tag is in a good state.
     * Other responses, such as a `400` error and highlighting the event in red, indicate that debugging is necessary.
  5. Double-click the event name to execute the request and show a full response with more error information.

For example, you might see a `400` error containing the message, "'visitorId' is required, and cannot be empty", indicating that `visitorId` was not set correctly.

  6. If no `userEvent` is fired, check the DevTools **Console** tab for syntax errors in the data layer.




## Record user events with server-side tagging

Server-side tagging lets you deploy a single server-side container with many downstream clients. This creates a single source of truth on the client side, with many server-side consumers. This architecture shifts the load off the web and into the server, making it desirable for users who want to maximize performance of their websites.

The other advantage of server-side tagging is that a single server-side tag can also support many upstream clients—for example, both web and mobile. Learn how to [set up server-side tagging](https://developers.google.com/tag-platform/learn/sst-fundamentals).

AI Commerce Search provides its own legacy server-side tag.

The Cloud Retail server-side tag requires and accepts similar parameters as the Cloud Retail web tag, such as:

  * Project number
  * API key (for authentication)
  * Overrides for key fields like `visitorId` and `searchQuery`



The key difference between the server version and the web version of the Cloud Retail tag is that you cannot define the data source. The data source for server tags is a data stream sent from the Google tag in the GA4 schema.

[Set up the Cloud Retail tag](https://developers.google.com/tag-platform/tag-manager/server-side/cloud-retail-setup)

## View recorded events

View event integration metrics in the **Events** tab on the AI Commerce Search in Gemini Enterprise for Customer Experience console **Data** page. This page shows all events written or imported in last year. Metrics can take up to 24 hours to appear after successful data ingestion. 

[Go to the Data page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/data/)

## What's next

  * Learn more about [user events](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/user-events).
  * You can also import historical user events. It can take a considerable amount of time to record sufficient user event data to train your models. You can accelerate initial model training by importing user event data from past events in bulk. See [Import historical user events](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/import-user-events).
  * [Rejoin events](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-user-events#rejoin-event) if they were recorded before catalog import was completed.
  * Learn about [importing and managing user events](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-user-events).
  * [Start getting predictions](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/predict).
  * [Monitor](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/monitor) and [troubleshoot](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/error-reporting) your data upload processes.
  * Learn more about [Tag Manager](https://support.google.com/ads-help/answer/4626391).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
