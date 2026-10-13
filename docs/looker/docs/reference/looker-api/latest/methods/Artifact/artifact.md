---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Artifact/artifact/
title: Get one or more artifacts \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:09.232717+00:00
---

# Get one or more artifacts  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Artifact/artifact/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Get one or more artifacts Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### Get one or more artifacts

Returns an array of artifacts matching the specified key value(s).

**Note** : The artifact storage API can only be used by Looker-built extensions.

## Request

GET /artifact/{namespace} 

Datatype

Description

Request

HTTP Request 

path

HTTP Path 

Expand HTTP Path definition... 

namespace

string 

Artifact storage namespace

query

HTTP Query 

Expand HTTP Query definition... 

key

string 

Comma-delimited list of keys. Wildcards not allowed.

fields

string 

Comma-delimited names of fields to return in responses. Omit for all fields

limit

integer 

Number of results to return. (used with offset)

offset

integer 

Number of results to skip before returning any. (used with limit)

tally

boolean 

Return the full count of results in the X-Total-Count response header. (Slight performance hit.)

## Response

### 200: Created or updated artifacts

Datatype

Description

(array)

[Artifact](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Artifact)[] 

key

string 

Key of value to store. Namespace + Key must be unique.

value

string 

Value to store.

content_type

string 

MIME type of content. This can only be used to override content that is detected as text/plain. Needed to set application/json content types, which are analyzed as plain text.

version

_lock_

integer 

Version number of the stored value. The version must be provided for any updates to an existing artifact.

namespace

_lock_

string 

Artifact storage namespace.

created_at

_lock_

string 

Timestamp when this artifact was created.

updated_at

_lock_

string 

Timestamp when this artifact was updated.

value_size

_lock_

integer 

Size (in bytes) of the stored value.

created_by_userid

_lock_

string 

User id of the artifact creator.

updated_by_userid

_lock_

string 

User id of the artifact updater.

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

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
