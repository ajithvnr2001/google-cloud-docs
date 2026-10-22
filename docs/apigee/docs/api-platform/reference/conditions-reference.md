---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/conditions-reference/
title: Conditions reference \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:36:09.509649+00:00
---

# Conditions reference  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/conditions-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Conditions reference Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Conditions enable API proxies to behave dynamically at runtime. Conditions define operations on variables, which are evaluated by the Apigee processing pipeline. Conditional statements are boolean and always evaluate to `true` or `false`.

## Conditions overview

This section describes how and where to use conditional statements with Apigee. In addition, the following sections describe the syntax:

  * Operators
  * Operands
  * Literals

**Tip:** For a tutorial-like topic that explains how to use pattern matching in conditional statements, see [Pattern matching with conditionals](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-variables-and-conditions#patternmatching).

### Structure of conditional statements

The basic structure of a conditional statement is:
    
    
    <Condition>variable.name operator "value"</Condition>

For example:
    
    
    <Condition>request.verb = "GET"</Condition>

You can combine conditions with `AND` to enforce more than one at a time. For example, the following conditions evaluate to `true` only if the URI of the request matches `/statuses` _and_ the HTTP verb of the request is `GET`:
    
    
    <Condition>(proxy.pathsuffix MatchesPath "/statuses") and (request.verb = "GET")</Condition>

### Where you can use conditional statements

You can use conditions to control behavior in the following:

  * Policy execution
  * Flow execution
  * Target endpoint route selection



#### Policy execution

Using conditional statements, you can control the enforcement of policies. A common use case is conditional transformation of response messages, based on HTTP header or message content.

The following example conditionally transforms XML to JSON based on the `Accept` header:
    
    
    <Step>
      <Condition>request.header.accept = "application/json"</Condition>
      <Name>XMLToJSON</Name>
    </Step>

#### Flow execution

Using conditional statements, you can control the execution of named flows in ` ProxyEndpoints` and `TargetEndpoints`. Note that only _named_ flows can be executed conditionally. Preflows and postflows (both request and response) on `ProxyEndpoints` and `TargetEndpoints` execute for every transaction, and thus provide unconditional _failsafe_ capabilities.

For example, to execute a conditional request flow based on the HTTP verb of the request message, and conditional response flow based on a (potential) HTTP status code representing an error:
    
    
    <Flow name="GetRequests">
      <Condition>request.verb = "GET"</Condition>
      <Request>
        <Step>
          <Condition>request.path MatchesPath "/statuses/**"</Condition>
          <Name>StatusesRequestPolicy</Name>
        </Step>
      </Request>
      <Response>
        <Step>
          <Condition>(response.status.code = 503) or (response.status.code = 400)</Condition>
          <Name>MaintenancePolicy</Name>
        </Step>
      </Response>
    </Flow>

#### Target endpoint route selection

Using conditional statements, you can control the target endpoint invoked by proxy endpoint configuration. A route rule forwards a request to a particular target endpoint. When more than one target endpoint is available, the route rule is evaluated for its condition and, if true, the request is forwarded to the named target endpoint.

For example, to conditionally route messages to designated target endpoints based on `Content-Type`:
    
    
    <RouteRule name="default">
     <!--this routing executes if the header indicates that this is an XML call. If true, the call is routed to the endpoint XMLTargetEndpoint-->
      <Condition>request.header.Content-Type = "text/xml"</Condition>
      <TargetEndpoint>XmlTargetEndpoint</TargetEndpoint>
    </RouteRule>

See [Flow variables and conditions](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-variables-and-conditions) for more information.

### Path expressions

Path expressions are used for matching URI paths, using `*` to represent a single path element and `**` to represent multiple URI levels. Curly braces `{name}` can also be used to match a single path element and provide clarity to the reader. The variable `name` is only only used for clarity and does not populate the matched value in a flow variable.

For example:

Pattern | Sample URI paths matched  
---|---  
`/*/a/` | `/x/a/` or `/y/a/`  
`/*/a/*` | `/x/a/b` or `/y/a/foo`  
`/*/a/**` | `/x/a/b/c/d`  
`/*/a/{reader}/feed/` | `/x/a/b/feed/` or `/y/a/foo/feed/`  
`/a/**/feed/**` | `/a/b/feed/rss/1234`  
  
`%` is treated as an escape character. The pattern` %{user%}` matches `{user}` but not `user`.

### Variables

You can use both built-in flow variables and custom variables in conditional statements. For more information, see:

  * [Flow variables reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference): A complete list of the built-in variables
  * [ExtractVariables policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/extract-variables-policy): Instructions on setting custom variables



## Operators

When using operators, observe the following restrictions:

  * Operators cannot be used as variable names.
  * A space character is required before and after an operator.
  * To include an operator in a variable, a variable name must be enclosed in single quotes. For example, `'request.header.help!me'`.
  * Arithmetic operators (`+ * - / %`) are not supported.
  * [Java precedence](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/operators.html) is used for operators.
  * Apigee relies on regular expressions as implemented in `java.util.regex`.



The following table lists the supported operators. You can use the symbol or the word in your expressions:

Symbol | Word | Description  
---|---|---  
`!` | `Not`, `not` | Unary operator (takes a single input)  
`=` | `Equals`, `Is` | Equals to (case sensitive)  
`!=` | `NotEquals`, `IsNot` | Not equals (case sensitive)  
`:=` | `EqualsCaseInsensitive` | Equals but is case insensitive  
`>` or `&gt;` | `GreaterThan` | Greater than. If you use > when defining the condition in the Apigee UI, it is converted to &gt;.  
`>=` or `&gt;=` | `GreaterThanOrEquals` | Greater than or equal to. If you use >= when defining the condition in the Apigee UI, it is converted to &gt;=.  
`&lt;` | `LesserThan` | Lesser than. The Apigee UI does not support the literal <.  
`&lt;=` | `LesserThanOrEquals` | Lesser than or equal to. The Apigee UI does not support the literal <=.  
`&&` | `And`, `and` | And  
`||` | `Or` | The Or operator is not case sensitive. For example, `OR`, `Or`, and `or` are all valid.  
`()` |  | Groups an expression. The `(` opens the expression and `)` closes it.  
`~~` | `JavaRegex` |  Matches a `javax.util.regex` compliant regular expression. The match is case-sensitive. For examples, see [ Pattern matching](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-variables-and-conditions#patternmatching).  
`~` | `Matches`, `Like` | Matches a glob-style pattern using the `*` wildcard character. The match is case-sensitive. For examples, see [ Pattern matching](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-variables-and-conditions#patternmatching).  
`~/` | `MatchesPath`, `LikePath` | Matches a path expression. The match is case-sensitive. For examples, see [ Pattern matching](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-variables-and-conditions#patternmatching).  
`=|` | `StartsWith` | Matches the first characters of a string. The match is case-sensitive.  
  
## Operands

Apigee adapts operands to a common data type before comparing them. For example, if the response status code is `404`, the expression `response.status.code = "400"` and the `response.status.code = 400` are equivalent.

For numeric operands, the data type is interpreted as integer unless the value is terminated as follows:

  * `f` or `F` (`float`, for example, `3.142f, 91.1F`)
  * `d` or `D` (`double`, for example, `3.142d, 100.123D`)
  * `l` or `L` (`long`, for example, `12321421312L`)



In these cases, the system performs adaptations shown in the following table (where RHS refers to the right side of the equation and LHS is the left side):

RHS LHS | Boolean | Integer | Long | Float | Double | String | Comparable | Object  
---|---|---|---|---|---|---|---|---  
Boolean | Boolean | Integer | Long | Float | Double | String |  | -  
Integer | Integer | Integer | Long | Float | Double | String | Comparable | -  
Long | Long | Long | Long | Float | Double | String | Comparable | -  
Float | Float | Float | Float | Float | Double | String | Comparable | -  
Double | Double | Double | Double | Double | Double | String | Comparable | -  
String | String | String | String | String | String | String | Comparable | -  
Comparable | Comparable | Comparable | Comparable | Comparable | Comparable | Comparable | Comparable | -  
Object | - | - | - | - | - | - | - | -  
**Note:** The dash character ( - ) in this table implies that the comparison is not performed, so the result of the comparison is `false`.

### Null operands

The following table shows whether conditions evaluate to `true` or `false` when values are null on the left-hand side (LHS) and/or right-hand side (RHS) of the operand shown:

Operator | LHS null | RHS null | LHS and RHS null  
---|---|---|---  
`=`, `==`, `:=` | false | false | true  
`=|` | false | false | false  
`!=` | true | true | false  
`>` or `&gt;` | true | false | false  
`>=` or `&gt;=` | false | true | true  
`&lt;` | true | false | false  
`&lt;=` | true | false | true  
`~` | false | N/A | false  
`~~` | false | N/A | false  
`!~` | true | false | false  
`~/` | false | N/A | false  
  
## Literals

In addition to string and numeric literals, you can use the following literals in conditional statements:

  * `null`
  * `true`
  * `false`



For example:

  * `request.header.host is null`
  * `flow.cachehit is true`



## Examples
    
    
    <RouteRule name="default">
         <Condition>request.header.content-type = "text/xml"</Condition>
         <TargetEndpoint>XmlTargetEndpoint</TargetEndpoint>
    </RouteRule>
    
    
    <Step>
        <Condition>response.status.code = 503</Condition>
        <Name>MaintenancePolicy</Name>
    </Step>
    
    
    <Flow name="GetRequests">
        <Condition>response.verb="GET"</Condition>
        <Request>
            <Step>
                <Condition>request.path ~ "/statuses/**"</Condition>
                <Name>StatusesRequestPolicy</Name>
            </Step>
        </Request>
        <Response>
            <Step>
                <Condition>(response.status.code = 503) or (response.status.code = 400)</Condition>
                <Name>MaintenancePolicy</Name>
            </Step>
        </Response>
    </Flow>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
