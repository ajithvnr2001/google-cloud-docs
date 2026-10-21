---
url: https://docs.cloud.google.com/integration-connectors/docs/eventsubscription/
title: Event subscriptions \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:41:34.210507+00:00
---

# Event subscriptions  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/eventsubscription/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Event subscriptions

Apart from letting you to perform read and write operations on your backend, Integration Connectors also let you subscribe to events that occur in your backend applications. For example, consider you want to get notified when a new Jira ticket is created. You can accomplish this by configuring the Jira Cloud connector for event subscriptions. By using the event subscriptions along with [Application Integration](https://docs.cloud.google.com/application-integration/docs/overview), you can create useful integrations to address your business needs. For more information, see Use event subscriptions in your integrations

**Note:** If you are setting up a [VPC service perimeter](https://docs.cloud.google.com/integration-connectors/docs/vpcsc-connectors) for your Google Cloud project, you must enable private connectivity for event subscriptions.

## Enable event subscriptions in connections

A connection that you create can be used for any of the following purposes:

  * For performing connector operations (entities and actions) only
  * For event subscriptions only
  * For performing connector operations and event subscriptions



The option to enable event subscriptions and configure event related details are available to you during [connection creation](https://docs.cloud.google.com/integration-connectors/docs/manage-connectors#create-a-connection). However, if you already have an existing connection and want to re-purpose it for event subscription, you can do so by [editing and re-configuring](https://docs.cloud.google.com/integration-connectors/docs/manage-connectors#edit-a-connection) the connection.

The following connectors support event subscriptions:

  * [Apache Kafka](https://docs.cloud.google.com/integration-connectors/docs/connectors/apachekafka/configure)
  * [Azure AD (Entra ID)](https://docs.cloud.google.com/integration-connectors/docs/connectors/azuread/configure)
  * [Hubspot](https://docs.cloud.google.com/integration-connectors/docs/connectors/hubspot/configure)
  * [HL7](https://docs.cloud.google.com/integration-connectors/docs/connectors/hl7/configure)
  * [IBM MQ](https://docs.cloud.google.com/integration-connectors/docs/connectors/ibmmq/configure)
  * [Jira Cloud](https://docs.cloud.google.com/integration-connectors/docs/connectors/jiracloud/configure#configure-event)
  * [Jira Server Data Center](https://docs.cloud.google.com/integration-connectors/docs/connectors/jiraserverdc/configure#configure-event)
  * [Rabbit MQ](https://docs.cloud.google.com/integration-connectors/docs/connectors/rabbitmq/configure)
  * [SAP Gateway](https://docs.cloud.google.com/integration-connectors/docs/connectors/sapgateway/configure)
  * [SAP ERP](https://docs.cloud.google.com/integration-connectors/docs/connectors/saperp/configure)
  * [ServiceNow](https://docs.cloud.google.com/integration-connectors/docs/connectors/servicenow/configure#configure-event)
  * [Solace](https://docs.cloud.google.com/integration-connectors/docs/connectors/solace/configure)
  * [TIBCOEMS](https://docs.cloud.google.com/integration-connectors/docs/connectors/tibcoems/configure)
  * [Webhook](https://docs.cloud.google.com/integration-connectors/docs/connectors/webhook/configure#configure-event)
  * [Zendesk](https://docs.cloud.google.com/integration-connectors/docs/connectors/zendesk/configure#configure-event)



## Data enrichment in event notifications

You can configure a connection to append additional information in an event notification response. The additional information is specific to the entity for which you have configured the event. To get the additional information, you must enable **Data enrichment** in your connection.

For example, if you have subscribed for a ticket creation event in Zendesk, you will be notified when a ticket gets created. However, the event notification payload consists only the basic ticket details. Additional details such as ticket description, assignee, and status aren't present in the payload. To get these additional details of the `ticket` entity, you must enable data enrichment in a Zendesk connection. For more information, see [Configure event subscription](https://docs.cloud.google.com/integration-connectors/docs/connectors/zendesk/configure#exp1). The following samples show the response payload without and with data enrichment.

### Payload without data enrichment

The following sample shows the Zendesk's create ticket event's response payload without data enrichment.
    
    
    {
      "account_id": 12345,
      "integration_key": "my_integration_key",
      "subdomain": "my_zendesk_subdomain",
      "input": {
        "ticket_event": {
          "meta": {
            "version": "1.0",
    ....
    ....
            "position": 1,
              "total": 9
            }
          },
          "type": "Ticket Created",
          "ticket": {
            "id": 35436,
    ....
    ....
            "external_id": "TEST1234",
            "tags": [
              "enterprise"
            ],
            "via": {
              "channel": "web"
            }
          }
        }
      }

### Payload with data enrichment

The following sample shows the Zendesk's create ticket event's response payload with data enrichment.
    
    
    {
        **"context-data"** : {
        "AllowChannelback": false,
        "Assignee": null,
        "AssigneeId": 1.6696812051473E13,
        "Brand": null,
        "BrandId": 1.6696812163985E13,
        "Cc": null,
        "CollaboratorIds": null,
        "Commenter": null,
        "HasAttachment": null,
        "CreatedAt": "2023-07-08 11:37:19.0",
        "CustomFields": null,
        "Description": "Test desc 2",
    ....
    ....
        "Status": "open",
        "Subject": "Test Zendesk Ticket Created -2 -DA",
        "Submitter": null,
        "SubmitterId": 1.6696812051473E13,
        "Tags": "tag-changed-after-cache,ticket-created",
    ....
    ....
        "ViaChannel": "web",
        "ViaFollowupSourceId": null,
        "ViaSource": "{\r\n  \"from\": null,\r\n  \"to\": null,\r\n  \"rel\": null\r\n}",
        "View_Id": null
      },
       "data":{
      "account_id": 12345,
      "integration_key": "my_integration_key",
      "subdomain": "my_zendesk_subdomain",
      "input": {
        "ticket_event": {
          "meta": {
            "version": "1.0",
    ....
    ....
            "position": 1,
              "total": 9
            }
          },
          "type": "Ticket Created",
          "ticket": {
            "id": 35436,
    ....
    ....
            "external_id": "TEST1234",
            "tags": [
              "enterprise"
            ],
            "via": {
              "channel": "web"
            }
          }
        }
      }
     }

**Note:**

  * If you have enabled data enrichment, the response payload contains the **context-data** field in addition to the normal response that you would have got without data enrichment. In the previous example, the **context-data** field contains additional details of the newly created ticket in Zendesk.
  * Only the [Zendesk](https://docs.cloud.google.com/integration-connectors/docs/connectors/zendesk/configure#configure-event) connector supports data enrichment for event notifications.



## Private connectivity for event subscription

For enhanced security, you can configure private connectivity between your backend application and your connection. In private connectivity, the event listener of your connection will not be made public directly. Instead, you must allow ingress network traffic to the event listener through a PSC service attachment that will be provided to you by Integration Connectors. 

During connection creation, if you have selected **Enable private connectivity** for event subscription, Integration Connectors creates a [PSC service attachment](https://docs.cloud.google.com/vpc/docs/private-service-connect#service-attachments). You must expose the PSC service attachment to your backend application by using any approach that is sutiable to you. One possible approach is to use the PSC service attachment in a load balancer, and then configure the load balancer to accept events from your backend application. The connection then listens to your backend's events on the load balancer's address. The following high-level steps show how you can use a load balancer to configure private connectivity:

  1. Go to the connection details page of the newly created connection.
  2. Click **Edit ingress endpoint**. This shows the **Event subscription settings** pane.
  3. Copy the service attachment name as displayed in the **PSC service attachment name** field.
  4. Create a [PSC network endpoint group](https://docs.cloud.google.com/load-balancing/docs/negs) pointing to the service attachment that you got in the previous step.
  5. Create an [external load balancer](https://docs.cloud.google.com/iap/docs/load-balancer-howto) with the PSC network endpoint group created in the previous step as the backend. **Tip:** If you already have an external load balancer, you can use it to configure private connectivity, instead of creating a new one.
  6. Configure the load balancer to accept requests from your event provider's (backend application) IP address. 

The subsequent setps (7 to 11) are applicable only in connectors whose backend supports auto-registration of event subscription. For example, Zendesk, and Jira.

  7. Go to the connection details page of the newly created connection.
  8. Click **Edit ingress endpoint**. This shows the **Event subscription settings** pane.
  9. Enter the address of the load balancer in the **Event listener ingress endpoint** field.
  10. Click **Done**.
  11. Click **Save** to save the changes to the connection.



## Use event subscriptions in your integrations

When you use event subscriptions along with your integrations, you can create integrations to solve your complex business problems. For example, you can start the execution of your entire integration based on a ServiceNow event. Application Integration provides the following triggers that listen to event notifications from your backend applications:

  * [Azure AD trigger](https://docs.cloud.google.com/application-integration/docs/configure-azuread-trigger) \- Listens for Azure AD events.
  * [HL7 trigger](https://docs.cloud.google.com/application-integration/docs/configure-hl7mllp-trigger) \- Listens for HL7 events.
  * [HubSpot trigger](https://docs.cloud.google.com/application-integration/docs/configure-hubspot-trigger) \- Listens for HubSpot events.
  * [IBM MQ trigger](https://docs.cloud.google.com/application-integration/docs/configure-ibmmq-trigger) \- Listens for IBM MQ events.
  * [Jira Cloud trigger](https://docs.cloud.google.com/application-integration/docs/configure-jira-cloud-trigger) \- Listens for Jira Cloud events.
  * [Rabbit MQ trigger](https://docs.cloud.google.com/application-integration/docs/configure-rabbitmq-trigger) \- Listens for Rabbit MQ events.
  * [ServiceNow trigger](https://docs.cloud.google.com/application-integration/docs/configure-servicenow-trigger) \- Listens for ServiceNow events.
  * [TIBCOEMS trigger](https://docs.cloud.google.com/application-integration/docs/configure-tibcoems-trigger) \- Listens for TIBCOEMS events.
  * [Webhook trigger](https://docs.cloud.google.com/application-integration/docs/configure-webhook-trigger) \- Listens for generic webhook events.
  * [Zendesk trigger](https://docs.cloud.google.com/application-integration/docs/configure-zendesk-trigger) \- Listens for Zendesk events.



To configure the triggers, you must enable event subscription for your connections. You can either enable the event subscription in an existing connection, or in a new connection. For detailed steps on how to configure these Application Integration triggers, see the corresponding trigger documentation.

## View active subscriptions

When you use an event subscription in your application integration, Integration Connectors creates an entry for the subscription in the corresponding connection. To view all the subscriptions for a connection, perform the following steps:

  1. Open the all Connections page for your Google Cloud project. 

[ Go to the Connections page](https://console.cloud.google.com/connectors/connections)

  2. Click the connection for which you want to view the subscriptions. 

This opens the **Connection Details** page.

  3. Click the **Subscriptions** tab. 

This displays all the subscriptions for the connection. A subscription listed on this page can be in any of the following states:

     * **Creating** \- The subscription is being created by an integration.
     * **Active** \- The subscription is valid and functioning.
     * **Suspended** \- The connection is in a [suspended state](https://docs.cloud.google.com/integration-connectors/docs/suspend-resume-connection#suspend-a-connection).
     * **Error** \- The subscription creation is unsuccessful. For example, authentication failure during subscription creation.

**Note:** If a connection has active event subscriptions, you can't delete the connection, or edit the backend's hostname or IP address of the connection. 

## Pricing for event subscription

The data (event payload) processed for event subscriptions in the preview triggers, isn't charged. However, you will be charged for event subscription data processed in a generally available triggers.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
