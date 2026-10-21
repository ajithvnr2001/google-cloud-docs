---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/splunk/configure/
title: Splunk \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:41:30.944867+00:00
---

# Splunk  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/splunk/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Splunk

The Splunk connector lets you perform insert, delete, update, and read operations on Splunk database.

## Before you begin

Before using the Splunk connector, do the following tasks:

  * In your Google Cloud project: 
    * Ensure that network connectivity is set up. For information about network patterns, see [Network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). 
    * Grant the [roles/connectors.admin](https://docs.cloud.google.com/integration-connectors/docs/connectors-access-permissions#iam-roles-for-integration-connectors) IAM role to the user configuring the connector.
    * Grant the following IAM roles to the service account that you want to use for the connector: 
      * `roles/secretmanager.viewer`
      * `roles/secretmanager.secretAccessor`

A service account is a special type of Google account intended to represent a non-human user that needs to authenticate and be authorized to access data in Google APIs. If you don't have a service account, you must create a service account. The connector and the service account must belong to the same project. For more information, see [Creating a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating). 

    * Enable the following services: 
      * `secretmanager.googleapis.com` (Secret Manager API)
      * `connectors.googleapis.com` (Connectors API)

To understand how to enable services, see [Enabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling).

If these services or permissions have not been enabled for your project previously, you are prompted to enable them when configuring the connector. 




## Configure the connector

A connection is specific to a data source. It means that if you have many data sources, you must create a separate connection for each data source. To create a connection, do the following:

  1. In the [Cloud console](https://console.cloud.google.com), go to the **Integration Connectors > Connections** page and then select or create a Google Cloud project. 

[ Go to the Connections page ](https://console.cloud.google.com/connectors/connections)

  2. Click **\+ CREATE NEW** to open the **Create Connection** page.
  3. In the **Location** section, choose the location for the connection. 
     1. **Region** : Select a location from the drop-down list. 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

     2. Click **NEXT**.
  4. In the **Connection Details** section, complete the following: 
     1. **Connector** : Select **Splunk** from the drop down list of available Connectors.
     2. **Connector version** : Select the Connector version from the drop down list of available versions. 
     3. In the **Connection Name** field, enter a name for the Connection instance. 

Connection names must meet the following criteria: 

        * Connection names can use letters, numbers, or hyphens.
        * Letters must be lower-case.
        * Connection names must begin with a letter and end with a letter or number.
        * Connection names cannot exceed 49 characters.
     4. Optionally, enter a **Description** for the connection instance.
     5. Optionally, enable [Cloud logging](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs), and then select a log level. By default, the log level is set to `Error`. 
     6. **Service Account** : Select a service account that has the required roles.
     7. Optionally, configure the **Connection node settings** : 

        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
     8. Optionally, click **\+ ADD LABEL** to add a label to the Connection in the form of a key/value pair.
     9. Click **NEXT**.
  5. In the **Destinations** section, enter details of the remote host (backend system) you want to connect to. 
     1. **Destination Type** : Select a **Destination Type**. 
        * To specify the destination hostname or IP address, select **Host address** and enter the address in the **host 1** field.
        * To establish a private connection, select **Endpoint attachment**. In the **Endpoint Attachment** list, select the endpoint attachment created for your backend system.
**Note:** To learn how to create an endpoint attachment, see [Private network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). After creating the endpoint attachment, it is visible in the **Endpoint Attachment** list.

If you want to establish a public connection to your backend systems with additional security, you can consider [configuring static outbound IP addresses for your connections](https://docs.cloud.google.com/integration-connectors/docs/configure-static-ip), and then configure your firewall rules to allowlist only the specific static IP addresses. 

To enter additional destinations, click **+ADD DESTINATION**.

  6. Click **NEXT**.


* In the **Authentication** section, enter the authentication details. 

  1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Splunk connection:

     * Username and password (Basic authentication)
     * AccessToken
     * HTTPEventCollectorToken

To understand how to configure these authentication types, see Configure authentication.

  2. Click **NEXT**.


* **Review** : Review your connection and authentication details.
* Click **Create**.

### Configure authentication

Enter the details based on the authentication you want to use.

  * **Username and password**
    * **Username** : The Splunk username to use for the connection.
    * **Password** : Secret Manager Secret containing the password associated with the Splunk username.
  * **AccessToken** \- Set this to perform token based authentication by using the `AccessToken` property. 
  * **HTTPEventCollectorToken** \- Set this to perform token based authentication by using the `HTTPEventCollectorToken` property. 



### Connection configuration samples 

This section lists the sample values for the various fields that you configure when creating the Splunk connection.

#### HTTP Event collector connection type

Field name | Details  
---|---  
Location | us-central1  
Connector | Splunk  
Connector version | 1  
Connection Name | splunk-http-event-coll-conn  
Enable Cloud Logging | No  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Enable SSL | Yes  
Trust store Insecure Connection | Yes  
Destination Type(Server) | Host address  
Host address | 192.0.2.0  
Port | PORT  
HTTP Event Collector Token based authentication | Yes  
HTTPEventCollectorToken | HTTPEVENTCOLLECTOR_TOKEN  
Secret version | 1  
  
For information about how to create an HTTP event collector token, see [Create an HTTP event collector](https://docs.splunk.com/Documentation/SplunkCloud/latest/Data/UsetheHTTPEventCollector#Create_an_Event_Collector_token_on_Splunk_Cloud_Platform).

#### SSL connection type

Field name | Details  
---|---  
Location | us-central1  
Connector | Splunk  
Connector version | 1  
Connection Name | splunk-ssl-connection  
Enable Cloud Logging | Yes  
Service Account | SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com  
Verbosity level | 5  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Enable SSL | Yes  
Insecure Connection | Yes  
Destination Type(Server) | Host address  
Host address | https://192.0.2.0  
Port | PORT  
User Password | Yes  
User Name | USER  
Password | PASSWORD  
Secret version | 1  
  
For basic authentication, you must have the user role or power user role. For information about how to configure a power user, see [Configure power user role](https://docs.splunk.com/Documentation/ES/7.3.2/Install/ConfigureUsersRoles). For information about defining roles in Splunk, see [Define the Role on Splunk Platform](https://docs.splunk.com/Documentation/Splunk/9.2.0/Security/Rolesandcapabilities).

## Entities, operations, and actions

All the Integration Connectors provide a layer of abstraction for the objects of the connected application. You can access an application's objects only through this abstraction. The abstraction is exposed to you as entities, operations, and actions.

**Note:** You can view the entities, operations, and actions of a connector in the [Connectors task](https://docs.cloud.google.com/application-integration/docs/connectors-task).

  * **Entity:** An entity can be thought of as an object, or a collection of properties, in the connected application or service. The definition of an entity differs from a connector to a connector. For example, in a database connector, tables are the entities, in a file server connector, folders are the entities, and in a messaging system connector, queues are the entities. 

However, it is possible that a connector doesn't support or have any entities, in which case the `Entities` list will be empty.

  * **Operation:** An operation is the activity that you can perform on an entity. You can perform any of the following operations on an entity: 
    * [List](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#config-prop)
    * [Get](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#config-prop)
    * [Create](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#config-prop)
    * [Update](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#config-prop)
    * [Delete](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#config-prop)

Selecting an entity from the available list, generates a list of operations available for the entity. For a detailed description of the operations, see the Connectors task's [entity operations](https://docs.cloud.google.com/application-integration/docs/connectors-task#config-prop). However, if a connector doesn't support any of the entity operations, such unsupported operations aren't listed in the `Operations` list.

  * **Action:** An action is a first class function that is made available to the integration through the connector interface. An action lets you make changes to an entity or entities, and vary from connector to connector. Normally, an action will have some input parameters, and an output parameter. However, it is possible that a connector doesn't support any action, in which case the `Actions` list will be empty. 

**Note:** All entities and actions will have a schema associated with them. For example, an action schema will have the parameter details such as; the parameter names, and its corresponding data type. The schema (metadata) for entities and actions is fetched by the connection at runtime from your backend. If there are any updates to the schema, such updates won't be automatically reflected in your existing connections; you must manually refresh the schema. To refresh the schema for a connection, open the **Connection details** page of the connection, and then click **Refresh connection schema**. 

## System limitations

The Splunk connector can process 5 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. However, the number transactions that this connector can process also depends on the constraints imposed by the Splunk instance. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Actions

This section lists the actions supported by the connector. To understand how to configure the actions, see Action examples.

**Note:** The results of all the actions will be available as a JSON response in the `Connectors` task's `connectorOutputPayload` response parameter after you run your integration.

### CreateHTTPEvent action

This action lets you send data and application events to a Splunk deployment over the HTTP and HTTPS protocols.

**Note** : To use this action, you must use the  HTTPEventCollectorToken authentication.

#### Input parameters of the CreateHTTPEvent action

Parameter name | Data type | Required | Description  
---|---|---|---  
EventContent | String | Yes | The name of the table or view.  
ContentType | String | No | The type of content specified for the `EventContent` input. The supported values are `JSON` and `RAWTEXT`.  
ChannelGUID | Integer | No | The GUID of the channel used for the event. You must specify this value if the `ContentType` is `RAWTEXT`.  
  
#### Output parameters of the CreateHTTPEvent action

This action returns the success status of the created event.

### CreateIndex action

This action lets you create indexes.

#### Input parameters of the CreateIndex action

Parameter name | Data type | Required | Description  
---|---|---|---  
MaxMetaEntries | String | No | Sets the maximum number of unique lines in .data files in a bucket, which may help to reduce memory consumption.  
FrozenTimePeriodInSecs | String | No | Number of seconds after which indexed data rolls to frozen. Defaults to 188697600 (6 years).  
HomePath | String | No | An absolute path that contains the hot and warm buckets for the index.  
MinRawFileSyncSecs | String | No | Specify an integer (or `disable`) for this parameter. This parameter sets how frequently splunkd forces a filesystem sync while compressing journal slices. | ProcessTrackerServiceInterval | String | No | Specifies, in seconds, how often the indexer checks the status of the child OS processes it launched to see if it can launch new processes for queued requests. If set to 0, the indexer checks child process status every second. | ServiceMetaPeriod | String | No | Defines how frequently (in seconds) metadata is synced to disk. | MaxHotSpanSecs | String | No | Upper bound of target maximum timespan (in seconds) of hot or warm buckets. | QuarantinePastSecs | String | No | Events with timestamp of quarantinePastSecs older than `>now` are dropped into quarantine bucket. | ColdToFrozenDir | String | No | Destination path for the frozen archive. Use as an alternative to a ColdToFrozenScript. | ColdPath | String | No | An absolute path that contains the colddbs for the index. The path must be readable and writable. | MaxHotIdleSecs | String | No | Maximum life, in seconds, of a hot bucket | WarmToColdScript | String | No | Path to a script to run when moving data from warm to cold. | ColdToFrozenScript | String | No | Path to the archiving script. | MaxHotBuckets | String | No | Maximum hot buckets that can exist per index. | TstatsHomePath | String | No | Location to store datamodel acceleration TSIDX data for this index. If specified, it must be defined in terms of a volume definition. Path must be writable | RepFactor | String | No | Index replication control. This parameter applies to only peer-nodes in the cluster. 

  * **auto** \- Use the master index replication configuration value.
  * **0** \- Turn off replication for this index.

| MaxDataSize | String | No | The maximum size in MB for a hot DB to reach before a roll to warm is triggered. Specifying `auto` or `auto_high_volume` causes Splunk to autotune this parameter (recommended). | MaxBloomBackfillBucketAge | String | No | Valid values are: integer[m|s|h|d] if a warm or cold bucket is older than the specified age, don't create or rebuild its bloomfilter. Specify 0 to never rebuild bloomfilters. | BlockSignSize | String | No | Controls how many events make up a block for block signatures. If this is set to 0, block signing is disabled for this index. A recommended value is 100. | Name | String | Yes | The name of the index to create | MaxTotalDataSizeMB | String | No | The maximum size of an index (in MB). If an index grows larger than the maximum size, the oldest data is frozen. | MaxWarmDBCount | String | No | The maximum number of warm buckets. If this number is exceeded, the warm bucket(s) with the lowest value for their latest times is moved to cold. | RawChunkSizeBytes | String | No | Target uncompressed size in bytes for individual raw slice in the rawdata journal of the index. 0 is not a valid value. If 0 is specified, rawChunkSizeBytes is set to the default value. | DataType | String | No | Specifies the type of index | MaxConcurrentOptimizes | String | No | The number of concurrent optimize processes that can run against a hot bucket. | ThrottleCheckPeriod | String | No | Defines how frequently (in seconds) Splunk checks for index throttling condition. | SyncMeta | String | No | When true, a sync operation is called before file descriptor is closed on metadata file updates. This functionality improves integrity of metadata files, especially in regards to operating system crashes or machine failures. | RotatePeriodInSecs | String | No | How frequently (in seconds) to check if a new hot bucket needs to be created. Also, how frequently to check if there are any warm/cold buckets that should be rolled/frozen.  
  
#### Output parameters of the CreateIndex action

This action returns confirmation message of the CreateIndex action.

For example on how to configure the `CreateIndex` action, see Action examples.

### CreateSavedSearch action

This action let you save your searches

#### Input parameters of the CreateSavedSearch action

Parameter name | Data type | Required | Description  
---|---|---|---  
IsVisible | Boolean | Yes | Indicates if this saved search appears in the visible saved search list.  
RealTimeSchedule | Boolean | Yes | If this value is set to 1, the scheduler bases its determination of the next scheduled search execution time on the current time. If this value is set to 0, it is determined based on the last search execution time.  
Search | String | Yes | The search query to save  
Description | String | No | Description of this saved search | SchedulePriority | String | Yes | Indicates the scheduling priority of a specific search | CronSchedule | String | Yes | The cron schedule to execute this search. For example, `*/5 * * * *` causes the search to execute every 5 minutes. | Name | String | Yes | A name for the search | UserContext | String | Yes | If user context is provided, servicesNS node is used (/servicesNS/[UserContext]/search), else defaults to the general endpoint, `/services`. | RunOnStartup | Boolean | Yes | Indicates whether this search runs on startup. If it does not run on startup, the search runs at the next scheduled time. | Disabled | Boolean | No | Indicates if this saved search is disabled. | IsScheduled | Boolean | Yes | Indicates if this search is to be run on a schedule.  
  
#### Output parameters of the CreateSavedSearch action

This action returns confirmation message of the CreateSavedSearch action.

For example on how to configure the `CreateSavedSearch` action, see Action examples.

### UpdateSavedSearch action

This action lets you update a saved search.

#### Input parameters of the UpdateSavedSearch action

Parameter name | Data type | Required | Description  
---|---|---|---  
IsVisible | Boolean | Yes | Indicates if this saved search appears in the visible saved search list.  
RealTimeSchedule | Boolean | Yes | If this value is set to 1, the scheduler bases its determination of the next scheduled search execution time on the current time. If this value is set to 0, it is determined based on the last search execution time.  
Search | String | Yes | The search query to save  
Description | String | No | Description of this saved search | SchedulePriority | String | Yes | Indicates the scheduling priority of a specific search | CronSchedule | String | Yes | The cron schedule to execute this search. For example, */5 * * * * causes the search to execute every 5 minutes. | Name | String | Yes | A name for the search | UserContext | String | Yes | If user context is provided, servicesNS node is used (/servicesNS/[UserContext]/search), else, it defaults to the general endpoint, `/services`. | RunOnStartup | Boolean | Yes | Indicates whether this search runs on startup. If it does not run on startup, the search runs at the next scheduled time. | Disabled | Boolean | No | Indicates if this saved search is disabled. | IsScheduled | Boolean | Yes | Indicates if this search is to be run on a schedule.  
  
#### Output parameters of the UpdateSavedSearch action

This action returns confirmation message of the UpdateSavedSearch action.

For example on how to configure the `UpdateSavedSearch` action, see Action examples.

### DeleteIndex action

This action lets you delete an index.

#### Input parameters of the DeleteIndex action

Parameter name | Data type | Required | Description  
---|---|---|---  
Name | String | Yes | The name of the index to delete.  
  
#### Output parameters of the DeleteIndex action

This action returns confirmation message of the DeleteIndex action

For example on how to configure the `DeleteIndex` action, see Action examples.

### UpdateIndex action

This action lets you update an index.

#### Input parameters of the UpdateIndex action

Parameter name | Data type | Required | Description  
---|---|---|---  
MaxMetaEntries | String | No | Sets the maximum number of unique lines in .data files in a bucket, which may help to reduce memory consumption.  
FrozenTimePeriodInSecs | String | No | Number of seconds after which indexed data rolls to frozen. Defaults to 188697600 (6 years).  
HomePath | String | No | An absolute path that contains the hot and warm buckets for the index.  
MinRawFileSyncSecs | String | No | Specify an integer (or `disable`) for this parameter. This parameter sets how frequently splunkd forces a filesystem sync while compressing journal slices. | ProcessTrackerServiceInterval | String | No | Specifies, in seconds, how often the indexer checks the status of the child OS processes it launched to see if it can launch new processes for queued requests. If set to 0, the indexer checks child process status every second. | ServiceMetaPeriod | String | No | Defines how frequently (in seconds) metadata is synced to disk. | MaxHotSpanSecs | String | No | Upper bound of target maximum timespan (in seconds) of hot or warm buckets. | QuarantinePastSecs | String | No | Events with timestamp of quarantinePastSecs older than `now` are dropped into quarantine bucket. | ColdToFrozenDir | String | No | Destination path for the frozen archive. Use as an alternative to a ColdToFrozenScript. | ColdPath | String | No | An absolute path that contains the colddbs for the index. The path must be readable and writable. | MaxHotIdleSecs | String | No | Maximum life, in seconds, of a hot bucket. | WarmToColdScript | String | No | Path to a script to run when moving data from warm to cold. | ColdToFrozenScript | String | No | Path to the archiving script. | MaxHotBuckets | String | No | Maximum hot buckets that can exist per index. | TstatsHomePath | String | No | Location to store datamodel acceleration TSIDX data for this index. If specified, it must be defined in terms of a volume definition. Path must be writable | RepFactor | String | No | Index replication control. This parameter applies to only peer-nodes in the cluster. 

  * **auto** \- Use the master index replication configuration value.
  * **0** \- Turn off replication for this index.

| MaxDataSize | String | No | The maximum size in MB for a hot DB to reach before a roll to warm is triggered. Specifying `auto` or `auto_high_volume` causes Splunk to autotune this parameter (recommended). | MaxBloomBackfillBucketAge | String | No | Valid values are: integer[m|s|h|d] if a warm or cold bucket is older than the specified age, do not create or rebuild its bloomfilter. Specify 0 to never rebuild bloomfilters. | BlockSignSize | String | No | Controls how many events make up a block for block signatures. If this is set to 0, block signing is disabled for this index. A recommended value is 100. | Name | String | Yes | The name of the index to create | MaxTotalDataSizeMB | String | Yes | The maximum size of an index (in MB). If an index grows larger than the maximum size, the oldest data is frozen. | MaxWarmDBCount | String | No | The maximum number of warm buckets. If this number is exceeded, the warm bucket(s) with the lowest value for their latest times is moved to cold. | RawChunkSizeBytes | String | No | Target uncompressed size in bytes for individual raw slice in the rawdata journal of the index. 0 is not a valid value. If 0 is specified, rawChunkSizeBytes is set to the default value. | DataType | String | No | Specifies the type of index | MaxConcurrentOptimizes | String | No | The number of concurrent optimize processes that can run against a hot bucket. | ThrottleCheckPeriod | String | No | Defines how frequently (in seconds) Splunk checks for index throttling condition. | SyncMeta | String | No | When true, a sync operation is called before file descriptor is closed on metadata file updates. This functionality improves integrity of metadata files, especially in regards to operating system crashes or machine failures. | RotatePeriodInSecs | String | No | How frequently (in seconds) to check if a new hot bucket needs to be created. Also, how frequently to check if there are any warm or cold buckets that should be rolled or frozen.  
  
#### Output parameters of the UpdateIndex action

This action returns confirmation message of the UpdateIndex action.

For example on how to configure the `UpdateIndex` action, see Action examples.

## Action examples

### Example - Create a HTTP event

This example creates a HTTP event.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CreateHTTPEvent` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "EventContent": "Testing Task",
         "ContentType": "RAWTEXT",
         "ChannelGUID": "ContentType=RAWTEXT"
         }

If the action is successful, the `CreateHTTPEvent` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": "Success"
    }] 
    




### Example - Create an index

This example creates an index.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CreateIndex` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Name": "http_testing"
         }

If the action is successful, the `CreateIndex` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "AssureUTF8": null,
    "BlockSignSize": null,
    "BlockSignatureDatabase": null,
    "BucketRebuildMemoryHint": null,
    "ColdPath": null,
    "FrozenTimePeriodInSecs": null,
    "HomePath": null,
    "HomePathExpanded": null,
    "IndexThreads": null,
    "IsInternal": null,
    "MaxConcurrentOptimizes": null,
    "MaxDataSize": null,
    "MaxHotBuckets": null,
    "SuppressBannerList": null,
    "Sync": null,
    "SyncMeta": null,
    "ThawedPath": null,
    "ThawedPathExpanded": null,
    "TstatsHomePath": null,
    "WarmToColdScript": null,
    }]




### Example - Create a saved search

This example creates a saved search.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CreateSavedSearch` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Name": "test_created_g",
         "Search": "index=\"http_testing\"",
         "CronSchedule": "*/1 * * * *",
         "IsVisible": true,
         "RealTimeSchedule": true,
         "RunOnStartup": true,
         "IsScheduled": true,
         "SchedulePriority": "highest",
         "UserContext": "nobody"
         }

If the action is successful, the `CreateSavedSearch` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": true,
    "Message": null
    }]




### Example - Update a saved search

This example updates a saved search.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UpdateSavedSearch` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Name": "test_created_g",
         "Search": "index=\"december_test_data\"",
         "CronSchedule": "*/1 * * * *",
         "IsVisible": true,
         "RealTimeSchedule": true,
         "RunOnStartup": true,
         "IsScheduled": true,
         "SchedulePriority": "highest"
         }

If the action is successful, the `UpdateSavedSearch` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": true,
    "Message": null
    }]




### Example - Delete an index

This example deletes an index.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DeleteIndex` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Name": "g_http_testing"
         }

If the action is successful, the `DeleteIndex` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Success": true,
    "ErrorCode": null,
    "ErrorMessage": null
    }]




### Example - Update an index

This example updates an index.

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UpdateIndex` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "MaxTotalDataSizeMB": "400000",
         "Name": "g_http_testing"
         }

If the action is successful, the `UpdateIndex` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "AssureUTF8": false,
    "BlockSignSize": null,
    "BlockSignatureDatabase": null,
    "BucketRebuildMemoryHint": "auto",
    "ColdPath": "$SPLUNK_DB\\g_http_testing\\colddb",
    "ColdPathExpanded": "C:\\Program Files\\Splunk\\var\\lib\\splunk\\g_http_testing\\colddb",
    "ColdToFrozenDir": "",
    "ColdToFrozenScript": "",
    "CurrentDBSizeMB": 1.0,
    "DefaultDatabase": "main",
    "EnableOnlineBucketRepair": true,
    "EnableRealtimeSearch": true,
    "FrozenTimePeriodInSecs": 1.886976E8,
    "HomePath": "$SPLUNK_DB\\g_http_testing\\db",
    "HomePathExpanded": "C:\\Program Files\\Splunk\\var\\lib\\splunk\\g_http_testing\\db",
    "IndexThreads": "auto",
    "IsInternal": false,
    "LastInitTime": "2024-01-08 05:15:28.0",
    "MaxBloomBackfillBucketAge": "30d",
    "ThawedPath": "$SPLUNK_DB\\g_http_testing\\thaweddb",
    "ThawedPathExpanded": "C:\\Program Files\\Splunk\\var\\lib\\splunk\\g_http_testing\\thaweddb",
    "ThrottleCheckPeriod": 15.0,
    "TotalEventCount": 0.0,
    "TsidxDedupPostingsListMaxTermsLimit": 8388608.0,
    "TstatsHomePath": "volume:_splunk_summaries\\$_index_name\\datamodel_summary",
    "WarmToColdScript": "",
    "Success": true,
    "ErrorCode": null,
    "ErrorMessage": null
    }]




## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List all the records

This example lists all the records in the `SearchJobs` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `SearchJobs` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. Optionally, in **Task Input** section of the **Connectors** task, you can filter your result set by specifying a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter). Specify the filter clause value always within the single quotes ('). 

**Note:**

List operations can be performed for the entities:

AlertsInInternalServer, DataModels, SavedSearch(Entity- googlecloud_created_saved), and Result logs(Entity- domestic_airline_test_data)

### Example - Get a record from an entity

This example gets a record with the specified ID from the `SearchJobs` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `SearchJobs` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **EntityId** and then enter `1698309163.1300` in the **Default Value** field. 

Here, `1698309163.1300` is a unique record ID in the `SearchJobs` entity.


**Note:**

Get operations can be performed for the entities:

AlertsInInternalServer, DataModels, SearchJobs(Web User Identification by Country), SearchJobs(Finding New Local Admin Accounts), SearchJobs(Unusual Access to the System), SearchJobs(Detecting Brute Force Attacks), SearchJobs(Find unencrypted web communications that could lead to a data breach), SearchJobs(Log Volume Trending), SearchJobs(Measuring Storage I/O Latency), SearchJobs(Measuring Storage Speed I/O Utilization by Host), SearchJobs(Measuring Memory Utilization by Host), SavedSearch(Entity- googlecloud_created_saved) 

### Example - Create a record in an entity

This example creates a record in the `SearchJobs` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `SearchJobs` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         { 
         "EventSearch": "search (index=\"antivirus_logs\") sourcetype=access_combined | rex  \"(?\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3})\" | iplocation IP_address| table IP_address, City, Country" 
         } 
         

If the integration is successful, the `SearchJobs` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
         "Sid": "1699336785.1919"
         } 
         




### Example - Create a record in an entity

This example creates a record in the `DataModels` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `DataModels` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Id": "Test1",
         "Acceleration": "{\"enabled\":false,\"earliest_time\":\"\",
         \"max_time\":3600,\"backfill_time\":\"\",\"source_guid\":\"\",
         \"manual_rebuilds\":false,\"poll_buckets_until_maxtime\":false,
         \"max_concurrent\":3,\"allow_skew\":\"0\",\"schedule_priority\":\"default\"
         ,\"allow_old_summaries\":false,\"hunk.file_format\":\"\",\"hunk.dfs_block_size\":0,
         \"hunk.compression_codec\":\"\",\"workload_pool\":\"\"}"
         }

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         [{
         "Id": "Test1"
         }]




### Example - Delete a record from an entity

This example deletes the record with the specified ID in the `DataModels` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `DataModels` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click **entityId** and then enter `Test1` in the **Default Value** field. 

**Note:** If your entity has a composite primary key, you can specify a [filter clause](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#filter).

### Example - Update a record in an entity

This example updates a record in the `DataModels` entity.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `DataModels` from the `Entity` list.
  3. Select the `Update` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "Acceleration": "{\"enabled\":true,\"earliest_time\":\"-3mon\",
         \"cron_schedule\":\"*/5 * * * *\",\"max_time\":60,
         \"backfill_time\":\"\",\"source_guid\":\"\",\"manual_rebuilds\":false,
         \"poll_buckets_until_maxtime\":false,\"max_concurrent\":3,
         \"allow_skew\":\"0\",\"schedule_priority\":\"default\",
         \"allow_old_summaries\":false,\"hunk.file_format\":\"\",\"hunk.dfs_block_size\":0,
         \"hunk.compression_codec\":\"\",\"workload_pool\":\"\"}"
         }

  5. Click **entityId** , and then enter `/servicesNS/nobody/search/datamodel/model/Testing` in the **Default Value** field. 

If the integration is successful, your connector task's `connectorOutputPayload` field will have a value similar to the following:
         
         [{
         "Id": "/servicesNS/nobody/search/datamodel/model/Testing"
         }]




### Example - Search flow using index

This section lists all the search flow using single index and multiple indices.

#### Create a search using single Index

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `SearchJobs` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
         "EventSearch": "search (index=\"http_testing\" sourcetype=\"googlecloud-testing\") "
         }
         

If the integration is successful, the `SearchJobs` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
         "Sid": "1726051471.76"
         } 
         


**Note:**
* To obtain the results of the above search, you need to perform a list operation on the specific index that was used in the input payload of the SearchJobs request.  

* You need to pass the Sid in the filterclause of the list operation on the index. This will ensure that the results are filtered correctly based on the specified Sid. 

#### List operation using the Index Name used in Search Query

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Index Name` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. **Task Input** section of the **Connectors** task, you can set the **filterClause** , such as Sid= '1726051471.76'.

If the integration is successful, the `Index Name` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
      "_bkt": "http_testing~0~D043151E-5A2D-4FAB-8647-4D5DA2F288AF",
      "_cd": "00:04:00",
      "_eventtype_color": null,
      "_indextime": 1.720702012E9,
      "_kv": null,
      "_raw": "hi How r yo\nplease\nfind \nmy notes",
      "_serial": 0.0,
      "_si": "googlecloud-bcone-splunk-vm\nhttp_testing",
      "_sourcetype": "googlecloud-testing",
      "_time": "2024-07-11 12:46:52.0",
      "eventtype": null,
      "host": "googlecloud-bcone-splunk-vm",
      "index": "http_testing",
      "linecount": 4.0,
      "punct": null,
      "source": "Testing.txt",
      "sourcetype": "googlecloud-testing",
      "splunk_server": "googlecloud-bcone-splunk-vm",
      "splunk_server_group": null,
      "timestamp": null,
      "JobId": "1726051471.76"
    }]
    


**Note:**
* The value for filter clause should be always passed within the single quotes (') in this format.
* Index Name is dynamically exposed as entity for example: http_testing.

#### Create a search using multiple Indices

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `SearchJobs` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
         "EventSearch": "search (index=\"http_testing\" OR index= \"googlecloud-demo\" sourcetype=\"googlecloud-testing\"  OR sourcetype=\"Demo_Text\")"
         }
         

If the integration is successful, the `SearchJobs` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
         "Sid": "1727261971.4007"
         } 
         




#### List operation using the Indices Name used in Search Query

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Index Name` Name from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. **Task Input** section of the **Connectors** task, you can set the **filterClause** , such as Sid= '1727261971.4007'.

If the integration is successful, the `Index` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
      "_bkt": "googlecloud-demo~0~D043151E-5A2D-4FAB-8647-4D5DA2F288AF",
      "_cd": "00:04:00",
      "_eventtype_color": null,
      "_indextime": 1.727155516E9,
      "_kv": null,
      "_raw": "Hi team\nwe have a demo please plan accordingly\nwith Google team",
      "_serial": 0.0,
      "_si": "googlecloud-bcone-splunk-vm\ngooglecloud-demo",
      "_sourcetype": "Demo_Text",
      "_time": "2024-09-24 05:25:16.0",
      "eventtype": null,
      "host": "googlecloud-bcone-splunk-vm",
      "index": "googlecloud-demo",
      "linecount": 3.0,
      "punct": null,
      "source": "Splunk_Demo.txt",
      "sourcetype": "Demo_Text",
      "splunk_server": "googlecloud-bcone-splunk-vm",
      "splunk_server_group": null,
      "timestamp": null,
      "JobId": "1727261971.4007"
    }, {
      "_bkt": "http_testing~0~D043151E-5A2D-4FAB-8647-4D5DA2F288AF",
      "_cd": "00:04:00",
      "_eventtype_color": null,
      "_indextime": 1.720702012E9,
      "_kv": null,
      "_raw": "hi How r yo\nplease\nfind \nmy notes",
      "_serial": 1.0,
      "_si": "googlecloud-bcone-splunk-vm\nhttp_testing",
      "_sourcetype": "googlecloud-testing",
      "_time": "2024-07-11 12:46:52.0",
      "eventtype": null,
      "host": "googlecloud-bcone-splunk-vm",
      "index": "http_testing",
      "linecount": 4.0,
      "punct": null,
      "source": "Testing.txt",
      "sourcetype": "googlecloud-testing",
      "splunk_server": "googlecloud-bcone-splunk-vm",
      "splunk_server_group": null,
      "timestamp": null,
      "JobId": "1727261971.4007"
    }]
    




### Example - Search flow using ReadJobResults

This section lists all the search flows that uses both single index and multiple indices supported by the Splunk connection. As of now,the maximum payload size for supported log results is 150MB.

#### Create a search with single index

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `SearchJobs` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
         "EventSearch": "search (index=\"http_testing\" sourcetype=\"googlecloud-testing\") "
         }
         

This example creates a search If the integration is successful, the `SearchJobs` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
         "Sid": "1732775755.24612"
         } 
         




To obtain the search results, perform the create operation on the ReadJobResults action. To ensure that the results are filtered based on the Sid, pass the Sid as a parameter to the action.

#### Get result logs using ReadJobResults action

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ReadJobResults` action, and then click **Done**.
  3. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
         "Sid": "1732775755.24612"
         }
         

If the action is successful, the `ReadJobResults` task's `connectorOutputPayload` response parameter will have a value similar to the following: 
    
    [{
    "_bkt": "http_testing~0~D043151E-5A2D-4FAB-8647-4D5DA2F288AF",
    "_cd": "0:4",
    "_indextime": "1720702012",
    "_raw": "hi How r yo\nplease\nfind \nmy notes",
    "_serial": "1",
    "_si": "googlecloud-bcone-splunk-vm\nhttp_testing",
    "_sourcetype": "googlecloud-testing",
    "_time": "2024-07-11T12:46:52.000+00:00",
    "host": "googlecloud-bcone-splunk-vm",
    "index": "http_testing",
    "linecount": "4",
    "source": "Testing.txt",
    "sourcetype": "googlecloud-testing",
    "splunk_server": "googlecloud-bcone-splunk-vm",
    "jobid": "1732775755.24612",
    "sid": "1732775755.24612"
    }]
    




#### Create a search with multiple indices

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `SearchJobs` from the `Entity` list.
  3. Select the `Create` operation, and then click **Done**.
  4. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
         "EventSearch": "search (index=\"http_testing\" OR index= \"googlecloud-demo\" sourcetype=\"googlecloud-testing\"  OR sourcetype=\"Demo_Text\")"
         }
         

If the integration is successful, the `SearchJobs` task's `connectorOutputPayload` response parameter will have a value similar to the following:
         
         {
         "Sid": "1732776556.24634"
         } 
         




To obtain the search results, perform the create operation on the ReadJobResults action. To ensure that the results are filtered based on the Sid, pass the Sid as a parameter to the action.

#### ResultsLogs using ReadJobResults Action

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ReadJobResults` action, and then click **Done**.
  3. In the **Data Mapper** section of the **Data Mapping** task, click `Open Data Mapping Editor` and then enter a value similar to the following in the `Input Value` field and choose the EntityId/ConnectorInputPayload as Local variable. 
         
         {
         "Sid": "1732776556.24634"
         }
         

If the action is successful, the `ReadJobResults` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "_bkt": "googlecloud-demo~0~D043151E-5A2D-4FAB-8647-4D5DA2F288AF",
    "_cd": "0:4",
    "_indextime": "1727155516",
    "_raw": "Hi team\nwe have a demo please plan accordingly\nwith Google team",
    "_serial": "0",
    "_si": "googlecloud-bcone-splunk-vm\googlecloud-demo",
    "_sourcetype": "Demo_Text",
    "_time": "2024-09-24T05:25:16.000+00:00",
    "host": "googlecloud-bcone-splunk-vm",
    "index": "googlecloud-demo",
    "linecount": "3",
    "source": "Splunk_Demo.txt",
    "sourcetype": "Demo_Text",
    "splunk_server": "googlecloud-bcone-splunk-vm",
    "jobid": "1732776556.24634",
    "sid": "1732776556.24634"
    },{
    "_bkt": "http_testing~0~D043151E-5A2D-4FAB-8647-4D5DA2F288AF",
    "_cd": "0:4",
    "_indextime": "1720702012",
    "_raw": "hi How r yo\nplease\nfind \nmy notes",
    "_serial": "1",
    "_si": "googlecloud-bcone-splunk-vm\nhttp_testing",
    "_sourcetype": "googlecloud-testing",
    "_time": "2024-07-11T12:46:52.000+00:00",
    "host": "googlecloud-bcone-splunk-vm",
    "index": "http_testing",
    "linecount": "4",
    "source": "Testing.txt",
    "sourcetype": "googlecloud-testing",
    "splunk_server": "googlecloud-bcone-splunk-vm",
    "jobid": "1732776556.24634",
    "sid": "1732776556.24634"
    }]
    




## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file:

Parameter name | Data type | Required | Description  
---|---|---|---  
verbosity | STRING | False | Verbosity level for connection, varies from 1-5. Higher verbosity level will log all the communication details (request,response & ssl certificates).   
proxy_enabled | BOOLEAN | False | Select this checkbox to configure a proxy server for the connection.   
proxy_auth_scheme | ENUM | False | The authentication type to use to authenticate to the ProxyServer proxy. Supported values are: BASIC, DIGEST, NONE  
proxy_user | STRING | False | A user name to be used to authenticate to the ProxyServer proxy.   
proxy_password | SECRET | False | A password to be used to authenticate to the ProxyServer proxy.   
proxy_ssltype | ENUM | False | The SSL type to use when connecting to the ProxyServer proxy. Supported values are: AUTO, ALWAYS, NEVER, TUNNEL  
  
## Use the Splunk connection in an integration

After you create the connection, it becomes available in both Apigee Integration and Application Integration. You can use the connection in an integration through the Connectors task.

  * To understand how to create and use the Connectors task in Apigee Integration, see [Connectors task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#configure-the-connectors-task).
  * To understand how to create and use the Connectors task in Application Integration, see [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task).



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
