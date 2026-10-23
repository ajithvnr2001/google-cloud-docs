---
url: https://docs.cloud.google.com/application-integration/docs/error-codes/
title: Error codes \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:16.346542+00:00
---

# Error codes  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/error-codes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Resources ](https://docs.cloud.google.com/application-integration/docs/release-notes)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Error codes

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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
