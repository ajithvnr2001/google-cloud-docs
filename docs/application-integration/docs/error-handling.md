---
url: https://docs.cloud.google.com/application-integration/docs/error-handling/
title: Introduction to error handling \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:17:52.820401+00:00
---

# Introduction to error handling  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/error-handling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Introduction to error handling

In Application Integration, errors might occur when you're testing and publishing an integration, or during the execution of an integration. These errors can occur due to various client-side and server-side issues, and are broadly classified as follows: 

  * **Permanent errors:** All client-side errors such as, authentication failures, data validation errors, are considered as permanent errors. Permanent errors cause permanent task failures. 
  * **Temporary errors:** All server-side errors such as, HTTP 503 (service unavailable), HTTP 400 (bad request), are considered as temporary errors. Temporary errors cause temporary task failures. 



Error messages appear in the following locations: 

  * **Execution logs page** : Displays errors encountered during the execution of an integration. Each execution of an integration has a separate log entry. For information about execution logs page, see [Execution logs](https://docs.cloud.google.com/application-integration/docs/viewing-logs). 
  * **Integration editor page** : Displays errors encountered when you publish an integration. The errors are displayed at the bottom of the integration editor page. For information about the integration editor page, see [Integration editor](https://docs.cloud.google.com/application-integration/docs/integrations-ui-layout). 



For information on the list of error codes that you might encounter, see Error codes.

## Error handling methods

Application Integration supports the following error handling methods to throw, catch, retry, and customize the errors encountered in your integration: 

  * [**Error handling strategies**](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy): The error handling strategy for a task specifies the action to take if the task fails due to a temporary error. You can specify different error handling strategies for both synchronous and asynchronous execution modes.
  * [**Error catcher**](https://docs.cloud.google.com/application-integration/docs/error-catcher): Error catcher defines a customized way to handle the failure of an identified trigger, task, or edge condition in your integration. You can define one or more error catchers in a single integration to handle task errors and/or execution failures. Each error catcher can be invoked using a trigger, called the [Error Catcher trigger](https://docs.cloud.google.com/application-integration/docs/configure-error-catcher-trigger), to run the set of configured integration tasks customized to handle the error.



You can use error handling methods for both synchronous and asynchronous modes of integration execution:

  * **Synchronous executions:** In synchronous mode, the execution result of the integration is available soon after the integration runs. Synchronous mode is helpful in scenarios where you want the execution result immediately after the integration runs. Triggers execute the integration in the synchronous mode include the following: 
    * [Test or publish an integration](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations)
    * Call the [`projects.locations.integrations.execute`](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations/execute) API
    * Call the integration from a [sub-integration in the synchronous mode](https://docs.cloud.google.com/application-integration/docs/configure-call-integration-task)
  * **Asynchronous executions:** Asynchronous executions use the fire and forget model. Asynchronous mode is helpful in scenarios where integrations can take a long time to run, or the execution result is not required immediately after the integration runs. Triggers that execute the integration in the asynchronous mode include the following: 
    * All execution that are not synchronous are executed in asynchronous mode. Some of the common asynchronous mode includes, but is not limited to: 
      * [Schedule trigger](https://docs.cloud.google.com/application-integration/docs/configure-schedule-trigger)
      * [Cloud Scheduler trigger](https://docs.cloud.google.com/application-integration/docs/configure-cloud-scheduler-trigger)
      * [Cloud Pub/Sub trigger](https://docs.cloud.google.com/application-integration/docs/configure-pubsub-trigger)
      * [Salesforce trigger](https://docs.cloud.google.com/application-integration/docs/configure-salesforce-trigger)
      * Call the [`projects.locations.integrations.schedule`](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations/schedule) API
    * Executions that are resumed from a suspension or a approval task are also executed in aynchronous mode, even if the initial execution was is synchronous mode. 



## Best practice

Use both [error handling strategy](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy) and [error catcher](https://docs.cloud.google.com/application-integration/docs/error-catcher) in your integration. For any error, the integration follows the strategy defined in the error handling section. After exhausting the error handling strategy that are configured, error catcher logic is triggered. Use [system variables](https://docs.cloud.google.com/application-integration/docs/variables#system-variables) to capture the value of error code and error message to send to your error catcher flow.

## Example

Suppose you have an integration flow to create an order. New orders are created in Cloud SQL for MySQL. The flow uses a [connector task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task) (**Create an order** in this example) to connect to Cloud SQL for MySQL. In case of a database outage, the connector task throws errors while inserting new orders into the database. As a best practice, you must use both error handling strategy and error catcher in your integration.

To add the error handling strategy, click the connector task in the integration designer to open the task configuration pane. The following diagram shows the error handling strategy configured for the **Create an order** connector task:

![Error handling strategy for Create an order connector task](https://docs.cloud.google.com/static/application-integration/images/example-add-retry-policy.png)![Error handling strategy for Create an order connector task](https://docs.cloud.google.com/static/application-integration/images/example-add-retry-policy.png)

To add the error handling strategy, click the **Call REST Endpoint** task in the integration designer to open the task configuration pane. The following diagram shows the error handling strategy configured for the **Call REST Endpoint** task:

![Error handling strategy for the Call REST Endpoint task](https://docs.cloud.google.com/static/application-integration/images/example-retry-fixed-interval.png)![Error handling strategy for the Call REST Endpoint task](https://docs.cloud.google.com/static/application-integration/images/example-retry-fixed-interval.png)

To add the error catcher, click the **Call REST Endpoint** task in the integration designer to open the task configuration pane. In the **Error Catcher** section, add the error catcher details. The following diagram shows the error catcher configured for the **Call REST Endpoint** task:

![Error catcher for the Call REST Endpoint task](https://docs.cloud.google.com/static/application-integration/images/example-add-error-catcher.png)![Error catcher for the Call REST Endpoint task](https://docs.cloud.google.com/static/application-integration/images/example-add-error-catcher.png)

## Error codes

The following table describes the errors that you might encounter, and the corresponding causes for the errors. Application Integration uses the canonical error codes defined in [`google.rpc.Code`](https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto).

For information about Application Integration errors and different error handling strategies, see [Errors and error handling](https://docs.cloud.google.com/application-integration/docs/error-handling).

Standard exception type | Canonical code | HTTP code | Description  
---|---|---|---  
FailedPreconditionException | `FAILED_PRECONDITION` | 400 | Request can not be executed in the current system state.   
BadRequestException | `INVALID_ARGUMENT` | 400 | Client specified an invalid argument. Check error message and error details for more information.   
UnauthenticatedException | `UNAUTHENTICATED` | 401 | Request not authenticated due to missing, invalid, or expired OAuth token.   
ForbiddenException | `PERMISSION_DENIED` | 403 | Client does not have sufficient permission. This can happen if the OAuth token doesn't have the right scopes, the client doesn't have the required permissions, or the API has not been enabled.   
NotFoundException | `NOT_FOUND` | 404 | A specified resource is not found.   
AlreadyExistsException | `ALREADY_EXISTS` | 409 | The resource that a client tried to create already exists.   
InternalError | `INTERNAL` | 500  | Internal server error. Typically a server bug. This can happen if any of the tasks or triggers are incorrectly configured.  
UnimplementedException | `UNIMPLEMENTED` | 501 | API method not implemented by the server.   
ServiceUnavailableException | `UNAVAILABLE` | 503 | Service unavailable. Typically the server is down.   
AbortedException | `ABORTED` | 409 | Response size is too large.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
