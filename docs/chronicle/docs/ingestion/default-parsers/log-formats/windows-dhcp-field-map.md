---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/log-formats/windows-dhcp-field-map/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:45:13.015547+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/log-formats/windows-dhcp-field-map/




Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON
        
        {
          "EventTime": 1629978331254,
          "Hostname": "user238.dummy2.local",
          "Keywords": "9223372036854775808",
          "EventType": "INFO",
          "SeverityValue": 2,
          "Severity": "INFO",
          "EventID": 75,
          "SourceName": "Microsoft-Windows-DHCP-Server",
          "ProviderGuid": "{6D64F02C-A125-4DAC-9A01-F0555B41CA84}",
          "Version": 0,
          "TaskValue": 0,
          "OpcodeValue": 0,
          "RecordNumber": 116,
          "ExecutionProcessID": 4160,
          "ExecutionThreadID": 4892,
          "Channel": "Microsoft-Windows-Dhcp-Server/Operational",
          "UserID": "S-1-2-3",
          "AccountType": "Unknown",
          "Message": "Scope: [[198.51.100.0]10] for IPv4 is Updated with Lease Duration: 691200 seconds by USER2\\\\Administrator. The previous configured Lease Duration was: 0 seconds.",
          "Opcode": "Info",
          "IP_ScopeName": "[[198.51.100.0]10]",
          "ModifiedDuration": "691200",
          "ClientName": "USER2\\\\Administrator",
          "OriginalDuration": "0",
          "EventReceivedTime": 1629978331254,
          "SourceModuleName": "dhcp_server_eventlog",
          "SourceModuleType": "im_msvistalog"
        }
        

  * SYSLOG
        
        9/12/2024 1:34:50 PM 18DC PACKET  00000291686F6100 UDP Rcv 198.51.100.0     48ea   Q [0001   D   NOERROR] SRV    (5)_ldap(4)_tcp(11)TD-P-MS-DC2(0)
        

  * CSV
        
        10,07/14/21,11:54:02,Assign,198.51.100.0,,00505683901B,,1261026911,0,,,,,,,,,0
        




Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-14 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-14 UTC."],[],[]] 
