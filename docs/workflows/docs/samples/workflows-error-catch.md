---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-error-catch/
title: Catch errors \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:49.887643+00:00
---

# Catch errors  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-error-catch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Catch errors Stay organized with collections  Save and categorize content based on your preferences. 

Implements a custom exception handler based on the HTTP status code returned by a GET request. The workflow catches a potential exception and returns a predefined error message. 

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Catch errors](https://docs.cloud.google.com/workflows/docs/reference/syntax/catching-errors)
  * [Make an HTTP request](https://docs.cloud.google.com/workflows/docs/http-requests)



## Code sample

### YAML
    
    
    # Use a custom exception handler to catch exceptions and return predefined
    # error messages; if the exception isn't recognized, the workflow
    # execution fails and throws the exception returned by the GET request
    - read_item:
        try:
          call: http.get
          args:
            url: https://example.com/someapi
            auth:
              type: OIDC
          result: API_response
        except:
          as: e
          steps:
            - known_errors:
                switch:
                  - condition: ${not("HttpError" in e.tags)}
                    next: connection_problem
                  - condition: ${e.code == 404}
                    next: url_not_found
                  - condition: ${e.code == 403}
                    next: auth_problem
            - unhandled_exception:
                raise: ${e}
    - url_found:
        return: ${API_response.body}
    - connection_problem:
        return: "Connection problem; check URL"
    - url_not_found:
        return: "Sorry, URL wasn't found"
    - auth_problem:
        return: "Authentication error"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
