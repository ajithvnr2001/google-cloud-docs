---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/azure-monitor/
title: Integrate Azure Monitor with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:45:57.661899+00:00
---

# Integrate Azure Monitor with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/azure-monitor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Azure Monitor with Google SecOps 

This document explains how to integrate Azure Monitor with Google Security Operations (Google SecOps).

## Use cases

The **Azure Monitor** integration can address the following use cases:

  * **Log enrichment and context** : Use Google SecOps capabilities to search Azure Monitor logs (such as, Azure Activity or Security Events) during an incident to retrieve additional context, confirming suspicious activities or identifying the scope of a breach involving Azure resources.

  * **Investigating Azure authentication events** : Use Google SecOps capabilities to query sign-in logs when a suspicious IP address or user entity is identified, quickly retrieving all related authentication attempts and access history from Azure to aid in account compromise investigations.

  * **Validation of cloud misconfigurations** : Use Google SecOps capabilities to execute specific Kusto Query Language (KQL) queries against the Azure Activity log to check for recent changes to network security groups, firewall rules, or key Azure service configurations that may have triggered an alert.




## Before you begin

Before you configure the integration in the Google SecOps platform, verify that you have the following:

  * **Azure AD Application Registration** : An Azure Active Directory (Azure AD) application with the necessary permissions (such as, Observability Analytics Reader) to access log data, from which you must obtain the Client ID and Client Secret. For detailed steps on setting up this application for API access, see [Access the Azure Monitor Logs API](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/api/access-api?tabs=rest).

  * **Tenant ID** : The unique identifier for your Azure Active Directory instance, which is required to complete the OAuth 2.0 authentication flow.

  * **Log Analytics Workspace ID** : The unique identifier of the specific Azure Monitor Observability Analytics workspace that the integration queries for logs. For more information on how to locate the Workspace ID, see [Workspaces](https://portal.azure.com/#browse/Microsoft.OperationalInsights%2Fworkspaces).




## Integration parameters

The **Azure Monitor** integration requires the following parameters:

Parameter | Description  
---|---  
`Login API Root` | Required. The login API root of the Azure Monitor service. The default value is `https://login.microsoftonline.com`.  
`API Root` | Required. The API root of the Azure Monitor service. The default value is `https://api.loganalytics.io`.  
`Tenant ID` | Required. The Azure Monitor account tenant ID.  
`Client ID` | Required. The Azure Monitor account Client ID.  
`Client Secret` | Required. The Azure Monitor account Client Secret.  
`Workspace ID` | Required. The Azure Monitor account Workspace ID.  
`Verify SSL` | Required. If selected, the integration validates the SSL certificate when connecting to the Azure Monitor server. Enabled by default.  
  
## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Ping

Use the **Ping** action to test the connectivity to Azure Monitor.

This action doesn't run on Google SecOps entities. 

#### Action inputs

None.

#### Action outputs

The **Ping** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result. | Available  
  
##### Output messages

The **Ping** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the Azure Monitor server with the provided connection parameters!` | The action succeeded.  
`Failed to connect to the Azure Monitor server! Error is ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Search Logs

Use the **Search Logs** action to execute KQL commands against your Azure Monitor workspace to retrieve specific log data based on the provided query string.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Search Logs** action requires the following parameters:

Parameter | Description  
---|---  
`Workspace ID` | Optional. The ID of the workspace to search. If no value is provided, the action uses the Workspace ID from the integration configuration.  
`Query` | Required. The query (KQL command) that the action executes against the log data.  
`Time Frame` | Optional. The timeframe for the query. If `Custom` is selected, you must also provide `Start Time`. The possible values are as follows:

  * `Last Hour`
  * `Last 6 Hours`
  * `Last 24 Hours`
  * `Last Week`
  * `Last Month`
  * `Custom`

The default value is `Last Hour`.  
`Start Time` | Optional. The start time for the query in ISO 8601 format. If `Custom` is selected in `Time Frame`, this parameter is required.  
`End Time` | Optional. The end time for the query in ISO 8601 format. If `Custom` is selected in `Time Frame` and no value is provided, the current time is used.  
`Max Results To Return` | Required. The maximum number of results for the search to return. The maximum value is`1000`. The default value is `100`.  
  
#### Action outputs

The **Search Logs** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result. | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Search Logs** action:
    
    
    [
     {
       "TimeGenerated": "2025-10-07T06:44:40.4570918Z",
       "OperationName": "Update datascanners"
     },
     {
       "TimeGenerated": "2025-10-07T06:44:41.1760472Z",
       "OperationName": "Update datascanners"
     },
    ]
    

##### Output messages

The **Search Logs** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned results for the query QUERY in Azure Monitor.` `No results were found for the query QUERY in Azure Monitor.` | The action succeeded.  
`Error executing action "Search Logs". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Search Logs** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
