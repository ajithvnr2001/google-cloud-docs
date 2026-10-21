---
url: https://docs.cloud.google.com/secure-web-proxy/docs/cel-matcher-language-reference/
title: CEL matcher language reference \u00a0|\u00a0 Secure Web Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:08:21.559566+00:00
---

# CEL matcher language reference  |  Secure Web Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/cel-matcher-language-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Reference ](https://docs.cloud.google.com/secure-web-proxy/docs/apis)



Send feedback 

#  CEL matcher language reference Stay organized with collections  Save and categorize content based on your preferences. 

[Common Expression Language (CEL)](https://opensource.google/projects/cel) is an open source non-Turing complete language that implements common semantics for expression evaluation. Secure Web Proxy uses a subset of CEL conditions to make boolean authorization decisions based on attribute data. In general, a condition expression consists of one or more statements that are joined by logical operators (`&&`, `||`, or `!`). Each statement expresses an attribute-based control rule that applies to the role binding and ultimately determines whether access is allowed.

## Attributes

Use session attributes and application attributes while defining Secure Web Proxy policies to describe either the session attributes or the application attributes that a policy applies to.

Session attributes, described by `SessionMatcher`, apply to session-specific attributes such as the source IP address, hosts, and IP range. Application attributes, described by `ApplicationMatcher`, apply to application attributes such as request headers, request method, and request path.

### Attributes available to `SessionMatcher` and `ApplicationMatcher`

The following table describes attributes that apply to both `SessionMatcher` and `ApplicationMatcher`.

Attribute | Attribute type | Description  
---|---|---  
`source.ip` | string | IP address of the client that sent the request.  
`source.port` | integer | Client port that sent the request.  
`destination.port` | integer | Upstream port to which your Secure Web Proxy instance sends the traffic.  
`host()` | string | Host value used for DNS resolution and upstream connections. _This doesn't include the port._ The value of **host()** is determined by the following: 

  * Raw HTTP requests: Host header
  * Proxy tunnel HTTP CONNECT requests: CONNECT target

  
`source.matchTag(SECURE_TAG)` | boolean | `True`, if the source is associated with `SECURE_TAG`. The argument is the permanent ID of the secure tag, such as `source.matchTag('tagValues/123456')`.  
`source.matchServiceAccount(SERVICE_ACCOUNT)` | boolean | `True`, if the source is associated with `SERVICE_ACCOUNT`, such as `source.matchServiceAccount('x@my-project.iam.gserviceaccount.com')`.   
`inUrlList(HOST_OR_URL, NAMED_LIST)` | boolean |  `True`, if `HOST_OR_URL` is present in the provided named list `NAMED_LIST`. For example:

  * `inUrlList(host(), 'projects/1234/locations/us-east1/urlLists/allowed-repos')`
  * `inUrlList(request.url(), 'projects/1234/locations/us-east1/urlLists/allowed-repos')`

When a `UrlList` pattern is matched against values without a forward-slash (`/`), such as in `host()`, only the domain portion of the pattern is matched. For more information, see [How `UrlList` interprets entries](https://docs.cloud.google.com/secure-web-proxy/docs/url-list-syntax-reference#how-urllist-interprets-entries).  
`inIpRange(IP_ADDRESS,  
IP_RANGE)` | boolean | `True`, if `IP_ADDRESS` is contained within the `IP_RANGE`, such as `inIpRange(source.ip, '1.2.3.0/24')`. Subnet masks for IPv6 addresses can't be larger than /64.   
  
### Attributes available only to `ApplicationMatcher`

The following table describes attributes that apply only to `ApplicationMatcher`.

Attribute | Attribute type | Description  
---|---|---  
`request.headers` | map | String-to-string map of the request headers. If a header contains multiple values, then the value in this map is a comma-separated string of all the values of the header. All keys in this map are in _lowercase_.  
`request.method` | string | Request method, such as GET or POST.  
`request.host` | string | Convenience equivalent to `request.headers['host']`. We recommend that you use `host()` in most cases.  
`request.path` | string | Requested URL path.  
`request.query` | string | URL query in the format of `name1=value&name2=value2`, as it appears in the first line of the request. No decoding is performed.  
`request.scheme` | string | URL scheme, such as HTTP or HTTPS. All values of this attribute are in lowercase.  
`request.url()` | string | Convenience for `host() + request.path`. _This doesn't include the port_ and uses a host value that might differ from the host header.  
`request.useragent()` | string | Convenience equivalent to `request.headers['user-agent']`.  
  
## Operators

Secure Web Proxy supports several operators that can be used to build complex logic expressions from simple expression statements. Secure Web Proxy supports logical operators, such as `&&`, `||,` and `!`, and string manipulation operators, such as `x.contains('y')`.

The logical operators let you verify multiple variables in a conditional expression. For example, `request.method == 'GET' && host().matches('.*\.example.com')` joins two statements and requires both statements to be `True` to produce an overall result of `True`.

The string manipulation operators match strings or substrings that you define, and let you develop rules to control access to resources without listing every possible combination.

### Logical operators

The following table describes the logical operators that Secure Web Proxy supports.

Example expression | Description  
---|---  
`x == "foo"` | Returns `True` if `x` is equal to the constant string literal argument.  
`x == R"fo'o"` | Returns `True` if `x` is equal to the given raw string literal that does not interpret escape sequences. Raw string literals are convenient for expressing strings that the code must use to escape sequence characters.  
`x == y` | Returns `True` if `x` is equal to `y`.  
` x != y ` | Returns `True` if `x` is not equal to `y`.  
` x && y ` | Returns `True` if both `x` and `y` are `True`.  
` x || y ` | Returns `True` if `x`, `y`, or both are `True`.  
` !x ` | Returns `True` if the boolean value `x` is `False`. Otherwise, it returns `False` if the boolean value `x` is `True`.  
` m['k'] ` | If key `k` is present, returns the value at key `k` in the string-to-string map `m`. If key `k` is not present, it returns an error that causes the rule under evaluation to not match.  
  
### String manipulation operators

The following table describes the string manipulation operators that Secure Web Proxy supports.

Expression | Description  
---|---  
` x.contains(y) ` | Returns `True` if the string `x` contains the substring `y`.  
` x.startsWith(y) ` | Returns `True` if the string `x` begins with the substring `y`.  
` x.endsWith(y) ` | Returns `True` if the string `x` ends with the substring `y`.  
` x.matches(y) ` | Returns `True` if the string `x` matches the specified [ RE2](https://www.wikipedia.org/wiki/RE2_\(software\)) pattern `y`. The RE2 pattern is compiled by using the RE2::Latin1 option that disables Unicode features.  
` x.lower() ` | Returns the lowercase value of the string `x`.  
` x.upper() ` | Returns the uppercase value of the string `x`.  
` x + y ` | Returns the concatenated string `xy`.  
` int(x) ` | Converts the string result of `x` to an `int` type. You can use the converted string to compare integers with standard arithmetic operators such as `>` and `<=`. This works only for integer values.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
