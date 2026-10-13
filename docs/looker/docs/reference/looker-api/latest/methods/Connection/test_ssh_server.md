---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Connection/test_ssh_server/
title: Test SSH Server \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:37:58.981051+00:00
---

# Test SSH Server  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Connection/test_ssh_server/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Test SSH Server Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.18 (latest) 

### Test the SSH Server

## Request

GET /ssh_server/{ssh_server_id}/test 

Datatype

Description

Request

HTTP Request 

path

HTTP Path 

Expand HTTP Path definition... 

ssh_server_id

string 

Id of SSH Server

## Response

### 200: Test SSH Server

Datatype

Description

(object)

[SshServer](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/SshServer)

ssh_server_id

_lock_

string 

A unique id used to identify this SSH Server

ssh_server_name

string 

The name to identify this SSH Server

ssh_server_host

string 

The hostname or ip address of the SSH Server

ssh_server_port

integer 

The port to connect to on the SSH Server

ssh_server_user

string 

The username used to connect to the SSH Server

finger_print

_lock_

string 

The md5 fingerprint used to identify the SSH Server

sha_finger_print

_lock_

string 

The SHA fingerprint used to identify the SSH Server

public_key

_lock_

string 

The SSH public key created for this instance

status

_lock_

string 

The current connection status to this SSH Server

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

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
