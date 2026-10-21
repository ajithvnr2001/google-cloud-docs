---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/cors-policy/
title: CORS policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:44:50.440307+00:00
---

# CORS policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/cors-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  CORS policy Stay organized with collections  Save and categorize content based on your preferences. 

[Standard policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types)

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Cross-origin resource sharing ([CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)) is a standard mechanism that allows JavaScript XMLHttpRequest (XHR) calls executed in a web page to interact with resources from non-origin domains. CORS is a commonly implemented solution to the _[same-origin policy](https://en.wikipedia.org/wiki/Same-origin_policy)_ that is enforced by all browsers. 

For example, if you make an XHR call to the Twitter API from JavaScript code executing in your browser, the call will fail. This is because the domain serving the page to your browser is not the same as the domain serving the Twitter API. CORS provides a solution to this problem by allowing servers to _opt-in_ if they wish to provide cross-origin resource sharing. 

One use case for CORS is the developer portal SmartDoc's [ **Try this API** feature](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/publish-apis#what-published). For information, see [ Configuring your API proxy to support the Try this API panel](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/publish-apis#cors). 

The CORS policy allows Apigee customers to set CORS policies for APIs consumed by web applications. 

**Caution:**

Implementing a CORS policy can relax the [ same-origin policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy) (SOP). If a proxy developer sets the `Access-Control-Allow-Origin` header to allow all (`*`), it effectively disables the same-origin protection. 

The `AllowOrigins` field is a required policy element and the default should not be set to allow all (`*`). Policy developers should make cautious decisions before exposing their resources. 

This policy is a _Standard policy_ and can be deployed to any environment type. For information on policy types and availability with each environment type, see [Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types).

## `<CORS>` element

Defines the CORS policy.

**Default Value** | See **Default Policy** tab, below  
---|---  
**Required?** | Required  
**Type** | Complex object  
**Parent Element** |  N/A   
**Child Elements** |  [`<AllowCredentials>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/cors-policy#allow-credentials)  
[`<AllowHeaders>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/cors-policy#allow-headers)  
[`<AllowMethods>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/cors-policy#allow-methods)  
[`<AllowOrigins>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/cors-policy#allow-origins)  
`<DisplayName>`  
[`<ExposeHeaders>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/cors-policy#expose-headers)  
[`<GeneratePreflightResponse>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/cors-policy#generate-preflight)  
[`<IgnoreUnresolvedVariables>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/cors-policy#ignore-unresolved)  
[`<MaxAge>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/cors-policy#max-age)  
  
  
The `<CORS>` element uses the following syntax:

### Syntax

The `<CORS>` element uses the following syntax:
    
    
    <CORS continueOnError="[false|true]" enabled="[false|true]" name="POLICY_NAME">
      <DisplayName>DISPLAY_NAME</DisplayName>
      <AllowOrigins>[{message template}|URL|URL, URL, ...|{context-variable}|{flow-variable}|*]</AllowOrigins>
      <AllowMethods>[GET, PUT, POST, DELETE, ...|*]</AllowMethods>
      <AllowHeaders>[origin, x-requested-with, accept, content-type, ...]</AllowHeaders>
      <ExposeHeaders>[X-CUSTOM-HEADER-A, X-CUSTOM-HEADER-B, ... | *]</ExposeHeaders>
      <MaxAge>[integer|-1]</MaxAge>
      <AllowCredentials>[false|true]</AllowCredentials>
      <GeneratePreflightResponse>[false|true]</GeneratePreflightResponse>
      <IgnoreUnresolvedVariables>[false|true]</IgnoreUnresolvedVariables>
    </CORS>

### Default policy

The following example shows the default settings when you add the CORS policy to your flow in the Edge UI:
    
    
    <CORS continueOnError="false" enabled="true" name="add-cors">
        <DisplayName>Add CORS</DisplayName>
        <AllowOrigins>{request.header.origin}</AllowOrigins>
        <AllowMethods>GET, PUT, POST, DELETE</AllowMethods>
        <AllowHeaders>origin, x-requested-with, accept, content-type</AllowHeaders>
        <ExposeHeaders>*</ExposeHeaders>
        <MaxAge>3628800</MaxAge>
        <AllowCredentials>false</AllowCredentials>
        <GeneratePreflightResponse>true</GeneratePreflightResponse>
        <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
    </CORS>

When you insert a new `CORS` policy in the Apigee UI, the template contains stubs for all possible operations. Typically, you select which operations you want to perform with this policy and remove the rest of the child elements. For example, if you want to specify the HTTP methods allowed to access the resource, use the [`<AllowMethods>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/cors-policy#allow-methods) element and remove the other child elements from the policy to make it more readable. 

This element has the following attributes that are common to all policies:

**Attribute** | **Default** | **Required?** | **Description**  
---|---|---|---  
`name` | N/A | **Required** |  The internal name of the policy. The value of the `name` attribute can contain letters, numbers, spaces, hyphens, underscores, and periods. This value cannot exceed 255 characters. Optionally, use the `<DisplayName>` element to label the policy in the management UI proxy editor with a different, natural-language name.  
`continueOnError` | false | Optional | Set to `false` to return an error when a policy fails. This is expected behavior for most policies. Set to `true` to have flow execution continue even after a policy fails. See also: 

  * [Fault rules are triggered ONLY in an error state (about continueOnError)](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#multiplefaultrulesandexecutionlogic-faultrulesaretriggeredonlyinanerrorstateaboutcontinueonerror)
  * [Handling faults within the current flow](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#continueonerror)

  
`enabled` | true | Optional | Set to `true` to enforce the policy. Set to `false` to _turn off_ the policy. The policy will not be enforced even if it remains attached to a flow.  
`async` not_interested | false | Deprecated | This attribute is deprecated.  
  
Each of the child elements is described in the sections that follow.

## Examples

Examples are provided for all of the child elements in the following sections.

## Child element reference

This section describes the child elements of [`<CORS>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/cors-policy#cors).

### `<AllowCredentials>`

Indicates whether the caller is allowed to send the actual request (not the preflight) using credentials. Translates to the `Access-Control-Allow-Credentials` header. 

**Default Value** | If not specified, `Access-Control-Allow-Credentials` will not be set.  
---|---  
**Required?** | Optional  
**Type** | Boolean  
**Parent Element** |  [`<CORS>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/cors-policy#cors)  
**Child Elements** |  None   
  
The `<AllowCredentials>` element uses the following syntax:

### Syntax
    
    
    <CORS continueOnError="[false|true]" enabled="[false|true]" name="POLICY_NAME">
      <AllowOrigins>[{message template}|URL|URL, URL, ...|{context-variable}|{flow-variable}|*]</AllowOrigins>
    ** <AllowCredentials>[false|true]</AllowCredentials>**
    </CORS>
          

### Example

This example sets the `Access-Control-Allow-Credentials` header to `false`. That is, the caller is _not_ allowed to send the actual request (not the preflight) using credentials. 
    
    
    <CORS continueOnError="false" enabled="true" name="add-cors">
      <AllowOrigins>{request.header.origin}</AllowOrigins>
      **< AllowCredentials>false</AllowCredentials>**
    </CORS>

### `<AllowHeaders>`

List of HTTP headers that can be used when requesting the resource. [Serialized](https://en.wikipedia.org/wiki/Serialization) to the `Access-Control-Allow-Headers` header. 

**Default Value** | `Origin, Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers`  
---|---  
**Required?** | Optional  
**Type** | String, with message template* support  
**Parent Element** |  [`<CORS>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/cors-policy#cors)  
**Child Elements** |  None   
**Tip:** Apigee recommends adding no more than 50 values to `<AllowHeaders>`.

* For more information, see [ What is a message template?](https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro#what-is-a-message-template)

The `<AllowHeaders>` element uses the following syntax:

### Syntax
    
    
    <CORS continueOnError="[false|true]" enabled="[false|true]" name="POLICY_NAME">
      <AllowOrigins>[{message template}|URL|URL, URL, ...|{context-variable}|{flow-variable}|*]</AllowOrigins>
    ** <AllowHeaders>[origin, x-requested-with, accept, content-type, ...]</AllowHeaders>**
    </CORS>

### Example

CORS AllowOrigins example

This example specifies the HTTP headers that can be used when requesting the resource. 
    
    
    <CORS continueOnError="false" enabled="true" name="add-cors">
      <AllowOrigins>{request.header.origin}</AllowOrigins>
      **< AllowHeaders>origin, x-requested-with, accept, content-type</AllowHeaders>**
    </CORS>

### `<AllowMethods>`

List of HTTP methods allowed to access the resource. The content will be [serialized](https://en.wikipedia.org/wiki/Serialization) into the `Access-Control-Allow-Methods` header. 

**Default Value** | `GET, POST, HEAD, OPTIONS`  
---|---  
**Required?** | Optional  
**Type** | String, with message template* support  
**Parent Element** |  [`<CORS>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/cors-policy#cors)  
**Child Elements** |  None   
  
* For more information, see [ What is a message template?](https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro#what-is-a-message-template)

The `<AllowMethods>` element uses the following syntax:

### Syntax
    
    
    <CORS continueOnError="[false|true]" enabled="[false|true]" name="POLICY_NAME">
      <AllowOrigins>[{message template}|URL|URL, URL, ...|{context-variable}|{flow-variable}|*]</AllowOrigins>
    ** <AllowMethods>[GET, PUT, POST, DELETE, ...|*]</AllowMethods>**
    </CORS>

### Example:  
List

This example specifies the HTTP methods that are allowed to access the resource. 
    
    
    <CORS continueOnError="false" enabled="true" name="add-cors">
      <AllowOrigins>{request.header.origin}</AllowOrigins>
      **< AllowMethods>GET, PUT, POST, DELETE</AllowMethods>**
    </CORS>

### Example:  
Wildcard

This example specifies that all HTTP methods are allowed to access the resource. 
    
    
    <CORS continueOnError="false" enabled="true" name="add-cors">
      <AllowOrigins>{request.header.origin}</AllowOrigins>
      **< AllowMethods>*</AllowMethods>**
    </CORS>

### `<AllowOrigins>`

A list of origins that are allowed to access the resource. Use an asterisk (`*`) to enable access to a resource from any origin. Otherwise, provide an allow list of comma-separated origins. If a match is found, then the outgoing `Access-Control-Allow-Origin` is set to the origin as provided by the client. 

**Default Value** | N/A  
---|---  
**Required?** | Required  
**Type** | String, with message template* support  
**Parent Element** |  [`<CORS>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/cors-policy#cors)  
**Child Elements** |  None   
**Tip:** Apigee recommends adding no more than 50 values to `<AllowOrigins>`.

* For more information, see [ What is a message template?](https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro#what-is-a-message-template)

The `<AllowOrigins>` element uses the following syntax:

### Syntax
    
    
    <CORS continueOnError="[false|true]" enabled="[false|true]" name="POLICY_NAME">
    ** <AllowOrigins>[{message template}|URL|URL, URL, ...|{context-variable}|{flow-variable}|*]</AllowOrigins>**
    </CORS>

### Example:  
Single URL

This example specifies a single URL origin that is allowed to access the resource. 
    
    
    <CORS continueOnError="false" enabled="true" name="add-cors">
      **< AllowOrigins>https://www.w3.org</AllowOrigins>**
    </CORS>

### Example:  
Multiple URLs

This example specifies multiple origins that are allowed to access the resource. 
    
    
    <CORS continueOnError="false" enabled="true" name="add-cors">
      **< AllowOrigins>https://www.w3.org, https://www.apache.org</AllowOrigins>**
    </CORS>

### Example:  
Context variable

This example specifies a context variable that represents one or more origins that are allowed to access the resource. 
    
    
    <CORS continueOnError="false" enabled="true" name="add-cors">
      **< AllowOrigins>{origins.list}</AllowOrigins>**
    </CORS>

### Example:  
Flow variable

This example specifies a [ flow variable](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference) that represents one origin that is allowed to access the resource. 
    
    
    <CORS continueOnError="false" enabled="true"**< name="add-cors">
      All<owOrigins>{**r<equest.header.origin}/AllowOrigins>
    /CORS>

### Example:  
Wildcard

This example specifies that all origins are allowed to access the resource. 

**Note:** You can also set a context variable in a message template to an asterisk (*). **Caution:** If a proxy developer sets the `Access-Control-Allow-Origin` header to allow all (`*`), it effectively disables the same-origin protection. The default should not be set to allow all (`*`). Policy developers should make cautious decisions before exposing their resources. 
    
    
    <CORS continueOnError="false" enabled="true" name="add-cors">
      **< AllowOrigins>*</AllowOrigins>**
    </CORS>

### `<DisplayName>`

Use in addition to the `name` attribute to label the policy in the management UI proxy editor with a different, more natural-sounding name.

The `<DisplayName>` element is common to all policies.

**Default Value** | N/A  
---|---  
**Required?** | Optional. If you omit `<DisplayName>`, the value of the policy's `name` attribute is used.  
**Type** | String  
**Parent Element** |  <PolicyElement>  
**Child Elements** |  None   
  
The `<DisplayName>` element uses the following syntax:

### Syntax
    
    
    <_PolicyElement_ >
      **< DisplayName>POLICY_DISPLAY_NAME</DisplayName>**
      ...
    </_PolicyElement_ >

### Example
    
    
    <_PolicyElement_ >
      **< DisplayName>My Validation Policy</DisplayName>**
    </_PolicyElement_ >

The `<DisplayName>` element has no attributes or child elements.

### `<ExposeHeaders>`

A list of HTTP headers that the browsers are allowed to access or an asterisk (`*`) to allow all HTTP headers. [Serialized](https://en.wikipedia.org/wiki/Serialization) into the `Access-Control-Expose-Headers` header. 

**Default Value** | If not specified, `Access-Control-Expose-Headers` will not be set. Non-simple headers are not exposed by default.  
---|---  
**Required?** | Optional  
**Type** | String, with message template* support  
**Parent Element** |  [`<CORS>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/cors-policy#cors)  
**Child Elements** |  None   
**Tip:** Apigee recommends adding no more than 50 values to `<ExposeHeaders>`.

* For more information, see [ What is a message template?](https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro#what-is-a-message-template)

The `<ExposeHeaders>` element uses the following syntax:

### Syntax
    
    
    <CORS continueOnError="[false|true]" enabled="[false|true]" name="POLICY_NAME">
      <AllowOrigins>[{message template}|URL|URL, URL, ...|{context-variable}|{flow-variable}|*]</AllowOrigins>
    ** <ExposeHeaders>[X-CUSTOM-HEADER-A, X-CUSTOM-HEADER-B, ... | *]</ExposeHeaders>**
    </CORS>

### Example

This example specifies that the browsers are allowed to access all HTTP headers. 
    
    
    <CORS continueOnError="false" enabled="true" name="add-cors">
      <AllowOrigins>{request.header.origin}</AllowOrigins>
      **< ExposeHeaders>*</ExposeHeaders>**
    </CORS>

### `<GeneratePreflightResponse>`

Indicate whether the policy should generate and return the CORS preflight response. If `false`, no response is sent. Instead, the following flow variables are populated: 

  * `cross_origin_resource_sharing.allow.credentials`
  * `cross_origin_resource_sharing.allow.headers`
  * `cross_origin_resource_sharing.allow.methods`
  * `cross_origin_resource_sharing.allow.origin`
  * `cross_origin_resource_sharing.allow.origins.list`
  * `cross_origin_resource_sharing.expose.headers`
  * `cross_origin_resource_sharing.max.age`
  * `cross_origin_resource_sharing.preflight.accepted`
  * `cross_origin_resource_sharing.request.headers`
  * `cross_origin_resource_sharing.request.method`
  * `cross_origin_resource_sharing.request.origin`
  * `cross_origin_resource_sharing.request.type`

**Default Value** | `true`  
---|---  
**Required?** | Optional  
**Type** | Boolean  
**Parent Element** |  [`<CORS>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/cors-policy#cors)  
**Child Elements** |  None   
  
The `<GeneratePreflightResponse>` element uses the following syntax:

### Syntax
    
    
    <CORS continueOnError="[false|true]" enabled="[false|true]" name="POLICY_NAME">
      <GeneratePreflightResponse>[false|true]</GeneratePreflightResponse>
    ** <GeneratePreflightResponse>[false|true]</GeneratePreflightResponse>**
    </CORS>

### Example

This example specifies that the policy should generate and return the CORS preflight response. 
    
    
    <CORS continueOnError="false" enabled="true" name="add-cors">
      <AllowOrigins>{request.header.origin}</AllowOrigins>
      **< GeneratePreflightResponse>true</GeneratePreflightResponse>**
    </CORS>

### `<IgnoreUnresolvedVariables>`

Determines whether processing stops when an unresolved variable is encountered. Set to `true` to ignore unresolved variables and continue processing; otherwise `false`. 

**Default Value** | `true`  
---|---  
**Required?** | Optional  
**Type** | Boolean  
**Parent Element** |  [`<CORS>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/cors-policy#cors)  
**Child Elements** |  None   
  
The `<IgnoreUnresolvedVariables>` element uses the following syntax:

### Syntax
    
    
    <CORS continueOnError="[false|true]" enabled="[false|true]" name="POLICY_NAME">
      <AllowOrigins>[{message template}|URL|URL, URL, ...|{context-variable}|{flow-variable}|*]</AllowOrigins>
    ** <IgnoreUnresolvedVariables>[false|true]</IgnoreUnresolvedVariables>**
    </CORS>

### Example

This example specifies that processing continues when an unresolved variable is encountered. 
    
    
    <CORS continueOnError="false" enabled="true" name="add-cors">
      <AllowOrigins>{request.header.origin}</AllowOrigins>
      **< IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>**
    </CORS>

### `<MaxAge>`

Specifies how long the results of a preflight request can be cached in seconds. A value of `-1` populates the `Access-Control-Max-Age` header with a value of `-1`, which disables caching, requiring a preflight [ `OPTIONS`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/OPTIONS) check for all calls. This is defined in the [` Access-Control-Max-Age` specification](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Max-Age#directives). 

**Default Value** | `1800`  
---|---  
**Required?** | Optional  
**Type** | Integer  
**Parent Element** |  [`<CORS>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/cors-policy#cors)  
**Child Elements** |  None   
  
The `<MaxAge>` element uses the following syntax:

### Syntax
    
    
    <CORS continueOnError="[false|true]" enabled="[false|true]" name="POLICY_NAME">
      <AllowOrigins>[{message template}|URL|URL, URL, ...|{context-variable}|{flow-variable}|*]</AllowOrigins>
    ** <MaxAge>[integer|-1]</MaxAge>**
    </CORS>

### Example:  
Cache

This example specifies that the results of a preflight request can be cached for `3628800` seconds. 
    
    
    <CORS continueOnError="false" enabled="true" name="add-cors">
      <AllowOrigins>{request.header.origin}</AllowOrigins>
      **< MaxAge>3628800</MaxAge>**
    </CORS>

### Example:  
No cache

This example specifies that the results of a preflight request cannot be cached. 
    
    
    <CORS continueOnError="false" enabled="true" name="add-cors">
      <AllowOrigins>{request.header.origin}</AllowOrigins>
      **< MaxAge>-1</MaxAge>**
    </CORS>

## Usage notes

### `OPTIONS` requests

When an [ `OPTIONS`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/OPTIONS) request is received and processed by the CORS policy, proxy flow execution transfers directly to the Proxy Response PreFlow, skipping the request flows entirely and continues execution from there. There is no need to create a Condition to ignore the OPTIONS request in the proxy request flow. 

On subsequent calls, when the CORS policy executes, if the `MaxAge` set in the policy has not expired, the flow continues as normal. During the final response flow just before "Response Sent to Client," a special CORS execution step "CORSResponseOrErrorFlowExecution" sets CORS response headers (`Access-Control-Allow-Credentials`, `Access-Control-Allow-Origin`, and `Access-Control-Expose-Headers`) to return a CORS-validated response. 

## Error codes

This section describes the fault codes and error messages that are returned and fault variables that are set by Apigee when this policy triggers an error. This information is important to know if you are developing fault rules to handle faults. To learn more, see [ What you need to know about policy errors](https://cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors) and [ Handling faults](https://cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling). 

### Runtime errors

These errors can occur when the policy executes. 

Fault code | HTTP status | Cause  
---|---|---  
`steps.cors.UnresolvedVariable` | `500` | This error occurs if a variable specified in the CORS policy is either: 

  * Out of scope (not available in the specific flow where the policy is being executed)
or
  * Can't be resolved (is not defined)

  
  
### Deployment errors

These errors can occur when you deploy a proxy containing this policy. 

Error name | Cause  
---|---  
`InvalidMaxAge` | `MaxAge` is not number  
`MissingAllowOrigins` | `AllowOrigins` is not specified  
`InvalidHTTPMethods` | One of the methods in `AllowMethods` is not valid  
`AllowHeadersSizeTooLarge` | The string size in `AllowHeaders` is too large.  
`ExposeHeadersSizeTooLarge` | The string size in `ExposeHeaders` is too large.  
  
### Fault variables

These variables are set when this policy triggers an error at runtime. For more information, see [ What you need to know about policy errors](https://cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors). 

**Note :** If `<GeneratePreflightResponse>` is set to true and an error occurs, the policy returns a response to the client immediately and the error flow is skipped. The following variables are not populated: Variables | Where | Example  
---|---|---  
`fault.name = "FAULT_NAME"` | FAULT_NAME is the name of the fault, as listed in the Runtime errors table above. The fault name is the last part of the fault code. | `fault.name Matches "UnresolveVariable"`  
`cors.POLICY_NAME.failed` | POLICY_NAME is the user-specified name of the policy that threw the fault. | `cors.AddCORS.failed = true`  
  
### Example error response

**Note:** For error handling, the best practice is to trap the errorcode part of the error response. Do not rely on the text in the faultstring, because it could change. 
    
    
    {
       "fault":{
          "detail":{
             "errorcode":"steps.cors.UnresolvedVariable"
          },
          "faultstring":"CORS[AddCORS]: unable to resolve variable wrong.var"
       }
    }

### Example fault rule
    
    
    <FaultRule name="Add CORS Fault">
        <Step>
            <Name>Add-CORSCustomUnresolvedVariableErrorResponse</Name>
            <Condition>(fault.name Matches "UnresolvedVariable") </Condition>
        </Step>
        <Condition>(cors.Add-CORS.failed = true) </Condition>
    </FaultRule>

## Flow variables

A `CorsFlowInfo` `FlowInfo` object will be added and it will be available to trace. 

Property | Type | Read/Write | Description | Scope begins  
---|---|---|---|---  
`cross_origin_resource_sharing.allow.credentials` | Boolean | Read/Write | Value from [`<AllowCredentials>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/cors-policy#allow-credentials) | Proxy request  
`cross_origin_resource_sharing.allow.headers` | String | Read/Write | Value from [`<AllowHeaders>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/cors-policy#allow-headers) | Proxy request  
`cross_origin_resource_sharing.allow.methods` | String | Read/Write | Value from [`<AllowMethods>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/cors-policy#allow-methods) | Proxy request  
`cross_origin_resource_sharing.allow.origin` | String | Read/Write | The request origin that is allowed, empty if it is not in the allow list | Proxy request  
`cross_origin_resource_sharing.allow.origins.list` | String | Read/Write | Value from [`<AllowOrigins>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/cors-policy#allow-origins) | Proxy request  
`cross_origin_resource_sharing.expose.headers` | String | Read/Write | Value from [`<ExposeHeaders>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/cors-policy#expose-headers) | Proxy request  
`cross_origin_resource_sharing.max.age` | Integer | Read/Write | Value from [`<MaxAge>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/cors-policy#max-age) | Proxy request  
`cross_origin_resource_sharing.preflight.accepted` | Boolean | Read/Write | Indicates if preflight request is accepted | Proxy request  
`cross_origin_resource_sharing.request.headers` | String | Read/Write | The value of request `Access-Control-Request-Headers` header | Proxy request  
`cross_origin_resource_sharing.request.method` | String | Read/Write | The value of request `Access-Control-Request-Method` header | Proxy request  
`cross_origin_resource_sharing.request.origin` | String | Read/Write | The same as `request.header.origin` | Proxy request  
`cross_origin_resource_sharing.request.type` | String | Read/Write |  Type of CORS request. Possible values:

  * **ACTUAL:** A request which is not a preflight request
  * **PRE_FLIGHT:** A preflight request

| Proxy request  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
