---
url: https://docs.cloud.google.com/application-integration/docs/configure-jiraserverdc-trigger/
title: Jira Server (Data Center) trigger \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:27.128554+00:00
---

# Jira Server (Data Center) trigger  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/configure-jiraserverdc-trigger/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Jira Server (Data Center) trigger

**Preview — Jira Server (Data Center) trigger**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The **Jira Server (Data Center) trigger** is a [Connector Event trigger](https://docs.cloud.google.com/application-integration/docs/triggers#event-triggers) that lets you invoke an integration based on the Jira Server (Data Center) events that you've subscribed to in your Jira Server (Data Center) connection.

**Important:** Integration Connectors is a billable component of Google Cloud. For information about the costs and charges of using Integration Connectors, see [Integration Connectors pricing](https://docs.cloud.google.com/integration-connectors/docs/pricing).

## Before you begin

  * If you plan to create or configure a new connection for the Jira Server (Data Center) trigger, make sure that you have the **Connector Admin** (`roles/connectors.admin`) IAM role on the project. For information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
  * Grant the **Application Integration Invoker** (`roles/integrations.integrationInvoker`) IAM role to the service account that you want to use for the Jira Server (Data Center) trigger. 
  * Create a new integration or open an existing integration to add the Jira Server (Data Center) trigger.



## Configure Jira Server (Data Center) trigger using an existing connection

You can configure the **Jira Server (Data Center) trigger** using an existing Jira Server (Data Center) connection in Integration Connectors. Note that the **Jira Server (Data Center) trigger** is an [Connector Event trigger](https://docs.cloud.google.com/application-integration/docs/triggers#event-triggers), therefore you can only use a Jira Server (Data Center) connection with event subscription enabled to configure the trigger. 

For information about how to configure a **Jira Server (Data Center) trigger** using a new Jira Server (Data Center) connection, See Configure Jira Server (Data Center) trigger using a new connection

To configure a **Jira Server (Data Center) trigger** using an existing Jira Server (Data Center) connection, perform the following steps:

  1. Click the **Jira Server (Data Center) trigger** element in the integration editor to open the trigger configuration pane.
  2. Click **Configure trigger**.
  3. Provide the following configuration details in the **Connector Event Trigger Editor** page: 
     1. **Region:** Select the region of your Jira Server (Data Center) connection.
     2. **Connection:** Select the Jira Server (Data Center) connection that you want to use. 

Application Integration only displays those Jira Server (Data Center) connections that are active and have an [event subscription](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription) enabled. 

     3. **Event subscription type:** Select the type of event subscription that triggers the integration. For information about the supported event subscription types for this trigger, see Supported event subscription types.
     4. **Service Account** : Select a service account with the required IAM roles for the Jira Server (Data Center) trigger.
  4. Click **Done** to complete the trigger configuration and close the page.



## Configure Jira Server (Data Center) trigger using a new connection

To configure the **Jira Server (Data Center) trigger** using a new Jira Server (Data Center) connection, perform the following steps:

  1. Click the **Jira Server (Data Center) trigger** element in the integration editor to open the trigger configuration pane.
  2. Click **Configure trigger**.
  3. Skip the **Region** field.
  4. Click **Connection** and select the **Create Connection** option from the drop-down menu.
  5. Complete the following steps in the **Create Connection** pane: 
     1. In the **Location** step, choose the location for the new Jira Server (Data Center) connection: 
        1. **Region:** Select a region from the drop-down list. 
        2. Click **Next**.
     2. In the **Connection Details** section, complete the following: 
        1. **Connector** : Select **Jira Server (Data Center)** from the drop down list of available Connectors.
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
        7. **Enable event subscription:** Select to create and enable a new event subscription for the Jira Server (Data Center) connection. You can either only enable event subscriptions or also include connection [entities, operations, and actions](https://docs.cloud.google.com/integration-connectors/docs/entities-operation-action). **Note:** The following additional connection configuration steps are required if you choose to enable [entities, operations, and actions](https://docs.cloud.google.com/integration-connectors/docs/entities-operation-action) for the connection: 
           * Destinations
           * Authentication
        8. Optionally, configure the **Connection node settings** : 

           * **Minimum number of nodes** : Enter the minimum number of connection nodes.
           * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
        9. Optionally, if you want to use SSL, select **Enable SSL**. This displays the SSL configuration details. 
           1. Select a trust store type. It can be either **Public** , **Private** , or **Insecure Connection**. 
           2. Select the certificates as displayed based on your trust store selection.
           3. If you are using mTLS, select the key store certificates in the **Key Store** section.
**Note:**
           * All your certificates must be X.509 certificates and must be in PEM (Privacy Enhanced Mail) format.
           * You can't directly select a certificate when configuring SSL. You must store all your certificates and private keys as a Secret Manager Secret, and then select the required secret during SSL configuration.
        10. Optionally, click **\+ ADD LABEL** to add a label to the Connection in the form of a key/value pair.
        11. Click **NEXT**.
     3. In the **Destinations** section, enter details of the remote host (backend system) you want to connect to. 
        1. **Destination Type** : Select a **Destination Type**. 
           * To specify the destination hostname or IP address, select **Host address** and enter the address in the **host 1** field.
           * To establish a private connection, select **Endpoint attachment**. In the **Endpoint Attachment** list, select the endpoint attachment created for your backend system.
**Note:** To learn how to create an endpoint attachment, see [Private network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). After creating the endpoint attachment, it is visible in the **Endpoint Attachment** list.

If you want to establish a public connection to your backend systems with additional security, you can consider [configuring static outbound IP addresses for your connections](https://docs.cloud.google.com/integration-connectors/docs/configure-static-ip), and then configure your firewall rules to allowlist only the specific static IP addresses. 

To enter additional destinations, click **+ADD DESTINATION**.

     4. Click **NEXT**.
  6. In the **Authentication** section, enter the authentication details. 
     1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Jira Server (Data Center) connection:

        * User password 
        * API Token 
        * Personal Access Token
        * OAuth 2.0 - Authorization code 

To understand how to configure these authentication types, see Configure authentication.

     2. Click **NEXT**.
  7. In the **Event subscription details** section, provide details of the Jira Server (Data Center) account where the event subscriptions will be created. 
     1. **Destination Type:** Select **Host address**.
     2. **Host:** Enter the registration URL of your Jira Server (Data Center) account. Event subscriptions will be created for this URL.
     3. **API token:** Select the Secret Manager secret containing the API token associated with the username.
     4. **Secret version:** Select a secret version.
     5. **Enable data enrichment:** Select this checkbox if you want the Jira Server (Data Center) trigger to retrieve the complete event payload from the Jira Server (Data Center) instance. See Trigger output for examples.
     6. Select **Enable private connectivity** for secured connectivity between your backend application and your connection. If you select this option, you must perform additional configuration steps after creating the connection. For more information, see [Private connectivity for event subscription](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription#psc-eventing). 
     7. Enter the dead-letter configuration. If you configure dead-letter, the connection writes the unprocessed events to the specified [Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/pubsub-basics). Enter the following details: 
        1. **Dead-letter project ID:** The Google Cloud project ID where you have configured the dead-letter Pub/Sub topic.
        2. **Dead-letter topic:** The Pub/Sub topic where you want to write the details of the unprocessed event.
     8. Click **Next**.
  8. **Review** : Review the provided Jira Server (Data Center) connection details.
  9. Click **Create** to complete creating a new Jira Server (Data Center) connection.


* **Event subscription type:** Select the type of event subscription that triggers the integration. For information about the supported event subscription types for this trigger, see Supported event subscription types.
* Click **Done** and close the page. 

The **Jira Server (Data Center) trigger** takes a couple of minutes to complete the event subscription configuration. You can view the status of your event subscription in the trigger configuration pane under **Event Subscription details**.

## Configure authentication

Enter the details based on the authentication you want to use.

  * **User Password**
    * **Username** : Enter the Jira Server (Data Center) user account used to authenticate.
    * **Password** : Enter the password associated with the account.
  * **API Token**
    * **Username** : Enter the Jira Server (Data Center) username used to create the API token.
    * **API token** : Enter the password for the username will be an API token. Select the Secret Manager Secret containing the API token.
  * **Personal Access Token**
    * **Personal access token** : Provide the secret manager secret containing the personal access token.
    * **Secret version** : Select the secret version for the secret selected.
  * **OAuth 2.0 - Authorization code**
    * **Client ID** : Provide the client ID as provided by your external application.
    * **Scopes** : Specify the required permission scopes.
    * **Client secret** : Select the [Secret Manager secret](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart). You must have created the Secret Manager secret before configuring this authorization.
    * **Secret version** : Select the secret manager secret version for client secret.
    * **Authorization URL:** Provide the URL generated during client creation.

For the `Authorization code` authentication type, after creating the connection, you must perform a few additional steps for configuring authentication. For more information, see [Additional steps after connection creation](https://docs.cloud.google.com/integration-connectors/docs/connectors/jiraserverdc/configure#add-steps).

**Note:** If you are using `Authorization code` authentication type and have made any configuration changes in your Jira Server (Data Center) application, you must re-authorize your Jira Server (Data Center) connection. To understand how to re-authorize, see [Re-authorization for Authorization code](https://docs.cloud.google.com/integration-connectors/docs/connectors/jiraserverdc/configure#re-auth). 



## Trigger output

In addition to the event subscription status, the **Event Subscription details** section also displays other details such as connection region, connection name, event subscription name, and more.

### Trigger output variable

For each event, the **Jira Server (Data Center) trigger** generates a `ConnectorEventPayload` output variable which you can use in your downstream tasks. The output variable is in JSON format containing the output Jira Server (Data Center) payload schema. 

#### An example output payload for the ` issue_created` Jira Server (Data Center) event
    
    
        {
          "timestamp": 1744689885826,
          "webhookEvent": "jira:issue_created",
          "issue_event_type_name": "issue_created",
          "user": {
            "self": "https://example.altostrat.com:8443/rest/api/2/user?username=vais_adminpat_user",
            "name": "vais_adminpat_user",
            "key": "JIRAUSER10401",
            "emailAddress": "baklavainthebalkans@gmail.com",
            "avatarUrls": {
              "48x48": "https://www.altostrat.com/avatar/c6e1562d286aa0bff37d0ff6b39b4e29?d=mm&s=48",
              "24x24": "https://www.altostrat.com/avatar/c6e1562d286aa0bff37d0ff6b39b4e29?d=mm&s=24",
              "16x16": "https://www.altostrat.com/avatar/c6e1562d286aa0bff37d0ff6b39b4e29?d=mm&s=16",
              "32x32": "https://www.altostrat.com/avatar/c6e1562d286aa0bff37d0ff6b39b4e29?d=mm&s=32"
            },
            "displayName": "VAIS Admin PAT Jira User",
            "active": true,
            "timeZone": "UTC"
          },
          "issue": {
            "id": "467526",
            "self": "https://example.altostrat.com:8443/rest/api/2/issue/467526",
            "key": "VISP-87",
            "fields": {
              "issuetype": {
                "self": "https://example.altostrat.com:8443/rest/api/2/issuetype/10003",
                "id": "10003",
                "description": "A task that needs to be done.",
                "iconUrl": "https://example.altostrat.com:8443/secure/viewavatar?size=xsmall&avatarId=10318&avatarType=issuetype",
                "name": "Task",
                "subtask": false,
                "avatarId": 10318
              },
              "timespent": null,
              "project": {
                "self": "https://example.altostrat.com:8443/rest/api/2/project/12015",
                "id": "12015",
                "key": "VISP",
                "name": "VAIS Incremental Sync Project",
                "projectTypeKey": "software",
                "avatarUrls": {
                  "48x48": "https://example.altostrat.com:8443/secure/projectavatar?avatarId=10324",
                  "24x24": "https://example.altostrat.com:8443/secure/projectavatar?size=small&avatarId=10324",
                  "16x16": "https://example.altostrat.com:8443/secure/projectavatar?size=xsmall&avatarId=10324",
                  "32x32": "https://example.altostrat.com:8443/secure/projectavatar?size=medium&avatarId=10324"
                }
              },
              "fixVersions": [],
              "customfield_10111": null,
              "aggregatetimespent": null,
              "resolution": null,
              "customfield_10107": "0|i269s7:",
              "customfield_10108": null,
              "customfield_10109": null,
              "resolutiondate": null,
              "workratio": -1,
              "lastViewed": null,
              "watches": {
                "self": "https://example.altostrat.com:8443/rest/api/2/issue/VISP-87/watchers",
                "watchCount": 0,
                "isWatching": false
              },
              "created": "2025-04-15T04:04:45.740+0000",
              "priority": {
                "self": "https://example.altostrat.com:8443/rest/api/2/priority/3",
                "iconUrl": "https://example.altostrat.com:8443/images/icons/priorities/medium.svg",
                "name": "Medium",
                "id": "3"
              },
              "customfield_10100": null,
              "customfield_10101": null,
              "customfield_10102": null,
              "labels": [],
              "customfield_10103": null,
              "timeestimate": null,
              "aggregatetimeoriginalestimate": null,
              "versions": [],
              "issuelinks": [],
              "assignee": null,
              "updated": "2025-04-15T04:04:45.740+0000",
              "status": {
                "self": "https://example.altostrat.com:8443/rest/api/2/status/10000",
                "description": "",
                "iconUrl": "https://example.altostrat.com:8443/",
                "name": "To Do",
                "id": "10000",
                "statusCategory": {
                  "self": "https://example.altostrat.com:8443/rest/api/2/statuscategory/2",
                  "id": 2,
                  "key": "new",
                  "colorName": "default",
                  "name": "To Do"
                }
              },
              "components": [],
              "timeoriginalestimate": null,
              "description": null,
              "timetracking": {},
              "archiveddate": null,
              "attachment": [],
              "aggregatetimeestimate": null,
              "summary": "Test Issue 1e704d97-3f89-452a-b8e2-aaba609f3a79",
              "creator": {
                "self": "https://example.altostrat.com:8443/rest/api/2/user?username=vais_adminpat_user",
                "name": "vais_adminpat_user",
                "key": "JIRAUSER10401",
                "emailAddress": "baklavainthebalkans@gmail.com",
                "avatarUrls": {
                  "48x48": "https://www.altostrat.com/avatar/c6e1562d286aa0bff37d0ff6b39b4e29?d=mm&s=48",
                  "24x24": "https://www.altostrat.com/avatar/c6e1562d286aa0bff37d0ff6b39b4e29?d=mm&s=24",
                  "16x16": "https://www.altostrat.com/avatar/c6e1562d286aa0bff37d0ff6b39b4e29?d=mm&s=16",
                  "32x32": "https://www.altostrat.com/avatar/c6e1562d286aa0bff37d0ff6b39b4e29?d=mm&s=32"
                },
                "displayName": "VAIS Admin PAT Jira User",
                "active": true,
                "timeZone": "UTC"
              },
              "subtasks": [],
              "reporter": {
                "self": "https://example.altostrat.com:8443/rest/api/2/user?username=vais_adminpat_user",
                "name": "vais_adminpat_user",
                "key": "JIRAUSER10401",
                "emailAddress": "baklavainthebalkans@gmail.com",
                "avatarUrls": {
                  "48x48": "https://www.altostrat.com/avatar/c6e1562d286aa0bff37d0ff6b39b4e29?d=mm&s=48",
                  "24x24": "https://www.altostrat.com/avatar/c6e1562d286aa0bff37d0ff6b39b4e29?d=mm&s=24",
                  "16x16": "https://www.altostrat.com/avatar/c6e1562d286aa0bff37d0ff6b39b4e29?d=mm&s=16",
                  "32x32": "https://www.altostrat.com/avatar/c6e1562d286aa0bff37d0ff6b39b4e29?d=mm&s=32"
                },
                "displayName": "VAIS Admin PAT Jira User",
                "active": true,
                "timeZone": "UTC"
              },
              "customfield_10000": "{}",
              "aggregateprogress": {
                "progress": 0,
                "total": 0
              },
              "customfield_10200": null,
              "environment": null,
              "duedate": null,
              "progress": {
                "progress": 0,
                "total": 0
              },
              "comment": {
                "comments": [],
                "maxResults": 0,
                "total": 0,
                "startAt": 0
              },
              "votes": {
                "self": "https://example.altostrat.com:8443/rest/api/2/issue/VISP-87/votes",
                "votes": 0,
                "hasVoted": false
              },
              "worklog": {
                "startAt": 0,
                "maxResults": 20,
                "total": 0,
                "worklogs": []
              },
              "archivedby": null
            }
          }
        }
      

#### An example data enriched output payload for the ` issue_updated` Jira Server (Data Center) event
    
    
          {
            "id": "f655bd2d-d9a9-4e52-bb0b-1453a825bdbe",
            "source": "JiraServer",
            "specVersion": "1",
            "attributes": {
              "action": {
                "ceString": "updated"
              },
              "entityID": {
                "ceString": "467517"
              },
              "entityType": {
                "ceString": "issues"
              },
              "time": {
                "ceTimestamp": "2025-04-14T05:48:58.785330694Z"
              }
            },
            "textData": "{\"changelog\":{\"id\":\"336642\",\"items\":[{\"field\":\"summary\",\"fieldtype\":\"jira\",\"from\":null,\"fromString\":\"New ValueTest2\",\"to\":null,\"toString\":\"New ValueTest3\"}]},\"context-data\":{\"aclInfo\":{\"readers\":[{\"principals\":[{\"user_id\":\"user4.ucs.qatest@altostrat.com\"},{\"user_id\":\"user5.ucs.qatest@altostrat.com\"},{\"user_id\":\"user3.ucs.qatest@altostrat.com\"},{\"user_id\":\"user6.ucs.qatest@altostrat.com\"},{\"user_id\":\"user1.ucs.qatest@altostrat.com\"},{\"user_id\":\"baklavainthebalkans@gmail.com\"},{\"user_id\":\"user2.ucs.qatest@altostrat.com\"},{\"user_id\":\"krishnasr@google.com\"}]}]},\"id\":\"467517\",\"structData\":{\"AffectedVersionsAggregate\":\"\",\"AggregateProgress\":0,\"AggregateTimeEstimate\":null,\"AggregateTimeOriginalEstimate\":null,\"AggregateTimeSpent\":null,\"AssigneeAccountId\":null,\"AssigneeDisplayName\":null,\"AssigneeEmail\":null,\"AssigneeKey\":null,\"AssigneeName\":null,\"ComponentsAggregate\":\"\",\"Created\":\"2025-04-11T15:20:16Z\",\"CreatorAccountId\":null,\"CreatorDisplayName\":\"VAIS Admin PAT Jira User\",\"CreatorEmail\":\"baklavainthebalkans@gmail.com\",\"CreatorKey\":\"JIRAUSER10401\",\"CreatorName\":\"vais_adminpat_user\",\"Description\":null,\"DueDate\":null,\"Environment\":null,\"FixVersionsAggregate\":\"\",\"HasVotes\":false,\"Id\":467517,\"IsWatching\":true,\"IssueLinksAggregate\":\"\",\"IssueTypeId\":\"10003\",\"IssueTypeName\":\"Task\",\"ItemURL\":\"https://34.134.129.75:8443/browse/VISP-78\",\"Key\":\"VISP-78\",\"Labels\":\"\",\"LastViewed\":null,\"OriginalEstimate\":null,\"OriginalEstimateSeconds\":null,\"ParentId\":null,\"ParentIssueTypeId\":null,\"ParentIssueTypeName\":null,\"ParentKey\":null,\"ParentStatusId\":null,\"ParentStatusName\":null,\"PriorityId\":\"3\",\"PriorityName\":\"Medium\",\"ProjectId\":\"12015\",\"ProjectKey\":\"VISP\",\"ProjectName\":\"VAIS Incremental Sync Project\",\"RemainingEstimate\":null,\"RemainingEstimateSeconds\":null,\"ReporterAccountId\":null,\"ReporterDisplayName\":\"VAIS Admin PAT Jira User\",\"ReporterEmail\":\"baklavainthebalkans@gmail.com\",\"ReporterKey\":\"JIRAUSER10401\",\"ReporterName\":\"vais_adminpat_user\",\"ResolutionDate\":null,\"ResolutionDescription\":null,\"ResolutionId\":null,\"ResolutionName\":null,\"SecurityLevel\":null,\"StatusCategoryId\":2,\"StatusCategoryKey\":\"new\",\"StatusCategoryName\":\"To Do\",\"StatusId\":\"10000\",\"StatusName\":\"To Do\",\"SubtasksAggregate\":\"\",\"Summary\":\"New ValueTest3\",\"TimeSpent\":null,\"TimeSpentSeconds\":null,\"TotalProgress\":0,\"Updated\":\"2025-04-14T05:48:58Z\",\"Votes\":0,\"WatchCount\":1,\"WorkRatio\":-1}},\"issue\":{\"fields\":{\"aggregateprogress\":{\"progress\":0,\"total\":0},\"aggregatetimeestimate\":null,\"aggregatetimeoriginalestimate\":null,\"aggregatetimespent\":null,\"archivedby\":null,\"archiveddate\":null,\"assignee\":null,\"attachment\":[],\"comment\":{\"comments\":[],\"maxResults\":0,\"startAt\":0,\"total\":0},\"components\":[],\"created\":\"2025-04-11T15:20:16.000+0000\",\"creator\":{\"active\":true,\"avatarUrls\":{\"16x16\":\"https://www.altostrat.com/avatar/c6e1562d286aa0bff37d0ff6b39b4e29?d=mm\\u0026s=16\",\"24x24\":\"https://www.altostrat.com/avatar/c6e1562d286aa0bff37d0ff6b39b4e29?d=mm\\u0026s=24\",\"32x32\":\"https://www.altostrat.com/avatar/c6e1562d286aa0bff37d0ff6b39b4e29?d=mm\\u0026s=32\",\"48x48\":\"https://www.altostrat.com/avatar/c6e1562d286aa0bff37d0ff6b39b4e29?d=mm\\u0026s=48\"},\"displayName\":\"VAIS Admin PAT Jira User\",\"emailAddress\":\"baklavainthebalkans@gmail.com\",\"key\":\"JIRAUSER10401\",\"name\":\"vais_adminpat_user\",\"self\":\"https://example.altostrat.com:8443/rest/api/2/user?username=vais_adminpat_user\",\"timeZone\":\"UTC\"},\"customfield_10000\":\"{}\",\"customfield_10100\":null,\"customfield_10101\":null,\"customfield_10102\":null,\"customfield_10103\":null,\"customfield_10107\":\"0|i269q7:\",\"customfield_10108\":null,\"customfield_10109\":null,\"customfield_10111\":null,\"customfield_10200\":null,\"description\":null,\"duedate\":null,\"environment\":null,\"fixVersions\":[],\"issuelinks\":[],\"issuetype\":{\"avatarId\":10318,\"description\":\"A task that needs to be done.\",\"iconUrl\":\"https://example.altostrat.com:8443/secure/viewavatar?size=xsmall\\u0026avatarId=10318\\u0026avatarType=issuetype\",\"id\":\"10003\",\"name\":\"Task\",\"self\":\"https://example.altostrat.com:8443/rest/api/2/issuetype/10003\",\"subtask\":false},\"labels\":[],\"lastViewed\":null,\"priority\":{\"iconUrl\":\"https://example.altostrat.com:8443/images/icons/priorities/medium.svg\",\"id\":\"3\",\"name\":\"Medium\",\"self\":\"https://example.altostrat.com:8443/rest/api/2/priority/3\"},\"progress\":{\"progress\":0,\"total\":0},\"project\":{\"avatarUrls\":{\"16x16\":\"https://example.altostrat.com:8443/secure/projectavatar?size=xsmall\\u0026avatarId=10324\",\"24x24\":\"https://example.altostrat.com:8443/secure/projectavatar?size=small\\u0026avatarId=10324\",\"32x32\":\"https://example.altostrat.com:8443/secure/projectavatar?size=medium\\u0026avatarId=10324\",\"48x48\":\"https://example.altostrat.com:8443/secure/projectavatar?avatarId=10324\"},\"id\":\"12015\",\"key\":\"VISP\",\"name\":\"VAIS Incremental Sync Project\",\"projectTypeKey\":\"software\",\"self\":\"https://example.altostrat.com:8443/rest/api/2/project/12015\"},\"reporter\":{\"active\":true,\"avatarUrls\":{\"16x16\":\"https://www.altostrat.com/avatar/c6e1562d286aa0bff37d0ff6b39b4e29?d=mm\\u0026s=16\",\"24x24\":\"https://www.altostrat.com/avatar/c6e1562d286aa0bff37d0ff6b39b4e29?d=mm\\u0026s=24\",\"32x32\":\"https://www.altostrat.com/avatar/c6e1562d286aa0bff37d0ff6b39b4e29?d=mm\\u0026s=32\",\"48x48\":\"https://www.altostrat.com/avatar/c6e1562d286aa0bff37d0ff6b39b4e29?d=mm\\u0026s=48\"},\"displayName\":\"VAIS Admin PAT Jira User\",\"emailAddress\":\"baklavainthebalkans@gmail.com\",\"key\":\"JIRAUSER10401\",\"name\":\"vais_adminpat_user\",\"self\":\"https://example.altostrat.com:8443/rest/api/2/user?username=vais_adminpat_user\",\"timeZone\":\"UTC\"},\"resolution\":null,\"resolutiondate\":null,\"status\":{\"description\":\"\",\"iconUrl\":\"https://example.altostrat.com:8443/\",\"id\":\"10000\",\"name\":\"To Do\",\"self\":\"https://example.altostrat.com:8443/rest/api/2/status/10000\",\"statusCategory\":{\"colorName\":\"default\",\"id\":2,\"key\":\"new\",\"name\":\"To Do\",\"self\":\"https://example.altostrat.com:8443/rest/api/2/statuscategory/2\"}},\"subtasks\":[],\"summary\":\"New ValueTest3\",\"timeestimate\":null,\"timeoriginalestimate\":null,\"timespent\":null,\"timetracking\":{},\"updated\":\"2025-04-14T05:48:58.000+0000\",\"versions\":[],\"votes\":{\"hasVoted\":false,\"self\":\"https://example.altostrat.com:8443/rest/api/2/issue/VISP-78/votes\",\"votes\":0},\"watches\":{\"isWatching\":true,\"self\":\"https://example.altostrat.com:8443/rest/api/2/issue/VISP-78/watchers\",\"watchCount\":1},\"worklog\":{\"maxResults\":20,\"startAt\":0,\"total\":0,\"worklogs\":[]},\"workratio\":-1},\"id\":\"467517\",\"key\":\"VISP-78\",\"self\":\"https://example.altostrat.com:8443/rest/api/2/issue/467517\"},\"issue_event_type_name\":\"issue_updated\",\"timestamp\":1744609737983,\"user\":{\"active\":true,\"avatarUrls\":{\"16x16\":\"https://www.altostrat.com/avatar/c6e1562d286aa0bff37d0ff6b39b4e29?d=mm\\u0026s=16\",\"24x24\":\"https://www.altostrat.com/avatar/c6e1562d286aa0bff37d0ff6b39b4e29?d=mm\\u0026s=24\",\"32x32\":\"https://www.altostrat.com/avatar/c6e1562d286aa0bff37d0ff6b39b4e29?d=mm\\u0026s=32\",\"48x48\":\"https://www.altostrat.com/avatar/c6e1562d286aa0bff37d0ff6b39b4e29?d=mm\\u0026s=48\"},\"displayName\":\"VAIS Admin PAT Jira User\",\"emailAddress\":\"baklavainthebalkans@gmail.com\",\"key\":\"JIRAUSER10401\",\"name\":\"vais_adminpat_user\",\"self\":\"https://example.altostrat.com:8443/rest/api/2/user?username=vais_adminpat_user\",\"timeZone\":\"UTC\"},\"webhookEvent\":\"jira:issue_updated\"}"
          }
        

## Edit Jira Server (Data Center) trigger

You can edit a **Jira Server (Data Center) trigger** to change or update the connection configuration and event subscription details.

**Important:** When you edit or modify a Jira Server (Data Center) trigger, you can either retain the previously configured event subscription that is attached to the trigger, or you can delete it. Deleting an event subscription will affect all the published integrations using that event subscription. 

To edit a Jira Server (Data Center) trigger, perform the following steps:

  1. Click the **Jira Server (Data Center) trigger** element in the integration editor to open the trigger configuration pane.
  2. Click **Configure Jira Server (Data Center) trigger**.
  3. Do the following in the **Connector Event Trigger Editor** page: 
     1. To retain the previously configured event subscription, click **Retain** , else click **Delete**. **Warning:** Deleting an event subscription will affect all the published integrations using the event subscription. This task cannot be undone.
     2. Update the connection configuration and event subscription details as desired.
     3. Click **Done**.

You can view the updated connection and event subscription details in the trigger configuration pane under **Event Subscription details**.




## Supported event subscription types

You can use the **Jira Server (Data Center) trigger** to invoke an integration for the following event subscription types:

Event subscription types | Description  
---|---  
issue_created  | Issue is created   
issued_deleted  | Issue is deleted   
issued_updated  | Issue is updated   
board_created  | Board is created.   
borard_deleted  | Board is deleted   
board_updated  | Board is updated   
comment_created  | Comment is created   
comment_deleted  | Comment is deleted   
comment_updated  | Comment is updated   
project_Created  | Project is created   
project_deleted  | Project is deleted   
project_updated  | Project is updated   
sprint_closed  | Sprint is closed   
sprint_deleted  | Sprint is deleted   
sprint_updated  | Sprint is updated   
sprint_created  | Sprint is created   
sprint_started  | Sprint is started   
user_Created  | User is created   
user_updated  | User is updated   
user_deleted  | User is deleted   
worklog_created  | Worklog is created   
worklog_deleted  | Worklog is deleted   
worklog_updated  | Worklog is updated   
  
## Quotas and limits

For information about quotas and limits, see [Quotas and limits](https://docs.cloud.google.com/application-integration/docs/quotas).

## What's next

  * Learn about [all tasks and triggers](https://docs.cloud.google.com/application-integration/docs/all-triggers-tasks).
  * Learn how to [test and publish an integration](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations).
  * Learn about [error handling](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy).
  * Learn about [integration execution logs](https://docs.cloud.google.com/application-integration/docs/introduction-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
