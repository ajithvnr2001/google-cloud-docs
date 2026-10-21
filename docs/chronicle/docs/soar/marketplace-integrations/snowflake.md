---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/snowflake/
title: Integrate Snowflake with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:09:48.700835+00:00
---

# Integrate Snowflake with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/snowflake/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Snowflake with Google SecOps 

This document explains how to integrate Snowflake with Google Security Operations (Google SecOps).

## Endpoints

The Snowflake integration uses the following Snowflake API endpoints:

  * `/api/statements?async=false`: used to test the connection to the Snowflake instance. This endpoint executes a simple query to verify the connectivity.

  * `/api/statements?async=true`: used to submit both custom and simple queries to Snowflake. The `async=true` parameter supports asynchronous execution and enables the actions to retrieve large datasets without blocking the Google SecOps platform.

  * `/api/statements/QUERY_ID`: used to retrieve the results of a previously submitted query. The integration replaces the `QUERY_ID` placeholder with the unique identifier, which the `/api/statements?async=true` endpoint returns.




## Before you begin

To use the Snowflake integration, generate a private key and encode it in the base64 format.

To generate the private key, use SnowSQL. For more information on how to use SnowSQL, see [Installing SnowSQL](https://docs.snowflake.com/en/user-guide/snowsql-install-config.html).

The Snowflake integration relies on the key pair authentication. For more information about keys in Snowflake, see [Using key-pair authentication](https://docs.snowflake.com/en/developer-guide/sql-api/authenticating.html#using-key-pair-authentication).

## Integration parameters

The Snowflake integration requires the following parameters:

Parameter | Description  
---|---  
`API Root` | Required.The API root of the Snowflake instance. The default value is `https://INSTANCE.snowflakecomputing.com`.   
`Account` | Required.The name of the Snowflake account.  
`Username` | Required.The username to access Snowflake.  
`Private Key` | Required.A private key to authenticate with.  
`Verify SSL` | Required.If selected, the integration validates the SSL certificate when connecting to Snowflake.Selected by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action).

### Execute Custom Query

Use the **Execute Custom Query** action to execute a custom query in Snowflake.

This action is asynchronous. Adjust the script timeout value in the Google SecOps integrated development environment (IDE) for the action as needed.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Execute Custom Query** action requires the following parameters:

Parameter | Description  
---|---  
`Query` | Required. The SQL query to execute in Snowflake.The action automatically adds the `LIMIT` keyword to the query. Don't manually set the `LIMIT` keyword. The query only supports single quotes.  
`Database` | Required. The name of the Snowflake database to query.  
`Schema` | Optional. The name of the schema within the specified database to query.  
`Max Results To Return` | Optional. The maximum number of results to return from the query for every action run.The default value is `50`.  
  
#### Action outputs

The **Execute Custom Query** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Execute Custom Query** action:
    
    
    {
        "C_CUSTKEY": "CUSTOMER_KEY",
        "C_NAME": "Customer#ID",
        "C_ADDRESS": "9Ii4zQn9cX",
        "C_NATIONKEY": "14",
        "C_PHONE": "800-555-0175"
    
    }
    

##### Output messages

The **Execute Custom Query** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully executed query "QUERY" in Snowflake.` `No results were found for the query "QUERY" in Snowflake.` | The action succeeded.  
`Error executing action "Execute Custom Query". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Execute Custom Query** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Execute Simple Query

Use the **Execute Simple Query** action to execute a query that is based on the provided parameters.

This action is asynchronous. Adjust the script timeout value in the Google SecOps IDE for the action as needed.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Execute Simple Query** action requires the following parameters:

Parameter | Description  
---|---  
`Database` | Required. The name of the database to query.  
`Table` | Required. The name of the table to query.  
`Schema` | Optional. The name of the schema to query.  
`Where Filter` | Optional. The `WHERE` clause to filter the query results.Don't use the `LIMIT` or `SORT` keywords. Don't set the `WHERE` string in the payload.The query only supports single quotes.  
`Fields To Return` | Optional. A comma-separated list of fields to return.If you don't configure this parameter, the action returns all fields. The default value is `*`.  
`Sort Field` | Optional. The value to sort the results.  
`Sort Order` | Optional. The sorting order (ascending or descending). The possible values are as follows:

  * `ASC`
  * `DESC`

The default value is `ASC`.  
`Max Results To Return` | Optional. The maximum number of results to return for every action run. The default value is `50`.  
  
#### Action outputs

The **Execute Simple Query** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Execute Simple Query** action:
    
    
    {
        "C_CUSTKEY": "CUSTOMER_KEY",
        "C_NAME": "Customer#ID",
        "C_ADDRESS": "9Ii4zQn9cX",
        "C_NATIONKEY": "14",
        "C_PHONE": "800-555-0175"
    
    }
    

##### Output messages

The **Execute Simple Query** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully executed query "QUERY" in Snowflake.` `No results were found for the query "QUERY" in Snowflake.` | The action succeeded.  
`Error executing action "Execute Simple Query". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Execute Simple Query** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Ping

Use the **Ping** action to test the connectivity to Snowflake.

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
Script result | Available  
  
##### Output messages

The **Ping** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the Snowflake server with the provided connection parameters!` | The action succeeded.  
`Failed to connect to the Snowflake server! The error is ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
