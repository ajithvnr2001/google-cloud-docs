---
url: https://docs.cloud.google.com/application-integration/docs/configure-zendesk-trigger/
title: Zendesk trigger \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:39:02.121350+00:00
---

# Zendesk trigger  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/configure-zendesk-trigger/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Zendesk trigger

The **Zendesk trigger** is a [Connector Event trigger](https://docs.cloud.google.com/application-integration/docs/triggers#event-triggers) that lets you invoke an integration based on the Zendesk events that you've subscribed to in your Zendesk connection.

**Important:** Integration Connectors is a billable component of Google Cloud. For information about the costs and charges of using Integration Connectors, see [Integration Connectors pricing](https://docs.cloud.google.com/integration-connectors/docs/pricing).

## Before you begin

If you plan to create or configure a new connection for the **Zendesk trigger** , make sure that you have the following IAM role on the project:

  * Connector Admin (`roles/connectors.admin`) 

For information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).




Grant the following IAM roles to the service account that you want to use for the **Zendesk trigger** :

  * Application Integration Invoker (`roles/integrations.integrationInvoker`) 

For information about granting roles to a service account, see [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).




## Add the Zendesk trigger

To add a **Zendesk trigger** to your integration, perform the following steps: 

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**

The **Integrations List** page appears listing all the integrations available in the Google Cloud project. 

  3. Select an existing integration or click **Create integration** to create a new one. 

If you are creating a new integration: 

     1. Enter a name and description in the **Create Integration** pane.
     2. Select a region for the integration. **Note:** The **Regions** dropdown only lists the regions provisioned in your Google Cloud project. To provision a new region, Click **Enable Region**. See [Enable new region](https://docs.cloud.google.com/application-integration/docs/enable-new-region) for more information. 
     3. Select a service account for the integration. You can change or update the service account details of an integration any time from the info **Integration summary** pane in the integration toolbar. **Note:** The option to select a service account is displayed only if you have enabled integration governance for the selected region. 
     4. Click **Create**.

The newly created integration opens in the _integration editor_. 

  4. In the _integration editor_ navigation bar, click **Triggers** to view the list of available triggers. 
  5. Click and place the **Zendesk trigger** element in the integration editor.

To configure the **Zendesk trigger** , you can either use an existing Zendesk connection available in Integration Connectors, or create a new Zendesk connection using the inline connection creation option.




## Configure Zendesk trigger using an existing connection

You can configure the **Zendesk trigger** using an existing Zendesk connection in Integration Connectors. Note that the **Zendesk trigger** is an [Connector Event trigger](https://docs.cloud.google.com/application-integration/docs/triggers#event-triggers), therefore you can only use a Zendesk connection with event subscription enabled to configure the trigger. 

For information about how to configure a **Zendesk trigger** using a new Zendesk connection, See Configure Zendesk trigger using a new connection

To configure a **Zendesk trigger** using an existing Zendesk connection, perform the following steps:

  1. Click the **Zendesk trigger** element in the integration editor to open the trigger configuration pane.
  2. Click **Configure trigger**.
  3. Provide the following configuration details in the **Connector Event Trigger Editor** page: 
     1. **Region:** Select the region of your Zendesk connection.
     2. **Connection:** Select the Zendesk connection that you want to use. 

Application Integration only displays those Zendesk connections that are active and have an event subscription enabled. 

     3. **Event subscription type:** Select the type of event subscription that triggers the integration. For information about the supported event subscription types for this trigger, see Supported event subscription types.
     4. **Service Account** : Select a service account with the required IAM roles for the Zendesk trigger.
  4. Click **Done** to complete the trigger configuration and close the page.



## Configure Zendesk trigger using a new connection

To configure the **Zendesk trigger** using a new Zendesk connection, perform the following steps:

  1. Click the **Zendesk trigger** element in the integration editor to open the trigger configuration pane.
  2. Click **Configure trigger**.
  3. Skip the **Region** field.
  4. Click **Connection** and select the **Create Connection** option from the drop-down menu.
  5. Complete the following steps in the **Create Connection** pane: 
     1. In the **Location** step, choose the location for the new Zendesk connection: 
        1. **Region:** Select a region from the drop-down list. 
        2. Click **Next**.
     2. In the **Connection Details** step, provide details about the new Zendesk connection: 
        1. **Connector version:** Choose an available version of the Zendesk connector from the drop-down list. 
        2. **Connection Name:** Enter a name for the Zendesk connection. **Note:** Connection names must meet the following criteria: 
           * Connection names can use letters, numbers, or hyphens.
           * Letters must be lower-case.
           * Connection names must begin with a letter and end with a letter or number.
           * Connection names cannot exceed 63 characters.
        3. (Optional) **Description:** Enter a description for the connection.
        4. (Optional) **Enable Cloud Logging:** Select this checkbox to store all log data of the connection.
        5. **Service Account** : Select a service account with the required IAM roles for the Zendesk connection.
        6. **Enable event subscription:** Select to create and enable a new event subscription for the Zendesk connection. You can either only enable event subscriptions or also include connection [entities, operations, and actions](https://docs.cloud.google.com/integration-connectors/docs/entities-operation-action). **Note:** The following additional connection configuration steps are required if you choose to enable [entities, operations, and actions](https://docs.cloud.google.com/integration-connectors/docs/entities-operation-action) for the connection: 
           * Destinations
           * Authentication
        7. (Optional) Expand **Advanced settings** to configure the connection node settings. 

For more information about the connection node settings for Zendesk, see the [Zendesk connection](https://docs.cloud.google.com/integration-connectors/docs/connectors/zendesk/configure) documentation. 

        8. (Optional) Click **\+ Add label** to add a label to the connection in the form of a key-value pair.
        9. Click **Next**.
     3. In the **Destinations** step, provide the Zendesk instance details: 
        1. **Destination Type:** Select **Host address**.
        2. **Host:** Enter the hostname or IP address of your Zendesk instance.
        3. Click **Next**.
     4. In the **Authentication** step, provide the authentication details for the Zendesk instance: 
        1. Select your desired authentication type and enter the relevant details to access the provided Zendesk host URL. 

To understand how to configure these authentication types, see [Configure authentication](https://docs.cloud.google.com/integration-connectors/docs/connectors/zendesk/configure#configure-auth).

        2. Click **Next**.
     5. In the **Event subscription details** step, provide details of the Zendesk instance where the event subscriptions will be created. 
        1. **Destination Type:** Select **Host address**.
        2. **Host:** Enter the registration URL of your Zendesk instance. Event subscriptions will be created for this URL.
        3. **Username:** Enter the username to access the provided registration URL.
        4. **Password:** Select the Secret Manager secret containing the password associated with the username.
        5. **Secret version:** Select a secret version.
        6. **Enable data enrichment:** Select this checkbox if you want the **Zendesk trigger** to retrieve the complete event payload from the Zendesk instance. See Trigger output for examples.
        7. Click **Next**.
     6. **Review** : Review the provided Zendesk connection details.
     7. Click **Create** to complete creating a new Zendesk connection.
  6. **Event subscription type:** Select the type of event subscription that triggers the integration. For information about the supported event subscription types for this trigger, see Supported event subscription types.
  7. Click **Done** and close the page.



## Trigger output

The **Zendesk trigger** takes a couple of minutes to complete the event subscription configuration. You can view the status of your event subscription in the trigger configuration pane under **Event Subscription details**.

The **Zendesk trigger** indicates the status of an event subscription using the following states:

  * restart_alt `Creating`: Indicates that the trigger is subscribing to the event subscription. 
  * check_circle `Active`: Indicates that the trigger is successfully subscribed to an event subscription.
  * error `Error`: Indicates that the there is an issue with the configured event subscription. 



In addition to the event subscription status, the **Event Subscription details** section also displays other details such as connection region, connection name, event subscription name, and more.

The following image shows a sample layout of the Zendesk trigger configuration pane:

![image showing Zendesk trigger configuration pane](https://docs.cloud.google.com/static/application-integration/images/zendesk_trigger_1.png)![image showing Zendesk trigger configuration pane](https://docs.cloud.google.com/static/application-integration/images/zendesk_trigger_1.png)

### Trigger output variable

For each event, the **Zendesk trigger** generates a `ConnectorEventPayload` output variable which you can use in your downstream tasks. The output variable is in JSON format containing the output Zendesk payload schema. 

#### Example 1: Output payload for the Zendesk event: **Agent Assignment Changed**
    
    
      {
        "description": "The root schema of event that has occurred in Zendesk.",
        "type": "object",
        "properties": {
            "data": {
        "description": "",
        "type": "object",
        "properties": {
            "accountId": {
                "description": "Zendesk account ID.",
                "type": "number",
                "readOnly": false
            },
            "integration_key": {
                "description": "Integration Key retrieved from ZIS bundle.",
                "type":  "string",
                "readOnly": false
            },
            "subdomain": {
                "description": "Account subdomain.",
                "type":  "string",
                "readOnly": false
            },
            "input": {
                "description": "Contains information about events changes.",
                "type": "object",
                "properties": {
                    "ticket_event": {
                        "description": "Type of event is ticket event.",
                        "type": "object",
                        "properties": {
                            "meta": {
                                "description": "Metadata about the ticket.",
                                "type": "object",
                                "properties": {
                                    "version": {
                                        "description": "Event version",
                                        "type":  ["string", "null"]
                                    },
                                    "occurred_at": {
                                        "description": "Timestamp when the event occurred.",
                                        "type":  "string"
                                    },
                                    "ref": {
                                        "description": "Reference ID",
                                        "type":  ["string", "null"]
                                    },
                                    "sequence": {
                                        "description": "Sequence of Occurrence",
                                        "type": "object",
                                        "properties": {
                                            "id": {
                                                "description": "",
                                                "type":  ["string", "null"]
                                            },
                                            "position": {
                                                "description": "",
                                                "type": ["number","null"]
                                            },
                                            "total": {
                                                "description": "",
                                                "type": ["number","null"]
                                            }
                                        }
                                    }
                                }
                            },
                            "type": {
                                "description": "Type of Ticket Event ",
                                "type":  "string"
                            },
                            "previous": {
                                "description": "Previous ID",
                                "type": ["number","null"]
                            },
                            "current": {
                                "description": "Current ID",
                                "type": ["number","null"]
                            },
                            "ticket": {
                                "description": "Properties related to the ticket",
                                "type": "object",
                                "properties": {
                                    "id": {
                                        "description": "Ticket ID",
                                        "type": "number"
                                    },
                                    "created_at": {
                                        "description": "Timestamp of ticket creation.",
                                        "type":  "string"
                                    },
                                    "updated_at": {
                                        "description": "Timestamp of ticket updation.",
                                        "type":  "string"
                                    },
                                    "type": {
                                        "description": "Type of ticket",
                                        "type":  ["string", "null"]
                                    },
                                    "priority": {
                                        "description": "Priority of ticket.",
                                        "type":  ["string", "null"]
                                    },
                                    "status": {
                                        "description": "Status of the ticket.",
                                        "type":  ["string", "null"]
                                    },
                                    "requester_id": {
                                        "description": "ID of the ticket requestor.",
                                        "type": ["number","null"]
                                    },
                                    "submitter_id": {
                                        "description": "ID of the ticket submitter.",
                                        "type": ["number","null"]
                                    },
                                    "assignee_id": {
                                        "description": "ID of the ticket assignee.",
                                        "type": ["number","null"]
                                    },
                                    "organization_id": {
                                        "description": "ID of the organization ticket belongs to.",
                                        "type": ["number","null"]
                                    },
                                    "group_id": {
                                        "description": "ID of the group ticket belongs to.",
                                        "type": ["number","null"]
                                    },
                                    "brand_id": {
                                        "description": "ID of the brand ticket belongs to",
                                        "type": ["number","null"]
                                    },
                                    "form_id": {
                                        "description": "ID of the form associated with the ticket.",
                                        "type": ["number","null"]
                                    },
                                    "external_id": {
                                        "description": "",
                                        "type":  ["string", "null"]
                                    },
                                    "tags": {
                                        "description": "Tags associated with the ticket.",
                                        "type": "array",
                                        "items": {
                                            "description": "",
                                            "type":  ["string", "null"]
                                        }
                                    },
                                    "via": {
                                        "description": "Channel via which change was made.",
                                        "type": "object",
                                        "properties": {
                                            "channel": {
                                                "description": "",
                                                "type":  "string"
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "readOnly": false
            }
        }
    }
    }
    }

#### Example 2: Data enriched output payload for the Zendesk event: **Agent Assignment Changed**
    
    
        {
          "description": "The root schema of event that has occurred in Zendesk.",
          "type": "object",
          "properties": {
            "data": {
              "description": "",
              "type": "object",
              "properties": {
                "accountId": {
                  "description": "Zendesk account ID.",
                  "type": "number",
                  "readOnly": false
                },
                "integration_key": {
                  "description": "Integration Key retrieved from ZIS bundle.",
                  "type": "string",
                  "readOnly": false
                },
                "subdomain": {
                  "description": "Account subdomain.",
                  "type": "string",
                  "readOnly": false
                },
                "input": {
                  "description": "Contains information about events changes.",
                  "type": "object",
                  "properties": {
                    "ticket_event": {
                      "description": "Type of event is ticket event.",
                      "type": "object",
                      "properties": {
                        "meta": {
                          "description": "Metadata about the ticket.",
                          "type": "object",
                          "properties": {
                            "version": {
                              "description": "Event version",
                              "type": [
                                "string",
                                "null"
                              ]
                            },
                            "occurred_at": {
                              "description": "Timestamp when the event occurred.",
                              "type": "string"
                            },
                            "ref": {
                              "description": "Reference ID",
                              "type": [
                                "string",
                                "null"
                              ]
                            },
                            "sequence": {
                              "description": "Sequence of Occurrence",
                              "type": "object",
                              "properties": {
                                "id": {
                                  "description": "",
                                  "type": [
                                    "string",
                                    "null"
                                  ]
                                },
                                "position": {
                                  "description": "",
                                  "type": [
                                    "number",
                                    "null"
                                  ]
                                },
                                "total": {
                                  "description": "",
                                  "type": [
                                    "number",
                                    "null"
                                  ]
                                }
                              }
                            }
                          }
                        },
                        "type": {
                          "description": "Type of Ticket Event ",
                          "type": "string"
                        },
                        "previous": {
                          "description": "Previous ID",
                          "type": [
                            "number",
                            "null"
                          ]
                        },
                        "current": {
                          "description": "Current ID",
                          "type": [
                            "number",
                            "null"
                          ]
                        },
                        "ticket": {
                          "description": "Properties related to the ticket",
                          "type": "object",
                          "properties": {
                            "id": {
                              "description": "Ticket ID",
                              "type": "number"
                            },
                            "created_at": {
                              "description": "Timestamp of ticket creation.",
                              "type": "string"
                            },
                            "updated_at": {
                              "description": "Timestamp of ticket updation.",
                              "type": "string"
                            },
                            "type": {
                              "description": "Type of ticket",
                              "type": "string"
                            },
                            "priority": {
                              "description": "Priority of ticket.",
                              "type": [
                                "string",
                                "null"
                              ]
                            },
                            "status": {
                              "description": "Status of the ticket.",
                              "type": [
                                "string",
                                "null"
                              ]
                            },
                            "requester_id": {
                              "description": "ID of the ticket requestor.",
                              "type": [
                                "number",
                                "null"
                              ]
                            },
                            "submitter_id": {
                              "description": "ID of the ticket submitter.",
                              "type": [
                                "number",
                                "null"
                              ]
                            },
                            "assignee_id": {
                              "description": "ID of the ticket assignee.",
                              "type": [
                                "number",
                                "null"
                              ]
                            },
                            "organization_id": {
                              "description": "ID of the organization ticket belongs to.",
                              "type": [
                                "number",
                                "null"
                              ]
                            },
                            "group_id": {
                              "description": "ID of the group ticket belongs to.",
                              "type": [
                                "number",
                                "null"
                              ]
                            },
                            "brand_id": {
                              "description": "ID of the brand ticket belongs to",
                              "type": [
                                "number",
                                "null"
                              ]
                            },
                            "form_id": {
                              "description": "ID of the form associated with the ticket.",
                              "type": [
                                "number",
                                "null"
                              ]
                            },
                            "external_id": {
                              "description": "",
                              "type": [
                                "string",
                                "null"
                              ]
                            },
                            "tags": {
                              "description": "Tags associated with the ticket.",
                              "type": "array",
                              "items": {
                                "description": "",
                                "type": [
                                  "string",
                                  "null"
                                ]
                              }
                            },
                            "via": {
                              "description": "Channel via which change was made.",
                              "type": "object",
                              "properties": {
                                "channel": {
                                  "description": "",
                                  "type": "string"
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  },
                  "readOnly": false
                }
              }
            },
    **"context-data" : {
              "description": "",
              "type": "object",
              "properties": {
                "Id": {
                  "type": "number",
                  "readOnly": false,
                  "description": "Automatically assigned when the ticket is created."
                },
                "Subject": {
                  "type": [
                    "string",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "The value of the subject field for this ticket. When used in WHERE clause: The text in the ticket subject"
                },
                "RawSubject": {
                  "type": [
                    "string",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "The dynamic content placeholder, if present, or the subject value, if not."
                },
                "Description": {
                  "type": [
                    "string",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "The first comment on the ticket. When used in WHERE clause: The text in the tickets description and comments"
                },
                "Type": {
                  "type": [
                    "string",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "The type of this ticket. Possible values: problem, incident, question or task."
                },
                "Priority": {
                  "type": [
                    "string",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "The urgency with which the ticket should be addressed. Possible values: urgent, high, normal, low."
                },
                "Status": {
                  "type": [
                    "string",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "The state of the ticket. Possible values: new, open, pending, hold, solved, closed."
                },
                "Recipient": {
                  "type": [
                    "string",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "The original recipient e-mail address of the ticket."
                },
                "HasIncidents": {
                  "type": [
                    "boolean",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "Is true of this ticket has been marked as a problem, false otherwise."
                },
                "DueAt": {
                  "type": [
                    "string",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "If this is a ticket of type task it has a due date. Due date format uses ISO 8601 format."
                },
                "RequesterId": {
                  "type": [
                    "number",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "The user who requested this ticket."
                },
                "SubmitterId": {
                  "type": [
                    "number",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "The user who submitted the ticket. The submitter always becomes the author of the first comment on the ticket. "
                },
                "AssigneeId": {
                  "type": [
                    "number",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "The agent currently assigned to the ticket."
                },
                "OrganizationId": {
                  "type": [
                    "string",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "The organization of the requester. You can only specify the ID of an organization associated with the requester."
                },
                "GroupId": {
                  "type": [
                    "number",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "The group this ticket is assigned to. When used in WHERE clause: The assigned agents group name."
                },
                "CollaboratorIds": {
                  "type": [
                    "string",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "The ids of users currently cc-ed on the ticket."
                },
                "FollowerIds": {
                  "type": [
                    "string",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "Agents currently following the ticket."
                },
                "ForumTopicId": {
                  "type": [
                    "number",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "The topic this ticket originated from, if any."
                },
                "ProblemId": {
                  "type": [
                    "number",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "For tickets of type incident, the ID of the problem the incident is linked to."
                },
                "ExternalId": {
                  "type": [
                    "string",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "An id you can use to link Zendesk Support tickets to local records."
                },
                "FollowupIds": {
                  "type": [
                    "string",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "Closed tickets only. The ids of the followups created from this ticket."
                },
                "ViaFollowupSourceId": {
                  "type": [
                    "string",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "POST requests only. The id of a closed ticket when creating a follow-up ticket.."
                },
                "MacroIds": {
                  "type": [
                    "string",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "POST requests only. List of macro IDs to be recorded in the ticket audit."
                },
                "TicketFormId": {
                  "type": [
                    "number",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "Enterprise only. The id of the ticket form to render for the ticket."
                },
                "BrandId": {
                  "type": [
                    "number",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "Enterprise only. The id of the brand this ticket is associated with."
                },
                "Tags": {
                  "type": [
                    "string",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "The array of tags applied to this ticket."
                },
                "ViaChannel": {
                  "type": [
                    "string",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "This tells you how the ticket or event was created. Examples: web, mobile, rule, system."
                },
                "ViaSource": {
                  "type": [
                    "string",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "The tickets source. "
                },
                "CustomFields": {
                  "type": [
                    "string",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "Custom fields for the ticket.The values of custom field are set and get dynamically"
                },
                "SatisfactionRating": {
                  "type": [
                    "string",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "The satisfaction rating of the ticket, if it exists, or the state of satisfaction, offered or unoffered."
                },
                "SharingAgreementIds": {
                  "type": [
                    "string",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "The ids of the sharing agreements used for this ticket."
                },
                "AllowChannelback": {
                  "type": [
                    "boolean",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "Is false if channelback is disabled, true otherwise. Only applicable for channels framework ticket."
                },
                "IsPublic": {
                  "type": [
                    "boolean",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "Is true if any comments are public, false otherwise."
                },
                "CreatedAt": {
                  "type": [
                    "string",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "When this record was created."
                },
                "UpdatedAt": {
                  "type": [
                    "string",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "When this record last got updated."
                },
                "Url": {
                  "type": [
                    "string",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "The API url of this ticket."
                },
                "View_Id": {
                  "type": [
                    "number",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "The view that tickets belong to."
                },
                "User_Id": {
                  "type": [
                    "number",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "The user that tickets belong to."
                },
                "Assignee": {
                  "type": [
                    "string",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "The assigned agent or other entity. You can specify none, me, user name (full name or partial), email address, user ID, or phone number"
                },
                "GroupName": {
                  "type": [
                    "string",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "The assigned agents group name."
                },
                "Requester": {
                  "type": [
                    "string",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "The ticket requester. You can specify none, me, user name (full name or partial), email address, user ID, or phone number."
                },
                "Submitter": {
                  "type": [
                    "string",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "The ticket submitter. This may be different than the requester if the ticket was submitted by an agent on behalf of the requester. You can specify none, me, user name (full name or partial), email address, user ID, or phone number. ."
                },
                "Brand": {
                  "type": [
                    "string",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "Search for a specific Brand on a ticket."
                },
                "Via": {
                  "type": [
                    "string",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "The tickets source, which can be any of the following:mail, api, phone, etc."
                },
                "Commenter": {
                  "type": [
                    "string",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "People who have added comments to tickets. You can specify none, me, user name (full name or partial), email address, user ID, or phone number."
                },
                "Cc": {
                  "type": [
                    "string",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "People who have been CCd on tickets. You can specify none, me, user name (full name or partial), email address, user ID, or phone number."
                },
                "HasAttachment": {
                  "type": [
                    "boolean",
                    "null"
                  ],
                  "readOnly": false,
                  "description": "Search for all tickets with or without attachments using true or false."
                },
                "Ticket status": {
                  "type": [
                    "string",
                    "null"
                  ],
                  "readOnly": false
                }
              }
            }**
          }
        }
        
      

### View event subscriptions

To view and manage all the event subscriptions associated with a connection in Integration Connectors, do the following:

  1. Go to **Integration Connectors > Connections** page. 

[ Go to the Connections page](https://console.cloud.google.com/connectors/connections)

  2. Click the connection for which you want to view the subscriptions.
  3. Click the **Event subscriptions** tab. 

This displays all the event subscriptions for the connection.




## Edit Zendesk trigger

You can edit a **Zendesk trigger** to change or update the connection configuration and event subscription details.

**Important:** When you edit or modify a Zendesk trigger, you can either retain the previously configured event subscription that is attached to the trigger, or you can delete it. Deleting an event subscription will affect all the published integrations using that event subscription. 

To edit a Zendesk trigger, perform the following steps:

  1. Click the **Zendesk trigger** element in the integration editor to open the trigger configuration pane.
  2. Click **Configure Zendesk trigger**.
  3. Do the following in the **Connector Event Trigger Editor** page: 
     1. To retain the previously configured event subscription, click **Retain** , else click **Delete**. **Warning:** Deleting an event subscription will affect all the published integrations using the event subscription. This task cannot be undone.
     2. Update the connection configuration and event subscription details as desired.
     3. Click **Done**.

You can view the updated connection and event subscription details in the trigger configuration pane under **Event Subscription details**.




## Supported event subscription types

You can use the **Zendesk trigger** to invoke an integration for the following event subscription types:

Event subscription types | Description  
---|---  
`organization.ExternalChanged` | An organization's external ID changed.   
`organization.OrganizationCreated` | An organization is created.   
`organization.TagsChanged` | An organization's tags changed.   
`ticket.AgentAssignmentChanged` | A ticket is reassigned to another agent in support.   
`ticket.AttachmentLinkedToComment` | An attachment is linked to a ticket comment in support.   
`ticket.AttachmentRedactedFromComment` | An attachment is redacted from an existing comment in a ticket.   
`ticket.BrandChanged` | The brand is changed. A brand is a customer-facing identity which can be represented as multiple products or services, or multiple brands owned by the company.   
`ticket.CcsChanged` | Users were added or removed from a ticket.   
`ticket.CommentAdded` | A comment is added when a support ticket is created or updated.   
`ticket.CommentMadePrivate` | A private comment is added on a support ticket.   
`ticket.CommentRedacted` | Words or strings were permanently removed from a ticket comment.   
`ticket.DescriptionChanged` | The description is changed in a ticket.   
`ticket.ExternalIdChanged` | The external ticket ID is changed.   
`ticket.FollowersChanged` | Followers were changed on a ticket.   
`ticket.GroupAssignmentChanged` | A ticket is reassigned to another group of agents.   
`ticket.MarkedAsSpam` | A ticket is marked as spam.   
`ticket.OrganizationChanged` | The organization is changed in the ticket.   
`ticket.PriorityChanged` | The priority is changed on a ticket.   
`ticket.ProblemLinkChanged` | The problem ID associated with an incident type ticket is changed.   
`ticket.RequesterChanged` | The requester of a ticket is changed.   
`ticket.StatusChanged` | The status of a ticket is changed.   
`ticket.SubjectChanged` | The subject of a ticket is changed.   
`ticket.SubmitterChanged` | The submitter of a ticket is changed.   
`ticket.TagsChanged` | Tags were changed in a ticket.   
`ticket.TaskDueAtChanged` | The task due date and time on a ticket is changed.   
`ticket.TicketCreated` | A support ticket is created.   
`ticket.TicketFormChanged` | The form is changed in the ticket.   
`ticket.TicketMerged` | A ticket is merged with another ticket.   
`ticket.TicketPermanentlyDeleted` | A ticket is permanently deleted.   
`ticket.TicketSoftDeleted` | A ticket is deleted such that it is not visible to any users, including admins using either the product interface or the API.   
`ticket.TicketTypeChanged` | A ticket type is changed.   
`ticket.TicketUndeleted` | A ticket is undeleted.   
`user.CustomRoleChanged` | A user's custom role changed.   
`user.ExternalidChanged` | A user's external ID changed.   
`user.LastLoginChanged` | A user's last login time changed.   
`user.OnlyPrivateCommentsChanged` | A user's ability to create public comments changed.   
`user.TageChanged` | A user's tags changed.   
`userTimeZoneChanged` | A user's time zone changed.   
`user.UserAliasChanged` | A user's alias changed.   
`user.UserCreated` | A user is created.   
`user.UserDetailsChanged` | A user's details changed.   
`user.UserGroupAdded` | A user is added to a group.   
`user.UserGroupRemoved` | A user is removed from a group.   
`user.UserIdentityChanged` | A user's identity changed.   
`user.UserIdentityCreated` | A user's identity is created.   
`user.UserIdentityRemoved` | A user's identity is deleted.   
`user.UserActiveChanged` | A user's active status changed.   
`user.UserMerged` | A user is merged with another user.   
`user.UserNameChanged` | A user's name changed.   
`user.UserNotesChanged` | A user's notes changed.   
`user.UserOrganizationAdded` | A user is added to an organization.   
`user.UserOrganizationRemoved` | A user is removed from an organization.   
`user.UserPhotoChanged` | A user's photo changed.   
`user.UserRoleChanged` | A user's role changed.   
  
## Quotas and limits

For information about quotas and limits, see [Quotas and limits](https://docs.cloud.google.com/application-integration/docs/quotas).

## What's next

  * Learn about [all tasks and triggers](https://docs.cloud.google.com/application-integration/docs/all-triggers-tasks).
  * Learn how to [test and publish an integration](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations).
  * Learn about [error handling](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy).
  * Learn about [integration execution logs](https://docs.cloud.google.com/application-integration/docs/introduction-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
