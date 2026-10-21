---
url: https://docs.cloud.google.com/integration-connectors/docs/viewconnections/
title: View connections \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:41:33.359695+00:00
---

# View connections  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/viewconnections/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# View connections

To view all the connections available within your Google Cloud project, go to the **Integration Connectors** page in the [Cloud console](https://console.cloud.google.com/) and select a Google Cloud project to open the **Connections** page. 

[ Go to the Connections page](https://console.cloud.google.com/connectors/connections)

To view the details of a specific connection, you click on a connection name in the table of existing connections. You can also filter the list of available connections by connection name (for example, `my-connection-1`) or connector type (for example, `BigQuery`).

Selecting an individual connection opens the **Connection Details** page, which displays the following information about the connection instance: 

  * Connector type
  * Connector status
  * Authentication type
  * Location
  * Connection details specific to the connector type
  * Locked status



## Connection status

A connection can be in any of the following statuses:

  * **Creating** : The connection is being provisioned.
  * **Active** : The connection is provisioned and is active.
  * **Refreshing schema** : The connection schema (for entities and actions) is being refreshed.
  * **Inactive** : The connection is inactive. The status will be inactive if you [suspend the connection](https://docs.cloud.google.com/integration-connectors/docs/suspend-resume-connection).
  * **Deleting** : The connection is getting deleted.
  * **Updating** : The connection is being updated.
  * **Error** : There is an error in the connection and it's not able to connect to the backend system. To identify the root cause, see the [Integration Connectors logs](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs).
  * **Authorization required** : The connection is created but the authorization is not configured.

**Note:** Your connection might be reset when the underlying infrastructure is restarted or updated. We recommend that you configure error handling strategies to re-establish the connection. For information about how to configure error handling strategies for Application Integration tasks, see [Configure error handling](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy#configure-error-handling-strategies).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
