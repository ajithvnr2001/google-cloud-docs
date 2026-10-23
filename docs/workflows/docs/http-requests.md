---
url: https://docs.cloud.google.com/workflows/docs/http-requests/
title: Make an HTTP request \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:55.998513+00:00
---

# Make an HTTP request  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/http-requests/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Make an HTTP request Stay organized with collections  Save and categorize content based on your preferences. 

You can define a workflow step that makes an HTTP call and assign the response from the call to a variable. For example, you can invoke a Google Cloud service [such as Cloud Run functions or Cloud Run](https://docs.cloud.google.com/workflows/docs/calling-run-functions) through an HTTP request.

Invoking a Google Cloud service through an HTTP request shouldn't be confused with using Workflows [connectors](https://docs.cloud.google.com/workflows/docs/connectors) to perform API operations. Connectors simplify calling services because they handle the formatting of requests for you, and provide methods and arguments so that you don't need to know the details of a Google Cloud API.

## Invoke an HTTP endpoint

This type of step lets you make an HTTP request. Both HTTP and HTTPS requests are supported. The most common HTTP request methods have a call shortcut (such as [http.get](https://docs.cloud.google.com/workflows/docs/reference/stdlib/http/get) and [http.post](https://docs.cloud.google.com/workflows/docs/reference/stdlib/http/post)), but you can make any type of HTTP request by setting the `call` field to `http.request` and specifying the type of request using the `method` field.

**Note:** Workflows doesn't support HTTP requests to the IP-based endpoints of Google Kubernetes Engine (GKE) cluster control planes. To ensure that your workflow functions as expected, you must access the DNS-based endpoints instead. For more information, see [HTTP requests to GKE](https://docs.cloud.google.com/workflows/docs/issues#gke-calls) and the [service announcement](https://docs.cloud.google.com/workflows/docs/service-announcements#2025-01-28).

### YAML
    
    
      - STEP_NAME:
          call: HTTP_REQUEST
          args:
              url: URL_VALUE
              method: REQUEST_METHOD
              private_service_name: "REGISTERED_SERVICE"
              headers:
                  HEADER_KEY:HEADER_VALUE
                  ...
              body:
                  BODY_KEY:BODY_VALUE
                  ...
              query:
                  QUERY_KEY:QUERY_VALUE
                  ...
              auth:
                  type: AUTH_TYPE
                  scope: AUTH_SCOPE
                  scopes: AUTH_SCOPE
                  audience: AUDIENCE
              timeout: TIMEOUT_IN_SECONDS
          result: RESULT_VALUE
        

### JSON
    
    
      [
        {
          "STEP_NAME": {
            "call": "HTTP_REQUEST",
            "args": {
              "url": "URL_VALUE",
              "method": "REQUEST_METHOD",
              "private_service_name": "REGISTERED_SERVICE",
              "headers": {"HEADER_KEY":"HEADER_VALUE",
              ...
              },
              "body": {"BODY_KEY":"BODY_VALUE",
              ...
              },
              "query": {"QUERY_KEY":"QUERY_VALUE",
              ...
              },
              "auth": {
                "type":"AUTH_TYPE",
                "scope":"AUTH_SCOPE",
                "scopes":"AUTH_SCOPE",
                "audience":"AUDIENCE"
              },
              "timeout": "TIMEOUT_IN_SECONDS"
            },
            "result": "RESULT_VALUE"
          }
        }
      ]
        

Replace the following: 

  * `HTTP_REQUEST`: required. Use one of the following for HTTP requests: 
    * `http.delete`
    * `http.get`
    * `http.patch`
    * `http.post`
    * `http.put`
    * `http.request`
  * `URL_VALUE`: required. URL where the request is sent.
  * `REQUEST_METHOD`: required if using call type `http.request`. The type of HTTP request method to use. For example: 
    * `GET`
    * `POST`
    * `PATCH`
    * `DELETE`
  * `REGISTERED_SERVICE`: optional. A registered Service Directory service name in the format `projects/PROJECT_ID/locations/LOCATION/namespaces/NAMESPACE_NAME/services/SERVICE_NAME`. For more information, see [Invoke a private endpoint using Service Directory's service registry](https://docs.cloud.google.com/workflows/docs/invoke-private-endpoint-vpc).
  * `HEADER_KEY`:`HEADER_VALUE`: optional. Header fields to supply input to the API. 

If using a `Content-Type` header to specify the media type of the request body, only the following types are supported:

    * `application/json` or `application/type+json`—must be a map
    * `application/x-www-form-urlencoded`—must be an unencoded string
    * `text/type`—must be a string

If a `Content-Type` header is specified, the body is encoded as prescribed. For example, it might be JSON or URL-encoded.

If using a `User-Agent` header to identify the requesting user agent, the following applies:

    * The default is `GoogleCloudWorkflows; (+https://cloud.google.com/workflows/docs)`
    * If a value is specified, `GoogleCloudWorkflows; (+https://cloud.google.com/workflows/docs)` is appended to that value 

For example, if `User-Agent: "MY_USER_AGENT_VALUE"` is specified, the HTTP request header would be as follows (with a space between the specified value and the appended default):
          
          MY_USER_AGENT_VALUE GoogleCloudWorkflows; (+https://cloud.google.com/workflows/docs)

  * `BODY_KEY`:`BODY_VALUE`: optional. Body fields to supply input to the API. 

If a `Content-Type` header is not specified, and if a request body is present, the following applies:

    * If the body value is bytes, the header is set to `Content-Type: application/octet-stream`.
    * Otherwise, the body is JSON-encoded and the header is set to `Content-Type: application/json; charset=utf-8`.
The following example is of a body structure equivalent to a JSON payload: 

### YAML
    
    body:
      requests:
      - image:
          source:
            gcsImageUri: ${gsUri}
        features:
        - type: LABEL_DETECTION
        - type: SAFE_SEARCH_DETECTION
        - type: IMAGE_PROPERTIES
    result: imageAnalysisResponse

### JSON
    
    {
      "requests":[
        {
          "image": {
            "source": {
                "gcsUri": "img.png"
            }
          },
          "features": [
            { "type":"LABEL_DETECTION" },
            { "type":"SAFE_SEARCH_DETECTION" },
            { "type":"IMAGE_PROPERTIES" },
          ]
        }
      ]
    }

  * `QUERY_KEY`:`QUERY_VALUE`: optional. Query fields to supply input to the API.
  * `AUTH_TYPE`: optional. Required if the API being called requires authentication. Use either `OIDC` or `OAuth2`. For more information, see [Make authenticated requests from a workflow](https://docs.cloud.google.com/workflows/docs/authenticate-from-workflow). 
    * `AUTH_SCOPE`: optional. Limits an application's access to a user's account. Use either the `scope` or `scopes` key. 

The `scope` key supports either a string or list of strings. For example: 

`"https://www.googleapis.com/auth/cloud-platform"`

or 

`["https://www.googleapis.com/auth/cloud-platform", "scope2", "scope3"]`

The `scopes` key, in addition to supporting a string or list of strings, supports space and comma-separated strings. For example:

`"https://www.googleapis.com/auth/cloud-platform scope2 scope3"`

or 

`"https://www.googleapis.com/auth/cloud-platform,scope2,scope3"`

For more information, see [ OAuth 2.0 Scopes for Google APIs](https://developers.google.com/identity/protocols/oauth2/scopes). 

    * `AUDIENCE`: optional. Specifies the audience for the OIDC token. By default, it's set to the same value as `url`; however, it should be set to your service's root URL. For example: `https://region-project.cloudfunctions.net/hello_world`. 
  * `TIMEOUT_IN_SECONDS`: optional. How long in seconds a request is allowed to run before throwing an exception. The maximum is 1800 seconds.
  * `RESULT_VALUE`: optional. Variable name where the result of an HTTP invocation step is stored.



## Access HTTP response data saved in a variable

If the `Content-Type` header for the response specifies an `application/json` media type, the JSON response that is stored in a variable is automatically converted to a map that can be accessed.

If necessary, modify the API that is being called to specify an `application/json` media type for the `Content-Type` response header. Otherwise, you can use the [`json.decode`](https://docs.cloud.google.com/workflows/docs/reference/stdlib/json/decode) and [`text.encode`](https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/encode) functions to convert the response body into a map. For example:
    
    
    json.decode(text.encode(RESPONSE_FROM_API))
    

Workflows includes a built-in parser for accessing this data. To access the fields from the HTTP response, use the following syntax:
    
    
    ${VARIABLE_NAME.body|code|headers.PATH_TO_FIELD}

Replace the following:

  * `VARIABLE_NAME`: the name of the workflow variable where you saved a JSON response.
  * `body`: use the `body` field to access the body of the HTTP response.
  * `code`: use the `code` field to access the HTTP response code.
  * `headers`: use the `headers` field to access the HTTP response headers by name.
  * `PATH_TO_FIELD`: the path to the field in the JSON response that you want to access. This might be the name of the field, or if the field is nested inside an object, it might take the form of `object1.object2.field`.



For example, if an API returns `{"age":50}` and a workflow stores that response in a variable called `age_response`, the following example returns the value of the `age` field; in this case, `50`:
    
    
    age_response.body.age
    

## Samples

These samples demonstrate the syntax.

### Assign the response from an API call

Unless you input your own search term, this sample uses your Google Cloud location to construct a search term, which it passes to the [Wikipedia API](https://wikipedia.org/w/api.php). A list of related Wikipedia articles is returned.

### YAML
    
    
    main:
      params: [input]
      steps:
        - checkSearchTermInInput:
            switch:
              - condition: '${"searchTerm" in input}'
                assign:
                  - searchTerm: '${input.searchTerm}'
                next: readWikipedia
        - getLocation:
            call: sys.get_env
            args:
              name: GOOGLE_CLOUD_LOCATION
            result: location
        - setFromCallResult:
            assign:
              - searchTerm: '${text.split(location, "-")[0]}'
        - readWikipedia:
            call: http.get
            args:
              url: 'https://en.wikipedia.org/w/api.php'
              query:
                action: opensearch
                search: '${searchTerm}'
            result: wikiResult
        - returnOutput:
            return: '${wikiResult.body[1]}'

### JSON
    
    
    {
      "main": {
        "params": [
          "input"
        ],
        "steps": [
          {
            "checkSearchTermInInput": {
              "switch": [
                {
                  "condition": "${\"searchTerm\" in input}",
                  "assign": [
                    {
                      "searchTerm": "${input.searchTerm}"
                    }
                  ],
                  "next": "readWikipedia"
                }
              ]
            }
          },
          {
            "getLocation": {
              "call": "sys.get_env",
              "args": {
                "name": "GOOGLE_CLOUD_LOCATION"
              },
              "result": "location"
            }
          },
          {
            "setFromCallResult": {
              "assign": [
                {
                  "searchTerm": "${text.split(location, \"-\")[0]}"
                }
              ]
            }
          },
          {
            "readWikipedia": {
              "call": "http.get",
              "args": {
                "url": "https://en.wikipedia.org/w/api.php",
                "query": {
                  "action": "opensearch",
                  "search": "${searchTerm}"
                }
              },
              "result": "wikiResult"
            }
          },
          {
            "returnOutput": {
              "return": "${wikiResult.body[1]}"
            }
          }
        ]
      }
    }
    

### Make an external HTTP POST request

This sample makes a POST request to an external HTTP endpoint.

### YAML
    
    
    - send_message:
        call: http.post
        args:
          url: https://www.example.com/endpoint
          body:
            some_val: "Hello World"
            another_val: 123
        result: the_message
    - return_value:
        return: ${the_message.body}

### JSON
    
    
    [
      {
        "send_message": {
          "call": "http.post",
          "args": {
            "url": "https://www.example.com/endpoint",
            "body": {
              "some_val": "Hello World",
              "another_val": 123
            }
          },
          "result": "the_message"
        }
      },
      {
        "return_value": {
          "return": "${the_message.body}"
        }
      }
    ]
    

### Make an external HTTP GET request with headers

This sample makes an HTTP GET request with a custom header. You can also supply custom header definitions when making other types of HTTP requests.

### YAML
    
    
    - get_message:
        call: http.get
        args:
          url: https://www.example.com/endpoint
          headers:
            Content-Type: "text/plain"
          query:
            some_val: "Hello World"
            another_val: 123
        result: the_message
    - return_value:
        return: ${the_message.body}

### JSON
    
    
    [
      {
        "get_message": {
          "call": "http.get",
          "args": {
            "url": "https://www.example.com/endpoint",
            "headers": {
              "Content-Type": "text/plain"
            },
            "query": {
              "some_val": "Hello World",
              "another_val": 123
            }
          },
          "result": "the_message"
        }
      },
      {
        "return_value": {
          "return": "${the_message.body}"
        }
      }
    ]

### Use OIDC to authenticate when making a request to Cloud Run functions

This sample makes an HTTP request using OIDC by adding an `auth` section to the `args` section of the workflow's definition, after specifying the URL.

### YAML
    
    
    - call_my_function:
        call: http.post
        args:
          url: https://us-central1-myproject123.cloudfunctions.net/myfunc1
          auth:
            type: OIDC
          body:
            some_val: "Hello World"
            another_val: 123
        result: the_message
    - return_value:
        return: ${the_message.body}

### JSON
    
    
    [
      {
        "call_my_function": {
          "call": "http.post",
          "args": {
            "url": "https://us-central1-myproject123.cloudfunctions.net/myfunc1",
            "auth": {
              "type": "OIDC"
            },
            "body": {
              "some_val": "Hello World",
              "another_val": 123
            }
          },
          "result": "the_message"
        }
      },
      {
        "return_value": {
          "return": "${the_message.body}"
        }
      }
    ]

### Catch and handle HTTP request errors

This sample implements a custom exception handler based on the HTTP status code returned by the GET request. The workflow catches a potential exception and returns a predefined error message. If an exception is not recognized, the workflow execution fails and throws the exception as returned by the GET request. For other error tags, see [Workflow errors](https://docs.cloud.google.com/workflows/docs/reference/syntax/error-types).

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

### JSON
    
    
    [
      {
        "read_item": {
          "try": {
            "call": "http.get",
            "args": {
              "url": "https://example.com/someapi",
              "auth": {
                "type": "OIDC"
              }
            },
            "result": "API_response"
          },
          "except": {
            "as": "e",
            "steps": [
              {
                "known_errors": {
                  "switch": [
                    {
                      "condition": "${not(\"HttpError\" in e.tags)}",
                      "next": "connection_problem"
                    },
                    {
                      "condition": "${e.code == 404}",
                      "next": "url_not_found"
                    },
                    {
                      "condition": "${e.code == 403}",
                      "next": "auth_problem"
                    }
                  ]
                }
              },
              {
                "unhandled_exception": {
                  "raise": "${e}"
                }
              }
            ]
          }
        }
      },
      {
        "url_found": {
          "return": "${API_response.body}"
        }
      },
      {
        "connection_problem": {
          "return": "Connection problem; check URL"
        }
      },
      {
        "url_not_found": {
          "return": "Sorry, URL wasn't found"
        }
      },
      {
        "auth_problem": {
          "return": "Authentication error"
        }
      }
    ]

## What's next

  * [Use Workflows with Cloud Run and Cloud Run functions tutorial](https://docs.cloud.google.com/workflows/docs/tutorials/run/cloud-run)
  * [Invoke a private endpoint using Service Directory's service registry](https://docs.cloud.google.com/workflows/docs/invoke-private-endpoint-vpc)
  * [Invoke an IAP-secured endpoint](https://docs.cloud.google.com/workflows/docs/invoke-iap-secured-endpoints)
  * [Workflows syntax reference](https://docs.cloud.google.com/workflows/docs/reference/syntax)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
