---
url: https://docs.cloud.google.com/workflows/docs/reference/stdlib/overview/
title: Standard library overview \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:20:59.982932+00:00
---

# Standard library overview  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/stdlib/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Standard library overview Stay organized with collections  Save and categorize content based on your preferences. 

The Workflows standard library modules allow you to easily construct arguments for services and process responses. There is no need to import or load libraries in a workflow—library functions work out of the box.

All functions can be called using `call` steps, but only non-blocking functions can be used inside an expression. For example, HTTP calls, `sys.sleep`, and `sys.log` cannot be used inside an expression. For more information, see [Blocking calls](https://docs.cloud.google.com/workflows/docs/reference/syntax/expressions#blocking-calls).

To optimize usage, you should understand which functions are considered a step and count towards the maximum steps limit. For more information, see [Optimize usage](https://docs.cloud.google.com/workflows/docs/best-practice#optimize-usage).

Workflows also includes frequently used functions, such as for data type and format conversions. See [Expression helpers](https://docs.cloud.google.com/workflows/docs/reference/stdlib/expression-helpers).

## Generate random identifiers or numbers

You can use [`uuid.generate`](https://docs.cloud.google.com/workflows/docs/reference/stdlib/uuid/generate) to return a random 128‑bit universally unique identifier (UUID) in string form.

You can use [`sys.now`](https://docs.cloud.google.com/workflows/docs/reference/stdlib/sys/now) to generate multiple random numbers. (The function returns a floating point number with nanosecond precision.)

  * If you need only one number, use [`sys.get_env`](https://docs.cloud.google.com/workflows/docs/reference/stdlib/sys/get_env) to retrieve the workflow's execution identifier.

  * If a unique ID is needed, you can use `string()` to convert the number returned from `sys.now` to a string and combine it with the execution ID; for example, `some_execution_id1635892223.4459958`.




Optionally, you can [use a Cloud Run function to generate a number](https://docs.cloud.google.com/workflows/docs/samples/workflows-functions-randomgen) and call the Cloud Run function from your workflow.

## Expression helpers

Built-in expression helper functions.

### Conversion functions

Convert values from one data type to another.

Functions  
---  
`[double()](https://docs.cloud.google.com/workflows/docs/reference/stdlib/expression-helpers#conversion-functions)` | Accepts an attribute of type string or integer and returns a double.  
`[int()](https://docs.cloud.google.com/workflows/docs/reference/stdlib/expression-helpers#conversion-functions)` | Accepts an attribute of type string or double and returns an integer.  
`[string()](https://docs.cloud.google.com/workflows/docs/reference/stdlib/expression-helpers#conversion-functions)` | Accepts an attribute of type integer, double, or boolean and returns a string.  
  
### Data type functions

Operate on lists, maps, and strings.

Functions  
---  
`[in()](https://docs.cloud.google.com/workflows/docs/reference/stdlib/expression-helpers#datatype-functions)` | Checks whether a given key is present in a list or map.  
`[keys()](https://docs.cloud.google.com/workflows/docs/reference/stdlib/expression-helpers#datatype-functions)` | Accepts an attribute of type map and returns a list of key elements in the map.  
`[len()](https://docs.cloud.google.com/workflows/docs/reference/stdlib/expression-helpers#datatype-functions)` | Computes the length of value according to its type.  
  
### Conditional functions

Support conditions within expressions.

Functions  
---  
`[default(val, defaultVal)](https://docs.cloud.google.com/workflows/docs/reference/stdlib/expression-helpers#conditional-functions)` | Returns a value if it is not null; otherwise returns a default value.  
`[if(condition, ifTrue, ifFalse)](https://docs.cloud.google.com/workflows/docs/reference/stdlib/expression-helpers#conditional-functions)` | Evaluates a condition and returns one of two arguments depending on what the condition evaluates to.  
  
### Type functions

Return data type.

Functions  
---  
`[get_type(arg)](https://docs.cloud.google.com/workflows/docs/reference/stdlib/expression-helpers#type_functions)` | Returns a string indicating the data type of the argument.  
  
## Module: base64

Base64 encoding/decoding.

Functions  
---  
`[decode](https://docs.cloud.google.com/workflows/docs/reference/stdlib/base64/decode)` | Decodes given Base64-encoded string to bytes.  
`[encode](https://docs.cloud.google.com/workflows/docs/reference/stdlib/base64/encode)` | Encodes given bytes to Base64 text.  
  
## Module: events

Events support.

Functions  
---  
`[await_callback](https://docs.cloud.google.com/workflows/docs/reference/stdlib/events/await_callback)` | Waits for a callback to be received at the given endpoint.  
`[create_callback_endpoint](https://docs.cloud.google.com/workflows/docs/reference/stdlib/events/create_callback_endpoint)` | Creates a callback endpoint expecting the specified HTTP method.  
  
## Module: experimental.executions

Execution management.

**Caution:** The behavior of routines in this module might change, and they might not be supported in the future.

Instead of using `experimental.executions.map` to support parallel work, we recommend you [execute workflow steps in parallel](https://docs.cloud.google.com/workflows/docs/execute-parallel-steps). If you are already using `experimental.executions.map`, you can [migrate your workflow to use parallel steps](https://docs.cloud.google.com/workflows/docs/migrate-function-to-parallel).

Functions  
---  
`[execution_error](https://docs.cloud.google.com/workflows/docs/reference/stdlib/experimental.executions/execution_error)` | Raised when a workflow execution finishes with an error or is cancelled.  
`[map](https://docs.cloud.google.com/workflows/docs/reference/stdlib/experimental.executions/map)` | Starts workflow executions and waits for all of them to finish.  
`[run](https://docs.cloud.google.com/workflows/docs/reference/stdlib/experimental.executions/run)` | Starts a workflow execution and waits for it to finish.  
  
## Module: hash

Common hashing algorithms.

Functions  
---  
`[compute_checksum](https://docs.cloud.google.com/workflows/docs/reference/stdlib/hash/compute_checksum)` | Computes checksum using a given hashing algorithm.  
`[compute_hmac](https://docs.cloud.google.com/workflows/docs/reference/stdlib/hash/compute_hmac)` | Computes the hash-based message authentication code (HMAC) for data given a secret key and hashing algorithm.  
  
## Module: http

HTTP/S request support.

Functions  
---  
`[default_retry_predicate](https://docs.cloud.google.com/workflows/docs/reference/stdlib/http/default_retry_predicate)` | Simple default retry predicate for idempotent targets.  
`[default_retry_predicate_non_idempotent](https://docs.cloud.google.com/workflows/docs/reference/stdlib/http/default_retry_predicate_non_idempotent)` | Simple default retry predicate for non-idempotent targets.  
`[delete](https://docs.cloud.google.com/workflows/docs/reference/stdlib/http/delete)` | Sends an HTTP `DELETE` request to the specified URL.  
`[get](https://docs.cloud.google.com/workflows/docs/reference/stdlib/http/get)` | Sends an HTTP `GET` request to the specified URL.  
`[patch](https://docs.cloud.google.com/workflows/docs/reference/stdlib/http/patch)` | Sends an HTTP `PATCH` request to the specified URL.  
`[post](https://docs.cloud.google.com/workflows/docs/reference/stdlib/http/post)` | Sends an HTTP `POST` request to the specified URL.  
`[put](https://docs.cloud.google.com/workflows/docs/reference/stdlib/http/put)` | Sends an HTTP `PUT` request to the specified URL.  
`[request](https://docs.cloud.google.com/workflows/docs/reference/stdlib/http/request)` | Sends an HTTP request.  
Objects  
---  
`[default_retry](https://docs.cloud.google.com/workflows/docs/reference/stdlib/http/default_retry)` | Simple default retry policy for idempotent targets.  
`[default_retry_non_idempotent](https://docs.cloud.google.com/workflows/docs/reference/stdlib/http/default_retry_non_idempotent)` | Simple default retry policy for non-idempotent targets.  
  
## Module: json

JSON encoding/decoding.

Functions  
---  
`[decode](https://docs.cloud.google.com/workflows/docs/reference/stdlib/json/decode)` | Decodes given JSON bytes (assuming UTF-8), or a string, into an object.  
`[encode](https://docs.cloud.google.com/workflows/docs/reference/stdlib/json/encode)` | Encodes given input object to JSON bytes, using UTF-8 charset.  
`[encode_to_string](https://docs.cloud.google.com/workflows/docs/reference/stdlib/json/encode_to_string)` | Encodes given object to a JSON string.  
  
## Module: list

List utility.

Functions  
---  
`[concat](https://docs.cloud.google.com/workflows/docs/reference/stdlib/list/concat)` | Creates a copy of a list with a new element concatenated at the end.  
`[prepend](https://docs.cloud.google.com/workflows/docs/reference/stdlib/list/prepend)` | Creates a copy of a list with a new element added to the beginning.  
  
## Module: map

Map utility.

Functions  
---  
`[delete](https://docs.cloud.google.com/workflows/docs/reference/stdlib/map/delete)` | Takes a map, creates a copy of the map, and removes the item with the specified key.  
`[get](https://docs.cloud.google.com/workflows/docs/reference/stdlib/map/get)` | Performs a safe lookup on a map, returning `null` if the key is not found.  
`[merge](https://docs.cloud.google.com/workflows/docs/reference/stdlib/map/merge)` | Takes two maps, creates a copy of the first map, and adds the items from the second map to the copy.  
`[merge_nested](https://docs.cloud.google.com/workflows/docs/reference/stdlib/map/merge_nested)` | Takes two maps, creates a copy of the first map, and recursively adds items from the second map to the copy.  
  
## Module: math

Math utility.

Functions  
---  
`[abs](https://docs.cloud.google.com/workflows/docs/reference/stdlib/math/abs)` | Returns the absolute value of a number.  
`[floor](https://docs.cloud.google.com/workflows/docs/reference/stdlib/math/floor)` | Returns the floor of a number.  
`[max](https://docs.cloud.google.com/workflows/docs/reference/stdlib/math/max)` | Returns the maximum of two numbers.  
`[min](https://docs.cloud.google.com/workflows/docs/reference/stdlib/math/min)` | Returns the minimum of two numbers.  
  
## Module: retry

Support for retries.

Functions  
---  
`[always](https://docs.cloud.google.com/workflows/docs/reference/stdlib/retry/always)` | Convenience retry condition that retries on any error.  
`[never](https://docs.cloud.google.com/workflows/docs/reference/stdlib/retry/never)` | Convenience retry condition that retries on no error at all.  
Objects  
---  
`[default_backoff](https://docs.cloud.google.com/workflows/docs/reference/stdlib/retry/default_backoff)` | Simple default truncated exponential backoff policy.  
  
## Module: sys

Common system interface, with platform-dependent implementation.

Functions  
---  
`[get_env](https://docs.cloud.google.com/workflows/docs/reference/stdlib/sys/get_env)` | Retrieves the value of the specified environment variable.  
`[log](https://docs.cloud.google.com/workflows/docs/reference/stdlib/sys/log)` | Writes one of `data`, `text`, or `json` to the log at specified severity.  
`[now](https://docs.cloud.google.com/workflows/docs/reference/stdlib/sys/now)` | Returns Unix time, as a floating-point number.  
`[sleep](https://docs.cloud.google.com/workflows/docs/reference/stdlib/sys/sleep)` | Suspends execution for the given number of seconds.  
`[sleep_until](https://docs.cloud.google.com/workflows/docs/reference/stdlib/sys/sleep_until)` | Suspends execution until the given time.  
  
## Module: text

Text processing.

To concatenate a string, see [Strings](https://docs.cloud.google.com/workflows/docs/reference/syntax/strings).

Functions  
---  
`[decode](https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/decode)` | Decodes given data to string, assuming the specified character set.  
`[encode](https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/encode)` | Encodes given text to bytes, using the specified character set.  
`[find_all](https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/find_all)` | Finds the index of all instances of a substring in a string.  
`[find_all_regex](https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/find_all_regex)` | Finds all matches of a regular expression in a string.  
`[match_regex](https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/match_regex)` | Reports whether a string contains a match of a regular expression.  
`[replace_all](https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/replace_all)` | Replaces all instances of a substring with a new string.  
`[replace_all_regex](https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/replace_all_regex)` | Replaces all matches of a regular expression with a new string.  
`[split](https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/split)` | Splits the source string into a list of all substrings between each instance of the separator.  
`[substring](https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/substring)` | Extracts the substring between two zero-based indexes of a source string.  
`[to_lower](https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/to_lower)` | Returns a string with all Unicode letters mapped to their lowercase.  
`[to_upper](https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/to_upper)` | Returns a string with all Unicode letters mapped to their uppercase.  
`[url_decode](https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/url_decode)` | Returns a string with pluses and percent-escaped characters converted to UTF-8.  
`[url_encode](https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/url_encode)` | Returns a string with percent-encoded reserved characters, including spaces.  
`[url_encode_plus](https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/url_encode_plus)` | Returns a string with percent-encoded reserved characters, and spaces replaced by pluses (`+`).  
  
## Module: time

Time-related utility functions.

Functions  
---  
`[format](https://docs.cloud.google.com/workflows/docs/reference/stdlib/time/format)` | Formats the given timestamp as a human-readable string.  
`[parse](https://docs.cloud.google.com/workflows/docs/reference/stdlib/time/parse)` | Parses the given RFC 3339-compatible string into a timestamp.  
  
## Module: uuid

UUID utility.

Functions  
---  
`[generate](https://docs.cloud.google.com/workflows/docs/reference/stdlib/uuid/generate)` | Returns a random universally unique identifier (UUID).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
