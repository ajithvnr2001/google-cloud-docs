---
url: https://docs.cloud.google.com/api-gateway/docs/path-templating/
title: Understand path templating \u00a0|\u00a0 API Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:14:09.249869+00:00
---

# Understand path templating  |  API Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/path-templating/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Understand path templating

Within API Gateway, it is possible to route incoming requests based on the [path template](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#path-template-syntax). A path template has three main components:

  * Exact match
  * Single wildcard match
  * Double wildcard match



The following sections describe each of these components and how they work within the context of API Gateway.

## Exact match

A templated path _without_ any single or double wildcard segments (`*` or `**`) is converted to an exact path match. For example, the OpenAPI spec for your gateway API config may contain a section like the following:
    
    
    ...
    paths:
      /shelves:
        get:
          summary: List shelves
    ...
    

In this example, the gateway will _only_ accept requests to `/shelves` and no other paths.

**Note:** URL-encoded forward slashes (`%2F`) won't be treated as actual forward slashes, meaning `%2Fshelves` will _not_ match the OpenAPI operation described earlier in the specification.

## Single wildcard matching

If a templated path contains a variable, a singular wildcard segment (`{var}`), or in OpenAPI 2.0 only, a singular wildcard segment (`{var=*}`), the gateway will allow incoming requests that comply with the following:

  * The requests don't contain an additional forward slash (`/`), meaning the variable will only match a single path segment.
  * The requests contain at least one character.
  * The requests may contain an additional trailing slash if present at the end of the path.

**Note:** For variable expansion, all characters except `[-_.~/0-9a-zA-Z]` are percent-encoded.

For example, the OpenAPI spec for your gateway API config may contain a section like the following:
    
    
    ...
    paths:
      /shelves/{shelf}/books/{book}:
        get:
          summary: Retrieve a book
    ...
    

In this example, the gateway will accept requests that match the following regular expression:
    
    
    ^/shelves/[^/]+/books/[^/]+/?$
    

**Note:** If you are using an OpenAPI 3.x specification, the syntax `/shelves/{shelf=*}/books/{book=*}` is not supported and will be rejected.

## Double wildcard matching

If a templated path contains a variable denoted by a double wildcard segment (e.g `{var=**}`), the gateway will allow incoming requests that comply with the following:

  * The requests can contain _all_ characters, including forward slashes (/).
  * The requests can contain 0 or more characters.
  * The requests may contain an additional trailing slash if present at the end of the path.

**Note:** If you are using an OpenAPI 3.x specification, double wildcard syntax is not supported. For OpenAPI 2.0 specifications, double wildcard variables can only be used in the _last_ segment of the provided path. This means that `/shelves/{shelf=**}/books/{book=**}` is not allowed, because `{shelf=**}` is not declared in the last segment of the path. For variable expansion, all characters except `[-_.~/0-9a-zA-Z]` are percent-encoded.

For example, the OpenAPI spec for your gateway API config may contain a section like the following:

### OpenAPI 2.0
    
    
    ...
    paths:
      /shelves/{shelf=*}/books/{book=**}:
        get:
          summary: Retrieve a book
    ...

### OpenAPI 3.x
    
    
    ...
    paths:
      /shelves/{shelf}/books/{book}:
        get:
          summary: Retrieve a book
          parameters:
          - name: shelf
            in: path
            schema:
              type: string
          - name: book
            in: path
            schema:
              type: string
            x-google-parameter:
              pattern: '**'
    ...

In this example, the gateway will accept requests where the `book` parameter matches any characters, including forward slashes. This corresponds to the following regular expression:
    
    
    ^/shelves/[^/]+/books/.*/?$
    

## URL encoded forward slashes

API Gateway follows [RFC 3986](https://tools.ietf.org/html/rfc3986), which does not treat URL encoded forward slashes (`%2F`) as actual slashes when matching URL paths for routing or security decisions. If URL encoded slashes are expected, your backend should handle these requests accordingly.

**Warning:** If your backend expects URL encoded forward slashes (%2F) to be treated as actual slashes when matching API Gateway path templates, then requests containing URL encoded forward slashes may match unexpected operations and result in over-privileged access to backend resources.

For example, consider the following OpenAPI spec:
    
    
    securityDefinitions:
      api_key:
        type: "apiKey"
        name: "key"
        in: "query"
    paths:
      /shelves/{shelf}:
          get:
            parameters:
            - in: path
              name: shelf
              type: string
              required: true
              description: Shelf ID.
            summary: List shelves
            operationId: GetShelf
              responses:
                '200':
                  description: A successful response
                  schema:
                    type: string
        /shelves/{shelf}/books/{book}:
          get:
            parameters:
            - in: path
              name: shelf
              type: string
              required: true
              description: Shelf ID.
            - in: path
              name: book
              type: string
              required: true
              description: Book ID
            summary: Retrieve a book
            operationId: GetBook
              responses:
                '200':
                  description: A successful response
                  schema:
                    type: string
             security:
             - api_key: []
    

In this example, the `/shelves/{shelf}/books/{book}` operation requires an API key, but the `/shelves/{shelf}` operation is unrestricted.

In the event that a user sends a request to `/shelves/shelf_1%2Fbooks%2Fbook_2`:

  * The gateway will process the request as a `GetShelf` operation for the shelf ID `shelf_1%2Fbooks%2Fbook_2`. In this case, an API key check is **not enforced**.
  * If the `%2F` is normalized before any request handling by the backend, the request may instead be processed as the `GetBook` operation for the book ID `book_2`. In other words, the backend processes `/shelves/shelf_1%2Fbooks%2Fbook_2` as `/shelves/shelf_1/books/book_2`.



In this example, the backend expects the `GetBook` operation to perform an API key check at the gateway. However, because the gateway read the request as a `GetShelf` operation, **no API key check was performed**.

## Normalization of Multiple Adjacent Forward Slashes

API Gateway follows [RFC 3986](https://tools.ietf.org/html/rfc3986), which states that paths with multiple adjacent forward slashes will be treated as a different path than those with singular forward slashes.

For example, a request containing `/shelves///` will **not be normalized by the gateway** to the request path `/shelves/` prior to matching a URI path template _nor_ upon forwarding to the specified backend.

**Warning:** If your backend normalizes URL paths by merging multiple forward slashes to a single slash, then requests containing multiple adjacent forward slashes may match unexpected gateway operations and may result in over-privileged access to your backend resources.

## Syntax rules

API Gateway enforces several syntax validation rules for path templates:

  * **Variable Naming Conventions:** Variable names must begin with a letter (lower or uppercase) or an underscore (`_`), and can only contain letters, numbers, underscores, dots (`.`), and hyphens (`-`). 
    * Valid: `{my_var}`, `{var-1}`, `{var.name}`
    * Invalid: `{1var}`, `{my var}`
  * **No Parameter and Literal Mixing:** A single path segment cannot contain both a parameter and literal characters. 
    * Valid: `/prefix/{var}`
    * Invalid: `/prefix-{var}`, `/{var}suffix`
  * **Allowed Custom Method Suffix:** The only exception to mixing parameters and literals is in the _last segment_ of the path, where a custom method suffix starting with a colon (`:`) is permitted. 
    * Valid: `/{var}:customMethod`
    * Invalid: `/{var}:customMethod/suffix`
  * **No Multiple Parameters per Segment:** A single path segment cannot contain more than one parameter. 
    * Valid: `/{var1}/{var2}`
    * Invalid: `/{var1}{var2}`
  * **No Nested Parameters:** Parameters cannot be nested within each other. 
    * Valid: `/{var}`
    * Invalid: `/{{var}}`
  * **Double Wildcard** : Double wildcard segments can only be in the last path segment. 
    * Valid: `/prefix/{var=**}`, `/prefix/**`
    * Invalid: `/{var=**}/suffix`, `/**/suffix`



## Limits

Limit | Value  
---|---  
Number of parameters per path | 60  
Variable name length | 100  
Path length (with or without templating) | 512  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
