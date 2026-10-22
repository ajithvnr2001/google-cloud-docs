---
url: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/troubleshoot-ca-errors/
title: Troubleshoot Conversational Analytics API errors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:45.863112+00:00
---

# Troubleshoot Conversational Analytics API errors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/troubleshoot-ca-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Conversational Analytics API ](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview)



Send feedback 

#  Troubleshoot Conversational Analytics API errors Stay organized with collections  Save and categorize content based on your preferences. 

If you encounter issues while using the Conversational Analytics API, refer to the following table for potential solutions.

**Note:** To provide feedback or request support for this feature, send an email to [conversational-analytics-api-feedback@google.com](mailto:conversational-analytics-api-feedback@google.com).**Error** | **Error cause** | **HTTP status code** | **gRPC status code** | **Resolution**  
---|---|---|---|---  
`AlreadyExistsException` | `ALREADY_EXISTS` | `409 Conflict` | 6  | The resource already exists (for example, you are creating a duplicate entry). Use a different identifier or confirm that the resource doesn't already exist before creating it.   
`BadRequestException` | `INVALID_ARGUMENT` | `400 Bad Request` | 3  | The input is invalid or malformed. Validate the inputs or payloads before sending the request.   
`ForbiddenException` | `PERMISSION_DENIED` | `403 Forbidden` | 7  | You are authenticated but you are not allowed to access the resource. Check your user role and permissions. Contact an administrator if needed.   
`PermissionDenied` (Organization policy) | `PERMISSION_DENIED` | `403 Forbidden` | 7 |  The request violates an organization policy constraint, such as a location restriction or a CMEK requirement. Review the error message in the response body to identify which constraint was violated. For more information, see [Troubleshoot policy violations](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/organization-policies#troubleshoot).   
`FailedPreconditionException` | `FAILED_PRECONDITION` | `400 Bad Request` | 9  | The request violates the system state (for example, trying to delete a non-empty folder). Check the preconditions and fix the logic.   
`NotFoundException` | `NOT_FOUND` | `404 Not Found` | 5  | The resource is not found. Verify resource IDs or URLs. Ensure that the resource exists before trying to access it. See [Frequently asked questions about the Conversational Analytics API](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/frequently-asked-questions#error-handling) for more troubleshooting information.  
`ServiceUnavailableException` | `UNAVAILABLE` | `503 Service Unavailable` | 14  | There is a temporary server issue. Wait and retry with exponential backoff between attempts. If the error persists, [file a bug report](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview#send_feedback).   
`Connection reset by peer` (during streaming)  | `UNAVAILABLE` | `503 Service Unavailable` | 14  |  If you use a standard HTTP or REST client to call the streaming `:chat` endpoint, the server may have encountered a fatal error (such as a timeout or permission denial) during the stream. Because HTTP headers are already sent, the true error code is placed in HTTP/2 trailers, which standard REST clients cannot parse, resulting in a socket crash. We recommend using the official Google Cloud gRPC client libraries, such as the Python SDK, to call streaming endpoints. These libraries parse these trailing headers and surface the true error cause.  
`Internal error encountered` (during streaming)  | `INTERNAL` | `500 Internal Server Error` | 13  |  If you use a standard HTTP or REST client to call the streaming `:chat` endpoint, the server may have encountered a fatal error during the stream. Because HTTP headers are already sent, the true error code is placed in HTTP/2 trailers, which standard REST clients cannot parse, resulting in a socket crash. We recommend using the official Google Cloud gRPC client libraries, such as the Python SDK, to call streaming endpoints. These libraries parse these trailing headers and surface the true error cause.  
`UnauthenticatedException` | `UNAUTHENTICATED` | `401 Unauthorized` | 16  | Authentication is required, or authentication failed. Ensure that you are using the correct login credentials, API key, or token.   
`UnimplementedException` | `UNIMPLEMENTED` | `501 Not Implemented` | 12  | The requested feature is not available or not supported. Avoid calling this API, or wait for implementation.   
  
## Additional resources

For additional troubleshooting tips and answers to frequently asked questions, see the [Frequently asked questions about the Conversational Analytics API](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/frequently-asked-questions#error-handling) page.

For guidance about asking effective questions of the Conversational Analytics API, see the [Ask effective questions](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/ask-effective-questions) documentation page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
