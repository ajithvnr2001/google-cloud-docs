---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/ukg/configure/
title: UKG \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:41:32.833368+00:00
---

# UKG  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/ukg/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# UKG

The UKG connector lets you perform various actions on UKG data.

## Before you begin

Before using the UKG connector, do the following tasks:

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
     1. **Connector** : Select **UKG** from the drop down list of available Connectors.
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
     7. **Service/Module** : Select the UKG module.
     8. Optionally, configure the **Connection node settings** : 

        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
     9. Optionally, click **\+ ADD LABEL** to add a label to the Connection in the form of a key/value pair.
     10. Click **NEXT**.
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

The following authentication types are supported by the UKG connection:

     * Basic Authentication
     * OAUTH 2.0 - Authorization code

To understand how to configure these authentication types, see Configure authentication.

  2. Click **NEXT**.


* **Review** : Review your connection and authentication details.
* Click **Create**.

### Configure authentication

Enter the details based on the authentication you want to use.

  * **Basic Authentication**
    * **Username** : The username used to authenticate the connector.
    * **Password** : Secret Manager Secret containing the password associated with the connector.
**OAUTH 2.0 - Authorization code**
    * **Client ID** : The client ID used for requesting access tokens.
    * **Scopes** :A comma-separated list of desired scopes.
    * **Client Secret** : Secret Manager Secret containing the client secret for the connected app you created.
    * **Enable PKCE** : Select this option if you want to enable Proof Key of Code Exchange (PKCE).
    * **Authorization URL** : Authorization URL for your app. You will be redirected to this page to login to your app.
    * **Access Token URL** : The URL to be used to echange access token. Provide complete URL including scheme.



## Connection configuration samples

This section lists the sample values for the various fields that you configure when creating the connection.

### OAUTH 2.0 - Authorization code connection type

Field name | Details  
---|---  
Location | us-central1  
Connector | UKG  
Connector version | 1  
Connection Name | gcp-ukg-oauth-conn  
Enable Cloud Logging | Yes  
Log Level | Error  
Service Account | SERVICEACCOUNT_NAME@developer.gserviceaccount.com  
Open API spec Module | Timekeeping  
Verbosity Level | 5  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Destination Type | Host address  
Host Address | https://google-connect-dev.cfn.mykronos.com  
Client ID | ZG******-****-****-****-*********uDN  
Client secret | Secret  
Secret Version | 1  
Authorization URL | https://google-connect-dev.cfn.mykronos.com/oauth2/authorize  
Access token URL | https://google-connect-dev.cfn.mykronos.com/api/authentication/access_token  
  
**Note** : You can pass the following URL as the hostname, which is the default host address: `https://login.UKG.com`. You must use a different host address if your organization uses a custom login endpoint.

## System limitations

The UKG connector can process 30 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## actions

This connector lets you perform various actions on UKG data.

This section lists the actions supported by the UKG connector. To understand how to configure the actions, see Action examples.

### RetrieveAllEmployeeGroupsOrByName action

Retrieves all employee groups by name.

#### Input parameters of the RetrieveAllEmployeeGroupsOrByName action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
all_details | boolean | True | A Boolean that indicates whether the response is lightweight, which is a response containing only ID and name fields.  
name | string | True | The name of an employee group.  
  
For example on how to configure the `RetrieveAllEmployeeGroupsOrByName` action, see Examples.

### Create PayCode action

Creates a paycode.

#### Input parameters of the Create PayCode action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
type | string | True | The type of the paycode.  
name | string | True | The name of the paycode.  
unit | string | True | The unit for the paycode.  
codeNumber | integer | True | The code number assigned to a pay code.  
  
For example on how to configure the `CreatePayCode` action, see Examples.

###  DeletePayCodebyId action

Deletes a paycode based on the ID.

#### Input parameters of the DeletePayCodebyId action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
id | integer | True | The ID of a paycode.  
  
For example on how to configure the `DeletePayCodebyId` action, see Examples.

###  Update Work Rule by ID action

Updates work rule using ID.

#### Input parameters of the Update Work Rule by ID action

Parameter Name | Data Type | Required | Description  
---|---|---|---  
workRuleId | integer | True | ID of the work rule  
workRuleVersion | json | True | The work rule version associated with a work rule.  
name | string | True | The name of a work rule.  
version | integer | True | Version of the work rule.  
  
For example on how to configure the `Update Work Rule by ID` action, see Examples.

## Action examples

### Example - RetrieveAllEmployeeGroupsOrByName

This example retrieves employee groups.

  1. In the `Configure connector task` dialog, click `actions`.
  2. Select the `RetrieveAllEmployeeGroupsOrByName ` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "Query parameters": {
             "all_details": true
           }
         } 
         
         
          If the action is successful, the
           RetrieveAllEmployeeGroupsOrByName task's connectorOutputPayload response
           parameter will have a value similar to the following:
         
         
           
         
         

[{ "ResponseBody": "[{\"name\":\"$U-South Region\",\"id\":1401,\"orgMapGroupRef\":{\"id\":2452,\"qualifier\":\"$U-South Region\"},\"version\":0,\"updateDtm\":\"2020-03-04T16:06:46\",\"persistentId\":\"$U-South#Region\"},{\"name\":\"$U-Canada Region\",\"id\":1451,\"orgMapGroupRef\":{\"id\":2453,\"qualifier\":\"$U-Canada Region\"},\"version\":0,\"updateDtm\":\"2020-03-04T16:07:21\",\"persistentId\":\"}]




### Example - Create PayCode

This example creates a pay code.

  1. In the `Configure connector task` dialog, click `actions`.
  2. Select the `Create PayCode` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
             "RequestBody": {
               "type": "Regular",
               "unit": "HOUR",
               "visibleToTimecardSchedule": true,
               "name": "2nd Meal Premium qaazxse",
               "shortName": "2MP",
               "combined": false,
               "money": false,
               "totals": true,
               "excusedAbsence": false,
               "wageMultiplier": 1.0,
               "wageAddition": 0.0,
               "addToTimecardTotal": true,
               "visibleToUser": true,
               "visibleToReports": true,
               "checkAvailability": 0.0,
               "codeNumber": 7663.0,
               "cascadingDuration": false,
               "processDurationAsSeparateShift": false,
               "editCountsTowardsOvertimeLimits": false,
               "editCountsTowardsConsecutiveDayOT": false,
               "repeating": false,
               "payrollOnly": false,
               "timekeepingOnly": false,
               "netDown": false
             },
             "Headers": {
               "Content-Type": "application/json"
             }
           }
           
           
           

If the action is successful, the `CreatePayCode` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
      [{
        "type": "Regular",
        "unit": "HOUR",
        "visibleToTimecardSchedule": true,
        "id": 5904.0,
        "name": "2nd Meal Premium qaazxse",
        "shortName": "2MP",
        "combined": false,
        "money": false,
        "totals": true,
        "excusedAbsence": false,
        "wageMultiplier": 1.0,
        "wageAddition": 0.0,
        "addToTimecardTotal": true,
        "visibleToUser": true,
        "visibleToReports": true,
        "checkAvailability": 0.0,
        "codeNumber": 7663.0,
        "cascadingDuration": false,
        "processDurationAsSeparateShift": false,
        "editCountsTowardsOvertimeLimits": false,
        "editCountsTowardsConsecutiveDayOT": false,
        "repeating": false,
        "payrollOnly": false,
        "timekeepingOnly": false,
        "netDown": false
      }]




### Example - DeletePayCodebyId 

This example deletes a paycode based on the ID.

  1. In the `Configure connector task` dialog, click `actions`.
  2. Select the `DeletePayCodebyId ` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "Path parameters": {
             "id": 6002.0
           }
         } 

If the action is successful, the `DeletePayCodebyId` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
     [{
      "ResponseBody": "",
      "StatusCode": 200.0
    }] 




### Example - Update Work Rule by ID

This example updates the work rule.

  1. In the `Configure connector task` dialog, click `actions`.
  2. Select the `Update Work Rule by ID ` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "Path parameters": {
             "id": 3701.0
           },
           "Headers": {
             "Content-Type": "application/json"
           },
           "RequestBody": {
             "version": 1.0,
             "workRuleId": 3701.0,
             "name": "$AU Call Back Sasori",
             "workRuleVersion": [{
               "effectiveWorkRuleId": 3801.0,
               "effectiveDateTime": "1853-01-01T00:00:00",
               "updateThisVersion": true,
               "expirationDateTime": "4000-01-01T00:00:00",
               "general": {
                 "breaks": [],
                 "coreHours": [],
                 "includeMinimumWagesAdjustment": false,
                 "deductions": [{
                   "id": 651.0,
                   "qualifier": "$AU Oncall Allowance",
                   "name": "$AU Oncall Allowance"
                 }]
               },
               "workRulePayCodeDistribution": {
                 "payCodeDistributionName": "$AU Oncall",
                 "deviations": [],
                 "overtimes": [],
                 "zones": [],
                 "majorities": []
               },
               "workRuleAutoBreakPlacement": {
                 "minimumTimeBetweenStartOfShiftAndFirstBreak": "0:0",
                 "minimumTimeBetweenEndOfBreakAndShiftEnd": "0:0",
                 "minimumTimeBetweenBreaks": "0:0",
                 "shiftLengthsToExclude": [],
                 "newShiftLengths": []
               },
               "version": 1.0
             }],
             "ivrAlias": "1234567890"
           }
         }

If the action is successful, the `Update Work Rule by ID` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
     [{
      "workRuleId": 3701.0,
      "name": "$AU Call Back Sasori",
      "ivrAlias": "1234567890",
      "workRuleVersion": [{
        "effectiveWorkRuleId": 3801.0,
        "effectiveDateTime": "1753-01-01T00:00:00",
        "updateThisVersion": false,
        "expirationDateTime": "3000-01-01T00:00:00",
        "general": {
          "breaks": [],
          "coreHours": [],
          "includeMinimumWagesAdjustment": false,
          "deductions": [{
            "id": 651.0,
            "qualifier": "$AU Oncall Allowance",
            "name": "$AU Oncall Allowance"
          }]
        },
        "workRulePayCodeDistribution": {
          "payCodeDistributionName": "$AU Oncall",
          "deviations": [],
          "overtimes": [],
          "zones": [],
          "majorities": []
        },
        "workRuleAutoBreakPlacement": {
          "minimumTimeBetweenStartOfShiftAndFirstBreak": "0:0",
          "minimumTimeBetweenEndOfBreakAndShiftEnd": "0:0",
          "minimumTimeBetweenBreaks": "0:0",
          "shiftLengthsToExclude": [],
          "newShiftLengths": []
        },
        "version": 3.0
      }],
      "version": 3.0
    }]




### Example - Delete Fixed Rule by ID

This example deletes a specific fixed rule.

  1. In the `Configure connector task` dialog, click `actions`.
  2. Select the `Delete Fixed Rule by ID ` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "Path parameters": {
             "id": 1152.0
           }
         } 

If the action is successful, the `Delete Fixed Rule by ID` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
     [{
      "ResponseBody": "",
      "StatusCode": 204.0
    }] 




### Example - Retrieve Accrual Codes 

This example retrieves accural codes.

  1. In the `Configure connector task` dialog, click `actions`.
  2. Select the `Retrieve Accrual Codes ` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "Query parameters": {
             "id": 1303.0
           }
         } 

If the action is successful, the `Retrieve Accrual Codes` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
     [{
      "ResponseBody": "[{\"id\":1303,\"typeId\":2,\"hoursPerDayInSeconds\":28800,\"name\":\"$LC Dia Familia\",\"shortName\":\"$LC Dia Familia\",\"typeName\":\"Day\",\"allowEdit\":true}]",
      "StatusCode": 200.0
    }]




### Example - Create Hours of Operation 

This example creates hours of operation.

  1. In the `Configure connector task` dialog, click `actions`.
  2. Select the `Create Hours of Operation ` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "Headers": {
             "Content-Type": "application/json"
           },
           "RequestBody": {
             "name": "$E-HoO Store 501 dummy3",
             "active": true,
             "effectiveVersions": [{
               "effectiveSpan": {
                 "startDate": "1900-01-01",
                 "endDate": "3000-01-01"
               },
               "unrestrictedEdit": true,
               "items": [{
                 "openTime": "09:00:00",
                 "closeTime": "21:00:00",
                 "closed": false,
                 "holiday": false,
                 "weekDay": {
                   "id": -1.0,
                   "qualifier": "EVERY_DAY"
                 }
               }, {
                 "openTime": "10:00:00",
                 "closeTime": "17:00:00",
                 "closed": false,
                 "holiday": false,
                 "weekDay": {
                   "id": 1.0,
                   "qualifier": "SUNDAY"
                 }
               }, {
                 "openTime": "10:00:00",
                 "closeTime": "18:00:00",
                 "closed": false,
                 "holiday": false,
                 "weekDay": {
                   "id": 7.0,
                   "qualifier": "SATURDAY"
                 }
               }]
             }]
           }
         }

If the action is successful, the `Create Hours of Operation` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
    [{
      "id": 851.0,
      "name": "$E-HoO Store 501 dummy3",
      "active": true,
      "version": 1.0,
      "effectiveVersions": [{
        "effectiveSpan": {
          "startDate": "1900-01-01",
          "endDate": "3000-01-01"
        },
        "unrestrictedEdit": true,
        "items": [{
          "id": 1051.0,
          "openTime": "09:00:00",
          "closeTime": "21:00:00",
          "closed": false,
          "holiday": false,
          "weekDay": {
            "id": -1.0,
            "qualifier": "EVERY_DAY"
          }
        }, {
          "id": 1052.0,
          "openTime": "10:00:00",
          "closeTime": "17:00:00",
          "closed": false,
          "holiday": false,
          "weekDay": {
            "id": 1.0,
            "qualifier": "SUNDAY"
          }
        }, {
          "id": 1053.0,
          "openTime": "10:00:00",
          "closeTime": "18:00:00",
          "closed": false,
          "holiday": false,
          "weekDay": {
            "id": 7.0,
            "qualifier": "SATURDAY"
          }
        }]
      }]
    }]




### Example - Update Timecard Setting by ID 

This example updates the specific time card setting.

  1. In the `Configure connector task` dialog, click `actions`.
  2. Select the `Update Timecard Setting by ID ` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "Path parameters": {
             "id": 3872335.0
           },
           "RequestBody": {
             "id": 3872335.0,
             "name": "Hourly Timecard -Employee Sharp",
             "label": "Hourly Timecard - Employee View",
             "description": "Hourly Timecard - Employee View",
             "timecardType": {
               "id": "HourlyEmployee",
               "name": "Hourly Employee"
             },
             "canEditFutureTimecard": false,
             "numberOfFutureDays": 0.0,
             "includeOvertimes": true,
             "fourPunchRow": false,
             "columnsOrder": [{
               "id": "Date",
               "name": "Date"
             }, {
               "id": "Schedule",
               "name": "Schedule"
             }, {
               "id": "Absence",
               "name": "Absence"
             }, {
               "id": "In",
               "name": "In"
             }, {
               "id": "Transfer",
               "name": "Transfer"
             }, {
               "id": "Out",
               "name": "Out"
             }, {
               "id": "PayCode",
               "name": "Pay Code"
             }, {
               "id": "Amount",
               "name": "Amount"
             }, {
               "id": "Shift",
               "name": "Shift"
             }, {
               "id": "Daily",
               "name": "Daily"
             }, {
               "id": "Period",
               "name": "Period"
             }],
             "includeActivityEvent": false,
             "includeActivityAllocation": false,
             "includeActivityTotalActual": false,
             "includeActivityTotalAllocated": false,
             "includeActivityTotalVariance": false,
             "hidePaidCorrection": false}

If the action is successful, the `Update Timecard Setting by ID` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
      [{
      "id": 3872335.0,
      "name": "Hourly Timecard -Employee Sharp",
      "label": "Hourly Timecard - Employee View",
      "description": "Hourly Timecard - Employee View",
      "timecardType": {
        "id": "HourlyEmployee",
        "name": "Hourly Employee"
      },
      "canEditFutureTimecard": false,
      "numberOfFutureDays": 0.0,
      "includeOvertimes": true,
      "fourPunchRow": false,
      "columnsOrder": [{
        "id": "Date",
        "name": "Date"
      }, {
        "id": "Schedule",
        "name": "Schedule"
      }, {
        "id": "Absence",
        "name": "Absence"
      }, {
        "id": "In",
        "name": "In"
      }, {
        "id": "Transfer",
        "name": "Transfer"
      }, {
        "id": "Out",
        "name": "Out"
      }, {
        "id": "PayCode",
        "name": "Pay Code"
      }, {
        "id": "Amount",
        "name": "Amount"
      }, {
        "id": "Shift",
        "name": "Shift"
      }, {
        "id": "Daily",
        "name": "Daily"
      }, {
        "id": "Period",
        "name": "Period"
      }],
      "includeActivityEvent": false,
      "includeActivityAllocation": false,
      "includeActivityTotalActual": false,
      "includeActivityTotalAllocated": false,
      "includeActivityTotalVariance": false,
      "hidePaidCorrection": false,
      "paidCorrectionFilterEnabled": true}] 




### Example - Retrieve People Information Profiles

This example retrieves people information profiles.

  1. In the `Configure connector task` dialog, click `actions`.
  2. Select the `Retrieve People Information Profiles ` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "Headers": {
             "Content-Type": "application/json"
           },
           "RequestBody": {
             "where": {
               "ids": [-1.0, 651.0]
             }
           }
         }

If the action is successful, the `Retrieve People Information Profiles` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
       [{
      "ResponseBody": "[{\"id\":-1,\"description\":\"Default People Information Profile with Default People Information Settings\",\"name\":\"Default People Information Profile\",\"peopleInfoSetting\":{\"id\":-1,\"description\":\"Default People Information Profile with All Hyperfind Query\",\"hfquery\":{\"id\":1,\"hfName\":\"&Person.All_Home\",\"name\":\"All Home\"},\"name\":\"Default People Information Profile\"}},{\"id\":651,\"description\":\"All Home Employees\",\"name\":\"$R-All Home\",\"peopleInfoSetting\":{\"id\":649,\"description\":\"All Home Employees\",\"hfquery\":{\"id\":1,\"hfName\":\"&Person.All_Home\",\"name\":\"All Home\"},\"name\":\"$R-All Home\"}}]",
      "StatusCode": 200.0
    }]




### Example - Retrieve All Employment Terms

This example retrieves all employment terms.

  1. In the `Configure connector task` dialog, click `actions`.
  2. Select the `Retrieve All Employment Terms ` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "Query parameters": {
             "id": 2202.0
           }
         } 

If the action is successful, the `Retrieve All Employment Terms` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
      [{
      "ResponseBody": "[{\"allowsInheritance\":false,\"isActive\":true,\"name\":\"$AU-Casual\",\"id\":2202,\"processType\":\"ENFORCE_END_DATE\",\"versions\":{\"employmentTermVersion\":[{\"id\":702,\"accrualProfile\":{\"id\":1402,\"qualifier\":\"$AU-Casual\",\"name\":\"$AU-Casual\"},\"endDate\":\"3000-01-01\",\"holidayProfile\":{\"id\":152,\"qualifier\":\"AU Casual Holiday Profile\",\"name\":\"AU Casual Holiday Profile\"},\"startDate\":\"1900-01-01\",\"minimumWage\":{}}]},\"persistentId\":\"$AU-Casual\"}]",
      "StatusCode": 200.0
    }]




### Example - Create Attestation Profiles

This example creates the attestation profiles.

  1. In the `Configure connector task` dialog, click `actions`.
  2. Select the `Create Attestation Profiles ` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "Headers": {
             "Content-Type": "application/json"
           },
           "RequestBody": {
             "versionCount": 0.0,
             "name": "Empty Profile 3",
             "deleted": false,
             "attestationAssignments": []
           }
         }

If the action is successful, the `Create Attestation Profiles` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
    [{
      "id": 434.0,
      "versionCount": 0.0,
      "name": "Empty Profile 3",
      "deleted": false
    }]




### Example - Retrieve Leave Profile by Id 

This example retrieves a leave profile based on the ID.

  1. In the `Configure connector task` dialog, click `actions`.
  2. Select the `Retrieve Leave Profile by Id ` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "Path parameters": {
             "id": 3.0
           }
         } 

If the action is successful, the `Retrieve Leave Profile by Id` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
     [{
      "id": 3.0,
      "isActive": true,
      "leaveProfileCategory": [{
        "id": 1.0,
        "qualifier": "Military",
        "leaveProfileCategoryConfigurableData": [{
          "configurableData": {
            "id": 1.0,
            "qualifier": "Active Duty Period"
          }
        }],
        "leaveProfileCategoryRule": [],
        "leaveProfileCategoryType": [{
          "leaveType": [{
            "id": 21.0,
            "qualifier": "Military Duty Leave Tracking"
          }]
        }, {
          "leaveType": [{
            "id": 53.0,
            "qualifier": "Personal Leave"
          }]
        }, {
          "leaveType": [{
            "id": 59.0,
            "qualifier": "Vacation Leave"
          }]
        }]
      }, {
        "id": 2.0,
        "qualifier": "Self",
        "leaveProfileCategoryConfigurableData": [{
          "configurableData": {
            "id": 2.0,
            "qualifier": "Amount Paid"
          }
        }, {
          "configurableData": {
            "id": 4.0,
            "qualifier": "Disability Case Number"
          }
    }]




### Example - Retrieve Available Rules

This example retrieves the available rules.

  1. In the `Configure connector task` dialog, click `actions`.
  2. Select the `Retrieve Available Rules ` action, and then click **Done**.
  3. In the **Data Mapping** section `Open Data Mapping Editor` and then enter a value similar to the following in the `Input` field: 
         
         {
           "Query parameters": {
             "leave_case_id": 189.0
           }
         } 

If the action is successful, the `Retrieve Available Rules` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    
     [{
      "leaveCase": {
        "id": 189.0,
        "qualifier": "Physical Therapy",
        "name": "Physical Therapy"
      },
      "availableLeaveRules": [{
        "id": 20.0,
        "availableLeaveTypes": [{
          "id": 1.0,
          "paid": false,
          "enabled": true,
          "payCode": {
            "id": 107.0,
            "qualifier": "LV-ADAA Leave",
            "name": "LV-ADAA Leave"
          },
          "accrualCode": {
            "id": 2.0,
            "qualifier": "LV-ADA Leave",
            "name": "LV-ADA Leave"
          },
          "qualifier": "ADA Leave",
          "name": "ADA Leave"
        }, {
          "id": 11.0,
          "paid": false,
          "enabled": true,
          "presentedInLeaveRule": true,
          "payCode": {
            "id": 134.0,
            "qualifier": "LV-FMLA Injury Illness",
            "name": "LV-FMLA Injury Illness"
          },
          "accrualCode": {
            "id": 12.0,
            "qualifier": "LV-FMLA",
            "name": "LV-FMLA"
          },
          "qualifier": "FMLA Illness Injury",
          "name": "FMLA Illness Injury"
        }, {
          "id": 31.0,
          "paid": false,
          "enabled": true,
          "presentedInLeaveRule": true,
          "payCode": {
            "id": 165.0,
            "qualifier": "LV-Non FMLA Tracking",
            "name": "LV-Non FMLA Tracking"
          },
          "accrualCode": {
            "id": 24.0,
            "qualifier": "LV-Tracking",
            "name": "LV-Tracking"
          },
          "qualifier": "Non-FMLA Illness Injury",
          "name": "Non-FMLA Illness Injury"
        }
    }]




## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file:

Parameter name | Data type | Required | Description  
---|---|---|---  
proxy_enabled | BOOLEAN | False | Select this checkbox to configure a proxy server for the connection.   
proxy_auth_scheme | ENUM | False | The authentication type to use to authenticate to the ProxyServer proxy. Supported values are: BASIC, DIGEST, NONE  
proxy_user | STRING | False | A user name to be used to authenticate to the ProxyServer proxy.   
proxy_password | SECRET | False | A password to be used to authenticate to the ProxyServer proxy.   
  
## Use the UKG connection in an integration

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
