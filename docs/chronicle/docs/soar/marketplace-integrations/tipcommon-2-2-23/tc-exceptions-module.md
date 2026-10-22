---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon-2-2-23/tc-exceptions-module/
title: exceptions module \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:03.496187+00:00
---

# exceptions module  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon-2-2-23/tc-exceptions-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# `exceptions` module

The **`exceptions` module** provides a standardized framework for error handling within the platform. It includes specialized exception classes for actions, connectors, jobs, and Google Cloud operations, allowing developers to catch and respond to specific failure scenarios with precision.

The following example demonstrates how to import and raise a specific error from this module:
    
    
    from TIPCommon.exceptions import ConnectorProcessingError
    raise ConnectorProcessingError('spam and eggs')
    

## Action exceptions

These exceptions handle errors that occur during the lifecycle of an action, from initialization to data reporting.

Exceptions  
---  
`GeneralActionException` | Bases: `Exception` Serves as the base class for all action-related exceptions.  
`ActionSetupError` | Bases: `GeneralActionException` Indicates an error during the initialization of an action.  
`CaseResultError` | Bases: `GeneralActionException` Occurs when errors happen while sending data to a case result.  
`EnrichActionError` | Bases: `GeneralActionException` Occurs when errors happen in an enrichment action.  
`SDKWrapperError` | Bases: `GeneralActionException` Occurs when errors happen in SDK method wrappers.  
`JobSetupError` | Bases: `GeneralActionException` Indicates a job initialization error.  
  
## Connector exceptions

These exceptions manage failure states specifically related to data connectors and their processing logic.

Exceptions  
---  
`GeneralConnectorException` | Bases: `Exception`Serves as the base class for all connector-related exceptions.  
`ConnectorSetupError` | Bases: `GeneralConnectorException`Indicates a failure during the initialization of a connector.  
`ConnectorContextError` | Bases: `GeneralConnectorException`Indicates an error within the connector context.  
`ConnectorProcessingError` | Bases: `GeneralConnectorException`Indicates a failure during the data processing phase of a connector.  
`ConnectorValidationError` | Bases: `GeneralConnectorException`Indicates that the connector encounters a validation error.  
  
## Google Cloud exceptions

These exceptions map to specific error states encountered when interacting with Google Cloud resources.

Exceptions  
---  
`GoogleCloudException` | Bases: `Exception` Serves as the general base class for Google Cloud errors.  
`AlreadyExistsError` | Bases: `GoogleCloudException` Occurs when a Google Cloud resource already exists.  
`NotFoundError` | Bases: `GoogleCloudException` Occurs when a Google Cloud resource isn't found.  
`PermissionDeniedError` | Bases: `GoogleCloudException` Occurs when the client lacks permission to perform the operation on the resource.  
`UnauthenticatedError` | Bases: `GoogleCloudException` Occurs when the client isn't authenticated properly.  
`DeadlineExceededError` | Bases: `GoogleCloudException` Occurs when the request does not complete in the time allocated.  
`ResourceExhaustedError` | Bases: `GoogleCloudException` Indicates that the quota for the cloud project is exceeded or there are too many concurrent requests from the client.  
`BadGatewayError` | Bases: `GoogleCloudException` Indicates that a server between the client and the backend Google Cloud servers detects a temporary issue.  
`UnavailableError` | Bases: `GoogleCloudException` Indicates the Google Cloud service is unable to process a request.  
`InvalidArgumentError` | Bases: `GoogleCloudException` Indicates an invalid request to a Google Cloud resource.  
`FailedPreconditionError` | Bases: `GoogleCloudException` Indicates a failed precondition error for a Google Cloud request.  
`ImpersonationUnauthorizedError` | Bases: `GoogleCloudException` Indicates the caller isn't authorized to impersonate the service account.  
  
## General and utility exceptions

This section contains exceptions for general system errors, parameter validation, and specialized data processing within Content Hub integrations.

Exceptions  
---  
`ParameterValidationError` | Bases: `Exception` Raised when a parameter is invalid.  
`EmptyMandatoryValues` | Bases: `Exception` Indicates an exception for empty mandatory values.  
`ParameterExtractionError` | Bases: `Exception` Indicates a parameter extraction error.  
`OauthError` | Bases: `Exception` Raised when a generic exception occurs in the OAuth 2.0 flow.  
`SMIMEMailError` | Bases: `Exception` Indicates a custom exception for S/MIME email processing errors.  
`InternalJSONDecoderError` | Bases: `Exception` Indicates an internal JSON parsing error using `json.load` or `json.dump`.  
`InvalidTimeException` | Bases: `Exception` Indicates an exception for invalid time.  
`NotSupportedPlatformVersion` | Bases: `Exception` Indicates a custom exception for platform version errors that aren't supported.  
`GeneralJobException` | Bases: `Exception` Serves as the general base class for job-related exceptions.  
`RefreshTokenRenewalJobException` | Bases: `GeneralJobException` Indicates a failure in a `RefreshTokenRenewalJob` instance.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
