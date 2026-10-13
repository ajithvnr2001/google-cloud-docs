---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/SshTunnel/
title: SshTunnel \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:40:29.101492+00:00
---

# SshTunnel  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/SshTunnel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  SshTunnel Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.16 

**Note:** These docs are for an older version of the API. The API reference is also available for [ the latest version, 4.0.26.20 ](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest). 

Datatype

Description

(object)

object 

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

## Related Methods

  * [Connection/create_ssh_tunnel](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/methods/Connection/create_ssh_tunnel "Connection/create_ssh_tunnel")
  * [Connection/ssh_tunnel](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/methods/Connection/ssh_tunnel "Connection/ssh_tunnel")
  * [Connection/update_ssh_tunnel](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/methods/Connection/update_ssh_tunnel "Connection/update_ssh_tunnel")
  * [Connection/test_ssh_tunnel](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/methods/Connection/test_ssh_tunnel "Connection/test_ssh_tunnel")



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
