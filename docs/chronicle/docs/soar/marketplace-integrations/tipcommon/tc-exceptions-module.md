---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-exceptions-module/
title: Exceptions module \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:07.577002+00:00
---

# Exceptions module  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-exceptions-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Exceptions module

This module contains all constants in use by the TIPCommon package and common constants used in Google Security Operations Content Hub integrations.

##### Example
    
    
    from TIPCommon.exceptions import ConnectorProcessingError
    raise ConnectorProcessingError('spam and eggs')
    

### _exception_ TIPCommon.exceptions.ActionSetupError

Bases: **GeneralActionException**

An action initialization error.

### _exception_ TIPCommon.exceptions.AlreadyExistsError

Bases: **GoogleCloudException**

A Google Cloud resource already exists.

### _exception_ TIPCommon.exceptions.BadGatewayError

Bases: **GoogleCloudException**

A server between the client and the backend Google Cloud servers detected a temporary issue.

### _exception_ TIPCommon.exceptions.CaseResultError

Bases: **GeneralActionException**

Error when sending data to the case result.

### _exception_ TIPCommon.exceptions.ConnectorContextError

Bases: **GeneralConnectorException**

A connector context error.

### _exception_ TIPCommon.exceptions.ConnectorProcessingError

Bases: **GeneralConnectorException**

A connector processing error.

### _exception_ TIPCommon.exceptions.ConnectorSetupError

Bases: **GeneralConnectorException**

A connector initialization error.

### _exception_ TIPCommon.exceptions.ConnectorValidationError

Bases: **GeneralConnectorException**

A connector validation error.

### _exception_ TIPCommon.exceptions.DeadlineExceededError

Bases: **GoogleCloudException**

The request did not complete in the time allocated.

### _exception_ TIPCommon.exceptions.EmptyMandatoryValues

Bases: **Exception**

An exception for empty mandatory values.

### _exception_ TIPCommon.exceptions.EnrichActionError

Bases: **GeneralActionException**

An enrichment action error.

### _exception_ TIPCommon.exceptions.FailedPreconditionError

Bases: **GoogleCloudException**

A failed precondition error for a Google Cloud request.

### _exception_ TIPCommon.exceptions.GeneralActionException

Bases: **Exception**

A general action exception.

### _exception_ TIPCommon.exceptions.GeneralConnectorException

Bases: **Exception**

A general connector exception.

### _exception_ TIPCommon.exceptions.GeneralJobException

Bases: **Exception**

A general job exception.

### _exception_ TIPCommon.exceptions.GoogleCloudException

Bases: **Exception**

A general Google Cloud exception.

### _exception_ TIPCommon.exceptions.ImpersonationUnauthorizedError

Bases: **GoogleCloudException**

The caller is not authorized to impersonate the service account.

### _exception_ TIPCommon.exceptions.InternalJSONDecoderError

Bases: **Exception**

An internal JSON parsing error using `json.load/dump`. Message only.

### _exception_ TIPCommon.exceptions.InvalidArgumentError

Bases: **GoogleCloudException**

An invalid request to the Google Cloud resource.

### _exception_ TIPCommon.exceptions.InvalidTimeException

Bases: **Exception**

An exception for invalid time.

### _exception_ TIPCommon.exceptions.JobSetupError

Bases: **GeneralActionException**

A job initialization error.

### _exception_ TIPCommon.exceptions.NotFoundError

Bases: **GoogleCloudPubSubException**

The Google Cloud resource was not found.

### _exception_ TIPCommon.exceptions.OauthError

Bases: **Exception**

A generic exception raised when an error occurs in an OAuth 2.0 flow.

### _exception_ TIPCommon.exceptions.ParameterExtractionError

Bases: **Exception**

A parameter extraction error.

### _exception_ TIPCommon.exceptions.ParameterValidationError

Bases: **Exception**

Invalid parameter.

### _exception_ TIPCommon.exceptions.PermissionDeniedError

Bases: **GoogleCloudException**

The client does not have permission to perform the operation on the resource.

### _exception_ TIPCommon.exceptions.RefreshTokenRenewalJobException

Bases: **GeneralJobException**

A failure in a `RefreshTokenRenewalJob` instance.

### _exception_ TIPCommon.exceptions.ResourceExhaustedError

Bases: **GoogleCloudException**

The quota for the Google Cloud project exceeded, or there are too many concurrent requests from the client.

### _exception_ TIPCommon.exceptions.SDKWrapperError

Bases: **GeneralActionException**

A SDK method wrapper error.

### _exception_ TIPCommon.exceptions.SMIMEMailError

Bases: **Exception**

A custom exception for S/MIME email processing errors.

### _exception_ TIPCommon.exceptions.UnauthenticatedError

Bases: **GoogleCloudException**

Client authentication error.

### _exception_ TIPCommon.exceptions.UnavailableError

Bases: **GoogleCloudException**

The Google Cloud service was unable to process a request.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
