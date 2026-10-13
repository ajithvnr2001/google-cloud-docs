---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/akamai/
title: Integrate Akamai with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:37:57.567340+00:00
---

# Integrate Akamai with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/akamai/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Akamai with Google SecOps 

This document explains how to integrate Akamai with Google Security Operations (Google SecOps).

## Integration parameters

The Akamai integration requires the following parameters:

Parameter | Description  
---|---  
`Host` | Required. The hostname of the Akamai instance.  
`Client Token` | Required. Your Akamai Client token.  
`Client Secret` | Required. Your Akamai Client Secret.  
`Access Token` | Required. Your Akamai access token.  
`Verify SSL` | Required. Validates the SSL certificate when connecting to Akamai.  Selected by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Activate Client List

Use the **Activate Client List** action to enable a specific client list within your Akamai environment.

#### Action inputs

The **Activate Client List** action requires the following parameters:

Parameter | Description  
---|---  
`Client List Name` | Optional. The name of the client list to update. If `Client List Name` and `Client List ID` are provided, the action prioritizes `Client List ID`.  
`Client List ID` | Optional. The unique identifier of the client list to update. If `Client List Name` and `Client List ID` are provided, the action prioritizes `Client List ID`.  
`Environment` | Optional. The target network environment for the activation. The possible values are as follows:

  * `Production`
  * `Staging`

The default value is `Production`.  
`Comment` | Optional. A brief description or justification associated with the activation operation.  
`Notification Recipients` | Optional. A comma-separated list of email addresses that receive a notification regarding the client list activation  
  
#### Action outputs

The **Activate Client List** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Activate Client Lists** action:
    
    
    {
        "action": "ACTIVATE",
        "activations": {
            "STAGING": {
                "activationId": 3797405,
                "activationStatus": "PENDING_ACTIVATION"
            }
        },
        "comments": "Activating 235466",
        "createDate": "2026-02-12T15:12:07.952+00:00",
        "createdBy": "4wksaj3wyt23jt2i",
        "listId": "235466_GOOGLESECOPSCLIENTLIST1",
        "notificationRecipients": [
            "12345@email.com"
        ],
        "version": 14
    }
    

##### Output messages

The **Activate Client List** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully activated the client list in Akamai.` | The action succeeded.  
`Error executing action "Activate Client List". Reason: ERROR_REASON` | The action failed.  
  
##### Script result

The following table describes the values for the script result output when using the **Activate Client List** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Activate Network List

Use the **Activate Network List** action to remove items from the network list in Akamai.

#### Action inputs

The **Activate Network List** action requires the following parameters:

Parameter | Description  
---|---  
`Network List Name` | Optional. The name of the network list to update. If `Network List Name` and `Network List ID` are provided, the action uses the ID  
`Network List ID` | Optional. The ID of the network list to update. If `Network List Name` and `Network List ID` are provided, the action uses the ID  
`Environment` | Optional. The target environment for the activation. The possible values are as follows:

  * `Production`
  * `Staging`

  
`Comment` | Optional. A comment describing the activation purpose.  
`Notification Recipients` | Optional. A comma-separated list of email addresses to notify about the network list activation.  
  
#### Action outputs

The **Activate Network List** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Activate Network Lists** action:
    
    
    {
       "activationId": 12345,
       "activationComments": "Allow IPs of new employees who joined this week",
       "activationStatus": "PENDING_ACTIVATION",
       "syncPoint": 5,
       "uniqueId": "25614_GENERALLIST",
       "fast": false,
       "dispatchCount": 1,
       "links": {
         "appendItems": {
           "href": "/networklist-api/rest/v2/network-lists/25614_GENERALLIST/append",
           "method": "POST"
         },
         "retrieve": {
           "href": "/networklist-api/rest/v2/network-lists/25614_GENERALLIST"
         },
         "statusInProduction": {
           "href": "/networklist-api/rest/v2/network-lists/25614_GENERALLIST/environments/PRODUCTION/status"
         },
         "statusInStaging": {
           "href": "/networklist-api/rest/v2/network-lists/25614_GENERALLIST/environments/STAGING/status"
         },
         "syncPointHistory": {
           "href": "/networklist-api/rest/v2/network-lists/25614_GENERALLIST/sync-points/5/history"
         },
         "update": {
           "href": "/networklist-api/rest/v2/network-lists/25614_GENERALLIST",
           "method": "PUT"
         },
         "activationDetails": {
           "href": "/network-list/v2/network-lists/activations/12345/"
         }
       }
     }
    

##### Output messages

The **Activate Network List** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully activated the network list in Akamai.` | Action succeeded.  
`Error executing action "Activate Network List". Reason: {0}''.format(error.Stacktrace)` `Error executing action "Activate Network List". Reason: "{network name or id}" network list wasn't found in Akamai.` `Error executing action "Activate Network List". Reason: provide a value in "Network List Name" or "Network List ID" parameter.` | Action failed.  
  
##### Script result

The following table describes the values for the script result output when using the **Activate Network List** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Add Items To Client List

Use the **Add Items To Client List** action to add items to the client list in Akamai.

#### Action inputs

The **Add Items To Client List** action requires the following parameters:

Parameter | Description  
---|---  
`Client List Name` | Optional. The name of the client list to update. Note: If `Client List Name` and `Client List ID` are provided, the action uses the ID.  
`Client List ID` | Optional. The ID of the client list to update. Note: If `Client List Name` and `Client List ID` are provided, the action uses the ID.  
`Item Value` | Required. A comma-separated list of items to add to the client list.  
`Item Description` | Optional. A description for the items added to the client list.  
`Item Expiration Date` | Optional. An expiration date for the added items, in ISO 8601 format.  
`Item Tags` | Optional. A comma-separated list of tags to associate with the added items.  
  
#### Action outputs

The **Add Items To Client List** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Add Items To Client List** action:
    
    
    [
      {
        "createDate": "2026-03-20T09:54:11.410+00:00",
        "createdBy": "4wksaj3wyt23jt2i",
        "description": "Testtinhbhjbjbjb",
        "expirationDate": "2026-04-05T19:29:02.320+00:00",
        "tags": [],
        "type": "IP",
        "updateDate": "2026-03-20T09:54:11.410+00:00",
        "updatedBy": "4wksaj3wyt23jt2i",
        "value": "127.0.0.1",
        "status": "added"
      },
      {
        "value": "127.0.0.3",
        "status": "duplicated"
      },
      {
        "value": "127.0.0.TT",
        "status": "failed",
        "error: "Validation failed: delete[0].value: Item of type IP has an invalid value 127.0.0.4E"
      },
    ]
    

##### Output messages

The **Add Items To Client List** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully returned client lists from Akamai.` | Action succeeded.  
`Error executing action "Add Items To Client List". Reason: {0}''.format (error.Stacktrace)` `Error executing action "Add Items To Client List". Reason: provide a value in "Client List Name" or "Client List ID" parameter.` `Error executing action "Add Items To Client List". Reason: "{client list name or id}" client list wasn't found in Akamai.` | Action failed.  
  
##### Script result

The following table describes the values for the script result output when using the **Add Items To Client List** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Add Items To Network List

Use the **Add Items To Network List** action to add items to the network list in Akamai.

#### Action inputs

The **Add Items To Network List** action requires the following parameters:

Parameter | Description  
---|---  
`Network List Name` | Optional. The name of the network list to update. If `Network List Name` and `Network List ID` are provided, the action uses the ID.  
`Network List ID` | Optional. The ID of the network list to update. If `Network List Name` and `Network List ID` are provided, the action uses the ID.  
`Items` | Required. A comma-separated list of items to add to the network list.  
  
#### Action outputs

The **Add Items To Network List** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Add Items To Network Lists** action:
    
    
         {
           "networkListType": "networkListResponse",
           "accessControlGroup": "KSD\nwith ION 3-13H1234",
           "name": "General List",
           "elementCount": 3011,
           "readOnly": false,
           "shared": false,
           "syncPoint": 22,
           "type": "IP",
           "uniqueId": "25614_GENERALLIST",
           "links": {
             "activateInProduction": {
               "href": "/network-list/v2/network-lists/25614_GENERALLIST/environments/PRODUCTION/activate",
               "method": "POST"
             },
             "activateInStaging": {
               "href": "/network-list/v2/network-lists/25614_GENERALLIST/environments/STAGING/activate",
               "method": "POST"
             },
             "appendItems": {
               "href": "/network-list/v2/network-lists/25614_GENERALLIST",
               "method": "POST"
             },
             "retrieve": {
               "href": "/network-list/v2/network-lists/25614_GENERALLIST"
             },
             "statusInProduction": {
               "href": "/network-list/v2/network-lists/25614_GENERALLIST/environments/PRODUCTION/status"
             },
             "statusInStaging": {
               "href": "/network-list/v2/network-lists/25614_GENERALLIST/environments/STAGING/status"
             },
             "update": {
               "href": "/network-list/v2/network-lists/25614_GENERALLIST",
               "method": "PUT"
             }
           }
         }
    

##### Output messages

The **Add Items To Network List** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully updated network list in Akamai.` | Action succeeded.  
`Error executing action "Add Items To Network List". Reason: {0}''.format (error.Stacktrace)` `Error executing action "Add Items To Network List". Reason: "{network name or id}" network list wasn't found in Akamai.` `Error executing action "Add Items To Network List". Reason: provide a value in "Network List Name" or "Network List ID" parameter.` | Action failed.  
  
##### Script result

The following table describes the values for the script result output when using the **Add Items To Network List** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Client Lists

Use the **Get Client Lists** action to get information about client lists in Akamai.

#### Action inputs

The **Get Client Lists** action requires the following parameters:

Parameter | Description  
---|---  
`Client List Name` | Optional. A comma-separated list of client list names to search for.  
`Client List ID` | Optional. A comma-separated list of client list IDs to search for.  
`Include Items` | Optional. Returns information about the items inside the client list.  The default value is `False`. Note: This information is only returned if `Client List Name` or `Client List ID` is provided.  
`Type` | Optional. The type of the client list to search. The possible values are as follows:

  * `IP`
  * `GEO`


* `ASN`
* `TLS`
* `Fingerprint`
* `File Hash`
Note: If `Select One` is provided, the action searches across all client lists.   
`Max Client Lists To Return` | Required. The maximum number of client lists to return. The default and maximum value is `100`.  
`Max Client List Items To Return` | Required. The maximum number of items to return per client list. The default and maximum value is `100`.  
  
#### Action outputs

The **Get Client Lists** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Get Client Lists** action:
    
    
    [
    {
       "contractId": "K-0N7RAK71",
       "createDate": "2023-04-05T18:20:42.090+00:00",
       "createdBy": "jsmith",
       "deprecated": false,
       "groupId": 32145,
       "groupName": "Acme IT Group",
       "items": [
         {
           "createDate": "2023-04-05T18:20:42.892+00:00",
           "createdBy": "jkowalski",
           "description": "Canada - North America",
           "expirationDate": "2023-12-31T23:59:19.700+00:00",
           "productionStatus": "INACTIVE",
           "stagingStatus": "INACTIVE",
           "tags": [
             "allowlist1"
           ],
           "type": "GEO",
           "updateDate": "2023-04-05T18:20:42.892+00:00",
           "updatedBy": "mrossi",
           "value": "CA"
         }
       ],
       "itemsCount": 3,
       "listId": "1234_NORTHAMERICAGEOALLOWLIST",
       "listType": "CL",
       "name": "NorthAmericaGeoAllowlist",
       "notes": "GEO code allowlist",
       "productionActivationStatus": "INACTIVE",
       "readOnly": false,
       "shared": false,
       "stagingActivationStatus": "INACTIVE",
       "tags": [
         "allowlist2"
       ],
       "type": "GEO",
       "updateDate": "2023-04-05T18:20:42.090+00:00",
       "updatedBy": "jdupont",
       "version": 1
     }
    ]
    

##### Output messages

The **Get Client Lists** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully returned client lists from Akamai.` `No clients lists were found for the provided criteria in Akamai.` | Action succeeded.  
`Error executing action "Get Client Lists". Reason: {0}''.format (error.Stacktrace)` | Action failed.  
  
##### Script result

The following table describes the values for the script result output when using the **Get Client Lists** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Network Lists

Use the **Get Network Lists** action to get information about a network's lists in Akamai.

#### Action inputs

The **Get Network Lists** action requires the following parameters:

Parameter | Description  
---|---  
`Network List Name` | Optional. A comma-separated list of network list names to search for.  
`Network List ID` | Optional. A comma-separated list of network list IDs to search for.  
`Include Items` | Optional. Returns information about the items inside the network lists. The default value is `False`.  
`Include Activation Status` | Optional. Returns the activation status for each network list. The default value is `False`. Note: This information is only returned if `Network List Name` or `Network List ID` is provided.  
`Activation Environment` | Optional. The environment for which the activation status is returned. The possible values are as follows:

  * `Production`
  * `Staging`

Note: This information is only returned if `Network List Name` or `Network List ID` is provided.  
`Max Network Lists To Return` | Required. The maximum number of network lists to return. The default and maximum value is `100`.  
`Max Network List Items To Return` | Required. The maximum number of items to return per network list. The default and maximum value is `100`.  
  
#### Action outputs

The **Get Network Lists** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Get Network Lists** action:
    
    
    [
       {
           "networkListType": "networkListResponse",
           "accessControlGroup": "KSD\nwith ION 3-13H1234",
           "name": "General List",
           "elementCount": 3011,
           "readOnly": false,
           "shared": false,
           "syncPoint": 22,
           "type": "IP",
           "uniqueId": "25614_GENERALLIST",
           "links": {
               "activateInProduction": {
                   "href": "/network-list/v2/network-lists/25614_GENERALLIST/environments/PRODUCTION/activate",
                   "method": "POST"
               },
               "activateInStaging": {
                   "href": "/network-list/v2/network-lists/25614_GENERALLIST/environments/STAGING/activate",
                   "method": "POST"
               },
               "appendItems": {
                   "href": "/network-list/v2/network-lists/25614_GENERALLIST",
                   "method": "POST"
               },
               "retrieve": {
                   "href": "/network-list/v2/network-lists/25614_GENERALLIST"
               },
               "statusInProduction": {
                   "href": "/network-list/v2/network-lists/25614_GENERALLIST/environments/PRODUCTION/status"
               },
               "statusInStaging": {
                   "href": "/network-list/v2/network-lists/25614_GENERALLIST/environments/STAGING/status"
               },
               "update": {
                   "href": "/network-list/v2/network-lists/25614_GENERALLIST",
                   "method": "PUT"
               }
           },
           "Activation_STAGING": {
               "activationId": 12345,
               "activationComments": "Allow IPs of new employees who joined this week",
               "activationStatus": "PENDING_ACTIVATION",
               "syncPoint": 5,
               "uniqueId": "25614_GENERALLIST",
               "fast": false,
               "dispatchCount": 1,
               "links": {
                   "appendItems": {
                       "href": "/networklist-api/rest/v2/network-lists/25614_GENERALLIST/append",
                       "method": "POST"
                   },
                   "retrieve": {
                       "href": "/networklist-api/rest/v2/network-lists/25614_GENERALLIST"
                   },
                   "statusInProduction": {
                       "href": "/networklist-api/rest/v2/network-lists/25614_GENERALLIST/environments/PRODUCTION/status"
                   },
                   "statusInStaging": {
                       "href": "/networklist-api/rest/v2/network-lists/25614_GENERALLIST/environments/STAGING/status"
                   },
                   "syncPointHistory": {
                       "href": "/networklist-api/rest/v2/network-lists/25614_GENERALLIST/sync-points/5/history"
                   },
                   "update": {
                       "href": "/networklist-api/rest/v2/network-lists/25614_GENERALLIST",
                       "method": "PUT"
                   },
                   "activationDetails": {
                       "href": "/network-list/v2/network-lists/activations/12345/"
                   }
               }
           },
           "Activation_PRODUCTION": {
               "activationId": 12345,
               "activationComments": "Allow IPs of new employees who joined this week",
               "activationStatus": "PENDING_ACTIVATION",
               "syncPoint": 5,
               "uniqueId": "25614_GENERALLIST",
               "fast": false,
               "dispatchCount": 1,
               "links": {
                   "appendItems": {
                       "href": "/networklist-api/rest/v2/network-lists/25614_GENERALLIST/append",
                       "method": "POST"
                   },
                   "retrieve": {
                       "href": "/networklist-api/rest/v2/network-lists/25614_GENERALLIST"
                   },
                   "statusInProduction": {
                       "href": "/networklist-api/rest/v2/network-lists/25614_GENERALLIST/environments/PRODUCTION/status"
                   },
                   "statusInStaging": {
                       "href": "/networklist-api/rest/v2/network-lists/25614_GENERALLIST/environments/STAGING/status"
                   },
                   "syncPointHistory": {
                       "href": "/networklist-api/rest/v2/network-lists/25614_GENERALLIST/sync-points/5/history"
                   },
                   "update": {
                       "href": "/networklist-api/rest/v2/network-lists/25614_GENERALLIST",
                       "method": "PUT"
                   },
                   "activationDetails": {
                       "href": "/network-list/v2/network-lists/activations/12345/"
                   }
               }
           }
       }
    ]
    

##### Output messages

The **Get Network Lists** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully returned network lists from Akamai.` `No network lists were found for the provided criteria in Akamai.` | Action succeeded.  
`Error executing action "Get Network Lists". Reason: {0}''.format (error.Stacktrace)` | Action failed.  
  
##### Script result

The following table describes the values for the script result output when using the **Get Network Lists** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Ping

Use the **Ping** action to test the connectivity to Akamai.

This action doesn't run on Google SecOps entities and doesn't have input parameters.

#### Action outputs

The **Ping** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment  | Not available   
Case wall link  | Not available   
Case wall table  | Not available   
Enrichment table  | Not available   
JSON result  | Not available   
Script result  | Available   
  
##### Output messages

The **Ping** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the Akamai server with the provided connection parameters!` | Action succeeded.   
`Failed to connect to the Akamai server! Error is {0}".format(exception.stacktrace)` | Action failed.  
  
##### Script result

The following table describes the values for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Remove Items From Client List

Use the **Remove Items From Client List** action to remove items from the client list in Akamai.

#### Action inputs

The **Remove Items From Client List** action requires the following parameters:

Parameter | Description  
---|---  
`Client List Name` | Optional. The name of the client list to update. Note: If `Client List Name` and `Client List ID` are provided, the action uses the ID.  
`Client List ID` | Optional. The ID of the client list to update. Note: If `Client List Name` and `Client List ID` are provided, the action uses the ID.  
`Item Value` | Required. A comma-separated list of items to remove from the client list.  
  
#### Action outputs

The **Remove Items From Client List** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Remove Items From Client List** action:
    
    
    [
      {
        "value": "127.0.0.1",
        "status": "doesn't exist"
      },
      {
        "value": "127.0.0.4",
        "status": "removed"
      },
      {
        "value": "127.0.0.4E",
        "status": "failed",
        "error": "Validation failed: delete[0].value: Item of type IP has an invalid value 127.0.0.4E"
      }
    ]
    

##### Output messages

The **Remove Items From Client List** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully updated client list in Akamai.` `None of the provided items were found in the client list in Akamai.` | Action succeeded.  
`Error executing action "Remove Items From Client List". Reason: {0}''.format(error.Stacktrace)` `Error executing action "Remove Items From Client List". Reason: provide a value in "Client List Name" or "Client List ID" parameter.` `Error executing action "Remove Items From Client List". Reason: "{client list name or id}" client list wasn't found in Akamai.` | Action failed.  
  
##### Script result

The following table describes the values for the script result output when using the **Remove Items From Client List** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Remove Items From Network List

Use the **Remove Items From Network List** action to remove items from the network list in Akamai.

#### Action inputs

The **Remove Items From Network List** action requires the following parameters:

Parameter | Description  
---|---  
`Network List Name` | Optional. The name of the network list to update. If `Network List Name` and `Network List ID` are provided, the action uses the ID  
`Network List ID` | Optional. The ID of the network list to update. If `Network List Name` and `Network List ID` are provided, the action uses the ID  
`Items` | Required. A comma-separated list of items to remove from the network list.  
  
#### Action outputs

The **Remove Items From Network List** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Remove Items From Network Lists** action:
    
    
    {
           "networkListType": "networkListResponse",
           "accessControlGroup": "KSD\nwith ION 3-13H1234",
           "name": "General List",
           "elementCount": 3011,
           "readOnly": false,
           "shared": false,
           "syncPoint": 22,
           "type": "IP",
           "uniqueId": "25614_GENERALLIST",
           "links": {
             "activateInProduction": {
               "href": "/network-list/v2/network-lists/25614_GENERALLIST/environments/PRODUCTION/activate",
               "method": "POST"
             },
             "activateInStaging": {
               "href": "/network-list/v2/network-lists/25614_GENERALLIST/environments/STAGING/activate",
               "method": "POST"
             },
             "appendItems": {
               "href": "/network-list/v2/network-lists/25614_GENERALLIST",
               "method": "POST"
             },
             "retrieve": {
               "href": "/network-list/v2/network-lists/25614_GENERALLIST"
             },
             "statusInProduction": {
               "href": "/network-list/v2/network-lists/25614_GENERALLIST/environments/PRODUCTION/status"
             },
             "statusInStaging": {
               "href": "/network-list/v2/network-lists/25614_GENERALLIST/environments/STAGING/status"
             },
             "update": {
               "href": "/network-list/v2/network-lists/25614_GENERALLIST",
               "method": "PUT"
             }
           }
         }
    

##### Output messages

The **Remove Items From Network List** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully updated network list in Akamai.` `None of the provided items were found in the network list in Akamai.` | Action succeeded.  
`Error executing action "Remove Items From Network List". Reason: {0}''.format (error.Stacktrace)` `Error executing action "Remove Items From Network List". Reason: "{network name or id}" network list wasn't found in Akamai.` `Error executing action "Remove Items From Network List". Reason: provide a value in "Network List Name" or "Network List ID" parameter.` | Action failed.  
  
##### Script result

The following table describes the values for the script result output when using the **Remove Items From Network List** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
