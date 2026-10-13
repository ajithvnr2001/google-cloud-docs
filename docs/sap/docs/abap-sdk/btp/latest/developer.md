---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/developer/
title: Application development with the SAP BTP edition of ABAP SDK for Google Cloud \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:30.596405+00:00
---

# Application development with the SAP BTP edition of ABAP SDK for Google Cloud  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/developer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Application development with the SAP BTP edition of ABAP SDK for Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

SAP BTP edition v1.1keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/developer)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/developer)



This document provides you with useful information and resources to help you develop SAP applications using the SAP BTP edition of ABAP SDK for Google Cloud.

This document is intended for SAP ABAP developers.

For a complete list of client libraries that the SAP BTP edition of ABAP SDK for Google Cloud provides, see [ABAP SDK for Google Cloud client libraries](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview).

## Single-window of interaction

Each Google Cloud API enabled in the ABAP SDK for Google Cloud is represented by an ABAP class, contained in the package `/GOOG/CLIENT`. An ABAP class consists of multiple public methods and each of these public methods corresponds to a Google Cloud API method. Each public method further consists of `IMPORTING` parameters and `EXPORTING` parameters. An ABAP class also contains custom data types, which can be used to construct and map the `IMPORTING` and `EXPORTING` parameters. These custom data types map to the API schema definitions.

For every interaction with a target Google Cloud API, its corresponding ABAP class acts as the only interaction point. We call this concept, _Single-window of interaction_ , which shields all the underlying complexities of interacting with a Google Cloud API and presents a simplified interface. This simplified interface lets you focus on the business solutions being developed using the SDK, without worrying about the underlying SDK features.

![Single-window of interaction](https://docs.cloud.google.com/static/sap/docs/images/abap-sdk-single-window-interaction.png)

### Interaction flow

To call an API method, you have the following interaction flow:

  1. Connect to an API.
  2. Construct an input request using the ABAP types.
  3. Call an API method.
  4. Parse errors and exceptions.
  5. Read the response using the ABAP types.



![Developer interaction](https://docs.cloud.google.com/static/sap/docs/images/abap-sdk-btp-developer-interaction.png)

### API client stub

A typical API client stub class consist of the following sections:

  * The ABAP types that map to the API schemas. You use ABAP types to construct an input request and parse the response.
  * The constants and attributes for internal or external usage.
  * The API methods for interacting with API resources.



![Class structure](https://docs.cloud.google.com/static/sap/docs/images/abap-sdk-class-structure.png)

### Features

The ABAP SDK for Google Cloud includes the following features:

  * HTTP communication: the SDK establishes HTTP connection with the API endpoints.
  * Request marshaling: the SDK converts data in ABAP types to JSON payload that is sent as the request body.
  * Error and exception handling: the SDK handles the return codes and error messages returned by the API, and raises exceptions, if any.
  * Unmarshalling response: the SDK converts back the JSON payload in the response body to corresponding ABAP types.
  * Local error logging: the SDK logs error messages using the logging framework.



## API design and Google API Explorer

APIs published by Google follow resource-oriented design. To learn more about Google's API design, see the [API design guide](https://docs.cloud.google.com/apis/design).

The ABAP SDK for Google Cloud enables integration with the REST based APIs published by Google.

[Google API Explorer](https://developers.google.com/apis-explorer) is a tool that lets you try Google Cloud API methods without writing code. You can use this tool to study the APIs and required input parameters that you want to pass to their corresponding ABAP methods.

## Code constructs

Explains the code constructs that you use to create your ABAP programs using the ABAP SDK for Google Cloud.

### Constructor

You first instantiate the API class that you want to use. The constructor of every API class would have a similar pattern as shown in the following example:
    
    
        METHODS constructor
          IMPORTING
            !iv_key_name   TYPE /goog/keyname OPTIONAL "Google Cloud Key Name
            !iv_log_obj    TYPE balobj_d OPTIONAL      "Application log: Object name
            !iv_log_subobj TYPE balsubobj OPTIONAL.    "Application log: Subobject
          RAISING
            /goog/cx_sdk .                 "Exception Classes
    

#### Importing parameters

The following table explains the importing parameters of a method constructor:

Parameter name | Type | Required/Optional | Description  
---|---|---|---  
`iv_key_name` | `/GOOG/KEYNAME` | Required | Specify the client key from the configuration that you use to create a connection to Google Cloud. For information about client key configuration, see [Authentication](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/authentication).   
`iv_log_object` | `balobj_d` | Optional | Specify the application log object, which you use to store the SDK generated errors. For information about logging configuration, see [Application logging](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/install-config#configure_logging).   
`iv_log_subobject` | `balsubobj` | Optional | Specify the application log subobject, which you use to store the SDK generated errors. For information about logging configuration, see [Application logging](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/install-config#configure_logging).  
  
### API method

With resource-oriented design of Google Cloud APIs, an API method is an action that can be performed on a resource published by the API.

For example, if `Topics` is a resource published by Pub/Sub API, then `topics.get` is an API method that represent an action on the resource `Topics` to get the configuration of a topic.

To map an ABAP class method to an API method, you can refer to the method description that follows the pattern:`<resource>.<method_verb>`.

For example, the method description for a Pub/Sub method is `pubsub.projects.topics.get`.

  * `projects.topics`: the resource name.
  * `get`: the method action.



![Method description SAP UI](https://docs.cloud.google.com/static/sap/docs/images/abap-sdk-btp-method-description-sap-ui.png)

The name on an ABAP method mapping to an API action follows the pattern:`<method_verb>_<resource>`.

For example, an ABAP method name for Pub/Sub is: `GET_TOPICS`

  * `GET`: the method action.
  * `TOPICS`: the resource name.



An ABAP method consists of the following sections that map to the REST API methods:

![Method name](https://docs.cloud.google.com/static/sap/docs/images/abap-sdk-btp-method-structure.png)

#### Importing parameters

An API method can have the following importing parameters. These parameters are optional and you can pass the parameters based on the requirements of an API method that you need to use.

Parameter name | Type | Category | Description  
---|---|---|---  
`iv_q_NAME` (`0` to `n`) | String | Query parameters | The query parameters are appended to the API endpoint after (`?`). They are used to define sort, pagination, or filter. There could be `0` to `n` query parameters.  
`iv_p_NAME` (`0` to `n`) | String | Path parameters | The path parameters are part of the endpoint. They are used to point to specific REST API resources. There could be `0` to `n` path parameters.  
`is_input` (`0` to `1`) | TY_CODE (Class type) | Input structure parameters | The data passed as the request body can be mapped using input structure. The REST API accepts JSON payload as request body. The parameter is a fully-typed parameter that is converted into JSON payload for the API class and the developer is not required to work with JSON. You can refer to the available class types to understand the ABAP types for mapping the data. For example, Type `/GOOG/CL_PUBSUB_V1=>TY_041` maps to the REST Resource: [Topic](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics#Topic), which is passed as the JSON Payload to the method [`CREATE_TOPICS`](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics/create). A method can have a maximum of one request body parameter. Some methods don't have a request body.  
  
#### Exporting parameters

An API method supports the following exporting parameters:

Parameter name | Type | Category | Description  
---|---|---|---  
`es_raw` | data | Raw output |  This parameter holds the JSON response (Error or Success) returned by the API method. Map this parameter to a variable of type String to receive the JSON response string. In cases where the response is of any other type, for example, xstring for file output in `/goog/cl_storage_v1->get_objects( )` the parameter returns an appropriate value. Use this parameter for advanced troubleshooting scenarios or for advanced API scenarios.  
`es_output` | TY_CODE (Class Type) | Output structure |  The JSON response is deserialized to ABAP structure and returned using this typed exporting parameter. You can use this as the **primary way** to read the API responses using ABAP constructs.  
`ev_ret_code` | I (Integer) | Return code |  The return code that you can use to verify if the API method execution was able to successfully perform its functionality. For more information, see API return codes, errors, and exceptions.  
`ev_err_text` | String | Error text |  If the method call failed, then this parameter contains the error message that you use to know the reason of failure. For more information, see  API return codes, errors, and exceptions.  
`ev_err_resp` | 

  * Error type = CHAR 60
  * Error description = STRING

| Error response |  The parameter provides additional information about the error. For more information, see API return codes, errors, and exceptions.  
  
### Class type

Google Cloud APIs use JSON as the primary format for data exchange. The ABAP SDK for Google Cloud provides ABAP types that map to the JSON schema expected by the Google Cloud APIs.

These ABAP types and related table types are available as class types in every API class that the SDK provides.

The following example shows class type for Pub/Sub API class `/GOOG/CL_PUBSUB_V1`.

![Class type](https://docs.cloud.google.com/static/sap/docs/images/abap-sdk-class-type.png)

The description of class type `TY_041` under `/GOOG/CL_PUBSUB_V1` maps to the REST Resource, [`Topic`](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics#Topic), which is passed as JSON Payload to the method [`CREATE_TOPICS`](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics/create).

`ABAP Doc` comments are added to all client API classes. While using ABAP Development Tools for SAP NetWeaver (ADT) for development, these comments provide you descriptions of the class types.

## API return codes, errors, and exceptions

If an error occurs when the API method of ABAP class is called, the ABAP SDK for Google Cloud passes the error information to the calling program by using the SDK exporting parameters or by raising exceptions.

![Return response name](https://docs.cloud.google.com/static/sap/docs/images/abap-sdk-btp-return-response.png)

### API return code and errors

Google Cloud APIs use an [error model](https://docs.cloud.google.com/apis/design/errors) that offers consistent experience across different APIs. When a Google Cloud API method is called from the SDK, the following parameters contain the API return code and messages:

  * `ev_ret_code`: [return code or error code](https://docs.cloud.google.com/apis/design/errors#error_codes) in the response.

  * `ev_error_text`: [error message](https://docs.cloud.google.com/apis/design/errors#error_messages) in the response, if any.

  * `es_raw`: raw error response, if an API method call failed.




To check the status of an API call, use the `IS_SUCCESS` method. You can use the value of `ev_ret_code` to determine if an API call was successful or not. In general, when `ev_ret_code = 2XX`, the method call is considered to be successful. For all other values, the method call is considered unsuccessful.
    
    
    IF lo_client->is_success( ev_ret_code ).
       "Success: Implement custom code
       ELSE
       "Handle the HTTP error status code
    ENDIF.

For some [Google Maps Platform APIs](https://developers.google.com/maps/documentation), in case you call an API with invalid inputs, the API returns an HTTP success status code `2XX` with an error message and error status, instead of an HTTP error status code (`4XX` or `5XX`). This error message and error status in the API response can help you troubleshoot the problem and fix the invalid inputs.

For such Google Maps Platform APIs, in addition to the return code `ev_ret_code`, check the error message and error status returned in the API response by calling the `IS_STATUS_OK` method after the API call. The following snippet shows an example of how you can use the `IS_STATUS_OK` method:
    
    
    IF lo_client->is_status_ok( ).
      "Success: Implement custom code
      ELSE
      "Handle the HTTP error status code
    ENDIF.

The parameter `es_err_resp` provides additional information about the error. The following table explains the fields in the parameter `es_err_resp`.

Field | Value  
---|---  
`es_err_resp-error_description` | Error message received from the API. This value is same as the parameter `ev_error_text`.  
`es_err_resp-error` | HTTP status description returned from the SAP HTTP client.  
  
### Handle errors returned by Google Cloud APIs

Use the following guidance to handle errors returned by Google Cloud APIs:

  * **Common error codes:** For information about common errors returned by Google Cloud APIs and their cause, see [error codes](https://docs.cloud.google.com/apis/design/errors#handling_errors).

  * **Capture detailed error:** To capture detailed error information with ABAP SDK for Google Cloud, use the exporting parameter `es_raw` from the SDK class methods and map this parameter to a variable of type `String`. This variable holds a JSON response containing detailed error messages and specific violations encountered by the APIs.

  * **View detailed error:** To view detailed error information, use one of the following methods:

    * Debugger: View the contents of the variable that holds the JSON response within the ABAP debugger tool for further analysis.
    * SAP GUI: Use the ABAP class `cl_demo_output=>display( lv_response )` for visual representation of the error within a report program. If you are using the API methods in a report program and the program execution is in foreground mode, then use the ABAP class `cl_demo_output=>display_json( lv_response )`.

The following code snippet illustrates how to display API response in case of an error: 
          
          DATA lv_response  TYPE string,
            TRY.
                lo_translate = NEW #( iv_key_name = 'DEMO_TRANSLATE' ).
                lo_translate->translate_translations
                  EXPORTING
                    is_input    = ls_input
                  IMPORTING
                    es_raw      = lv_response
                    es_output   = ls_output
                    ev_ret_code = lv_ret_code
                    ev_err_text = lv_err_text
                    es_err_resp = ls_err_resp.
                IF lo_translate->is_error( lv_ret_code ) = abap_true.
                  " Display API response in case of an error
                  cl_demo_output=>display_json( lv_response ).
                ENDIF.
              CATCH /goog/cx_sdk INTO lo_exception.
                lv_err_text = lo_exception->get_text( ).
            ENDTRY.
          

  * **API specific documentation:** Some Google Cloud APIs provide detailed error information and troubleshooting guidance within their individual documentation. To resolve an error related to an API, see the documentation specific to that API, for example, [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/reference/error-codes), [Document AI](https://docs.cloud.google.com/document-ai/docs/error-messages), and [Cloud Storage](https://docs.cloud.google.com/storage/docs/troubleshooting#error_codes).




### Exceptions

When an unexpected error occurs during an API method call, such as incorrect SDK configuration or HTTP communication failure, the SDK raises a class exception of type `/GOOG/CX_SDK`. You must catch this exception in your code and write an appropriate error handling logic.

![Handle exception](https://docs.cloud.google.com/static/sap/docs/images/abap-sdk-btp-handle-exception.png)

You can get the error message by calling the method `get_text` of the exception class. The error message returned by the exception class has the following format:

`/GOOG/MSG : Return_Code - Error_Message`

The cause of the error and resolution steps depends on the value of `Return_Code`.

Value of `Return_Code` | Cause of the error | Resolution  
---|---|---  
`461` | The ABAP SDK for Google Cloud uses a special return code, `461`, to inform that a specific installation and configuration step is not done or completed incorrectly. Corresponding `Error_Message` provides more details about the error. | You must carefully review the installation and configuration instructions for the SDK and ensure they are done correctly.  
Any other value | This return code is the last HTTP error from the standard SAP HTTP Client Class. This error signifies that the SAP ICM faced a communication issue when calling a Google REST API method. | You must carefully review your network, firewall, SAP ICM settings, and make sure that configurations allow HTTP calls to Google Cloud APIs.  
  
For typical error messages triggered in the ABAP SDK for Google Cloud and their resolution, see the [troubleshooting guide](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/troubleshooting).

## Logging

The SAP BTP edition of ABAP SDK for Google Cloud lets you log error messages using an embedded logging framework. The log object `/GOOG/LOG_OBJECT` and subobject `/GOOG/LOG_SUBOBJECT` are shipped with the SDK that you can use for creating your default log configuration. For more information about creating default log configuration, see [Configure logging](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/install-config#configure_logging).

You can view application logs using the **Google SDK:Application Logs Display** app. For more information, see [View logs](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/troubleshooting#view_logs).

## Data type mapping

The following table provides a full list of `type` and `format` values supported by Google APIs Discovery Service and corresponding ABAP data type.

For more information about `type` and `format` values supported by Google APIs Discovery Service, see [Type and format summary](https://developers.google.com/discovery/v1/type-format).

Type value | Format value | ABAP data type | Meaning  
---|---|---|---  
any |  | TYPE REF TO DATA | The property may have any type. Defined by the JSON Schema spec.  
array |  | TABLE TYPE WITH NON UNIQUE KEYS | A JavaScript array of values. The items property indicates the schema for the array values. Defined by the JSON Schema spec.  
boolean |  | ABAP_BOOLEAN | A boolean value, either "true" or "false". Defined by the JSON Schema spec.  
integer | int32 | INT4 | A 32-bit signed integer. It has a minimum value of -2,147,483,648 and a maximum value of 2,147,483,647 (inclusive).  
integer | uint32 | INT4 | A 32-bit unsigned integer. It has a minimum value of 0 and a maximum value of 4,294,967,295 (inclusive).  
number | double | `/GOOG/NUM_DOUBLE` (string) | A double-precision 64-bit IEEE 754 floating point.  
number | float | `/GOOG/NUM_FLOAT` (string) | A single-precision 32-bit IEEE 754 floating point.  
object |  | TYPES | A JavaScript object. Defined by the JSON Schema spec.  
string |  | STRING | An arbitrary string. Defined by the JSON Schema spec.  
string | byte | STRING | A padded, base64-encoded string of bytes, encoded with a URL and filename safe alphabet (sometimes referred to as "web-safe" or "base64url"). Defined by RFC 4648.  
string | date | STRING | An RFC 3339 date in the format YYYY-MM-DD. Defined in the JSON Schema spec.  
string | date-time | STRING | An RFC 3339 timestamp in UTC time. This in the format of yyyy-MM-ddTHH:mm:ss.SSSZ. The milliseconds portion (".SSS") is optional. Defined in the JSON Schema spec.  
string | google-datetime | STRING | An RFC 3339 timestamp in UTC time. This in the format of yyyy-MM-ddTHH:mm:ss.SSSZ. The milliseconds portion (".SSS") is optional.  
string | google-duration | STRING | A string ends in the suffix "s" (indicating seconds) and is preceded by the number of seconds, with nanoseconds expressed as fractional seconds. The period is always used as the decimal point, not a comma.  
string | google-fieldmask | STRING | A string where field names are separated by a comma. Field names are  
represented in lower-camel naming conventions.  
string | int64 | STRING | A 64-bit signed integer. It has a minimum value of -9,223,372,036,854,775,808 and a maximum value of 9,223,372,036,854,775,807 (inclusive).  
string | uint64 | STRING | A 64-bit unsigned integer. It has a minimum value of 0 and a maximum value of (2^64)-1 (inclusive).  
  
## Serialization and deserialization of API request and response

By default, the SAP BTP edition of ABAP SDK for Google Cloud takes care of marshalling and unmarshalling API requests and responses. Each ABAP class for a Google Cloud API has embedded ABAP types to form the input and output of the methods. To implement custom transformation of request and response, you can use the enhancement spot with SAP [Business Add In (BAdI)](https://help.sap.com/doc/saphelp_nw75/7.5.5/en-US/8f/f2e540f8648431e10000000a1550b0/frameset.htm) definitions that are shipped with the SDK.

### Implement custom transformation

The enhancement spot `/GOOG/ES_TRANSFORM_JSON`, which is shipped with the SDK, includes the following BAdI definitions:

  * `/GOOG/BADI_SERIALIZE_JSON`: to implement custom serialization logic.
  * `/GOOG/BADI_DESERIALIZE_JSON`: to implement custom deserialization logic.



You can write specific transformation logic in implementations of these BAdIs. The interfaces of these BAdIs have `IV_METHOD_NAME` as the importing parameter. You use this parameter to segregate the transformation logic for each API and API method using `IF….ENDIF` blocks. In your implementation block, set the exporting parameter `EV_HANDLED` to `X`.

**Important:** You assume the responsibility for any custom code written within the implementation of these BAdIs. We strongly recommend that you test your custom code thoroughly in a non-production environment before deploying it to production. Google Cloud does not provide support for custom features.

To implement custom transformation, follow these steps:

  1. For `/GOOG/BADI_SERIALIZE_JSON`, create an enhancement implementation:

     * For transforming API requests, create an implementation for BAdI `/GOOG/BADI_SERIALIZE_JSON` with an implementation class.
     * For transforming API responses, create an implementation for BAdI `/GOOG/BADI_DESERIALIZE_JSON` with an implementation class.
  2. Determine the method ID of the API method for which you need to write the transformation. The method ID is concatenation of the following:

     * The value of the class attribute constant `C_SERVICE_NAME`.
     * The character `#`.
     * The description of the API class method for which you need to implement the transformation.

For example, to write transformations for publishing messages to a Pub/Sub topic, the method ID would be: `pubsub:v1#pubsub.projects.topics.publish`

  3. In the method implementation of the BAdI:

     1. For the method ID, write your custom transformation under an `IF….ENDIF block`.
     2. Set the exporting parameter `EV_HANDLED` to `X`.

If `EV_HANDLED` is not set to `X`, then the default marshalling and unmarshalling logic of the SDK is applied.

  4. Mark the `API State` of the implementing class as `Use System-Internally (Contract C1)`. The custom transformation logic is invoked during runtime. The default serialization and deserialization logic shipped with the SDK would be skipped.




## Namespace

All Google provided code is placed under the reserved namespace `/GOOG/`.

## Reference architectures

Explore the ABAP SDK for Google Cloud with the help of the reference architectures and discover how the SDK can bring innovation to your SAP application landscape. You can use the SDK to integrate with [Agent Platform](https://docs.cloud.google.com/vertex-ai/docs/start/introduction-unified-platform) for advanced AI and machine learning capabilities, and other Google Cloud services such as [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction), [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview), [Cloud Storage](https://docs.cloud.google.com/storage/docs/overview) and many more. For more information, see [Reference architectures for the ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/architectures/abap-sdk/overview).

## Get support

If you need help resolving problems with the SAP BTP edition of ABAP SDK for Google Cloud, then do the following:

  * Refer to the [ SAP BTP edition of ABAP SDK for Google Cloud troubleshooting guide](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/troubleshooting).

  * Ask your questions and discuss ABAP SDK for Google Cloud with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).

  * Collect all available [diagnostic information](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/getting-support-diag-info) and contact Cloud Customer Care. For information about contacting Customer Care, see [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
