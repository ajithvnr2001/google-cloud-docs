---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/http-v2/
title: HTTP v2 \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:49.887897+00:00
---

# HTTP v2  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/http-v2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# HTTP v2

This document provides guidance on how to integrate HTTP v2 with the SOAR module of Google Security Operations and work with the _Execute HTTP Request_ action.

## Overview

Use HTTP v2 to integrate with third-party products without writing code and solve use cases such as executing API requests, working with files, and managing asynchronous flows.

### Authentication flows

Depending on the product that you authenticate to, HTTP v2 supports the following authentication flows:

  * Basic authentication flow
  * API key flow
  * Dedicated authentication flow



#### Basic authentication flow

With the basic authentication flow, authenticate using the `Test URL`, `Basic Auth Username`, and `Basic Auth Password` parameters.

#### API key flow

With the API key flow, authenticate using the `Test URL`, `API Key Field Name`, and `API Key Field Value` parameters.

#### Dedicated authentication flow

In the dedicated authentication flow, the following two-step authentication is used:

  1. An action generates an access token.

When either Ping or the Execute HTTP Request action runs, the integration retrieves the parameters required for authentication.

  2. An action uses the generated access token to authenticate to API requests.




The dedicated authentication flow requires the following integration parameters:

  * `Dedicated Auth API Request Method`
  * `Dedicated Auth API Request URL`
  * `Dedicated Auth API Request Headers`
  * `Dedicated Auth API Request Body`
  * `Dedicated Auth API Request Token Field Name`



For more details about the integration parameters, see Integrate HTTP v2 with Google SecOps.

To use the token from the response, provide the key name in the `Dedicated Auth API Request Token Field Name` parameter. In the following response example, the key name is `access_token`:
    
    
    {
       "access_token": "eyJhbGciOiJSUzI1NiIsImtpZCIO4",
       "expires_in": 1799,
       "token_type": "bearer"
    }
    

To apply the token, the integration requires the following dedicated placeholder: `{{integration.token}}`. When you provide this placeholder in the payload, the integration uses the generated token.

If the `access_token` key in the JSON response appears nested, provide the full token location for the `Dedicated Auth API Request Token Field Name` parameter value. For example, instead of the `access_token` provide the `data_access_token` key for the nested response like the following:
    
    
    {
       "data": {
           "access_token": "eyJhbGciOiJSUzI1NiIsImtpZCIZMI3DQAQsYibMpO4",
           "expires_in": 1799,
           "token_type": "bearer"
       }
    }
    

The following example shows the request for the dedicated authentication flow to the Crowdstrike API:
    
    
    POST /falconx/entities/submissions/v1 HTTP/1.1
    Host: api.crowdstrike.com
    Content-Type: application/json
    Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6
    Content-Length: 209
    
    {
       "sandbox": [{
           "sha256": "9854c9dfded29d8442499daba01082ba5d164aa02e44",
           "environment_id": 100,
           "submit_name": "filename.pdf"
       }]
    }
    

The example uses the `Authorization` header with a `Bearer` token to authenticate to the API. To populate the header with the correct information, the HTTP v2 integration requires the following input: `Authorization: Bearer {{integration.token}}`.

## Integrate HTTP v2 with Google SecOps

The integration requires the following parameters:

Parameter | Description  
---|---  
`Test URL` | _Optional_ A test URL to use for the basic authentication or the API key authentication flow.  
`Basic Auth Username` | _Optional_ A parameter to add as a basic authentication header to every action execution alongside the **Basic Auth Password** parameter. Provide both the **Basic Auth Username** and **Basic Auth Password** parameters.  
`Basic Auth Password` | _Optional_ A parameter to add as a basic authentication header to every action execution alongside the **Basic Auth Username** parameter. Provide both the **Basic Auth Username** and **Basic Auth Password** parameters.  
`API Key Field Name` | _Optional_ The name of the header that contains the API key. Provide both the **API Key Field Name** and **API Key Secret** parameters to add them to every action execution.  
`API Key Secret` | _Optional_ The API key secret value. Provide both the **API Key Field Name** and **API Key Secret** parameters to add them to every action execution.  
`Dedicated Auth API Request Method` | _Optional_ The method to use in the dedicated authentication API flow to generate the access token.Default value is `POST`.   
`Dedicated Auth API Request URL` | _Optional_ The API request to use in the dedicated authentication API flow to generate the access token, such as `https://api.crowdstrike.com/oauth2/token`.  
`Dedicated Auth API Request Headers` | _Optional_ Headers to use in the dedicated authentication API flow to generate the access token.Provide headers as a JSON object, such as the following:
    
    
        {
        "Content-type": "application/x-www-form-urlencoded"
        }
          
  
`Dedicated Auth API Request Body` | _Optional_ The request body to use in the dedicated authentication API flow to generate the access token. Provide the parameter value as a JSON object, such as the following:
    
    
        {
        "client_id": "CLIENT_ID",
        "client_secret": "CLIENT_SECRET"
        }
          
  
##### `Dedicated Auth API Request Token Field Name`

| _Optional_ The name of the field that contains the generated access token. To use the access token in actions, use the following placeholder: `{{integration.token}}`. The response for token generation uses the underscore (`_`) as a delimiter.  
`CA Certificate` | _Optional_ The certificate authority (CA) certificate to use for validating the secure connection.If you use a remote agent to connect to an on-premises product, provide an additional layer of security by supplying the integration with the CA certificate to ensure the integrity of the connection. After you provide a CA certificate, all of the API requests use it.This parameter accepts the CA certificate in a form of the base64-encoded string.  
`Verify SSL` | _Required_ If selected, the system verifies that the SSL certificate for all integration connections is valid. Selected by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

The HTTP v2 integration includes the following actions:

  * Execute HTTP Request
  * Ping



### Execute HTTP Request

Use the **Execute HTTP Request** action to construct and execute a customized HTTP API request against a target URL.

This action doesn't run on Google SecOps entities. 

#### Action behavior

This action supports complex behaviors including asynchronous polling, dynamic payload construction, and file management.

##### Asynchronous polling

When `Expected Response Values` is provided, the action operates in asynchronous mode. In this mode, the action repeatedly polls the target endpoint to track the state of a response (for example, waiting for a long-running task to complete). 

The action evaluates the response body against the JSON conditions provided in the parameter and continues execution until the conditions are met or the action reaches its timeout.

###### Condition logic

The action supports the following logic for tracking response states:

  * **Single field matching** : The action waits for a specific field to reach a single value.
        
        {
          "state": "finished"
        }
        

  * **Multiple values (OR logic)** : The action stops execution if a field matches any value in a provided list. This is useful for stopping on both "success" and "error" states to avoid unnecessary polling.
        
        {
          "state": ["finished", "error"]
        }
        

  * **Multiple fields (AND logic)** : The action waits until all specified fields match their respective values simultaneously.
        
        {
          "state": "finished",
          "percentage": "100"
        }
        

  * **Combined logic** : You can combine multiple conditions within the JSON object.
        
        {
          "state": ["finished", "error"],
          "percentage": "10"
        }
        




###### JSON parsing behavior

When evaluating conditions, the action follows these rules:

  * **Global search** : The action searches the entire JSON response object for the specified keys. Provide the key name exactly as it appears in the JSON without prepending parent object names or using prefixes (for example, use `"state"`, not `"data_state"` or `"data-state"`).

  * **Multiple identical keys** : If the response contains multiple keys with the same name at different levels of the JSON hierarchy, the expected output is only reached when all matching key names satisfy the identical expected value.

For example, to search for the `finished` state in the JSON response and ignore other states, set all `state` keys in `Expected Response Values` to `finished`:
        
        {
        "data": {
          "state": "finished"
          },
          "state": "finished"
        }
        




##### Body payload construction

The action constructs the request body based on the `Content-Type` header provided in `Headers`. 

This is the `Body Payload` input used for the following construction examples:
    
    
    {
      "Id": "123123",
      "sorting": "asc"
    }
    

  * **`application/x-www-form-urlencoded`** : The action generates the payload as `Id=123123&sorting=asc`.

  * **`application/json`** : The action generates the following JSON payload:
        
        {
          "Id": "123123",
          "sorting": "asc"
        }
        

  * **`XML`** : If the third-party product requires XML, provide an XML-formatted input directly in `Body Payload`:
        
        <?xml version="1.0" encoding="utf-8"?>
        <soap:Envelope xmlns:soap="[http://schemas.xmlsoap.org/soap/envelope/](http://schemas.xmlsoap.org/soap/envelope/)">
        <soap:Body>
          <NumberToWords xmlns="[http://www.dataaccess.com/webservicesserver/](http://www.dataaccess.com/webservicesserver/)">
            <ubiNum>500</ubiNum>
          </NumberToWords>
        </soap:Body>
        </soap:Envelope>
        




##### File handling

The action supports the following workflows for managing files:

  * **Downloading files** :

    * To return file data as part of the JSON result in base64 format, select `Base64 Output`.

    * To save a file directly to the Case Wall as a ZIP archive, select `Save To Case Wall`.

  * **Uploading files** : To upload a file, convert it to a base64-encoded string and include it as part of the `Body Payload` value.

The following example shows an image file converted to a base64-encoded string:
        
        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
        

  * **Security** : For sensitive files (such as malware), select `Password Protect Zip`. This automatically encrypts the saved ZIP archive created using `Save To Case Wall` with the password `infected`.




#### Playbook block configuration

The following configuration demonstrates how to use the **Execute HTTP Request** action within a playbook block. Use this example to understand how to apply placeholders and input prefixes.

When using block inputs as placeholders, you must include the `Input.` prefix (for example, `[Input.comment]`).

  * **Method** : `PUT`

  * **URL Path** :
        
        https://{API_URL}/[Input.table_name]/[Input.sys_id]
        

  * **Headers** :
        
        {
          "Content-type": "application/json; charset=utf-8",
          "Accept": "application/json",
          "User-Agent": "GoogleSecops"
        }
        

  * **Body Payload** :
        
        {
          "work_notes": "[Input.comment]"
        }
        




#### Action inputs

The Execute HTTP Request action requires the following parameters:

Parameter | Description  
---|---  
  
##### `Method`

| _Optional_ The method to use in the request.Default value is `GET`. Possible values are:

  * `GET`
  * `POST`
  * `PUT`
  * `PATCH`
  * `DELETE`
  * `HEAD`
  * `OPTIONS`

  
  
##### `URL Path`

| _Optional_ The URL to execute.  
`URL Params` | _Optional_ The URL parameters.The action uses any value provided alongside the values that are directly provided in the **URL Path** parameter.For example, the `?parameter=value&sorting=asc` string in the backend means that the input is as follows: 
    
    
        {
        "parameter": "value",
        "sorting": "asc"
        }
        

This parameter requires the JSON object format as an input. The default value is as follows:
    
    
    {
        "URL Field Name": "URL_FIELD_VALUE"
        }  
  
##### `Headers`

| _Optional_ Headers to use in the HTTP request. For example, the HTTP request with the `Accept` and `User-Agent` headers requires the following input:
    
    
        {
        "Accept": "application/json",
        "User-Agent": "Google Secops"
        }
        

This parameter requires the JSON object format as an input. The default value is as follows:
    
    
    {
        "Content-Type": "application/json; charset=utf-8",
        "Accept": "application/json",
        "User-Agent" : "GoogleSecOps"
        }  
  
`Cookie` | _Optional_ The parameters to use in the Cookie header. This parameter overwrites the cookie provided in the **Headers** parameter. For example, to contain a Cookie header with the `PHPSESSID=298zf09hf012fh2; csrftoken=u32t4o3tb3gg43;` value, the HTTP request requires the following input:
    
    
        {
        "PHPSESSID": "298zf09hf012fh2",
        "csrftoken": "u32t4o3tb3gg43"
        }
        

This parameter requires the JSON object format as an input. The default value is as follows:
    
    
    {
        "Cookie_1": "COOKIE_1_VALUE"
        }  
  
##### `Body Payload`

| _Optional_ The body for the HTTP request. The action constructs different payloads depending on the `Content-Type` header value provided in the **Headers** parameter. This parameter requires the JSON object format as an input except when a third-party product requires an XML or the `multipart/form-data` content. If you submit or upload a file using the API request, provide the base64-encoded version of the file in the **Body Payload** parameter and set the header to `"Content-type": "multipart/form-data"`. The default value is as follows:
    
    
    {
        "Body Field Name": "BODY_FIELD_VALUE"
        }  
  
`Expected Response Values` | Optional. The JSON object containing the field-value pairs that define the required state of the response body. **Note:** Providing a value for this parameter triggers asynchronous polling behavior. For detailed information on formatting conditions and logical operators, see Action behavior.   
  
##### `Save To Case Wall`

| _Optional_ If selected, the action saves the file and attaches the saved file to the case wall. The file is archived with the `.zip` extension. The `.zip` file isn't password-protected.Not selected by default.  
  
##### `Password Protect Zip`

| _Optional_ If selected, the action adds a password to the `.zip` file created using the **Save To Case Wall** parameter. The password is as follows: `infected`. Use this parameter when working with suspicious files.Selected by default.  
`Follow Redirects` | _Optional_ If selected, the action follows the redirects.Selected by default.  
`Fail on 4xx/5xx` | _Optional_ If selected, the action fails if the status code of the response is 4xx or 5xx errors.Selected by default.  
  
##### `Base64 Output`

| _Optional_ If selected, the action converts the response to the base64 format.Use this parameter when downloading files.The JSON result cannot exceed 15 MB.Not selected by default.  
`Fields To Return` | _Required_ The fields to return. Possible values are:

  * `response_data`
  * `redirects`
  * `response_code`
  * `response_cookies`
  * `response_headers`
  * `apparent_encoding`

  
`Request Timeout` | _Required_ The amount of time to wait for the server to send data before the action fails.Default value is 120 seconds.  
  
#### Action outputs

The Execute HTTP Request action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the Execute HTTP Request action:
    
    
    {
       "response_data": {
           "data": {
               "relationships": {
                   "comment": [
                       {
                           "name": "item",
                           "description": "Object to which the comment belongs to."
                       },
                       {
                           "name": "author",
                           "description": "User who wrote the comment."
                       }
                   ]
               }
           }
       },
       "redirects": [],
       "response_code": 200,
       "cookies": {},
       "response_headers": {
           "Content-Type": "application/json",
           "X-Cloud-Trace-Context": "1ca450b35c66634a2ae01248cca50b19",
           "Date": "Fri, 03 Nov 2023 16:14:13 GMT",
           "Server": "Google Frontend",
           "Content-Length": "36084"
       },
       "apparent_encoding": "ascii"
    }
    

##### Output messages

On a Case Wall, the Execute HTTP Request action provides the following output messages:

Output message | Message description  
---|---  
`Successfully executed API request.` `Successfully executed API request, but status code STATUS_CODE was in response.` | Action succeeded.  
`Failed to execute API request. Error: ERROR_REASON` `Failed to execute API request. Error: Invalid parameter "PARAMETER_NAME".` `The JSON structure is invalid. Wrong value provided: VALUE` | Action failed.Check the connection to the server, input parameters, JSON file value, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the Execute HTTP Request action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Ping

Use this action to test the connectivity.

#### Action inputs

None.

#### Action outputs

The Ping action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

On a Case Wall, the Ping action provides the following output messages:

Output message | Message description  
---|---  
`Successfully tested connectivity.` | Action succeeded.  
`Failed to test connectivity.` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the Ping action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
