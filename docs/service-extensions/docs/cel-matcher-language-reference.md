---
url: https://docs.cloud.google.com/service-extensions/docs/cel-matcher-language-reference/
title: CEL matcher language reference \u00a0|\u00a0 Service Extensions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:49.996044+00:00
---

# CEL matcher language reference  |  Service Extensions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-extensions/docs/cel-matcher-language-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Service Extensions ](https://docs.cloud.google.com/service-extensions/docs)
  * [ Reference ](https://docs.cloud.google.com/service-extensions/docs/apis)



Send feedback 

#  CEL matcher language reference Stay organized with collections  Save and categorize content based on your preferences. 

[Common Expression Language (CEL)](https://opensource.google/projects/cel) is an open source non-Turing complete language that implements common semantics for expression evaluation. Service Extensions uses a subset of CEL conditions to make chain evaluation decisions based on attribute data. In general, a condition expression consists of one or more statements that are joined by logical operators (`&&`, `||`, or `!`).

## Attributes

For any given connection request, the proxy extracts attributes, which are a set of contextual information. Attributes have a fixed type (such as `string` or `int`), and might be absent or present, depending on the context. Attributes are exposed to the CEL runtime during match condition processing. Attributes are not available to be sent to an extension service.

### Request attributes

The following attributes can be extracted from requests:

Attribute | Attribute type | Description  
---|---|---  
`request.headers` | map{string,string} | A string-to-string map of the HTTP request headers. If a header contains multiple values, the value in this map is a comma-separated string of all values of the header. The keys in this map are in lowercase.  
`request.method` | string | The HTTP request method, such as `GET` or `POST`.  
`request.host` | string | Convenience equivalent to `request.headers['host']`.   
`request.path` | string | The requested HTTP URL path.  
`request.query` | string | The HTTP URL query in the format of `name1=value&name2=value2`, as it appears in the first line of the HTTP request. No decoding is performed.  
`request.scheme` | string | The HTTP URL scheme, such as HTTP or HTTPS. Values for this attribute are in lowercase.  
`request.backend_service_name` | string | The backend service to which the request is forwarded. Not applicable for edge extensions.  
`request.backend_service_project_number` | int | When using Shared VPC, the project number of the backend service to which the request is forwarded. Not applicable for edge extensions.  
  
### Connection attributes

The following attributes can be extracted from connections:

Attribute | Attribute type | Description  
---|---|---  
`source.ip` | string | The source IP address of the request.  
`source.port` | int | The connection port of the downstream client.  
`connection.sni` | string | The requested server name of the downstream TLS connection.  
`connection.tls_version` | string | The TLS version of the downstream TLS connection. Valid values: `TLSv1`, `TLSv1.1`, `TLSv1.2`, and `TLSv1.3`.   
`connection.sha256_peer_certificate_digest` | string | The hexadecimal-encoded SHA256 hash of the peer certificate in the downstream TLS connection, if present.  
  
## Operators

Service Extensions supports several operators that you can use to build complex match conditions from simple expression statements. Service Extensions supports logical operators, such as `&&`, `||`, and `!`, and string manipulation operators, such as `x.contains('y')`.

String manipulation operators match strings or substrings that you define. For example, `request.host.endsWith('.example.com')` evaluates to `true` if the HTTP request was made to a domain ending with `example.com`.

Logical operators let you verify multiple variables in a conditional expression. For example, `request.method == 'GET' && request.host.matches('.example.com')` joins two statements and requires both statements to be `true` to produce an overall result of `true`.

### Logical operators

The following table describes the logical operators that Service Extensions supports.

Example expression | Description  
---|---  
`x == "foo"` | Returns `true` if `x` is equal to the constant string literal argument.  
`x == R"fo'o"` | Returns `true` if `x` is equal to the given raw string literal that does not interpret escape sequences. Raw string literals are convenient for expressing strings that the code must use to escape sequence characters.  
`x == y` | Returns `true` if `x` is equal to `y`.  
`x != y` | Returns `true` if `x` is not equal to `y`.  
`x && y` | Returns `true` if both `x` and `y` are `true`.  
`x || y` | Returns `true` if `x`, `y`, or both are `true`.  
`!x` | Returns `true` if the boolean value `x` is `false`, or returns `false` if the boolean value `x` is `true`.  
` m['k'] ` | If key `k` is present, returns the value at key `k` in the string-to-string map `m`. If key `k` is not present, returns an error that causes the rule under evaluation to not match.  
` k in m ` | Returns `true` if key `k` is present in the string-keyed map `m`. Otherwise, returns `false`.  
  
### String manipulation operators

The following table describes the string manipulation operators that Service Extensions supports.

Expression | Description  
---|---  
` x.contains(y) ` | Returns `true` if the string `x` contains the substring `y`.  
` x.startsWith(y) ` | Returns `true` if the string `x` begins with the substring `y`.  
` x.endsWith(y) ` | Returns `true` if the string `x` ends with the substring `y`.  
` x.matches(y) ` | Returns `true` if the string `x` matches the specified [ RE2](https://www.wikipedia.org/wiki/RE2_\(software\)) pattern `y`. Service Extensions uses the RE2::Latin1 option when it compiles the RE2 pattern, which disables Unicode features. Edge extensions let you use only one regular expression per CEL expression.  
`x.lower()` | Returns the lowercase value of string `x`.  
`x.upper()` | Returns the uppercase value of string `x`.  
`int(x)` | Converts the string result of `x` to an `int` type. You can use the converted string for integer comparison by using standard arithmetic operators, such as greater than (`>`) and less than or equal to (`≤`). This works only for values that can be integers.  
  
## Sample expressions

Match all requests to host `example.com` with backend service `bs1` in `123` as the final destination:
    
    
    request.host == "example.com" && request.backend_service_name == "bs1" &&
      request.backend_service_project_number == 123
    

Match all requests for the path `*/inventory` with an HTTP header `Hello`. Note that header names are case insensitive for CEL matching:
    
    
    request.path.endsWith("/inventory") && "Hello" in request.headers
    

## Limitations

The following limitations apply to CEL expressions when specified for Service Extensions:

  * Maximum expressions per extension: 1 for edge extensions and 5 for other extensions
  * Maximum number of characters per regular expression: 100
  * Maximum number of characters per CEL expression: 500



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
