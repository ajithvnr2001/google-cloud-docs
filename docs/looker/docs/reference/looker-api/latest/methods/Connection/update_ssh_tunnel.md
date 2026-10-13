---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Connection/update_ssh_tunnel/
title: Update SSH Tunnel \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:47:00.642530+00:00
---

# Update SSH Tunnel  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Connection/update_ssh_tunnel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Update SSH Tunnel Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.18 (latest) 

### Update an SSH Tunnel

## Request

PATCH /ssh_tunnel/{ssh_tunnel_id} 

Datatype

Description

Request

HTTP Request 

path

HTTP Path 

Expand HTTP Path definition... 

ssh_tunnel_id

string 

Id of SSH Tunnel

body

HTTP Body 

Expand HTTP Body definition... 

body

[SshTunnel](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/SshTunnel)

SSH Tunnel

Expand SshTunnel definition... 

tunnel_id

_lock_

string 

Unique ID for the tunnel

ssh_server_id

string 

SSH Server ID

ssh_server_name

_lock_

string 

SSH Server name

ssh_server_host

_lock_

string 

SSH Server Hostname or IP Address

ssh_server_port

_lock_

integer 

SSH Server port

ssh_server_user

_lock_

string 

Username used to connect to the SSH Server

last_attempt

_lock_

string 

Time of last connect attempt

local_host_port

integer 

Localhost Port used by the Looker instance to connect to the remote DB

database_host

string 

Hostname or IP Address of the Database Server

database_port

integer 

Port that the Database Server is listening on

status

_lock_

string 

Current connection status for this Tunnel

## Response

### 200: SSH Tunnel

Datatype

Description

(object)

[SshTunnel](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/SshTunnel)

tunnel_id

_lock_

string 

Unique ID for the tunnel

ssh_server_id

string 

SSH Server ID

ssh_server_name

_lock_

string 

SSH Server name

ssh_server_host

_lock_

string 

SSH Server Hostname or IP Address

ssh_server_port

_lock_

integer 

SSH Server port

ssh_server_user

_lock_

string 

Username used to connect to the SSH Server

last_attempt

_lock_

string 

Time of last connect attempt

local_host_port

integer 

Localhost Port used by the Looker instance to connect to the remote DB

database_host

string 

Hostname or IP Address of the Database Server

database_port

integer 

Port that the Database Server is listening on

status

_lock_

string 

Current connection status for this Tunnel

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

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
