---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-ts/
title: Ticketing System (TS) \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:41:06.331230+00:00
---

# Ticketing System (TS)  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-ts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Ticketing System (TS) Stay organized with collections  Save and categorize content based on your preferences. 

## Application login

Application login operations include:

  * Application sign in success
  * Application sign in failure

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  `jimmy.watchcommander` _(Also present: user_id=8e3e...)_  
**Target / Mode** | `mode` |  `login` _(Also relevant: url=/login.do)_  
**Action / Event** | `event` |  `LOGIN_SUCCESS`  
**Event timestamp** |  `Time` |  `1669936335020` _(Epoch milliseconds, corresponds to Thu, 01 Dec 2022 18:12:15.020 GMT)_  
**Source of action** | `source_ip`, `host`, `http_uagent` |  Source IP: `10.253.168.66` Host: `as1` User Agent: `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36`  
**Outcome** | `event` |  `LOGIN_SUCCESS`  
**Other useful fields** | `session_id`, `user_roles`, `log_type` |  Session ID: `5307B5` User Roles: `sn_request_read` Log Type: `SECLOG` Host: `as1`  
  
**Example log**
    
    
    Time=1669936335020 host=as1 Default-thread-23  event="LOGIN_SUCCESS" authentication_multi_factor_enabled="false" mode="login" authentication_parameter1="user_name=jimmy.watchcommander" user_roles="sn_request_read" log_type="SECLOG" session_id="5307B5" source_ip="10.253.168.66" tx_num="2985" url="/login.do" domain="global" http_last_time="1668193688784" jsession_id="A6F412" http_uagent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36" user="jimmy.watchcommander" user_id="8e3e1d3b872a5910f91431dd0ebb357c" http_time_zone="America/New_York" user_group="[c92a31ea979d5910ea2a7b021153af00, 9a293b0897155110ea2a7b021153af84]" http_browser="chrome"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
