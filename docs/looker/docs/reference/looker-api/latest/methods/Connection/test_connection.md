---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Connection/test_connection/
title: Test Connection \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:32.919534+00:00
---

# Test Connection  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Connection/test_connection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Test Connection Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### Test an existing connection.

Note that a connection's 'dialect' property has a 'connection_tests' property that lists the specific types of tests that the connection supports.

This API is rate limited.

Unsupported tests in the request will be ignored.

## Request

PUT /connections/{connection_name}/test 

Datatype

Description

Request

HTTP Request 

path

HTTP Path 

Expand HTTP Path definition... 

connection_name

string 

Name of connection

query

HTTP Query 

Expand HTTP Query definition... 

tests

string[] 

## Response

### 200: Test results

Datatype

Description

(array)

[DBConnectionTestResult](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/DBConnectionTestResult)[] 

can

_lock_

object 

Operations the current user is able to perform on this object

connection_string

_lock_

string 

JDBC connection string. (only populated in the 'connect' test)

message

_lock_

string 

Result message of test

name

_lock_

string 

Name of test

status

_lock_

string 

Result code of test

### 400: Bad Request

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

### 404: Not Found

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

### 422: Validation Error

Datatype

Description

(object)

[ValidationError](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ValidationError)

message

_lock_

string 

Error details

errors

[ValidationErrorDetail](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ValidationErrorDetail)[] 

Expand ValidationErrorDetail definition... 

field

_lock_

string 

Field with error

code

_lock_

string 

Error code

message

_lock_

string 

Error info message

documentation_url

_lock_

string 

Documentation link

documentation_url

_lock_

string 

Documentation link

### 429: Too Many Requests

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

## Examples

### Python

[https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/test_connection.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/test_connection.py#L51 "https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/test_connection.py")  
---  
  
### TypeScript

[https://github.com/looker-open-source/sdk-codegen/blob/main/examples/typescript/testDBConnections.ts ](https://github.com/looker-open-source/sdk-codegen/blob/main/examples/typescript/testDBConnections.ts#L28 "https://github.com/looker-open-source/sdk-codegen/blob/main/examples/typescript/testDBConnections.ts")  
---  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
