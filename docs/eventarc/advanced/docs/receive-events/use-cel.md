---
url: https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/use-cel/
title: Use Common Expression Language \u00a0|\u00a0 Eventarc Advanced \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:46.550576+00:00
---

# Use Common Expression Language  |  Eventarc Advanced  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/use-cel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/advanced/docs/overview)



Send feedback 

#  Use Common Expression Language Stay organized with collections  Save and categorize content based on your preferences. 

[ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs/overview)

[Common Expression Language (CEL)](https://opensource.google/projects/cel) is an open source non-Turing-complete language that can be used to evaluate expressions. Every enrollment in Eventarc Advanced includes a condition expression written in CEL that is used to evaluate and filter messages. In Eventarc Advanced, you can also use CEL to do the following:

  * Control publishing access by applying a CEL condition expression to an event context attribute

  * Transform your event data content by writing transformation expressions using CEL


**Caution:** Don't include sensitive information such as passwords, secrets, or personally identifiable information (PII) in CEL transformation expressions. These expressions are treated as service configuration data by Eventarc Advanced and don't have the same level of [data security](https://cloud.google.com/trust-center/security) as event payloads.

In general, a condition expression consists of one or more statements that are joined by logical operators (`&&`, `||`, or `!`). Each statement expresses an attribute-based rule that is applied to the data. Most commonly, operators are used to compare the value contained in a variable with a literal value.

For example, if the value of `message.type` is `google.cloud.dataflow.job.v1beta3.statusChanged`, then the expression `message.type == "google.cloud.dataflow.job.v1beta3.statusChanged"` evaluates to `True`.

For more information, see the following:

  * [Create an enrollment to receive events](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/create-enrollment)
  * [Control publishing access](https://docs.cloud.google.com/eventarc/advanced/docs/control-publishing-access)
  * [Transform received events](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events)
  * [CEL language definition](https://github.com/google/cel-spec/blob/master/doc/langdef.md)



## Available attributes

All event context attributes can be accessed as variables through a predefined `message` object. These variables are populated with values based on event context attributes at runtime. An enrollment can use a variable to express a given attribute. For example, `message.type` returns the value of the `type` attribute.

Note the following:

  * Events might include, and enrollments can use, any number of additional custom [CloudEvents](https://cloudevents.io/) attributes with distinct names (also known as [extension attributes](https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md#extension-context-attributes)). However, they are represented as `String` types in CEL expressions regardless of their actual format. You can use a CEL expression to cast their values to other types.

  * You can't evaluate enrollments or control publishing access based on the event payload content. Both `message.data` and `message.data_base64` are reserved variables and can't be used in expressions. However, CEL is supported when [transforming event data](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events) which lets you modify the event payload content (for example, to satisfy the API contract for a specific destination).




The following attributes can be accessed when evaluating condition expressions: 

Attribute | Attribute type | Description  
---|---|---  
`message.datacontenttype` | `String` | The content type of the `data` value  
`message.dataschema` | `URI` | Identifies the schema that the `data` adheres to  
`message.id` | `String` | Identifies the event; producers must ensure that `source` \+ `id` is unique for each distinct event  
`message.source` | `URI-reference` | Identifies the context in which an event happened  
`message.specversion` | `String` | The version of the CloudEvents specification which the event uses  
`message.subject` | `String` | Describes the subject of the event in the context of the event producer (identified by `source`)  
`message.time` | `Timestamp` | Timestamp of when the occurrence happened; might be set to some other time (such as the current time) by the CloudEvents producer; however, all producers for the same `source` must be consistent   
`message.type` | `String` | Describes the type of event related to the originating occurrence; see the [Google event types supported by Eventarc](https://docs.cloud.google.com/eventarc/advanced/docs/event-types)  
  
## Operators and functions

You can use operators and functions to build complex logic expressions.

Logical operators, such as `&&`, `||`, and `!`, let you verify multiple variables in a conditional expression. For example, `message.time.getFullYear() < 2020 && message.type == "google.cloud.dataflow.job.v1beta3.statusChanged"` joins two statements, and requires both statements to be `True` to produce an overall result of `True`.

**Note:** A distinction is made between an attribute that is not set versus an attribute with an empty value. You can use the `has` macro to test for a field's existence. For example, `has(message.bucket)` returns `True` if the extension attribute `bucket` is set. If an attribute isn't set, any logical operations using it always evaluate to `False` regardless of the literal value.

String manipulation operators, such as `x.contains('y')`, match strings or substrings that you define, and let you develop rules to match messages without listing every possible combination.

Eventarc Advanced also supports extension functions, such as `merge` and `flatten`, which can be used to transform data and simplify the modification of events received from a bus.

See the list of [CEL predefined operators and functions](https://github.com/google/cel-spec/blob/master/doc/langdef.md#standard-definitions) and [CEL predefined macros](https://github.com/google/cel-spec/blob/master/doc/langdef.md#macros).

### Logical operators

The following table describes the logical operators that Eventarc Advanced supports.

Expression | Description  
---|---  
`x == "my_string"` | Returns `True` if `x` is equal to the constant string literal argument.  
`x == R"my_string\n"` | Returns `True` if `x` is equal to the given raw string literal that does not interpret escape sequences. Raw string literals are convenient for expressing strings which themselves must use escape sequences, such as regular expressions or program text.  
`x == y` | Returns `True` if `x` is equal to `y`.  
`x != y` | Returns `True` if `x` is not equal to `y`.  
`x && y` | Returns `True` if both `x` and `y` are `True`.  
`x || y` | Returns `True` if `x`, `y`, or both are `True`.  
`!x` | Returns `True` if the boolean value `x` is `False`, or returns `False` if the boolean value `x` is `True`.  
`m['k']` | If key `k` is present, returns the value at key `k` in the string-to-string map `m`. If key `k` is not present, returns an error that causes the rule under evaluation to not match.  
  
### String manipulation operators

The following table describes the string manipulation operators that Eventarc Advanced supports.

Expression | Description  
---|---  
`double(x)` | Converts the string result of `x` to a `double` type. The converted value can be used to compare floating-point numbers with standard arithmetic operators such as `>` and `<=`. This works only for values that can be floating-point numbers.  
`int(x)` | Converts the string result of `x` to an `int` type. The converted value can be used to compare integers with standard arithmetic operators such as `>` and `<=`. This works only for values that can be integers.  
`x + y` | Returns the concatenated string `xy`.  
`x.contains(y)` | Returns `True` if the string `x` contains the substring `y`.  
`x.endsWith(y)` | Returns `True` if the string `x` ends with the substring `y`.  
`x.join()` | Returns a new string where the elements of a string list are concatenated. Accepts an optional separator which is placed between the elements in the resulting string. For example, the following expression returns `'hello world'`: `['hello', 'world'].join(' ')`  
`x.lowerAscii()` | Returns a new string where all ASCII characters are lowercase.  
`x.matches(y)` | Returns `True` if the string `x` matches the specified [RE2](https://github.com/google/re2/wiki/Syntax) pattern `y`. The RE2 pattern is compiled using the RE2::Latin1 option that disables Unicode features.  
`x.replace(y,z)` | Returns a new string where occurrences of substring `y` are replaced by substring `z`. Accepts an optional argument that limits how many replacements to make. For example, the following expression returns `'wello hello'`: `'hello hello'.replace('he', 'we', 1)`  
`x.split(y)` | Returns a list of strings split from the input by separator `y`. Accepts an optional argument that limits how many substrings to produce. For example, the following expression returns `['hello', 'hello hello']`: `'hello hello hello'.split(' ', 2)`  
`x.startsWith(y)` | Returns `True` if the string `x` begins with the substring `y`.  
`x.upperAscii()` | Returns a new string where all ASCII characters are uppercase.  
  
### Regular expression functions

The following table describes the regular expression functions that Eventarc Advanced supports.

Expression | Description  
---|---  
`re.capture(target,regex)` | Uses `regex` to capture the first unnamed or named group value in the `target` string, and returns a string. For example, the following expression returns `"o"`: `re.capture("hello", R"hell(o)")`  
`re.captureN(target,regex)` | Uses `regex` to capture the group name and string (for named groups) and the group index and string (for unnamed groups) from the `target` string, and returns a map of key and value pairs. For example, the following expression returns `{"1": "user", "Username": "testuser", "Domain": "testdomain"}`: `re.captureN("The user testuser belongs to testdomain", R"The (user|domain) (?P.*) belongs to (?P.*)")`  
`re.extract(target,regex,rewrite)` | Uses `regex` to extract matched group values from the `target` string, and returns a string of the extracted values that is formatted based on the `rewrite` argument. For example, the following expression returns `"example.com"`: `re.extract("alex@example.com", "(^.*@)(.*)", "\\2")`  
`x.matches(regex)` | Returns `True` if the string `x` matches the specified [RE2](https://github.com/google/re2/wiki/Syntax) pattern `regex`. The RE2 pattern is compiled using the RE2::Latin1 option that disables Unicode features.  
  
The regular expressions follow the [RE2 syntax](https://github.com/google/re2/wiki/Syntax). Note that the `R` preceding the regular expressions indicates a raw string that doesn't require escaping.

### Extension functions

Eventarc Advanced supports certain extension functions that can be used to transform the event data received through a bus. For more information and examples, see [Transform received events](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events#transform-functions).

## What's next

  * [Transformation examples](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transformation-examples)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
