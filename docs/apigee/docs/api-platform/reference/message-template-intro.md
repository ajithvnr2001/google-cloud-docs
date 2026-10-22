---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro/
title: Message templates \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:45:54.872737+00:00
---

# Message templates  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Message templates Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This topic discusses how to use message templates in API proxies and provides a function reference.

## What is a message template?

A _message template_ permits you to perform _variable string substitution_ in certain policy and `<TargetEndpoint>` elements. This feature, where supported, lets you populate strings dynamically when a proxy executes.

You can include any combination of flow variable references and literal text in a message template. Flow variable names must be enclosed in curly braces, while any text not in curly braces is output as literal text.

See also Where can you use message templates?

### Example

For example, the [AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy) lets you use a message template within in the `<Payload>` element:
    
    
    <AssignMessage name="AM-set-payload-with-dynamic-content">
      <Set>
        <Payload contentType="application/json">
          {"name":"Alert", "message":"You entered an invalid username: {user.name}"}
        </Payload>
      </Set>
      <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
    </AssignMessage>

In the above example, the value of flow variable `user.name` (in curly braces) will be evaluated and substituted into the payload string at runtime. So, for example, if `user.name=jdoe`, then the resulting message output in the payload will be: `You entered an invalid username: jdoe`. If the variable cannot be resolved, then an empty string is output.

### Example

When a quota is exceeded, it is a good practice to return a meaningful message to the caller. This pattern is commonly used with a "fault rule" to provide output to give the caller information about the quota violation. In the following [AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy), message templates are used to populate quota information dynamically in several XML elements:
    
    
    <AssignMessage name='AM-QuotaViolationMessage'>
      <Description>message for quota exceeded</Description>
      <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
      <Set>
        <Headers>
          <Header name='X-Quota-Reset'>{ratelimit.Quota-1.expiry.time}</Header>
          <Header name='X-Quota-Allowed'>{ratelimit.Quota-1.allowed.count}</Header>
          <Header name='X-Quota-Available'>{ratelimit.Quota-1.available.count}</Header>
        </Headers>
        <Payload contentType='application/json'>{
      "error" : {
        "message" : "you have exceeded your quota",
        "clientId" : "{request.queryparam.apikey}"
      }
    }
        </Payload>
        <StatusCode>429</StatusCode>
      </Set>
    </AssignMessage>

In the [AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy), the following elements in the `<Set>` element support message templating:

  * `<Header>`
  * `<QueryParam>`
  * `<FormParam>`
  * `<PayLoad>`
  * `<Version>`
  * `<Verb>`
  * `<Path>`
  * `<StatusCode>`



Again, note that flow variables in a message template **must be enclosed in curly braces**.

When this policy executes:

  * The `<Header>` elements receive values of the specified flow variables.
  * The Payload includes a mix of literal text and variables (the `client_id` is populated dynamically).
  * The `<StatusCode>` only includes literal text; however, this element also supports message templating if you want to use it.



### Example

In a proxy `<TargetEndpoint>` definition, child-elements of `<SSLInfo>` support message templating. Following the same pattern used in policies, the flow variables in curly braces are replaced when the proxy executes.
    
    
    <TargetEndpoint name="default">
      ...
      <HTTPTargetConnection>
        <SSLInfo>
            <Enabled>{myvars.ssl.enabled}</Enabled>
            <ClientAuthEnabled>{myvars.ssl.client.auth.enabled}</ClientAuthEnabled>
            <KeyStore>{myvars.ssl.keystore}</KeyStore>
            <KeyAlias>{myvars.ssl.keyAlias}</KeyAlias>
            <TrustStore>{myvars.ssl.trustStore}</TrustStore>
        </SSLInfo>
      </HTTPTargetConnection>
      ...
    </TargetEndpoint>

## Where can you use message templates?

Message templates are supported in several **policies** as well as certain elements used in the **TargetEndpoint configuration**.

**Note:** You can also refer to the policy documentation to learn which policy and `<TargetEndpoint>` elements support message templates.

### Policies that accept message templates

The following table lists the policies and which elements/child elements are supported:

Policy | Elements/Child Elements  
---|---  
[AccessControl policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/access-control-policy) | `<SourceAddress>`, for the `mask` attribute and the IP address.  
[AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy) | [`<Set>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy#set) child elements: Payload, ContentType, Verb, Version, Path, StatusCode, Headers, QueryParams, FormParams [`<Add>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy#add) child elements: Headers, QueryParams, FormParams [`<AssignVariable>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy#assignvariable) child element: [`<Template>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy#assignvariable-template)  
[CORS policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/cors-policy) |  [`<AllowHeaders>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/cors-policy#allow-headers) [`<AllowMethods>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/cors-policy#allow-methods) [`<AllowOrigins>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/cors-policy#allow-origins) [`<ExposeHeaders>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/cors-policy#expose-headers)  
[ExtractVariables policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/extract-variables-policy) | `<JsonPath>` **Note:** Message template is **not** accepted for `<XMLPath>`.  
[GenerateJWS policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/generate-jws-policy)  
[VerifyJWS policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-jws-policy) |  `<Payload>` ([GenerateJWS policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/generate-jws-policy) only) `<AdditionalHeaders><Claim>` * These elements support message template only when **type=map**. **Important:** See [ Prevent template injection when using JWS and JWT policies](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/jwt-policies-overview#prevent-template-injection) for important security information.  
[GenerateJWT policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/generate-jwt-policy)  
[VerifyJWT policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-jwt-policy) | `<AdditionalClaims><Claim>` `<AdditionalHeaders><Claim>` * These elements support message template only when **type=map**. **Important:** See [ Prevent template injection when using JWS and JWT policies](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/jwt-policies-overview#prevent-template-injection) for important security information.  
[HTTPModifier policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy) | `<Set>` child elements: 

  * `<ContentType>`
  * `<Verb>`
  * `<Version>`
  * `<Path>`
  * `<StatusCode>`
  * `<Headers>`
  * `<QueryParams>`
  * `<FormParams>`

`<Add>` child elements: 

  * `<Headers>`
  * `<QueryParams>`
  * `<FormParams>`

  
[MessageLogging policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/message-logging-policy) | `<CloudLogging><Message>` `<Syslog><Message>` `<File><Message>`  
[OASValidation policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/oas-validation-policy) | ``<OASResource>` ` element   
[RaiseFault policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/raise-fault-policy) |  `<Set>` elements:

  * `<ContentType>`
  * `<FormParams>`
  * `<Headers>`
  * `<QueryParams>`
  * `<StatusCode>`
  * `<Path>`
  * `<Payload>`
  * `<Verb>`
  * `<Version>`

`<Add>` elements:

  * `<FormParams>`
  * `<Headers>`
  * `<QueryParams>`

  
[SAMLAssertion policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/saml-assertion-policy) | ` <Template>` * Only when the policy signature is `<GenerateSAMLAssertion>`  
[ServiceCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/service-callout-policy) |  `<Set>` elements:

  * `<ContentType>`
  * `<FormParams>`
  * `<Headers>`
  * `<QueryParams>`
  * `<StatusCode>`
  * `<Path>`
  * `<Payload>`
  * `<Verb>`
  * `<Version>`

`<Add>` elements:

  * `<FormParams>`
  * `<Headers>`
  * `<QueryParams>`

`<HTTPTargetConnection>/<URL>`: See URL templating.  
  
### `<TargetEndpoint>` elements that accept message templates

`<HTTPTargetConnection>` elements | Child elements that support message templates  
---|---  
`<SSLInfo>` |  `<Enabled>`, `<KeyAlias>`, `<KeyStore>`, `<TrustStore>`, `<ClientAuthEnabled>`, `<CLRStore>`  
`<LocalTargetConnection>` | `<ApiProxy>`, `<ProxyEndpoint>`, `<Path>`  
`<Path>` | N/A  
`<URL>` | No child elements. See URL templating for usage.  
  
## Message template syntax

This section explains the rules you must follow to use message templates.

### Use curly braces to denote variables

Enclose variable names in curly braces **{ }**. If the variable does not exist, an empty string is returned in the output; however, you can specify default values in message templates (values that are substituted if the variable is unresolved). See Setting default values in message templates. 

Note that enclosing the entire message template string in quotes is permitted, but optional. For example, the following two message templates are equivalent:  

    
    
    <Set>
      <Headers>
        <Header name="x-h1">"Hello {user.name}"</Header>
        <Header name="x-h1">Hello {user.name}</Header>
      </Headers>
    </Set>

### Spaces are not allowed in function expressions

Spaces are not allowed anywhere in message template function expressions. For example:

Allowed:
    
    
    {substring(alpha,0,4)}
    {createUuid()}
    {randomLong(10)}

Not Allowed: 
    
    
    {substring( alpha, 0, 4 )}
    { createUuid( ) }
    {randomLong( 10 )}

### Nested functions are not supported

Calling a function within another function in a template is not supported. For example, you cannot use: 
    
    
    {substring({timeFormat('yyyy-MM-dd','1494390266')},0,4)}

### Enclose string literals in template functions in single quotes

When providing string literals in functions, enclose them in single quotes rather than double quotes.

For example, 
    
    
    {replaceAll('BEARER: 1234','^Bearer ','TOKEN:')}

### Avoid using special characters in string literals

Avoid special characters, such as ':', '/', '\', '<', or '>', in string literals. These characters can cause errors. If a string literal requires special characters, assign the value to a variable using a Python or JavaScript policy and then use the variable in the template.

### Setting default values in message templates

If a templated variable can't be resolved, Apigee substitutes an empty string. However, you can specify a default value as follows:
    
    
    <Header name="x-h1">Test message. id = {request.header.id:Unknown}</Header>

In the above sample if the variable `request.header.id` cannot be resolved then its value is replaced by `Unknown`. For example:
    
    
    Test message. id = Unknown

### URL templating

The `URL` element supports templating following the same syntax as other elements.

This example shows a URL constructed using variables:
    
    
    <URL>{targeturl}</URL>

This example shows a default value for the protocol:
    
    
    <URL>{protocol:https}://{site:google.com}/path</URL>

### Legacy syntax for JSON payloads

In Apigee versions **before Cloud release 16.08.17** , you could **not** use curly braces to denote variable references within JSON payloads. In those older versions, you needed to use the `variablePrefix` and `variableSuffix` attributes to specify delimiter characters, and use those to wrap variable names, like so:
    
    
    <Set>
      <Payload contentType="application/json" variablePrefix="@" variableSuffix="#">
        {"name":"foo","type":"@variable_name#"}
      </Payload>
    </Set>

Although Apigee recommends that you use the newer curly-brace syntax, the older syntax still works.

## Using message template functions

Apigee provides a set of functions that you can use within message templates to escape, encode, hash, and format string variables, as described below. 

### Example: toLowerCase()

Use the built-in `toLowerCase()` function to transform a string variable to lowercase:
    
    
    <AssignMessage name="AM-Set-Custom-Response">
      <AssignTo createNew="false" type="response"/>
      <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
      <Set>
        <Headers>
          <Header name="x-h1">Test header: {toLowerCase(foo.bar:FOO)}</Header>
        </Headers>
      </Set>
    </AssignMessage>

If the `foo.bar` flow variable resolves, then its characters will be all lowercase. If `foo.bar` is unresolved then the default value `FOO` is substituted and converted to lowercase characters. For example:
    
    
    Test header: foo

### Example: escapeJSON()

Here's an interesting use case: Let's say your backend app returns a JSON response that contains valid escape characters. For example:
    
    
    {
      "code": "INVALID",
      "user_message": "Invalid value for \"logonId\" check your input."
    }

Then, let's say you want to return this message to the client caller in a custom payload. The usual way to do this is to extract the message from the target response payload and use AssignMessage to add it to a custom proxy response (that is, send it back to the client).

Here's the [ExtractVariables policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/extract-variables-policy) that extracts the `user_message` information into a variable called `standard.systemMessage`:
    
    
    <ExtractVariables name="EV-BackendErrorResponse">
      <DisplayName>EV-BackendErrorResponse</DisplayName>
      <JSONPayload>
        <Variable name="standard.systemMessage">
          <JSONPath>$.user_message</JSONPath>
        </Variable>
      </JSONPayload>
    </ExtractVariables>

Now, here's a perfectly valid [AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy) that adds the extracted variable to the response payload (the proxy response):
    
    
    <AssignMessage name="AM-SetStandardFaultResponse">
      <DisplayName>AM-SetStandardFaultResponse</DisplayName>
      <Set>
        <Payload contentType="application/json">
         {
           "systemMessage": "{standard.systemMessage}"
         }
        </Payload>
      </Set>
      <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
      <AssignTo>response</AssignTo>
    </AssignMessage>

Unfortunately, there's a problem. The [ExtractVariables policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/extract-variables-policy) removed the escaped quotation characters around part of the message. This means that the response returned to the client is invalid JSON. This is clearly not what you intended!
    
    
    {
      "systemMessage": "Invalid value for "logonId" check your input."
    }

To work around this problem, you can modify the AssignMessage policy to use a **message template function** that escapes the quotes within the JSON for you. This function, `escapeJSON()`, escapes any quotes or other special characters that occur within a JSON expression: 
    
    
    <AssignMessage name="AM-SetStandardFaultResponse">
      <DisplayName>AM-SetStandardFaultResponse</DisplayName>
      <Set>
        <Payload contentType="application/json">
         {
           "systemMessage": "{escapeJSON(standard.systemMessage)}"
         }
        </Payload>
      </Set>
      <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
      <AssignTo>response</AssignTo>
    </AssignMessage>

The function escapes the embedded quotes, resulting in valid JSON, which is exactly what you wanted:
    
    
    {
      "systemMessage": "Invalid value for \"logonId\" check your input.",
    }

A message template is a dynamic string substitution feature that you can use in certain policies and in `<TargetEndpoint>` definitions. Message template **functions** let you perform useful operations such as hashing, string manipulation, character escaping, and others within a message template.

For example, in the following AssignMessage policy, the function `toLowerCase()` is used in a message template:
    
    
    <AssignMessage name="AM-Set-Custom-Response">
      <AssignTo>response</AssignTo>
      <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
      <Set>
       <Headers>
         <Header name="x-h1">Test header: Hello, {toLowerCase(user.name)}</Header>
       </Headers>
      </Set>
    </AssignMessage>

This section describes the message template functions, their arguments, and outputs. This topic assumes that you are familiar with message templates and the contexts in which they are used.

## Hash functions

Compute a hash value and return the string representation of that hash.

**Note:** Spaces are not allowed anywhere within function expressions. See Spaces are not allowed in function expressions.

### Hexadecimal hash functions

Compute a hash value and return the string representation of that hash as a hexadecimal number. 

#### Syntax

Function | Description  
---|---  
`md5Hex(string)` | Computes an MD5 hash expressed as a hexadecimal number.  
`sha1Hex(string)` | Computes a SHA1 hash expressed as a hexadecimal number.  
`sha256Hex(string)` | Computes a SHA256 hash expressed as a hexadecimal number.  
`sha384Hex(string)` | Computes a SHA384 hash expressed as a hexadecimal number.  
`sha512Hex(string)` | Computes a SHA512 hash expressed as a hexadecimal number.  
  
#### Arguments

`string`: The Hash functions take a single string argument upon which the hash algorithm is computed. The argument can be a literal string (enclosed in single quotes) or a string flow variable.

#### Examples

Function call:
    
    
    sha256Hex('abc')

Result:
    
    
    ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad

Function call:
    
    
    var str = 'abc';
    sha256Hex(str)

Result:
    
    
    ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad

### Base64 hash functions

Compute a hash value and return the string representation of that hash as a Base64 encoded value.

#### Syntax

Function  | Description   
---|---  
`md5Base64(string)` | Computes an MD5 hash expressed as a Base64 encoded value.   
`sha1Base64(string)` | Computes a SHA1 hash expressed as a Base64 encoded value.   
`sha256Base64(string)` | Computes a SHA256 hash expressed as a Base64 encoded value.   
`sha384Base64(string)` | Computes a SHA384 hash expressed as a Base64 encoded valuer.   
`sha512Base64(string)` | Computes a SHA512 hash expressed as a Base64 encoded value.   
  
#### Arguments

`string`: The Hash functions take a single string argument upon which the hash algorithm is computed. The argument can be a literal string (enclosed in single quotes) or a string flow variable. 

#### Examples

Function call: 
    
    
    sha256Base64('abc')

Result: 
    
    
    ungWv48Bz+pBQUDeXa4iI7ADYaOWF3qctBD/YfIAFa0=

Function call: 
    
    
    var str = 'abc';
    sha256Base64(str)

Result: 
    
    
    ungWv48Bz+pBQUDeXa4iI7ADYaOWF3qctBD/YfIAFa0=

## String functions

Perform operations on strings within a message template. 

**Note:** Spaces are not allowed anywhere within function expressions. See Spaces are not allowed in function expressions.

### Base64 encoding functions

Encode and decode strings using the Base64 encoding scheme.

#### Syntax

Function  | Description   
---|---  
`encodeBase64(string)` | Encodes a string using Base64 encoding. For example: `encodeBase64(value)`, when value holds `abc`, the function returns the string: `YWJj`  
`decodeBase64(string)` | Decodes a Base64 encoded string. For example: `decodeBase64(value)` when value holds `aGVsbG8sIHdvcmxk`, the function returns the string `hello, world`.   
  
#### Arguments

`string`: The string to encode or decode. Can be a literal string (enclosed in single quotes) or a string flow variable. 

#### Example
    
    
    <AssignMessage name="AM-Set-Custom-Response">
        <AssignTo createNew="false" type="response"/>
        <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
        <Set>
           <Headers>
             <Header name="x-h1">Hello, {decodeBase64('d29ybGQK')}</Header>
           </Headers>
        </Set>
    </AssignMessage>

**Note:****Base64** encoding is different from **Base64URL**. Attempting to decode a **Base64URL** encoded string produces an empty string.

### Case conversion functions

Convert a string to all uppercase or all lowercase letters. 

#### Syntax

Function | Description  
---|---  
`toUpperCase(string)` | Converts a string to uppercase.   
`toLowerCase(string)` | Converts a string to lowercase.   
  
#### Arguments

`string`: The string to convert. Can be a literal string (enclosed in single quotes) or a string flow variable. 

#### Example
    
    
    <AssignMessage name="AM-Set-Custom-Response">
        <AssignTo createNew="false" type="response"/>
        <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
        <Set>
           <Headers>
             <Header name="x-h1">Hello, {toLowerCase(user.name)}</Header>
           </Headers>
        </Set>
    </AssignMessage>

### Substring function

Returns the characters between the starting and ending index of the specified string. 

#### Syntax
    
    
    substring(str,start_index,end_index)

#### Arguments

  * `str`: A literal string (enclosed in single quotes) or string flow variable. 
  * `start_index`: The starting index into the string. 
  * `end_index`: (Optional) The ending index into the string. If not supplied, ending index is the end of the string.



#### Examples

For the following examples, suppose that these flow variables exist: 

Variable name | Value  
---|---  
`alpha` | ABCDEFGHIJKLMNOPQRSTUVWXYZ   
`seven` | 7   
  
  
Here are results of function calls that use these variables:  


Message template expression | Result  
---|---  
`{substring(alpha,22)}` | `WXYZ`  
`hello {substring(alpha,22)}` | `hello WXYZ`  
`{substring(alpha,-4)}` | `WXYZ `  
`{substring(alpha,-8,-4)}` | `STUV`  
`{substring(alpha,0,10)}` | `ABCDEFGHIJ`  
`{substring(alpha,0,seven)}` | `ABCDEFG`  
  
### Replace All function

Applies a regular expression to a string and for any matches, replaces the match with a replacement value. 

#### Syntax
    
    
    replaceAll(string,regex,value)

#### Arguments

  * **string** \- A literal string (enclosed in single quotes) or string flow variable in which to make replacements. 
  * **regex** \- A regular expression. 
  * **value** \- The value to replace all regex matches within the string.



#### Examples

For the following examples, suppose these flow variables exist:  


Variable name | Value  
---|---  
`header` | `Bearer ABCDEFGHIJKLMNOPQRSTUVWXYZ-9993 `  
`regex1` | `"^Bearer "`  
`replacement` | `"TOKEN: "`  
  
Here are results of function calls that use these variables:  


Message template expression  | Result   
---|---  
`{replaceAll(header,'9993','')}` | `Bearer ABCDEFGHIJKLMNOPQRSTUVWXYZ-`  
`{replaceAll(header,regex1,'')}` | `ABCDEFGHIJKLMNOPQRSTUVWXYZ-9993`  
`{replaceAll(header,regex1,replacement)}` | `TOKEN: ABCDEFGHIJKLMNOPQRSTUVWXYZ-9993`  
  
### Replace First function

Replaces only the first occurrence of the specified regular expression match in the string. 

#### Syntax
    
    
    replaceFirst(string,regex,value)

#### Arguments

  * `string`: A literal string (enclosed in single quotes) or string flow variable in which to make replacements. 
  * `regex`: A regular expression. 
  * `value`: The value to replace regex matches within the string.



## Character escape and encoding functions

Functions that escape or encode special characters in a string. 

**Note:** Spaces are not allowed anywhere within function expressions. See Spaces are not allowed in function expressions.

### Syntax

Function | Description  
---|---  
`escapeJSON(string)` | Backslash-escapes double-quotes.   
`escapeXML(string)` | Replaces angle brackets, apostrophe, double-quote and ampersands with the respective XML entities. Use for XML 1.0 documents. Use escapeXML for XML1.0 documents and escapeXML11 for XML 1.1 documents.  
`escapeXML11(string)` | Works the same way as escapeXML, but for XML v1.1 entities. See Usage notes below.   
`encodeHTML(string)` | Encodes apostrophe, angle brackets, and ampersand.   
  
### Arguments

`string`: The string to escape. Can be a literal string (enclosed in single quotes) or a string flow variable.

### Usage notes

XML 1.1 can represent certain control characters, but it cannot represent the null byte or unpaired Unicode surrogate codepoints, even after escaping. The `escapeXML11()` function removes characters that do not fit in the following ranges:
    
    
    [#x1-#xD7FF] | [#xE000-#xFFFD] | [#x10000-#x10FFFF]

The `escapeXML11()` function escapes characters in the following ranges:
    
    
    [#x1-#x8] | [#xB-#xC] | [#xE-#x1F] | [#x7F-#x84] | [#x86-#x9F]

### Examples

Assume a flow variable called **food** exists with this value: **`"bread"& "butter"`**. Then, the function:
    
    
    {escapeHTML(food)}

Results in:
    
    
    &quot;bread&quot; &amp; &quot;butter&quot;

## Time format functions

Return a string representation of the time, formatted in UTC.

**Notes:**  
  
Spaces are not allowed anywhere within function expressions. See Spaces are not allowed in function expressions.  
  
Colons inside time format string literals (such as "HH:mm:ss") interfere when setting default values in message templates. Use variables instead of literals to specify string formats involving colons. See Avoid using special characters in string literals.

### Syntax

Function | Description  
---|---  
`timeFormat(format,str)` |  Returns the date formatted in UTC. DEPRECATED: _Returns the date formatted in the local time zone._  
`timeFormatMs(format,str)` |  Returns the date formatted in UTC. DEPRECATED: _Returns the date formatted in the local time zone._  
`timeFormatUTC(format,str)` | Returns the date formatted in UTC.   
`timeFormatUTCMs(format,str)` | Returns the date formatted in UTC.   
  
### Arguments

  * `format`: A date/time format string. Can be a literal string (enclosed in single quotes) or a string variable. Use a variable instead of a literal when the format includes a colon. See the previous note in this section.
  * `str`: A string or string flow variable containing a time value. The value can be in seconds-since-epoch or milliseconds-since-epoch for timeFormatMs.



### Examples

Assume the following values and assume the local timezone is Pacific: 

  * `epoch_time_ms = 1494390266000`
  * `epoch_time = 1494390266`
  * `fmt1 = yyyy-MM-dd`
  * `fmt2 = yyyy-MM-dd HH-mm-ss`
  * `fmt3 = yyyyMMddHHmmss`



The functions return the following results: 

Function | Output  
---|---  
`timeFormatMs(fmt1,epoch_time_ms)` | `2017-05-09`  
`timeFormat(fmt1,epoch_time)` | `2017-05-09`  
`timeFormat(fmt2,epoch_time)` | `2017-05-09 21:24:26`  
`timeFormat(fmt3,epoch_time)` | `20170509212426`  
`timeFormatUTC(fmt1,epoch_time)` | `2017-05-10`  
`timeFormatUTC(fmt2,epoch_time)` | `2017-05-10 04:24:26`  
`timeFormatUTC(fmt3,epoch_time)` | `20170510042426`  
  
## HMAC calculation functions

The HMAC calculation functions provide an alternative to using the [HMAC policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/hmac-policy) to compute an HMAC. The functions are handy when performing a cascaded HMAC calculation, as when the output of one HMAC is used as the key for a second HMAC. 

**Note:** Spaces are not allowed anywhere within function expressions. See Spaces are not allowed in function expressions.

### Syntax

Function  | Description   
---|---  
`hmacSha224(key,valueToSign[,keyencoding[,outputencoding]])` | Computes an HMAC with the SHA-224 hash function.   
`hmacSha256(key,valueToSign[,keyencoding[,outputencoding]])` | Encodes an HMAC with the SHA-256 hash function.   
`hmacSha384(key,valueToSign[,keyencoding[,outputencoding]])` | Encodes an HMAC with the SHA-384 hash function.   
`hmacSha512(key,valueToSign[,keyencoding[,outputencoding]])` | Encodes an HMAC with the SHA-512 hash function.   
`hmacMd5(key,valueToSign[,keyencoding[,outputencoding]])` | Encodes an HMAC with the MD5 hash function.   
`hmacSha1(key,valueToSign[,keyencoding[,outputencoding]])` | Encodes an HMAC with the SHA-1 encryption algorithm.   
**Security note:** SHA-1 and MD-5 are included here for completeness, but Google recommends that people do not use these hashes. Google first demonstrated collision attacks against SHA-1 in [2017](https://security.googleblog.com/2017/02/announcing-first-sha1-collision.html), and recommends against using it; NIST also recommends that people [stop using SHA-1](https://csrc.nist.gov/projects/hash-functions/nist-policy-on-hash-functions). The CMU Software Engineering Institute first recommended that people should [avoid using the MD5 algorithm](https://www.kb.cert.org/vuls/id/836068) in any capacity, in 2008.

### Arguments

  * **key** \- (Required) Specifies the secret key, encoded as a string, used to compute the HMAC. 
  * **valueToSign** \- (Required) Specifies the message to sign. It should be a string.
  * **keyencoding** \- (Optional) The secret key string will be decoded according to this specified encoding. Valid values: `hex`, `base16`, `base64`, `utf-8`. Default: `utf-8`
  * **outputencoding** \- (Optional) Specifies the encoding algorithm to use for the output. Valid values: `hex`, `base16`, `base64`. The values are case insensitive; `hex` and `base16` are synonyms. Default: `base64`



### Examples

This example uses the AssignMessage policy to compute an HMAC-256 and assign it to a flow variable: 
    
    
    <AssignMessage name='AM-HMAC-1'>
      <AssignVariable>
        <Name>valueToSign</Name>
        <Template>{request.header.apikey}.{request.header.date}</Template>
      </AssignVariable>
      <AssignVariable>
        <Name>hmac_value</Name>
        <Template>{hmacSha256(private.secretkey,valueToSign)}</Template>
      </AssignVariable>
    </AssignMessage>

This example illustrates how to generate a cascading HMAC that can be used with the [AWS Signature v4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signing process. The example uses the AssignMessage policy to generate the five levels of cascaded HMAC used to calculate a signature for AWS Signature v4: 
    
    
    <AssignMessage name='AM-HMAC-AWS-1'>
      <!-- 1 -->
      <AssignVariable>
        <Name>DateValue</Name>
        <Template>{timeFormatUTCMs('yyyyMMdd',system.timestamp)}</Template>
      </AssignVariable>
      <!-- 2 -->
      <AssignVariable>
        <Name>FirstKey</Name>
        <Template>AWS4{private.secret_aws_access_key}</Template>
      </AssignVariable>
      <!-- 3 -->
      <AssignVariable>
        <Name>DateKey</Name>
        <Template>{hmacSha256(FirstKey,DateValue,'utf-8','base16')}</Template>
      </AssignVariable>
      <!-- 4 -->
      <AssignVariable>
        <Name>DateRegionKey</Name>
        <Template>{hmacSha256(DateKey,aws_region,'base16','base16')}</Template>
      </AssignVariable>
      <!-- 5 -->
      <AssignVariable>
        <Name>DateRegionServiceKey</Name>
        <Template>{hmacSha256(DateRegionKey,aws_service,'base16','base16')}</Template>
      </AssignVariable>
      <!-- 6 -->
      <AssignVariable>
        <Name>SigningKey</Name>
        <Template>{hmacSha256(DateRegionServiceKey,'aws4_request','base16','base16')}</Template>
      </AssignVariable>
      <!-- 7 -->
      <AssignVariable>
        <Name>aws4_hmac_value</Name>
        <Template>{hmacSha256(SigningKey,stringToSign,'base16','base16')}</Template>
      </AssignVariable>
    </AssignMessage>

## Other functions

### Create UUID function

Generates and returns a UUID.

**Note:** Spaces are not allowed anywhere within function expressions. See Spaces are not allowed in function expressions.

#### Syntax
    
    
    createUuid()

#### Arguments

None.

#### Example
    
    
    {createUuid()}

Sample result:
    
    
    ec3ca9be-d1e1-4ef4-aee4-4a58f3130db8

### Random Long Generator function

Returns a random long integer.

#### Syntax
    
    
    randomLong(args)

#### Arguments

  * If no arguments are specified, the function returns a random long integer, as computed by the Java SecureRandom class.
  * If one argument is present, it is treated as the minimum value of the computation.
  * If a second argument is present, it is treated as the maximum value of the computation.



#### Example
    
    
    {randomLong()}

Results in something like this:
    
    
    5211338197474042880

### Regex text generator

Generate a text string that matches a given regular expression.

#### Syntax
    
    
    xeger(regex)

#### Argument

`regex`: A regular expression.

#### Example

This example generates a seven digit string with no zeros:
    
    
    xeger( '[1-9]{7}' )

Example result:
    
    
    9857253

### Null-coalescing function

The `firstnonnull()` function returns the value of the left-most, non-null argument.

#### Syntax
    
    
    firstnonnull(var1,varnn>)

#### Argument

`var1`: A context variable.

`varn`: One or more context variables. You can set the right-most argument to a string to provide a fallback value (a value that will be set if none of the left-hand arguments are set). 

#### Examples

The following table illustrates how to use the function: 

Template  | Var1  | Var2  | Var3  | Result   
---|---|---|---|---  
`{firstnonnull(var1,var2)}` | Not set  | `foo` | N/A  | `foo`  
`{firstnonnull(var1,var2)}` | `foo` | `bar` | N/A  | `foo`  
`{firstnonnull(var1,var2)}` | `foo` | Not set  | N/A  | `foo`  
`{firstnonnull(var1,var2,var3)}` | `foo` | `bar` | `baz` | `foo`  
`{firstnonnull(var1,var2,var3)}` | Not set  | `bar` | `baz` | `bar`  
`{firstnonnull(var1,var2,var3)}` | Not set  | Not set  | `baz` | `baz`  
`{firstnonnull(var1,var2,var3)}` | Not set  | Not set  | Not set  | `null`  
`{firstnonnull(var1)}` | Not set  | N/A  | N/A  | `null`  
`{firstnonnull(var1)}` | `foo` | N/A  | N/A  | `foo`  
`{firstnonnull(var1,var2)}` | `""` | `bar` | N/A  | `""`  
`{firstnonnull(var1,var2,'fallback value')}` | `null` | `null` | `fallback value` | `fallback value`  
  
### XPath function

Applies an XPath expression to an XML variable.

#### Syntax
    
    
    xpath(xpath_expression,xml_string[,datatype])

#### Arguments

`xpath_expression`: An XPath expression.

`xml_string`: A flow variable or string containing XML.

`datatype`: (Optional) Specifies the desired return type of the query. Valid values are `nodeset`, `node`, `number`, `boolean`, or `string`. The default value is `nodeset`. The default is usually the right choice.

The function returns an empty string if the expression does not match.

#### Example 1

Suppose these context variables define an XML string and an XPath expression:
    
    
    xml = "<tag><tagid>250397</tagid><readerid>1</readerid><rssi>74</rssi><date>2019/06/15</date></tag>"
    xpath = "/tag/tagid"

And the `xpath()` function is used in an AssignMessage policy, as follows:
    
    
    <AssignMessage>
      <AssignVariable>
        <Name>extracted_tag</Name>
        <Template>{xpath(xpath,xml)}</Template>
      </AssignVariable>
    </AssignMessage>

The function returns the value `<tagid>250397</tagid>`. This value is placed in the context variable called `extracted_tag`. 

#### Example 2: XML namespaces

To specify a namespace, append additional parameters, each one a string that looks like `prefix:namespaceuri`. For example, an `xpath()` function that selects the child element of a SOAP body might be like this:
    
    
    <AssignMessage>
      <AssignVariable>
        <Name>soapns</Name>
        <Value>soap:http://schemas.xmlsoap.org/soap/envelope/</Value>
      </AssignVariable>
      <AssignVariable>
        <Name>xpathexpression</Name>
        <Value>/soap:Envelope/soap:Body/*</Value>
      </AssignVariable>
      <AssignVariable>
        <Name>extracted_element</Name>
        <Template>{xpath(xpathexpression,xml,soapns)}</Template>
      </AssignVariable>
    </AssignMessage>

For additional namespaces, you can add up to 10 additional parameters to the `xpath()` function.

Rather than specify a XPath expressions with special characters as a string literal, use a variable to include that string in the function. See Avoid using special characters in string literals for details.
    
    
    {xpath(xpathexpression,xml,ns1)}

#### Example 3: Specifying a desired return type

The optional third parameter passed to the `xpath()` function specifies the desired return type of the query.

Some XPath queries can return numeric or boolean values. For example the `count()` function returns a number. This is a valid XPath query:
    
    
    count(//Record/Fields/Pair)

This valid query returns a boolean:
    
    
    count(//Record/Fields/Pair)>0

In those cases invoke the `xpath()` function with a third parameter specifying that type:
    
    
    {xpath(expression,xml,'number')}
    {xpath(expression,xml,'boolean')}

If the third parameter contains a colon, then it is interpreted as a namespace argument. If not, then it is treated as the desired return type. In this case, if the third parameter is not one of the valid values (ignoring case), the `xpath()` function defaults to returning a nodeset.

### JSON Path function

Evaluates [a JSON Path](https://www.rfc-editor.org/rfc/rfc9535.html) expression against a JSON variable.

#### Syntax
    
    
    jsonPath(json-path,json-var,want-array)

#### Arguments

  * (Required) `json-path`: (String) A JSON Path expression.
  * (Required) `json-var`: (String) A flow variable or string containing JSON.
  * (Optional) `want-array`: (String) If this parameter is set to `true` and if the result set is an array, then all array elements are returned. If set to any other value or if this parameter is omitted, then only the zeroth element of a result set array is returned. If the result set is not an array, then this third parameter, if present, is ignored. 




You can use variables for any of the arguments. If you use fixed strings, enclose them in single quotes.

The function returns an empty string if the expression does not match.

#### Example 1

If this is the message template:
    
    
    The address is {jsonPath('$.results[?(@.name == "Mae West")].address.line1',the_json_variable)}

and `the_json_variable` contains:
    
    
    {
      "results" : [
        {
          "address" : {
            "line1" : "18250 142ND AV NE",
            "city" : "Woodinville",
            "state" : "Washington",
            "zip" : "98072"
          },
          "name" : "Fred Meyer"
        },
        {
          "address" : {
            "line1" : "1060 West Addison Street",
            "city" : "Chicago",
            "state" : "Illinois",
            "zip" : "60613"
          },
          "name" : "Mae West"
        }
      ]
    } 

The result of the function is:
    
    
    The address is 1060 West Addison Street

The return value for this jsonPath query will be an array containing a single element. The jsonPath function in Apigee by default assumes you want a single value, for use within string interpolation. Therefore Apigee returns only the zeroth element of the array. To request the full array, call the function with `true` as the third parameter, as shown in the next example. 

#### Example 2

If this is the message template:
    
    
    {jsonPath('$.config.quota[?(@.operation=="ManageOrder")].appname',the_json_variable,true)}

and `the_json_variable` contains:
    
    
    {
      "config": {
        "quota": [
          {
            "appname": "A",
            "operation": "ManageOrder",
            "value": "900"
          },
          {
            "appname": "B",
            "operation": "ManageOrder",
            "value": "1000"
          },
          {
            "appname": "B",
            "operation": "SubmitOrder",
            "value": "800"
          }
        ]
      }
    }

The result of the function is:
    
    
    ["A","B"]

In this case the third parameter to the function is set to `true`, therefore the jsonPath function returns the full array, in JSON array syntax, rather than the zeroth element. 

#### Example 3

If `the_json_variable` contains:
    
    
    {
      "config": {
        "quota": [
          {
            "appname": "A",
            "operation": "ManageOrder",
            "value": "900"
          },
          {
            "appname": "B",
            "operation": "ManageOrder",
            "value": "1000"
          },
          {
            "appname": "B",
            "operation": "SubmitOrder",
            "value": "800"
          }
        ]
      }
    }

and `the_query` contains:
    
    
    $.config.quota[?(@.operation=="ManageOrder")].appname

The result of the message template: `{jsonPath(the_query,the_json_variable,true)}` is `["A","B"]`

Using a variable for the query allows you to construct a query at runtime, using dynamic data. You can do that with the [`<AssignVariable>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy#assignvariable) element within the [AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy). 

For example, supposing the variable `operationname` contains the value `ManageOrder`, the following policy will set `the_query` to the query shown above. 
    
    
    <AssignMessage>
        <AssignVariable>
          <Name>the_query</Name>
          <Template>$.config.quota[?(@.operation=="{operationname}")].appname</Template>
        </AssignVariable>
      </AssignMessage>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
