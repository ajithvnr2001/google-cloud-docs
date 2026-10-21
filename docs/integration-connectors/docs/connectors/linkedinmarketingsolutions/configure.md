---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedinmarketingsolutions/configure/
title: LinkedIn Marketing Solutions \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:41:23.211764+00:00
---

# LinkedIn Marketing Solutions  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedinmarketingsolutions/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# LinkedIn Marketing Solutions

The LinkedIn Marketing Solutions connector lets you perform insert, update, delete, and read operations on the LinkedIn data.

## Supported versions

This connector supports LinkedIn REST APIs.

## Before you begin

In your Google Cloud project, do the following tasks:

  * Ensure that network connectivity is set up. For information about network patterns, see [Network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private).
  * Grant the [roles/connectors.admin](https://docs.cloud.google.com/integration-connectors/docs/connectors-access-permissions#iam-roles-for-integration-connectors) IAM role to the user configuring the connector.
  * Grant the `roles/secretmanager.viewer` and `roles/secretmanager.secretAccessor` IAM roles to the [service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating) that you want to use for the connector. 
  * Enable the following services: 
    * `secretmanager.googleapis.com` (Secret Manager API)
    * `connectors.googleapis.com` (Connectors API)

To understand how to enable services, see [Enabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling). If these services or permissions have not been enabled for your project previously, you are prompted to enable them when you configure the connector.




## Configure the connector

A connection is specific to a data source. It means that if you have many data sources, you must create a separate connection for each data source. To create a connection, do the following:

  1. In the [Cloud console](https://console.cloud.google.com), go to the **Integration Connectors > Connections** page and then select or create a Google Cloud project. 

[ Go to the Connections page ](https://console.cloud.google.com/connectors/connections)

  2. Click **\+ CREATE NEW** to open the **Create Connection** page.
  3. In the **Location** section, choose the location for the connection. 
     1. **Region** : Select a location from the list. 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

     2. Click **NEXT**.
  4. In the **Connection Details** section, complete the following: 
     1. **Connector** : Select **LinkedIn Marketing Solutions** from the list of available connectors.
     2. **Connector version** : Select the connector version from the list of available versions. 
     3. In the **Connection Name** field, enter a name for the connection instance. The connection name can contain lowercase letters, numbers, or hyphens. The name must begin with a letter and end with a letter or number and the name must not exceed 49 characters.
     4. **Description** : Enter a description for the connection instance.
     5. Optionally, enable [Cloud logging](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs), and then select a log level. By default, the log level is set to `Error`. 
     6. **Service Account** : Select a service account that has the required roles.
     7. Optionally, configure the **Connection node settings** : 

        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
     8. **\+ ADD LABEL** : Click this to add a label to the connection in the form of a key-value pair.
     9. Click **NEXT**.
     10. In the **Authentication** section, enter the authentication details. 
        1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the LinkedIn Marketing Solutions connection:

           * OAuth 2.0 - client credentials

To understand how to configure these authentication types, see Configure authentication.

        2. Click **NEXT**.
     11. **Review** : Review your connection and authentication details.
     12. Click **Create**.

### Configure authentication

Enter the details based on the authentication you want to use.

     * **OAuth 2.0 - client credentials**
       * **Client ID** : Enter the client ID to use for the connection.
       * **Scopes** : Enter the scopes to use for the connection.
       * **Client Secret** : Enter the secret manager secret containing the client secret.
       * **Secret version** : Select the secret version for the client secret.
       * **Authorization URL** : Enter the authorization URL.
       * **Enable Authentication Override** : Select this to enable override authentication.

## Connection configuration samples

This section lists the sample values for the various fields that you configure when creating the connection.

### OAuth 2.0 - client credentials connection type

Field name | Details  
---|---  
Location | us-central1  
Connector | LinkedIn Marketing Solutions  
Connector version | 1  
Connection Name | linkedin-ads-connection  
Enable Cloud Logging | true  
Service Account | 123456789012-compute@developer.gserviceaccount.com  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Authentication | OAuth 2.0 - client credentials  
Client ID | 78xuvoqkfeoj5n  
Scopes | openid, profile, rw_organization_admin, w_member_social, rw_events, w_organization_social, rw_ads, r_basicprofile, email, r_1st_connections_size  
Client Secret | projects/secrets/new-client-secret  
Secret version | 1  
Authorization URL | https://www.linkedin.com/oauth/v2/authorization  
  
## System limitations

The LinkedIn Marketing Solutions connector can process a maximum of 14 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 
     * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
     * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).

The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Use the LinkedIn Marketing Solutions connection in an integration

After you create the connection, it becomes available in both Apigee Integration and Application Integration. You can use the connection in an integration through the Connectors task.

     * To understand how to create and use the Connectors task in Apigee Integration, see [Connectors task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#configure-the-connectors-task).
     * To understand how to create and use the Connectors task in Application Integration, see [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task).

## Entity operation examples

This section shows how to perform some of the [entity operations](https://docs.cloud.google.com/integration-connectors/docs/entities-operation-action) in this connector.

### Example - List all the accounts

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select `Accounts` from the `Entity` list.
     3. Select the `List` operation, and then click **Done**.
     4. In the **Task Input** section of the **Connectors** task, you can set the **filterClause** as per your filtering requirements.

You must use single quotes (') to enclose the value for filterClause. You can use the filterClause to filter records based on the columns.

### Example - Get account details

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select `Accounts` from the `Entity` list.
     3. Select the `Get` operation, and then click **Done**.
     4. Set the **entityId** to `Id="514824232"` which is the key to be passed.
     5. To set the **entityId** in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `Id="514824232"` in the **Input Value** field and set the **entityId** as local variable.

If passing an **entityId** throws an error due to composite primary keys, you can use the **filterClause** , such as `Id='514824232'`.

### Example - Create a user account

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select `AccountUsers` from the `Entity` list.
     3. Select the `Create` operation, and then click **Done**.
     4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and set the `connectorInputPayload` as local variable. 
            
            {
              "AccountURN": "urn:li:sponsoredAccount:515414784",
              "UserURN": "urn:li:person:jjWUdOLL5W",
              "Role": "VIEWER"
            }
            

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
            
            { }
            

### Example - Create a campaign group

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select `CampaignGroups` from the `Entity` list.
     3. Select the `Create` operation, and then click **Done**.
     4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and set the `connectorInputPayload` as local variable. 
            
            {
              "Account": "urn:li:sponsoredAccount:514824232",
              "ScheduleStartTime": "2025-09-04 17:13:52",
              "ScheduleEndTime": "2025-11-21 14:49:13",
              "Status": "ACTIVE",
              "TotalBudgetAmount": 60000,
              "TotalBudgetCurrencyCode": "USD",
              "AdAccountId": "514824232",
              "Name": "campaigngroups1758517846396"
            }
            

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
            
            {
              "Id": "776885434"
            }

### Example - Create a campaign

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select `Campaigns` from the `Entity` list.
     3. Select the `Create` operation, and then click **Done**.
     4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and set the `connectorInputPayload` as local variable. 
            
            {
              "Name": "Updated Campaign",
              "Account": "urn:li:sponsoredAccount:514824232",
              "CampaignGroup": "urn:li:sponsoredCampaignGroup:752369254",
              "DailyBudgetAmount": "5667",
              "Country": "US",
              "Language": "en",
              "OffsiteDeliveryEnabled": false,
              "ScheduleStartTime": "2025-09-04 17:13:52",
              "Status": "ACTIVE",
              "Type": "SPONSORED_UPDATES",
              "UnitCostAmount": "3.50",
              "UnitCostCurrency": "USD",
              "AdAccountId": "514824232",
              "DailyBudgetCurrency": "USD"
            }
            

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
            
            {
              "Id": "416012984"
            }

### Example - Create a creative

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select `Creatives` from the `Entity` list.
     3. Select the `Create` operation, and then click **Done**.
     4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and set the `connectorInputPayload` as local variable. 
            
            {
              "Campaign": "urn:li:sponsoredCampaign:382923024",
              "Content": "{    \"reference\": \"urn:li:share:7331580382389149698\"  }",
              "IntendedStatus": "DRAFT",
              "AdAccountId": "514824232",
              "Name": "Conversation creative"
            }
            

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
            
            {
              "Id": "urn:li:sponsoredCreative:776547754"
            }

### Example - Create a form

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select `Forms` from the `Entity` list.
     3. Select the `Create` operation, and then click **Done**.
     4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and set the `connectorInputPayload` as local variable. 
            
            {
              "Account": "urn:li:sponsoredAccount:514824232",
              "Description": "This is a sample form used for collecting leads",
              "Headline": "Join our newsletter!",
              "Name": "Sample Form Name",
              "Questions": "[\n\n  {\n\n    \"question\": {\n\n      \"localized\": {\n\n        \"en_US\": \"First Name\"\n\n      }\n\n    },\n\n    \"name\": \"firstName\",\n\n    \"questionDetails\": {\n\n      \"textQuestionDetails\": {}\n\n    },\n\n    \"predefinedField\": \"FIRST_NAME\"\n\n  },\n\n  {\n\n    \"question\": {\n\n      \"localized\": {\n\n        \"en_US\": \"Last Name\"\n\n      }\n\n    },\n\n    \"name\": \"lastName\",\n\n    \"questionDetails\": {\n\n      \"textQuestionDetails\": {}\n\n    },\n\n    \"predefinedField\": \"LAST_NAME\"\n\n  }\n\n]",
              "Message": "This is a sample message.",
              "Country": "us",
              "Language": "EN",
              "Status": "ARCHIVED",
              "LegalDisclaimer": "This is a legal disclaimer which is mandatory",
              "LandingPage": "https://altostrat.com/thank-you"
            }
            

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
            
            {
              "Id": "1000154089"
            }
            

### Example - Create a message creative

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select `MessageCreatives` from the `Entity` list.
     3. Select the `Create` operation, and then click **Done**.
     4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and set the `connectorInputPayload` as local variable. 
            
            {
              "Name": "New Message Creative",
              "Subject": "Message creative",
              "BodyContent": "Message advertisement",
              "SubContent": "{\"regular\":{\"rightRailAdPicture\":\"urn:li:image:C5F22AQFIMShx0jJbQw\",\"callToActionLandingPageUrl\":\"http://www.linkedin.com\",\"callToActionText\":\"sample string\"}}",
              "SenderURN": "urn:li:person:6fmYVhh9wx",
              "AccountURN": "urn:li:sponsoredAccount:514824232"
            }
            

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
            
            {
              "URN": "urn:li:adInMailContent:144290084"
            }

### Example - Create a publisher restriction file

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select `PublisherRestrictionFiles` from the `Entity` list.
     3. Select the `Create` operation, and then click **Done**.
     4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and set the `connectorInputPayload` as local variable. 
            
            {
              "Id": "1",
              "Creative": "urn:li:sponsoredCreative:668131684",
              "Account": "urn:li:sponsoredAccount:514824232",
              "Event": "IMPRESSION",
              "Platform": "DOUBLECLICK",
              "TrackingUrl": "https://ad.doubleclick.net/ddm/trackimp/N123456.123LINKEDIN/B12345678.123456789;dc_trk_aid=123456789;dc_trk_cid=987654321;ord=%%CACHEBUSTER%%;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=?"
            }
            

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
            
            {
              "Id": "52164006"
            }

### Example - Create an image

     1. In the `Configure connector task` dialog, click `Action`.
     2. Select `Uploadimage` from the `Action` list.
     3. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and set the `connectorInputPayload` as local variable. 
            
            {
              "FileData": "/9j/4AAQSkZJ",
              "AccountURN": "urn:li:sponsoredAccount:514824232",
              "OwnerURN": "urn:li:organization:106639229",
              "AssetName": "New Image"
            }
            

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
            
            [
              {
                "ImageURN": "urn:li:image:D4E10AQHeZAiDW6657A"
              }
            ]
            

### Example - Create a video

     1. In the `Configure connector task` dialog, click `Action`.
     2. Select `UploadVideo` from the `Action` list.
     3. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and set the `connectorInputPayload` as local variable. 
            
            {
              "OwnerURN": "urn:li:organization:106639229",
              "AccountURN": "urn:li:sponsoredAccount:514824232",
              "FileData": "AAAAIGZ0eXBpc29tAAA",
              "AssetName": "Pink Bird",
              "HasThumbnail": true
            }
            

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
            
            [
              {
                "VideoURN": "urn:li:video:D4E10AQHYb2Oez5t1mg",
                "CaptionsUploadURL": null,
                "ThumbnailUploadURL": "https://www.linkedin.com/dms-uploads/sp/v2/D4E10AQHYb2Oez5t1mg/ads-video-userUploadedThumbnail/D4E01AQHTY8R0IkYdHA/0?ca=vector_ads&cn=uploads_secure&ccn=ambry-video&iri=B01-78&sync=0&v=beta&ut=2E4HdFnCb3Cs01"
              }
            ]
            

### Example - Create a document

     1. In the `Configure connector task` dialog, click `Action`.
     2. Select `UploadDocument` from the `Action` list.
     3. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and set the `connectorInputPayload` as local variable. 
            
            {
              "OwnerURN": "urn:li:organization:106639229",
              "FileData": "JVBERi0xLjQKJcOkw7zDtsOfCjIgM"
            }
            

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
            
            [
              {
                "DocumentURN": "urn:li:document:D4E10AQEZDx05fFC1hA"
              }
            ]
            

### Example - Create a multi image post

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select `CompanyStatusUpdates` from the `Entity` list.
     3. Select the `Create` operation, and then click **Done**.
     4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and set the `connectorInputPayload` as local variable. 
            
            {
              "Comment": "MultiImage 1",
              "CreatedBy": "urn:li:organization:106639229",
              "Visibility": "PUBLIC",
              "LifecycleState": "PUBLISHED",
              "IsReshareDisabled": false,
              "Content": "{\n        \"multiImage\": {\n            \"images\": [\n                {\n                    \"id\": \"urn:li:image:D4E10AQG8WCH_KRHhMw\",\n                    \"altText\": \"testing for alt tags1\"\n                },\n                {\n                    \"id\": \"urn:li:image:D4E10AQHeZAiDW6657A\",\n                    \"altText\": \"testing for alt tags2\"\n                }\n            ]\n        }\n    }"
            }
            

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
            
            {
              "Id": "urn:li:ugcPost:7399721854405484544"
            }

### Example - Create a poll post

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select `CompanyStatusUpdates` from the `Entity` list.
     3. Select the `Create` operation, and then click **Done**.
     4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and set the `connectorInputPayload` as local variable. 
            
            {
              "Comment": "Test Post",
              "CreatedBy": "urn:li:organization:108472058",
              "Visibility": "PUBLIC",
              "LifecycleState": "PUBLISHED",
              "IsReshareDisabled": false,
              "Content": "{\n     \"poll\": {\n       \"question\" :\"What is your favorite color?\",\n       \"options\" : [ { \"text\" : \"Red\" }, { \"text\" : \"Blue\" }, {\"text\": \"Yellow\"}, {\"text\": \"green\"} ],\n       \"settings\" : { \"duration\" : \"THREE_DAYS\" }\n     }\n }"
            }
            

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
            
            {
              "Id": "urn:li:ugcPost:7399410172072357888"
            }

### Example - Create a post

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select `Posts` from the `Entity` list.
     3. Select the `Create` operation, and then click **Done**.
     4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and set the `connectorInputPayload` as local variable. 
            
            {
              "Author": "urn:li:organization:106639229",
              "Commentary": "Image Post",
              "Visibility": "PUBLIC",
              "FeedDistribution": "MAIN_FEED",
              "LifecycleState": "PUBLISHED",
              "IsReshareDisabledByAuthor": false,
              "Content": "{\n    \"media\": {\n      \"title\":\"title of the video\",\n      \"id\": \"urn:li:image:D4E10AQHeZAiDW6657A\"\n    }\n  }"
            }
            

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
            
            {
              "Id": "urn:li:share:7397570971332669440"
            }
            

### Example - Create a audience templates

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select `SavedAudienceTemplates` from the `Entity` list.
     3. Select the `Create` operation, and then click **Done**.
     4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and set the `connectorInputPayload` as local variable. 
            
            {
              "AccountURN": "urn:li:sponsoredAccount:514824232",
              "Name": "Saved Template 1",
              "TargetingCriteria": "{\n  \"include\": {\n    \"and\": [\n      {\n        \"or\": {\n          \"urn:li:adTargetingFacet:locations\": [\n            \"urn:li:geo:90000034\",\n            \"urn:li:geo:104079912\"\n          ]\n        }\n      },\n      {\n        \"or\": {\n          \"urn:li:adTargetingFacet:titles\": [\n            \"urn:li:title:1\",\n            \"urn:li:title:107\"\n          ]\n        }\n      }\n    ]\n  },\n  \"exclude\": {\n    \"or\": {\n      \"urn:li:adTargetingFacet:degrees\": [\n        \"urn:li:degree:1000\",\n        \"urn:li:degree:1100\"\n      ]\n    }\n  }\n}"
            }
            

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
            
            {
              "Id": "42831292"
            }
            

### Example - Create a saved audience template

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select `SavedAudienceTemplates` from the `Entity` list.
     3. Select the `Create` operation, and then click **Done**.
     4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
            
            {
              "AccountURN": "urn:li:sponsoredAccount:514824232",
              "Name": "Saved Template 1",
              "TargetingCriteria": "{\n  \"include\": {\n    \"and\": [\n      {\n        \"or\": {\n          \"urn:li:adTargetingFacet:locations\": [\n            \"urn:li:geo:90000034\",\n            \"urn:li:geo:104079912\"\n          ]\n        }\n      },\n      {\n        \"or\": {\n          \"urn:li:adTargetingFacet:titles\": [\n            \"urn:li:title:1\",\n            \"urn:li:title:107\"\n          ]\n        }\n      }\n    ]\n  },\n  \"exclude\": {\n    \"or\": {\n      \"urn:li:adTargetingFacet:degrees\": [\n        \"urn:li:degree:1000\",\n        \"urn:li:degree:1100\"\n      ]\n    }\n  }\n}"
            }
            

This example will create the SavedAudienceTemplates If the integration is successful, the `Dashboard` task's `connectorOutputPayload` response parameter will have a value similar to the following:
            
            {
              "Id": "42831292"
            }

## Examples

### Example - CREATE operation on Entity "Event"

     1. In the `Configure connector task` dialog, click `Actions`.
     2. Select CreateEvent from the `Action` list.
     3. Select the `CreateEvent` operation, and then click **Done**.
     4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
            
            {
              "OrganizerURN": "urn:li:organization:106639229",
              "Name": "New Event 1",
              "Type": "IN_PERSON",
              "StartsAt": "2026-01-13 12:00:00"
            }

This example will create the Event If the integration is successful, the `Dashboard` task's `connectorOutputPayload` response parameter will have a value similar to the following:
            
            [
              {
                "Id": "7416342722296508416"
              }
            ]

### Example - Update an account

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select `Accounts` from the `Entity` list.
     3. Select the `Update` operation, and then click **Done**.
     4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and set the `connectorInputPayload` as local variable. 
            
            {
              "NotifiedOnEndOfCampaign": true
            }
            

     5. Set the **entityId** in **Data Mapper** to the entity of the `Accounts`.
     6. To set the **entityId** , click `Open Data Mapping Editor` and then enter `Id="514824232"` in the `Input Value` field and set the **entityId** as local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `Id='514824232'`

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
            
            { }
            

### Example - Update a campaign group

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select `CampaignGroups` from the `Entity` list.
     3. Select the `Update` operation, and then click **Done**.
     4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and set the `connectorInputPayload` as local variable. 
            
            {
              "Name": "jack"
            }
            

     5. Set the **entityId** in **Data Mapper** to the entity of the `CampaignGroups`.
     6. To set the **entityId** , click `Open Data Mapping Editor` and then enter `Id="776885434"` in the `Input Value` field and set the **entityId** as local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `Id='776885434' AND AdAccountId='514824232'`

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
            
            { }
            

### Example - Update a campaign

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select `Campaigns` from the `Entity` list.
     3. Select the `Update` operation, and then click **Done**.
     4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and set the `connectorInputPayload` as local variable. 
            
            {
              "Name": "Last Campaign"
            }
            

     5. Set the **entityId** in **Data Mapper** to the entity of the `Campaigns`.
     6. To set the **entityId** , click `Open Data Mapping Editor` and then enter `Id="411932694"` in the `Input Value` field and set the **entityId** as local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `Id='411932694' AND Name='New Campaign'`.

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
            
            { }
            

### Example - Update a creative

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select `Creatives` from the `Entity` list.
     3. Select the `Update` operation, and then click **Done**.
     4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and set the `connectorInputPayload` as local variable. 
            
            {
              "AdAccountId": "514824232",
              "Campaign": "urn:li:sponsoredCampaign:382923024",
              "Name": "New"
            }
            

     5. Set the **entityId** in **Data Mapper** to the entity of the `Creatives`.
     6. To set the **entityId** , click `Open Data Mapping Editor` and then enter `Id="urn:li:sponsoredCreative:668131684"` in the `Input Value` field and set the `entityId` as local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `Id='urn:li:sponsoredCreative:668131684' AND AdAccountId='514824232'`.

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
            
            { }
            

### Example - Update form details

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select `Forms` from the `Entity` list.
     3. Select the `Update` operation, and then click **Done**.
     4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and set the `connectorInputPayload` as local variable. 
            
            {
              "Description": "new description",
              "Headline": "new headline",
              "Questions": "[\n  {\n    \"question\": {\n      \"localized\": {\n        \"en_US\": \"Last name\"\n      }\n    },\n    \"responseEditable\": true,\n    \"name\": \"Last name\",\n    \"questionDetails\": {\n      \"textQuestionDetails\": {\n        \"maxResponseLength\": 300\n      }\n    },\n    \"predefinedField\": \"LAST_NAME\",\n    \"label\": \"Last name\",\n    \"responseRequired\": true\n  },\n  {\n    \"question\": {\n      \"localized\": {\n        \"en_US\": \"First name\"\n      }\n    },\n    \"responseEditable\": true,\n    \"name\": \"First name\",\n    \"questionDetails\": {\n      \"textQuestionDetails\": {\n        \"maxResponseLength\": 300\n      }\n    },\n    \"predefinedField\": \"FIRST_NAME\",\n    \"label\": \"First name\",\n    \"responseRequired\": true\n  },\n  {\n    \"question\": {\n      \"localized\": {\n        \"en_US\": \"Email address\"\n      }\n    },\n    \"responseEditable\": true,\n    \"name\": \"Email address\",\n    \"questionDetails\": {\n      \"textQuestionDetails\": {\n        \"maxResponseLength\": 300\n      }\n    },\n    \"predefinedField\": \"EMAIL\",\n    \"label\": \"Email address\",\n    \"responseRequired\": true\n  }\n]",
              "LegalDisclaimer": "new legal"
            }
            

     5. Set the **entityId** in **Data Mapper** to the entity of the `Forms`.
     6. To set the **entityId** , click `Open Data Mapping Editor` and then enter `Id="12882604"` in the `Input Value` field and set the **entityId** as local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `Id='12882604'`.

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
            
            { }
            

### Example - Update a message creative

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select `MessageCreatives` from the `Entity` list.
     3. Select the `Update` operation, and then click **Done**.
     4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and set the `connectorInputPayload` as local variable. 
            
            {
              "Name": "updated creative"
            }
            

     5. Set the **entityId** in **Data Mapper** to the entity of the `MessageCreatives`.
     6. To set the **entityId** , click `Open Data Mapping Editor` and then enter `Id="urn:li:adInMailContent:144110044"` in the `Input Value` field and set the **entityId** as local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `Id='urn:li:adInMailContent:144110044'`

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
            
            { }
            

### Example - Update a post

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select `Posts` from the `Entity` list.
     3. Select the `Update` operation, and then click **Done**.
     4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and set the `connectorInputPayload` as local variable. 
            
            {
              "Commentary": "updated post"
            }
            

     5. Set the **entityId** in **Data Mapper** to the entity of the `Post`.
     6. To set the **entityId** , click `Open Data Mapping Editor` and then enter `Id="urn:li:share:7331580382389149698"` in the `Input Value` field and set the **entityId** as local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `Id='urn:li:share:7331580382389149698'`

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
            
            { }
            

### Example - Update an image

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select `Images` from the `Entity` list.
     3. Select the `Update` operation, and then click **Done**.
     4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and set the `connectorInputPayload` as local variable. 
            
            {
              "MediaLibraryName": "New Image Name",
              "MediaLibraryStatus": "ACTIVE"
            }
            

     5. Set the **entityId** in **Data Mapper** to the entity of the `Images`.
     6. To set the **entityId** , click `Open Data Mapping Editor` and then enter `URN="urn:li:image:D4E10AQHeZAiDW6657A"` in the `Input Value` field and set the **entityId** as local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `AccountURN = 'urn:li:sponsoredAccount:514824232' AND URN= 'urn:li:image:D4E10AQHeZAiDW6657A'`.

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
            
            { }
            

### Example - Update a video

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select `Video` from the `Entity` list.
     3. Select the `Update` operation, and then click **Done**.
     4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and set the `connectorInputPayload` as local variable. 
            
            {
              "MediaLibraryName": "Updated Name"
            }
            

     5. Set the **entityId** in **Data Mapper** to the entity of the `Video`.
     6. To set the **entityId** , click `Open Data Mapping Editor` and then enter `URN="urn:li:video:D4E10AQHpuPTHnb1wXw"` in the `Input Value` field and set the **entityId** as local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `AccountURN = 'urn:li:sponsoredAccount:514824232' AND URN= 'urn:li:video:D4E10AQHpuPTHnb1wXw'`

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
            
            { }
            

### Example - Update an event

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select `Event` from the `Entity` list.
     3. Select the `Update` operation, and then click **Done**.
     4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and set the `connectorInputPayload` as local variable. 
            
            {
              "VanityName": "mytestevent7382067115601719297456"
            }
            

     5. Set the **entityId** in **Data Mapper** to the entity of the `Event`.
     6. To set the **entityId** , click `Open Data Mapping Editor` and then enter `Id="7399372283628306432"` in the `Input Value` field and set the **entityId** as local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `Id='7399372283628306432'`

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
            
            { }
            

### Example - Update a saved audience template

     1. In the `Configure connector task` dialog, click `Entities`.
     2. Select `SavedAudienceTemplates` from the `Entity` list.
     3. Select the `Update` operation, and then click **Done**.
     4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and set the `connectorInputPayload` as local variable. 
            
            {
              "Name": "Updated Saved Audience Templates"
            }
            

     5. Set the **entityId** in **Data Mapper** to the entity of `SavedAudienceTemplates`.
     6. To set the **entityId** , click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the `entityId` as local variable.

Instead of specifying the **entityId** , you can also set the **filterClause** to `Id='42831292'`

If the integration is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    {"Id": "null"}
    




### Example - Delete an account

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Accounts` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. Set the **entityId** to `Id="514824232"` which is the key to be passed.
  5. To set the **entityId** , in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `Id="514824232"` in the **Input Value** field and set the **entityId** as local variable.



## Get help from the Google Cloud community

You can post your questions and discuss this connector in the Google Cloud community at [Cloud Forums](https://www.googlecloudcommunity.com/gc/Integration-Services/bd-p/cloud-integration-services). 

## What's next

  * Understand how to [suspend and resume a connection](https://docs.cloud.google.com/integration-connectors/docs/suspend-resume-connection).
  * Understand how to [monitor connector usage](https://docs.cloud.google.com/integration-connectors/docs/cloud-monitoring).
  * Understand how to [view connector logs](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
