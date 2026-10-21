---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/oauth-http-status-code-reference/
title: OAuth HTTP error response reference \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:41:41.516515+00:00
---

# OAuth HTTP error response reference  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/oauth-http-status-code-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  OAuth HTTP error response reference Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**Note:** **This topic is deprecated.** The error names and HTTP response codes associated with the OAuthV2 policies are described in each policy's reference documentation: 

  * [OAuthv2 policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy)
  * [GetOAuthv2Info policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/get-oauth-v2-info-policy)
  * [SetOAuth v2 Info policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-oauth-v2-info-policy)
  * [DeleteOAuthv2Info policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/delete-oauth-v2-info)



This topic provides HTTP status codes you may encounter when an OAuth policy throws errors in Apigee. 

For guidance on handling errors, see [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

For policy-specific error codes, see [OAuth v2 policy error reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#errorreference).

## Authorization Code

### Invalid Redirect URI
    
    
    HTTP/1.1 400 Bad Request
    {"ErrorCode" : "invalid_request", "Error" :"Invalid redirection uri http://www.invalid_example.com"}

### No Redirect URI
    
    
    HTTP/1.1 400 Bad Request {"ErrorCode" : "invalid_request", "Error" :"Redirection URI is required"}

### Invalid Key
    
    
    HTTP/1.1 401 Unauthorized {"ErrorCode" : "invalid_request", "Error" :"Invalid client id : AVD7ztXReEYyjpLFkkPiZpLEjeF2aYAz. ClientId is Invalid"}

### Missing Key
    
    
    HTTP/1.1 400 Bad Request
    {"ErrorCode" : "invalid_request", "Error" :"The request is missing a required parameter : client_id"}

### Invalid Response Type
    
    
    HTTP/1.1 400 Bad Request
    {"ErrorCode" : "invalid_request", "Error" :"Response type must be code"}

### Missing Response Type
    
    
    HTTP/1.1 400 Bad Request
    {"ErrorCode" : "invalid_request", "Error" :"The request is missing a required parameter : response_type"}

## Generate AccessToken

### Invalid Auth Code
    
    
    HTTP status: 400 Bad Request
    {"ErrorCode" : "invalid_request", "Error" :"Invalid Authorization Code"}

### No Redirect URI
    
    
    HTTP/1.1 400 Bad Request
    {"ErrorCode" : "invalid_request", "Error" :"Required param : redirect_uri"}

### Invalid Redirect URI
    
    
    HTTP/1.1 400 Bad Request
    {"ErrorCode" : "invalid_request", "Error" :"Invalid redirect_uri : oob"}

### Invalid Client ID when GenerateResponse is false

This error is returned when the `<GenerateResponse>` property is set to **false** and the client credentials are invalid.
    
    
    {
        "fault": {
            "faultstring": "Invalid client identifier {0}",
            "detail": {
                "errorcode": "oauth.v2.InvalidClientIdentifier"
            }
        }
    }

### Invalid Client ID when GenerateResponse is true

This error is returned when the `<GenerateResponse>` property is set to **true** and the client credentials are invalid.
    
    
    {"ErrorCode" : "invalid_client", "Error" :"ClientId is Invalid"}

### Invalid GrantType
    
    
    HTTP/1.1 400 Bad Request
    {"ErrorCode" : "invalid_request", "Error" :"Unsupported grant type : client_credentials_invalid"}

### No Username
    
    
    HTTP/1.1 400 Bad Request
    {"ErrorCode" : "invalid_request", "Error" :"Required param : username"}

### No Password
    
    
    HTTP/1.1 400 Bad Request
    {"ErrorCode" : "invalid_request", "Error" :"Required param : password"}

### No GrantType (Custom Policy)
    
    
    HTTP/1.1 400 Bad Request
    {"ErrorCode" : "invalid_request", "Error" :"Required param : grant_type"}

### No AuthCode
    
    
    HTTP/1.1 400 Bad Request
    {"ErrorCode" : "invalid_request", "Error" :"Required param : code"}

## Implicit

### Invalid Client ID
    
    
    HTTP/1.1 401 Unauthorized
    {"ErrorCode" : "invalid_request", "Error" :"Invalid client id : AVD7ztXReEYyjpLFkkPiZpLEjeF2aYAz. ClientId is Invalid"}

### No Client ID
    
    
    HTTP/1.1 400 Bad Request
    {"ErrorCode" : "invalid_request", "Error" :"The request is missing a required parameter : client_id"}

### Invalid Response Type
    
    
    HTTP/1.1 400 Bad Request
    {"ErrorCode" : "invalid_request", "Error" :"Response type must be token"}

### No Response Type
    
    
    HTTP/1.1 400 Bad Request
    {"ErrorCode" : "invalid_request", "Error" :"The request is missing a required parameter : response_type"}

### Invalid Redirect URI
    
    
    HTTP/1.1 400 Bad Request
    {"ErrorCode" : "invalid_request", "Error" :"Invalid redirection uri http://www.invalid_example.com"}

### No Redirect URI
    
    
    HTTP/1.1 400 Bad Request
    {"ErrorCode" : "invalid_request", "Error" :"Redirection URI is required"}

## Refresh Token

### Invalid RefreshToken
    
    
    HTTP/1.1 400 Bad Request
    {"ErrorCode" : "invalid_request", "Error" :"Invalid Refresh Token"}

### Expired RefreshToken
    
    
    HTTP/1.1 400 Bad Request
    {"ErrorCode" : "invalid_request", "Error" :"Refresh Token expired"}

### Invalid Scope
    
    
    HTTP/1.1 400 Bad Request
    {"ErrorCode" : "invalid_request", "Error" :"Invalid Scope"}

### Invalid Client ID when GenerateResponse is false

This error is returned when the GenerateResponse property is set to **false** and the client credentials are invalid.
    
    
    {
        "fault": {
            "faultstring": "Invalid client identifier {0}",
            "detail": {
                "errorcode": "oauth.v2.InvalidClientIdentifier"
            }
        }
    }

### Invalid Client ID when GenerateResponse is true

This error is returned when the GenerateResponse property is set to **true** and the client credentials are invalid.
    
    
    {"ErrorCode" : "invalid_client", "Error" :"ClientId is Invalid"}

## Verify AccessToken

### Invalid AccessToken
    
    
    HTTP/1.1 401 Unauthorized
    {"fault":{"faultstring":"Invalid Access Token","detail":{"errorcode":"keymanagement.service.invalid_access_token"}}}

### Invalid Resource
    
    
    HTTP/1.1 401 Unauthorized
    {"fault":{"faultstring":"APIResource \/facebook\/acer does not exist","detail":{"errorcode":"keymanagement.service.apiresource_doesnot_exist"}}}

### Invalid Scope
    
    
    HTTP/1.1 403 Forbidden
    {"fault":{"faultstring":"Required scope(s) : VerifyAccessToken.scopeSet","detail":{"errorcode":"steps.oauth.v2.InsufficientScope"}}}

### No Auth Header
    
    
    HTTP/1.1 401 Unauthorized
    {"fault":{"faultstring":"Invalid access token","detail":{"errorcode":"oauth.v2.InvalidAccessToken"}}}

### No match for ApiProduct (With Env & Proxy Configured)
    
    
    HTTP/1.1 401 Unauthorized
    {"fault":{"faultstring":"Invalid API call as no apiproduct match found","detail":{"errorcode":"keymanagement.service.InvalidAPICallAsNoApiProductMatchFound"}}}

### Access token expired
    
    
    HTTP/1.1 401 Unauthorized
    {"fault":{"faultstring":"Access Token expired","detail":{"errorcode":"keymanagement.service.access_token_expired"}}}

### Access token revoked
    
    
    HTTP/1.1 401 Unauthorized
    {"fault":{"faultstring":"Access Token not approved","detail":{"errorcode":"keymanagement.service.access_token_not_approved"}}}

## Get OAuth V2 Info

### Invalid Refresh Token
    
    
    HTTP/1.1 404 Not Found
    {"fault::{"detail":{"errorcode":"keymanagement.service.invalid_refresh_token"},"faultstring":"Invalid Refresh Token"}}

### Invalid Access Token
    
    
    HTTP/1.1 404 Not Found
    {
      "fault": {
        "faultstring": "Invalid Access Token",
        "detail": {
          "errorcode": "keymanagement.service.invalid_access_token"
        }
      }
    }

### Expired Access Token
    
    
    HTTP/1.1 500 Not Found
    {
      "fault": {
        "faultstring": "Access Token expired",
        "detail": {
          "errorcode": "keymanagement.service.access_token_expired"
        }
      }
    }

### Expired Refresh Token
    
    
    HTTP/1.1 500 Not Found
    {
      "fault": {
        "faultstring": "Refresh Token expired",
        "detail": {
          "errorcode": "keymanagement.service.refresh_token_expired"
        }
      }
    }

### Invalid Client ID
    
    
    HTTP/1.1 404 Not Found
    {
      "fault": {
        "faultstring": "Invalid Client Id",
        "detail": {
          "errorcode": "keymanagement.service.invalid_client-invalid_client_id"
        }
      }
    }

### Invalid Authorization Code
    
    
    HTTP/1.1 404 Not Found
    {
      "fault": {
        "faultstring": "Invalid Authorization Code",
        "detail": {
          "errorcode": "keymanagement.service.invalid_request-authorization_code_invalid"
        }
      }
    }

### Expired Authorization Code
    
    
    HTTP/1.1 500 Not Found
    {
      "fault": {
        "faultstring": "Authorization Code expired",
        "detail": {
          "errorcode": "keymanagement.service.authorization_code_expired"
        }
      }
    }

## Set OAuth V2 Info

### Invalid Access Token
    
    
    HTTP/1.1 404 Not Found
    {
      "fault": {
        "faultstring": "Invalid Access Token",
        "detail": {
          "errorcode": "keymanagement.service.invalid_access_token"
        }
      }
    }

### Expired Access Token
    
    
    HTTP/1.1 500 Not Found
    {
      "fault": {
        "faultstring": "Access Token expired",
        "detail": {
          "errorcode": "keymanagement.service.access_token_expired"
        }
      }
    }

## Delete OAuth V2 Info

On success, the policy returns a 200 status.

On failure, the policy returns 404 and output similar to the following (depending on whether you are deleting an access token or an auth code):
    
    
    HTTP/1.1 404 Not Found
    Content-Type: application/json
    Content-Length: 144
    Connection: keep-alive
    
    {"fault":{"faultstring":"Invalid Authorization Code","detail":{"errorcode":"keymanagement.service.invalid_request-authorization_code_invalid"}}}

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
