---
url: https://docs.cloud.google.com/workflows/docs/reference/stdlib/http/delete/
title: Function: http.delete \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:07.949657+00:00
---

# Function: http.delete  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/stdlib/http/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Function: http.delete Stay organized with collections  Save and categorize content based on your preferences. 

Sends an HTTP `DELETE` request to the specified URL.

For more information, see [Make an HTTP request](https://cloud.google.com/workflows/docs/http-requests).

## Arguments

Arguments  
---  
`url` |  `string` The URL to send the request to.  
`timeout` |  `float` The request timeout, in seconds (default: `300.0`). If the request takes longer than the timeout, a `TimeoutError` is raised. The maximum allowed timeout is `1800` seconds.  
`body` | If present, the request body (it is rare but allowed to send body in a DELETE request).  
`headers` | The HTTP request headers. If present, must be a map of strings.  
`query` | Optional query parameters. If present, must be a map that will get URL-encoded and appended to the URL. The map values must be strings, ints, floats, booleans, or lists of those.  
`auth` | Optional authentication properties. If present, must be a map with `type` attribute in `["OIDC", "OAuth2"]`. A `scopes` key is also supported. For details, see [Make authenticated requests to Google Cloud APIs](https://cloud.google.com/workflows/docs/authenticate-from-workflow#authenticate-apis).  
`private_service_name` |  `string` If present, `private_service_name` must be a string that specifies a registered Service Directory service name with format `projects/my-project/locations/us-east1/namespaces/` `my-namespace/services/my-service`.  
`ca_certificate` |  `bytes` If present, `ca_certificate` must be a bytes value describing a custom CA certificate in DER format that will be used in place of the standard certificate pool. The certificate must be signed by a subject alternative name as defined by [RFC 3280](https://www.rfc-editor.org/rfc/rfc3280).  
  
## Returns

The HTTP response as a map with `body`, `code` (status code), and `headers` attributes.

## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (DNS failure, truncated response, etc.).  
`ConnectionFailedError` | When the connection is halted during transfer (failed connection, refused connection, etc.).  
`TimeoutError` | When the specified timeout is reached before the response is received.  
`HttpError` | If the response status is >= 400.  
`ValueError` | If timeout is > 1800\. If the URL is invalid or if authType is present and URL is invalid for the given authType. If the private_service_name is invalid. If private_service_name is present and URL contains a port. If ca_certificate is present but not of type bytes.  
  
## Examples
    
    
    # Make a `DELETE` request to an external HTTP endpoint
    - delete_resource:
        call: http.delete
        args:
          url: https://www.example.com/endpoint
        result: message
    - return_value:
        return: ${message.body}

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
