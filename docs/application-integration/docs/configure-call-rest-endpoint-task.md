---
url: https://docs.cloud.google.com/application-integration/docs/configure-call-rest-endpoint-task/
title: Call REST Endpoint task \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:05.221854+00:00
---

# Call REST Endpoint task  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/configure-call-rest-endpoint-task/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Call REST Endpoint task

The **Call REST Endpoint** task lets you call any third-party REST API from your integration. The response from the REST API call will be available to you in an integration variable and can be used in other down-stream tasks. 

**Note:**

  * The network configuration of the **Call REST Endpoint** task allows it to call endpoints only available over the public internet. Hence, the task can't connect to hosts or IPs that reside only within a private network such as a VPC, even if that VPC is peered with your other Google Cloud services such as Apigee X.
  * This task can process a maximum of 34 MB (34,000,000 bytes) of REST response.



## Before you begin

  * To connect to an authentication endpoint for the REST API call, ensure that you have either [created an OAuth 2.0 profile](https://docs.cloud.google.com/application-integration/docs/configuring-auth-profile#createAuthProfile) or [attached a user-managed service account](https://docs.cloud.google.com/application-integration/docs/access-control#add-service-account) to your integration. If your API does not require authentication, then the **Authentication profile** field in the task configuration pane can be left empty. To see a list of configurations, see Configuration properties. 

If your integration has both OAuth 2.0 profile and a user-managed service account configured, then by default the OAuth 2.0 profile is used for authentication. If neither OAuth 2.0 profile nor user-managed service account is configured, then the execution fails.

  * If your integration has a service account attached, then based on the REST endpoint URL, grant the required IAM role to that service account. For example, if your REST endpoint URL calls a Cloud Storage service, then grant the required IAM role for the Cloud Storage service. 

For information about granting roles to a service account, see [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).

  * Ensure that [VPC Service Controls](https://docs.cloud.google.com/application-integration/docs/vpc-service-controls) is **NOT** setup for Application Integration in your Google Cloud project. **Warning:** **Cloud Function** does not function or stops functioning if [VPC Service Controls](https://docs.cloud.google.com/application-integration/docs/vpc-service-controls) is setup for Application Integration in your Google Cloud project. 



## Configure the Call REST Endpoint task

To configure the **Call REST Endpoint** task: 

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**. 

The **Integrations** page appears listing all the integrations available in the Google Cloud project. 

  3. Select an existing integration or click **Create integration** to create a new one. 

If you are creating a new integration: 

     1. Enter a name and description in the **Create Integration** pane.
     2. Select a region for the integration. **Note:** The **Regions** dropdown only lists the regions provisioned in your Google Cloud project. To provision a new region, click **Enable Region**. See [Enable new region](https://docs.cloud.google.com/application-integration/docs/enable-new-region) for more information. 
     3. Select a service account for the integration. You can change or update the service account details of an integration any time from the info **Integration summary** pane in the integration toolbar. **Note:** The option to select a service account is displayed only if you have enabled integration governance for the selected region. 
     4. Click **Create**. The newly created integration opens in the _integration editor_. 

  4. In the _integration editor_ navigation bar, click **Tasks** to view the list of available tasks and connectors. 
  5. Click and place the **Call REST Endpoint** element in the integration editor.
  6. Click the **Call REST Endpoint** element on the designer to view the **Call REST Endpoint** task configuration pane.
  7. Configure the displayed fields using the configuration properties of the task as detailed in the table below. 

Changes to the properties are saved automatically. 

**Note:** If you update the authentication profile for a **Call REST Endpoint** task, and test the integration without publishing the changes, the integration uses the old authentication profile. To ensure that the integration uses the updated authentication profile, you must [publish the integration](https://cloud.google.com/application-integration/docs/test-publish-integrations) before testing. 



## Configuration properties

The following table describes the configuration properties of the **Call REST Endpoint** task. 

**Property** | **Data type** | **Description**  
---|---|---  
Label | String | Optional: add a label for your task.  
Authentication | String | Optional: configures and stores the authentication details for connections to external systems. For more information, see [Create authentication profiles in Application Integration](https://docs.cloud.google.com/application-integration/docs/configuring-auth-profile).  
Endpoint base URL  | String  | REST endpoint URL without the query parameters.   
HTTP method  | NA  | HTTP method to use.  You can select any of the following HTTP methods:

  * DELETE 
  * GET 
  * HEAD 
  * PATCH 
  * POST 
  * PUT

  
URL query string parameters  | Query string key : **String** Value: **String** | Query parameters required for the REST API call.  The query parameters are in the form of key-value pairs where key is the key name and the value is the corresponding key value. You can enter more than one key-value pair by clicking on the plus icon.   
HTTP headers  | HTTP header key: **String** Value: **String** | HTTP headers required for the REST API call.  The HTTP headers are in the form of key-value pairs where key is the key name and the value is the corresponding key value. You can enter more than one key-value pair by clicking on the plus icon.   
Request body  | String  | Payload of the REST request. Applicable for `POST`, `PUT`, and `PATCH` HTTP methods. Maximum supported size is 20 MB.   
Follow redirects  | Boolean  | Follow URL redirects.  You can select any one of the values:

  * **True** : Calls the redirected URL if the Endpoint base URL is forwarded to another URL.
  * **False** : Does not call the redirected URL if the Endpoint base URL is forwarded to another URL.

  
Task should fail on HTTP error  | Boolean  | Exception handling strategy when the REST API call fails. The **Call REST Endpoint** fails if the HTTP response code is `4xx` or `5xx`. For a list of error codes, see [Error codes](https://docs.cloud.google.com/application-integration/docs/error-codes). For other HTTP response codes, return error code and error message in the response. **Note:** For errors that are not related to REST API call, such as incorrect URL, the task always fail irrespective of what this option is set to. You can select any one of the values: 

  * **True** : Throws an exception.
  * **False** : Does not throw an exception. But returns the error code and the error message in the response. 

  
Response header (<Task name>)  | String  | Uncompressed response header from the REST APIs response.   
Response body (<Task name>)  | String  | Uncompressed response body from the REST APIs response.   
Response status (<Task name>)  | String  | HTTP response code and the corresponding code text from the REST APIs response.   
  
## Best practices

For information about the usage limits that apply to the **Call REST Endpoint** task, see [ Usage limits](https://docs.cloud.google.com/application-integration/docs/quotas#usage-limits). 

## Error handling strategy

An error handling strategy for a task specifies the action to take if the task fails due to a [temporary error](https://docs.cloud.google.com/application-integration/docs/error-handling). For information about how to use an error handling strategy, and to know about the different types of error handling strategies, see [Error handling strategies](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy). 

To learn how to handle retry strategies for `4xx` or `5xx` errors, see the [How to retry Rest Caller Task based on Response Status](https://www.googlecloudcommunity.com/gc/Integration-Services/How-to-retry-Rest-Caller-Task-based-on-Response-Status/m-p/618079) blog.

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
