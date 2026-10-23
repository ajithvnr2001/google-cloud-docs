---
url: https://docs.cloud.google.com/armor/docs/rules-language-reference/
title: Configure custom rules language attributes \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:58.539190+00:00
---

# Configure custom rules language attributes  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/rules-language-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Guides ](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)



Send feedback 

#  Configure custom rules language attributes Stay organized with collections  Save and categorize content based on your preferences. 

Each Google Cloud Armor security policy rule has a priority, a match condition, and an action. Cloud Armor performs the action of the highest priority rule that matches a request. Rules with a lower priority than the highest priority matching rule are not evaluated, even if they have the same match conditions.

Each security policy rule supports two types of match conditions:

  * A _basic match condition_ contains lists of IP addresses or lists of IP address ranges. Basic match conditions are defined by using the `--src-ip-ranges` flag when creating a rule using the Google Cloud CLI.
  * An _advanced match condition_ contains an expression with up to five subexpressions that can match a variety of attributes of an incoming request. Advanced match conditions are defined using the `--expression` flag when creating a rule using the Google Cloud CLI.



This page discusses advanced match conditions and the Cloud Armor _custom rules language_ that you use to write expressions in the advanced match conditions of security policy rules. The Cloud Armor custom rules language is a subset of the [Common Expression Language (CEL)](https://github.com/google/cel-spec).

Expressions written in the Cloud Armor custom rules language require two components:

  * The _attribute_ : the data to inspect
  * The _operation_ : how to use the data



For example, the following expression uses the attributes `origin.ip` and `198.51.100.0/24` in the operation `inIpRange`. In this case, the expression returns `true` if `origin.ip` is within the `198.51.100.0/24` IP address range.
    
    
    inIpRange(origin.ip, '198.51.100.0/24')
    

Even though the previous example expression only matches on client IP address, when you use the example expression in a Cloud Armor security policy rule, the rule is considered a rule _with advanced match conditions_ from a quota perspective. For more information, see [Cloud Armor quotas and limits](https://docs.cloud.google.com/armor/quotas).

## Operations

The following reference describes the operators that you can use with attributes (represented by `x`, `y`, and `k`) to define rule expressions.

Operations | Expressions | Description  
---|---|---  
Equality | `x == y` | Returns `true` if _x_ is equal to _y_.  
Equality, string literal | `x == "foo"` | Returns `true` if _x_ is equal to the given constant string literal.  
Equality, raw string literal | `x == R"fo'o"` | Returns `true` if _x_ is equal to the given raw string literal that does not interpret escape sequences. Raw string literals are convenient for expressing strings that themselves must use escape sequence characters.   
Logical NOT | `!x` | Returns `true` if the Boolean value _x_ is `false`, or returns `false` if the Boolean value _x_ is `true`.  
Inequality | `x != y` | Returns `true` if _x_ is not equal to _y_.  
Concatenation | `x + y` | Returns the concatenated string _xy_.  
Logical AND | `x && y` | Returns `true` if both _x_ and _y_ are `true`.  
Logical OR | `x || y` | Returns `true` if _x_ , _y_ , or both are `true`.  
Contains substring | `x.contains(y)` | Returns `true` if the string _x_ contains the substring _y_.  
Starts with substring | `x.startsWith(y)` | Returns `true` if the string _x_ begins with the substring _y_.  
Ends with substring | `x.endsWith(y)` | Returns `true` if the string _x_ ends with the substring _y_.  
Regular expression match | `x.matches(y)` | Returns `true` if the string _x_ is partially matched by the specified [RE2](https://www.wikipedia.org/wiki/RE2_\(software\)) pattern _y_. The RE2 pattern is compiled by using the RE2::Latin1 option that disables Unicode features.  
IP address within range | `inIpRange(x, y)` | Returns `true` if the IP address _x_ is contained within the IP range _y_.  
Lowercase | `x.lower()` | Returns the lowercase value of the string _x_.  
Uppercase | `x.upper()` | Returns the uppercase value of the string _x_.  
Base64 decoded value | `x.base64Decode()` | Returns the base64 decoded value of _x_ ; the underscore (`_`) and hyphen (`-`) are first replaced with forward slash (`/`) and plus sign (`+`) respectively. Returns `""` (empty string) if _x_ is not a valid base64 value.  
Key-map value | `m['k']` | Returns the value at key _k_ in the string-to-string map _m_ if _k_ is available; otherwise, returns an error. Recommended approach is to first check for availability by using `"has(m['k'])==true"`.  
Check key availability in a map | `has(m['k'])` | Returns `true` if key _k_ is available in the map _m_.  
Convert to integer | `int(x)` | Converts the string result of _x_ to an `int` type. It can then be used to do an integer comparison by using standard arithmetic operators such as > and <=. This works only for values that are supposed to be integers.  
Length | `size(x)` | Returns the length of string _x_.  
Decode URL | `x.urlDecode()` | Returns the url-decoded value of _x_ ; character sequences in `%##` format are replaced with the non-ASCII equivalents, and `+` is replaced with a space. Invalid encodings are returned as-is.  
Decode URL (Unicode) | `x.urlDecodeUni()` | Returns the url-decoded value of _x_ ; in addition to `urlDecode()`, this also handles unicode character sequences in `%u###` format. Invalid encodings are returned as-is.  
Convert utf8 to Unicode | `x.utf8ToUnicode()` | Returns the _lowercase_ Unicode representation of a UTF-8 encoded _x_.  
Exists | `m.exists(k, expr)` | Returns `true` if at least one entry in the map m satisfies expr, where k represents the key of each map entry. **Note:** This operator only works when `request.body` or `request.params` exists in the rule expression.  
Exists one | `m.exists_one(k, expr)` | Returns `true` if exactly one entry in the map m satisfies expr, where k represents the key of each map entry. **Note:** This operator only works when `request.body` or `request.params` exists in the rule expression.  
All | `m.all(k, expr)` | Returns `true` if all entries in the map m satisfy expr, where k represents the key of each map entry. **Note:** This operator only works when `request.body` or `request.params` exists in the rule expression.  
Filter | `m.filter(k, expr)` | Returns a map containing only the entries from map m where the entry satisfies expr, where k represents the key of each map entry. **Note:** This operator only works when `request.body` or `request.params` exists in the rule expression.  
Map | `m.map(k, expr)` | Returns a list containing the result of evaluating expr for each key in map m, where k represents the key of each map entry. **Note:** This operator only works when `request.body` or `request.params` exists in the rule expression.  
**Note:** The precedence for CEL logical operators is `NOT`, `AND`, and `OR`. You can use parentheses to override this order. For more information, see [Syntax](https://github.com/google/cel-spec/blob/master/doc/langdef.md#syntax).**Note:** The map-iteration operators (`m.exists`, `m.exists_one`, `m.all`, `m.filter`, and `m.map`) only work when `request.body` or `request.params` exist in the rule expression.

## Attributes

Attributes represent information from an incoming request, such as the client IP address or the requested URL path.

Field | Type | Field description  
---|---|---  
`origin.ip` | string | The IP address of the client that initiated the request.  
`origin.user_ip` | string | The IP address of the originating client, which is included in the `HTTP-HEADER` by an upstream proxy. Before you use this attribute, you must configure the `userIpRequestHeaders[]` option in the security policy's `advancedOptionsConfig` field to match a source like `True-Client-IP`, `X-Forwarded-For`, or `X-Real-IP`. For more information, see [User IP addresses overview](https://docs.cloud.google.com/armor/docs/user-ip-overview). If you don't configure the `userIpRequestHeaders[]` option, if the configured header contains invalid IP address values, or if the configured header is not present, `origin.user_ip` defaults to `origin.ip`. For more information, see the [securityPolicy](https://docs.cloud.google.com/compute/docs/reference/rest/beta/securityPolicies) resource reference.  
`origin.tls_ja4_fingerprint` | string | [JA4 TLS/SSL fingerprint](https://github.com/FoxIO-LLC/ja4) if the client connects using `HTTPS`, `HTTP/2`, or `HTTP/3`. If not available, an empty string is returned.  
`origin.tls_ja3_fingerprint` | string | [JA3 TLS/SSL fingerprint](https://github.com/salesforce/ja3) if the client connects using `HTTPS`, `HTTP/2`, or `HTTP/3`. If not available, an empty string is returned.  
`request.headers` | map | A string-to-string map of the HTTP request headers. If a header has multiple values, the corresponding value in this map is a single string that contains all of the values, separated by commas. The keys in this map are all _lowercase_. The external Application Load Balancers inspect all accepted headers, and the same header [limitations](https://docs.cloud.google.com/load-balancing/docs/quotas#https-lb-header-limits) apply.Use `has()` to check for availability, such as `has(request.headers['header-key']) && request.headers['header-key'] != 'header-value'`. You can iterate over the map to check both keys and values. However, you can only use map-iteration operators (`exists()`, `exists_one()`, `all()`, `filter()`, and `map()`) on `request.headers` in combination with `request.body` or `request.params` in the same expression—for example, `request.body && request.headers.exists(k, k.lower().startsWith('header-prefix'))`.  
`request.body` | string | Represents the request body as a raw string. It can represent data of any `Content-Type`. It stores the content as a string without any automatic parsing.   
`request.params` | map | A map of key-value pairs that are appended to the URL or included in the body of requests.  
URI request: `name1=value1&name2=value2`  
JSON request body with `Content-Type: application/json`:  
`{ "username": "johndoe", "email": "johndoe@example.com" }`  
GraphQL POST request body with `Content-Type: application/graphql`:  
`{ Username: "exampleUser", query: "/* other fields */" }`  
Form POST request body with `Content-Type: application/x-www-form-urlencoded`:  
`"username=exampleUser&email=johndoe%40example.com"`  
`request.method` | string | The HTTP request method.  
`request.path` | string | The requested HTTP URL path. When you write rules that match on `request.path`, we recommend that you normalize the path to facilitate matching syntax in case of URL encoding, case variations, or backslashes. For more information and examples, see [Path traversal and normalization](https://docs.cloud.google.com/armor/docs/configure-security-policies#path-traversal-and-normalization).  
`request.scheme` | string | The HTTP URL scheme such as `http` or `https`. Values for this attribute are all _lowercase_.  
`request.query` | string | The HTTP URL query in the format of `name1=value&name2=value2`, as it appears in the first line of the HTTP request. No decoding is performed.   
`origin.region_code` | string | The Unicode country code that is associated with the client IP, such as `US`. If you're creating a rule or expression that uses [ISO 3166-1 alpha 2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) country or region codes, Cloud Armor treats each code independently. Cloud Armor rules and expressions explicitly use those region codes to allow or deny requests.   
`origin.asn` | integer | The autonomous system number (ASN) that is associated with the client IP address. The globally unique ASN is determined based on the network operator supporting the IP address prefixes that contain the client IP address.   
**Note:** Edge security policies support filtering based on only `origin.asn`, `origin.ip`, `origin.region_code`, `request.headers`,`request.method`,`request.path`, `request.query`, and `request.scheme`.

### reCAPTCHA attributes

This section lists attributes that are only applicable to reCAPTCHA tokens or exemption cookies. A subexpression based on these attributes returns `false` if the reCAPTCHA token or exemption cookie to be evaluated is not available or is invalid for one of the following reasons:

  * The token is malformed and cannot be decoded.
  * The token contains invalid attributes. For example, the token was generated using a reCAPTCHA key that does not match the rule's associated reCAPTCHA keys.
  * The token is expired.



#### Exemption cookie attributes

Field | Type | Field description  
---|---|---  
`token.recaptcha_exemption.valid` | `bool` | The presence of a valid reCAPTCHA exemption cookie.  
  
#### Action-token attributes

Field | Type | Field description  
---|---|---  
`token.recaptcha_action.score` | `float` | The score from a reCAPTCHA action-token. A valid score ranges from `0.0` to `1.0`, with `0.0` being very likely an illegitimate user, and `1.0` being very likely a legitimate user.  
`token.recaptcha_action.captcha_status` | `string` | The captcha status from a reCAPTCHA action-token. A valid status is `NONE`, `PASS`, or `FAIL`, where `NONE` refers to when there are no challenges involved during reCAPTCHA assessment, such that the captcha field is missing in the action-token.  
`token.recaptcha_action.action` | `string` | The action name (up to 100 characters) from a reCAPTCHA action-token. See [Action names](https://docs.cloud.google.com/recaptcha/docs/actions-website).  
`token.recaptcha_action.valid` | `bool` | The presence of a valid reCAPTCHA action-token.  
  
#### Session-token attributes

Field | Type | Field description  
---|---|---  
`token.recaptcha_session.score` | `float` | The score from a reCAPTCHA session-token. A valid score ranges from `0.0` to `1.0`, with `0.0` being very likely an illegitimate user, and `1.0` being very likely a legitimate user.  
`token.recaptcha_session.valid` | `bool` | The presence of a valid reCAPTCHA session-token.  
  
## Example expressions

For each of these expressions, the action taken depends on whether the expression is included in a deny rule or an allow rule.

### Allow or deny access based on an IP address range in IPv4 or IPv6

  * The following expression matches with requests from the `198.51.100.0/24` IP address range:
        
        inIpRange(origin.ip, '198.51.100.0/24')
        

  * The following expression matches with requests from the `2001:db8::/32` IP address range:
        
        inIpRange(origin.ip, '2001:db8::/32')
        




### Allow or deny access based on a custom client IP address range behind an upstream proxy

If you have configured the `origin.user_ip` operator, you can match based on the header values that you specified in your `advancedOptionsConfig.userIpRequestHeaders[]` field.

  * The following expression matches with requests that originated from the `192.0.2.0/24` IP address range:
        
        inIpRange(origin.user_ip, '192.0.2.0/24')
        

  * The following expression matches with requests that originated from the `2001:db8::/32` IP address range:
        
        inIpRange(origin.user_ip, '2001:db8::/32')
        




### Allow or deny traffic with a specific cookie

  * The following expression matches with requests that have a cookie containing `80=BLAH`:
        
        has(request.headers['cookie']) && request.headers['cookie'].contains('80=BLAH')
        




### Allow or deny traffic with a non-empty `referer` header

  * The following expression matches with requests that have a non-empty `referer` header:
        
        has(request.headers['referer']) && request.headers['referer'] != ""
        




### Allow or deny traffic based on host header

You can allow or deny traffic based on the value of the `Host` header in the request.

  * The following expression matches with requests to a specific URL using `==`:
        
        request.headers['host'].lower() == 'test.example.com'
        

  * The following expression matches with requests to a specific URL using `endsWith`:
        
        request.headers['host'].lower().endsWith('.example.com')
        

  * The following expression matches with requests to a specific URL using `contains`:
        
        request.headers['host'].lower().contains('test.example.com')
        


**Note:** Use `==` when you want to match to a specific host exactly and `contains` where the host contains a specific substring. Use `contains` with caution, as it can lead to unintended matches. For more information, see Operations.

  * The following expression matches with requests to multiple domains using `contains`:
        
        request.headers['host'].lower().contains('test.example.com') || request.headers['host'].lower().contains('test22.example.com')
        

  * The following expression matches requests for a domain and its subdomains using `matches`:
        
        request.headers['host'].matches('(?i:(sub\.)?test\.example\.com)')
        




### Allow or deny traffic from a specific region

If your web application isn't available in the `AU` region, then all requests from that region must be blocked.

  * In a deny rule, use the following expression, which matches requests from the `AU` region:
        
        origin.region_code == 'AU'
        




Alternatively, if your web application is _only_ available in the `AU` region, then requests from all other regions must be blocked.

  * In a deny rule, use the following expression, which matches requests from all regions other than the `AU` region:
        
        origin.region_code != 'AU'
        




The region codes are based on the [ISO 3166-1 alpha 2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) codes. In some cases, a region corresponds to a country, but this is not always the case. For example, the `US` code includes all states of the United States, one district, and six outlying areas.

### Allow or deny traffic from a specific ASN

If your web application needs to be blocked to customers serviced by a specific network operator, you can use the ASN number of the network operator to block.

  * In a deny rule, use the following expression, which matches requests from a specific ASN:
        
        origin.asn == 123
        




Alternatively, if your web application is to be _only_ available to customers behind a specific network operator, then requests from all other network operators must be blocked.

  * In a deny rule, use the following expression, which matches all other network operators other than the one that you are interested in allowing:
        
        origin.asn != 123
        




### Multiple expressions

To include multiple conditions in a single rule, combine multiple subexpressions.

  * In the following example, requests from `1.2.3.0/24` (such as your alpha testers) in the `AU` region match the following expression:
        
        origin.region_code == "AU" && inIpRange(origin.ip, '1.2.3.0/24')
        

  * The following expression matches requests from `1.2.3.4` where a user agent contains the string `WordPress`:
        
        inIpRange(origin.ip, '1.2.3.4/32') &&
        has(request.headers['user-agent']) && request.headers['user-agent'].contains('WordPress')
        




### Allow or deny traffic for a request URI that matches a regular expression

  * The following expression matches with requests that contain the string `/example_path/` in the URI:
        
        request.path.matches('/example_path/')
        

  * The following expression matches with requests that have `Chrome` in the `User-Agent` header field:
        
        request.headers['user-agent'].matches('Chrome')
        

  * The following expression shows case-insensitive matching for the `User-Agent` header containing `wordpress`; it matches with `User-Agent:WordPress/605.1.15`, `User-Agent:wordPress`, and other variations of `wordpress`:
        
        request.headers['user-agent'].matches('(?i:wordpress)')
        




### Allow or deny traffic that contains a specific base64 decoded value

  * The following expression matches with requests that have a base64 decoded value of `myValue` for the `user-id` header:
        
        has(request.headers['user-id']) && request.headers['user-id'].base64Decode().contains('myValue')
        




### Allow or deny traffic that contains a string value of a specific length

  * The following expression matches requests that have a URL length greater than 10 characters:
        
        size(request.path) > 10
        

  * The following expression matches requests that have a header `x-data` length greater than or equal to 1024 characters:
        
        size(request.headers['x-data']) >= 1024
        




### Allow or deny traffic that has zero `content-length` in the HTTP body

  * The following expression matches requests that have a zero `content-length` in the HTTP body:
        
        int(request.headers["content-length"]) == 0
        




### Allow or deny traffic that contains a specific URL encoded value

  * The following expression matches with requests that have a cookie value containing `%3c`:
        
        has(request.headers['cookie']) && request.headers['cookie'].urlDecode().contains('<')
        




### Allow or deny traffic that contains a specific URL encoded value of a Unicode string

  * The following expression matches with requests that have a cookie value equal to `Match%2BValue` or `Match%u002BValue`:
        
        has(request.headers['cookie']) && request.headers['cookie'].urlDecodeUni() == 'Match+Value'
        




### Allow or deny traffic that contains a specific Unicode string of a UTF-8 text

  * The following expression matches with requests that have a cookie value equal to `¬`:
        
        has(request.headers['cookie']) && request.headers['cookie'].utf8ToUnicode() == '%u00ac'
        




### Allow or deny traffic based on a known JA4 fingerprint

  * The following expression matches with requests that have a JA4 fingerprint equal to `t13d1516h2_8daaf6152771_b186095e22b6`:
        
        origin.tls_ja4_fingerprint == 't13d1516h2_8daaf6152771_b186095e22b6'
        




### Allow or deny traffic based on a list of JA4 fingerprints

  * The following expression matches with requests that have a JA4 fingerprint equal to any of the following JA4 fingerprints:

    * `t00d0000h0_000000000000_000000000000`
    * `t13d1516h2_8daaf6152771_b186095e22b6`
    
    origin.tls_ja4_fingerprint == 't00d0000h0_000000000000_000000000000' || origin.tls_ja4_fingerprint == 't13d1516h2_8daaf6152771_b186095e22b6'
    




### Allow or deny traffic based on the request body content

  * The following expression matches POST requests that contain `malicious-value` in the request body:
        
        request.method == 'POST' && request.body.contains('malicious-value')
        

  * The following expression matches requests that start with `<!DOCTYPE html>`:
        
        request.body.startsWith('<!DOCTYPE html>')
        

  * The following expression matches requests where the body matches the regular expression `\w+@\w+.com`:
        
        request.body.matches('\w+@\w+.com')
        




### Allow or deny traffic based on request parameters

  * The following expression matches requests that don't contain a parameter named `category`:
        
        !has(request.params.category)
        

  * The following expression matches requests where the `category` parameter is `electronics`:
        
        request.params.category == 'electronics'
        

  * The following expression matches requests where all parameter values are non-empty:
        
        request.params.all(k, request.params[k] != '')
        

  * The following expression matches requests where any parameter contains the string `admin`:
        
        request.params.exists(k, request.params[k].contains('admin'))
        

  * The following expression matches requests where exactly one parameter name contains `admin`:
        
        request.params.exists_one(k, k.contains('admin'))
        

  * The following expression matches requests where at least one parameter name contains `id`:
        
        size(request.params.filter(k, k.contains('id'))) > 0
        

  * The following expression matches requests where the parameter values include the string `admin`:
        
        request.params.map(k, request.params[k]).contains('admin')
        




### Allow or deny traffic based on structured data in the request body

  * The following expression matches requests where the `password` field in a JSON request body contains `123`:
        
        has(request.params.password) && request.params.password.contains('123')
        

  * The following expression matches requests where the `city` field in form data is `NewYork`:
        
        has(request.params.city) && request.params.city == 'NewYork'
        

  * The following expression matches requests where the nested `newsletter` field is `true`:
        
        has(request.params.preferences) && has(request.params.preferences.newsletter) && request.params.preferences.newsletter == true
        

  * The following expression matches requests where the `name` field of the first element in the `friends` array is `johndoe`:
        
        request.params['friends'][0]['name'] == 'johndoe'
        




## Preconfigured WAF rules

Preconfigured WAF rules use preconfigured static signatures, regular expressions, or both to match on the HTTP request body, HTTP request headers, and query parameters. The available preconfigured WAF rules are based on the [OWASP Core Rule Set 4.22](https://github.com/coreruleset/coreruleset/releases/tag/v4.22.0). Cloud Armor provides several predefined preconfigured WAF rules. For a complete list of preconfigured WAF rules, see the [Cloud Armor preconfigured WAF rules overview](https://docs.cloud.google.com/armor/docs/waf-rules).

To list all of the available preconfigured WAF rules, see [List available preconfigured WAF rules](https://docs.cloud.google.com/armor/docs/manage-security-policies#list-preconfig-rules).

For more information about preconfigured WAF rules, see the use case [Mitigate application layer attacks by using preconfigured WAF rules](https://docs.cloud.google.com/armor/docs/common-use-cases#protect_your_deployment_against_application_layer_attacks_and_help_mitigate_owasp_top_10_risks).

### Preconfigured WAF rule names

Preconfigured WAF rule names have the format `<attack category>-<OWASP CRS version>-<version field>`. The attack category specifies the type of attacks that you want to protect against, such as `xss` (cross-site scripting) or `sqli` (SQL injection).

The supported version fields are `stable` and `canary`. Additions and modifications to the rules are released in the `canary` version first. When additions and modifications are considered safe and stable, they are promoted to the `stable` version.

### Preconfigured WAF rule member IDs

A preconfigured WAF rule contains several expressions, each with its signature. For example, the preconfigured WAF rule `xss-v422-stable` includes an expression called `owasp-crs-v042200-id941100-xss`, which corresponds to rule ID `id941100` for version 4.22. You can use the signatures to exclude specific expressions from being used, which is useful if a particular expression consistently triggers a false positive. For more information, see the [false positives](https://docs.cloud.google.com/armor/docs/troubleshooting#false-positives) troubleshooting information.

For information about the core rule set and tuning at different sensitivity levels, see [Tuning Cloud Armor WAF rules](https://docs.cloud.google.com/armor/docs/rule-tuning).

### Operator for preconfigured WAF rules

Expressions | Description  
---|---  
`evaluatePreconfiguredWaf(string, MAP<string, dyn>)` | Returns `true` if any one of the WAF signatures inside the specified WAF rule set returns `true`. The first argument is the name of the WAF rule set, such as `xss-v422-stable`. The second argument (optional) is a map in which the key is a string and the value is dynamically typed depending on the key. The purpose of this argument is to fine tune which WAF signatures are evaluated. Accepted keys include the following: 

  * `sensitivity`: this corresponds to the OWASP Core Rule Set paranoia level, which has 4 levels, ranging from 1 to 4. Its value is an integer with a valid range from 0 to 4. Note that 0 is reserved as a valid value when used in combination with `opt_in_rule_ids` (described later). When specifying a sensitivity of x (x >= 1), all the associated WAF signatures with a sensitivity value from 1 to x are evaluated. When omitted, 4 is used as the sensitivity value.
  * `opt_out_rule_ids`: WAF signatures (represented by rule IDs) to be opted out from evaluation, where the base set is determined by the sensitivity value. Its value is a list of strings. The maximum number of rule IDs allowed is `128`.
  * `opt_in_rule_ids`: WAF signatures (represented by rule IDs) to be opted in for evaluation, where the base set is empty. Its value is a list of strings. The maximum number of rule IDs allowed is `128`. When using this, a `sensitivity` of `0` must be specified. 

The keys `opt_out_rule_ids` and `opt_in_rule_ids` are mutually exclusive. You can choose to use `opt_in_rule_ids` if you want to review and manually opt in new WAF signatures that are added later into an existing rule set.  
`evaluateManagedRules(string, MAP<string, dyn>)` | Returns `true` if any one of the signatures inside the specified managed rules returns `true`. The first argument is the fully qualified name of the category, such as `google:xss:stable` or `google:sqli:canary`. The second argument (optional) is a map where the key is a string and the value is dynamically typed depending on the key. Accepted keys include the following: 

  * `opt_in_rule_ids`: a list of rule IDs from the corresponding rule set that are the only rules evaluated. For example, `evaluateManagedRules('google:xss:canary', {'opt_in_rule_ids': ['google-xss-8057544707029182464']})`.
  * `opt_out_rule_ids`: a list of rule IDs from the corresponding rule set that are excluded from the evaluation. For example, `evaluateManagedRules('google:xss:canary', {'opt_out_rule_ids': ['google-xss-8057544707029182464']})`.

  
`evaluatePreconfiguredWaf(string, LIST)` | **Caution:** `evaluatePreconfiguredExpr()` is deprecated. We recommend that you use `evaluatePreconfiguredWaf()` instead.Returns `true` if any one of the expressions inside the specified preconfigured WAF rule returns `true`. The first argument is the name of the preconfigured WAF rule, such as `xss-stable`. The second argument (optional) is a comma-separated string list of IDs that must be excluded from evaluation. The exclusion list is useful when a given member of the preconfigured WAF rule triggers a false positive.  
  
### Preconfigured WAF rule examples

  * The following expression uses the `xss-v422-stable` preconfigured WAF rule to mitigate XSS attacks:
        
        evaluatePreconfiguredWaf('xss-v422-stable')
        

  * The following expression uses all the expressions from the `xss-v422-stable` preconfigured WAF rule except for member IDs `941100` and `941110`:
        
        evaluatePreconfiguredWaf('xss-v422-stable', {'opt_out_rule_ids': ['owasp-crs-v042200-id941100-xss',
        'owasp-crs-v042200-id941110-xss']})
        

  * The following expression uses a preconfigured WAF rule to mitigate SQLi attacks from the `198.51.100.0/24` IP address range:
        
        inIpRange(origin.ip, '198.51.100.0/24') && evaluatePreconfiguredWaf('sqli-v422-stable')
        

  * The following expression uses the `xss-v422-stable` preconfigured WAF rule to mitigate XSS attacks for requests to `example.com`, excluding paths that start with `/login/api/`:
        
        request.headers['host'].lower() == 'example.com' && !request.path.startswith('/login/api/') && evaluatePreconfiguredWaf('xss-v422-stable')
        




### Managed rules examples

  * The following expression uses the stable SQL injection (`sqli`) managed rules to help prevent SQLi attacks:
        
        evaluateManagedRules('google:sqli:stable')
        

  * The following expression uses the stable `xss` managed rules only if the request has the host `example.com`:
        
        request.headers['host'].lower() == 'example.com' && evaluateManagedRules('google:xss:stable')
        




## Other operators

Expressions | Description  
---|---  
`evaluateThreatIntelligence(string)`  
`evaluateThreatIntelligence(string, LIST)`  
`evaluateThreatIntelligence(string, string, LIST)` |  Returns `true` if the client IP address matches any of the IP ranges in the given IP list, unless explicitly excluded with the exclusion list. The first argument is the Google Threat Intelligence feed name, such as `iplist-known-malicious-ips`. If the second argument is a string (optional), it determines where the IP address is extracted from, and it can be either `origin.ip`, `origin.user_ip` or a specific header name. If the second or third argument (optional) is a comma-separated list of strings, where each string is an IP address or CIDR range, that will be excluded from evaluation. The exclusion list is useful when a feed contains some IP address that triggers a false positive. **Note:** You have to configure the `userIpRequestHeaders[]` option in the security policy's `advancedOptionsConfig` field when using `origin.user_ip`.  
`evaluateAddressGroup(string, string)`  
`evaluateAddressGroup(string, string, LIST)`  
  
`evaluateOrganizationAddressGroup(string, string)`  
`evaluateOrganizationAddressGroup(string, string, LIST)` |  Returns `true` if the client IP address matches any of the IP ranges in the given address group, unless explicitly excluded with the exclusion list. The first argument is the address group name. The second argument determines where the IP address is extracted from, and it can be either `origin.ip`, `origin.user_ip` or a specific header name. The third argument (optional) is a comma-separated list of strings, where each string is an IP address or CIDR range, that will be excluded from evaluation. The exclusion list is useful when an address group contains some IP address that triggers a false positive. **Note:** You have to configure the `userIpRequestHeaders[]` option in the security policy's `advancedOptionsConfig` field when using `origin.user_ip`.  
`evaluateAdaptiveProtection(string)`  
|  Returns `true` if the request matches the attack signature produced by Google Cloud Armor Adaptive Protection. The argument is the ID of a specific alert generated by Adaptive Protection upon detecting an attack.  
`evaluateAdaptiveProtectionAutoDeploy()`  
|  Returns `true` if the request is from a heavy hitter IP address that matches the attack signature of an ongoing attack detected by Adaptive Protection.  
  
### Examples

  * The following expression matches the incoming request against the Google Threat Intelligence `iplist-known-malicious-ips` feed for protection from the known list of malicious IPs:
        
        evaluateThreatIntelligence('iplist-known-malicious-ips')
        

  * The following expression matches the incoming request against the Google Threat Intelligence `iplist-known-malicious-ips` feed for protection from the known list of malicious IPs except for IPs in `203.0.113.0/24`:
        
        evaluateThreatIntelligence('iplist-known-malicious-ips', ['203.0.113.0/24'])
        

  * The following expression matches the custom request header for user IP against the address group named `my-own-list-of-bad-ips`:
        
        evaluateAddressGroup('my-own-list-of-bad-ips', origin.user_ip)
        




## What's next

  * [Create and view Cloud Armor security policies](https://docs.cloud.google.com/armor/docs/configure-security-policies)
  * [Tune Cloud Armor preconfigured WAF rules](https://docs.cloud.google.com/armor/docs/rule-tuning)
  * [Troubleshoot Cloud Armor issues](https://docs.cloud.google.com/armor/docs/troubleshooting)
  * [Quotas and limit](https://docs.cloud.google.com/armor/quotas)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
