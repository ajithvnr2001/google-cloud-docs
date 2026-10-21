---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_google_calendar/configure/
title: Google Calendar \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:41:14.491283+00:00
---

# Google Calendar  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_google_calendar/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — BigQuery Connector**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

# Google Calendar

## Supported versions

This connector supports Google Calendar REST APIs.

## Before you begin

In your Google Cloud project, do the following tasks:

  * Ensure that network connectivity is set up. For information, see [Network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). 
  * Grant the [roles/connectors.admin](https://docs.cloud.google.com/integration-connectors/docs/connectors-access-permissions#iam-roles-for-integration-connectors) IAM role to the user configuring the connector.
  * Grant `roles/secretmanager.viewer` and `roles/secretmanager.secretAccessor` IAM roles to the [service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating) that you want to use for the connector 
  * Enable `secretmanager.googleapis.com` (Secret Manager API) and `connectors.googleapis.com` (Connectors API). For more information, see [Enabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling). 



## Configure the connector

A connection is specific to a data source. It means that if you have many data sources, you must create a separate connection for each data source. To create a connection, do the following:

  1. In the [Cloud console](https://console.cloud.google.com), go to the **Integration Connectors > Connections** page and then select or create a Google Cloud project. 

[ Go to the Connections page ](https://console.cloud.google.com/connectors/connections)

  2. Click **\+ CREATE NEW** to open the **Create Connection** page.
  3. In the **Location** section, complete the following: 
     1. **Region** : Select a location from the drop-down list. 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

     2. Click **Next**.
  4. In the **Connection Details** section, complete the following: 
     1. **Connector** : Select **Google Calendar** from the list of available connectors.
     2. **Connector version** : Select the connector version from the list of available versions. 
     3. In the **Connection Name** field, enter a name for the connection instance. The connection name can contain lowercase letters, numbers, or hyphens. The name must begin with a letter and end with a letter or number and the name must not exceed 49 characters.
     4. **Description** : Enter a description for the connection instance.
     5. Optionally, enable [Cloud logging](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs), and then select a log level. By default, the log level is set to `Error`. 
     6. **Service Account** : Select a service account that has the required roles.
     7. **Connection Timeout** : Optionally, enter the connection timeout in seconds.
     8. Optionally, configure the **Connection node settings** : 

        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
     9. **\+ ADD LABEL** : click this to add a label to the connection in the form of a key/value pair.
     10. Click **Next**.
  5. In the **Authentication** section, enter the authentication details. 
     1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Google Calendar connection:

        * Service Account Authentication
        * OAuth 2.0 - JWT Bearer
        * OAuth 2.0 - Authorization code

To understand how to configure these authentication types, see Configure authentication.

     2. Click **Next**.
  6. **Review** : Review your connection and authentication details.
  7. Click **Create**.



### Configure authentication

Enter the details based on the authentication you want to use.

  * **Service Account Authentication** : No additional configuration is required for this authentication type. The service account you selected in the **Connection Details** section will be used for authentication. 
  * **OAuth 2.0 - JWT Bearer**
    * **JWT Certificate** : Select the certificate to use for JWT authentication.
    * **Secret version** : Enter the secret version of the JWT certificate.
    * **JWT Subject** : Enter the JWT subject.
  * **OAuth 2.0 - Authorization code**
    * **Client ID** : Enter the client ID to use for OAuth authentication.
    * **Scopes** : Enter a list of desired scopes.
    * **Client Secret** : Enter the client secret to use for OAuth authentication.
    * **Secret version** : Enter the secret version of the client secret.
When you configure your third-party OAuth application, use this **authorized redirect URI** (callback URL): 

`https://console.cloud.google.com//connectors/oauth?project=PROJECT_ID`

Replace `PROJECT_ID` with your Google Cloud project ID.




## Connection configuration samples

This section lists the sample values for the various fields that you configure when creating the connection.

### Service account connection type

Field name | Details  
---|---  
Location | us-central1  
Connector | Google Calendar  
Connector version | 1  
Connection Name | service-account-auth  
Enable Cloud Logging | Yes  
Service Account | iam.gserviceaccount.com  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Authentication | Yes  
Service Account Authentication | Yes  
  
### OAuth 2.0 - JWT bearer connection type

Field name | Details  
---|---  
Location | us-central1  
Connector | Google Calendar  
Connector version | 1  
Connection Name | jwt-bearer-auth  
Enable Cloud Logging | Yes  
Service Account | iam.gserviceaccount.com  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Authentication | Yes  
OAuth 2.0 - JWT bearer | Yes  
JWT Cert | projects/google-cloud-project/secrets/jwt-cert/versions/1  
Secret version | 1  
  
### OAuth 2.0 - Authorization code connection type

Field name | Details  
---|---  
Location | us-central1  
Connector | Google Calendar  
Connector version | 1  
Connection Name | gcpcloud-googlecalendar-rest-conn  
Enable Cloud Logging | Yes  
Service Account | iam.gserviceaccount.com  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Authentication | Yes  
Client Id | 60875425788659-mt0cm1tguyiagvst468fvaw7.apps.googleusercontent.com  
Scope | https://www.googleapis.com/auth/calendar https://www.googleapis.com/auth/drive  
Client Secret | ygdruoX-Rtyah9gzkdZc-7CB0Eng9hyaufD0VD  
Secret version | 1  
  
## System limitations

The Google Calendar connector can process a maximum of 2 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Use the Google Calendar connection in an integration

After you create the connection, it becomes available in both Apigee Integration and Application Integration. You can use the connection in an integration through the Connectors task.

  * To understand how to create and use the connectors task in Apigee Integration, see [Connectors task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#configure-the-connectors-task).
  * To understand how to create and use the Connectors task in Application Integration, see [connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task).



## Entity operation examples

This section shows how to perform some of the [ entity operations](https://docs.cloud.google.com/integration-connectors/docs/entities-operation-action) in this connector.

### Example - List all the calendars

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Calendars` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, you can set the **filterClause** as per the customer requirement.

You must use single quotes (') to enclose the value for a filterClause.

You can use the filterClause to filter records based on the columns.




### Example - Get calendar details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Calendars` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. Set the `entityId` to `"c_3054d6e09a9dfae7886f995311@group.calendar.altostrat.com"` which is the key to be passed. 
  5. To set the **entityId** , in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `"c_3054d6e09a9dfae7886f995311@group.calendar.altostrat.com"` in the **Input Value** field and set the **entityId** as local variable.

The value for **entityId** should be passed directly, such as `"c_3054d6e09a9dfae7886f995311@group.calendar.altostrat.com"`. Here `"c_3054d6e09a9dfae7886f995311@group.calendar.altostrat.com"` is the unique primary key value, which must be passed.

In certain cases, passing an **entityId** might throw an error if the entity uses two composite keys. In such cases, you can use the **filterClause** to pass the value, such as `id='c_3054d6e09a9dfae7886f995311@group.calendar.altostrat.com'`.




### Example - Delete a calendar

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Calendars` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. Set the **entityId** to `"c_3054d6e09a9dfae7886f995311@group.calendar.altostrat.com"` which is the key to be passed. To set the **entityId** , in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `"c_3054d6e09a9dfae7886f995311@group.calendar.altostrat.com"` in the **Input Value** field and set the **entityId** as local variable. 

If entity has two composite business or primary keys instead of specifying the **entityId** , you can also set the **filterClause** to `id='c_3054d6e09a9dfae7886f995311@group.calendar.altostrat.com'`.




### Example - Create a calendar

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Calendars` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and set the `connectorInputPayload` as local variable. 
         
         {
           "Summary": "New calendar"
         }
         

If the integration is successful, the `calendar` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "c_5bae32e1c48ed38af98efecbd6da6bb002a31e887276aa65cc2530717123b75f@group.calendar.altostrat.com"
         }
         




### Example - Create an event in a calendar

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `AllCalendars` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and set the `connectorInputPayload` as local variable. 
         
         {
           "Summary": "New event",
           "CalendarId": "c_b4e891cebb19267bf5ac838f0c5f691bee164a7cec9dcc1a93e54625279baa80@group.calendar.altostrat.com",
           "StartDate": "2025-09-01",
           "EndDate": "2025-09-02"
         }
         

If the integration is successful, the `calendar` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "fnf0p7292pbm2buk59ubc1a37k",
           "CalendarId": null
         }
         




### Example - Create an event in your primary calendar

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select your email ID from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and set the `connectorInputPayload` as local variable. 
         
         {
           "Summary": "new event for my calendar",
           "CalendarId": "xyz@xwf.altostrat.com",
           "StartDate": "2025-09-01",
           "EndDate": "2025-09-02"
         }
         

If the integration is successful, the `AllCalendars` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "fnf0p7292pbm2buk59ubc1a37k",
           "CalendarId": null
         }
         




### Example - Create a type of event in a calendar

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `AllCalendars` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and set the `connectorInputPayload` as local variable. 
         
         {
           "EventType": "outOfOffice",
           "Summary": "outOfOffice",
           "CalendarId": "xyz@xwf.altostrat.com",
           "StartDateTime": "2025-09-03 14:00:00",
           "EndDateTime": "2025-09-03 15:00:00"
         }
         

If the integration is successful, the `AllCalendars` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "fnf0p7292pbm2buk59ubc1a37k",
           "CalendarId": null
         }
         




### Example - Create a recurring event in a calendar

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `AllCalendars` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and set the `connectorInputPayload` as local variable. 
         
         {
           "Summary": "Google Cloud Recurring event",
           "CalendarId": "xyz@xwf.altostrat.com",
           "StartDateTime": "2025-11-2 14:00:00",
           "EndDateTime": "2025-11-2 14:30:00",
           "Recurrences": "RRULE:FREQ=WEEKLY;BYDAY=TH;COUNT=5",
           "StartDateTimeZone": "America/Los_Angeles",
           "EndDateTimeZone": "America/Los_Angeles"
         }
         

If the integration is successful, the `AllCalendars` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
           "Id": "fnf0p7292pbm2buk59ubc1a37k",
           "CalendarId": null
         }
         




### Example - Update calendar details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Calendars` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and set the `connectorInputPayload` as local variable. 
         
         {
           "Summary": "Updated from Google Cloud"
         }
         

  5. Set the **entityId** in Data Mapper to the entity of the Calendar.
  6. To set the **entityId** , click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and set the **entityId** as local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `id='c_3054d6e09a9dfae7886f995311@group.calendar.altostrat.com'`.

Running this example returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         {
           "Id": "c_5bae32e1c48ed38af98efecbd6da6bb002a31e887276aa65cc2530717123b75f@group.calendar.altostrat.com"
         }
         




### Example - Update all calendars details

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `AllCalendars` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and set the connectorInputPayload as local variable. 
         
         {
           "Summary": "Great event"
         }
         

  5. Set the **entityId** in Data Mapper to the entity of the AllCalendars.
  6. To set the **entityId** , click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and set the **entityId** as local variable. 

Instead of specifying the **entityId** , you can also set the **filterClause** to `Summary='New sep event'`.

Running this example returns a response similar to the following in the connector task's `connectorOutputPayload` output variable:
         
         {
           "Id": "fnf0p7292pbm2buk59ubc1a37k",
           "CalendarId": null
         }
         




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
