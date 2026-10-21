---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/log-formats/windows-dns-field-map/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:22:21.735837+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/log-formats/windows-dns-field-map/




Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON:
        
        {
          "EventTime": 1640073312000,
          "Hostname": "WIN-TEST",
          "Keywords": "4611686018427912192",
          "EventType": "INFO",
          "SeverityValue": 2,
          "Severity": "INFO",
          "EventID": 514,
          "SourceName": "Microsoft-Windows-DNSServer",
          "ProviderGuid": "{EB79061A-A566-4698-9119-3ED2807060E7}",
          "Version": 0,
          "TaskValue": 5,
          "OpcodeValue": 0,
          "RecordNumber": 1,
          "ExecutionProcessID": 2244,
          "ExecutionThreadID": 1448,
          "Channel": "Microsoft-Windows-DNSServer/Audit",
          "Domain": "DNSTEST",
          "AccountName": "Administrator",
          "UserID": "S-1-2-3",
          "AccountType": "User",
          "Message": "The zone dnstest.local was updated. The SecondaryServers setting has been set to deny zone transfers. [virtualization instance: .].",
          "Category": "ZONE_OP",
          "Opcode": "Info",
          "Zone": "dnstest.local",
          "PropertyKey": "SecondaryServers",
          "NewValue": "deny zone transfers",
          "VirtualizationID": ".",
          "EventReceivedTime": 1640073312001,
          "SourceModuleName": "auditeventlog",
          "SourceModuleType": "im_msvistalog"
        }
        
        

  * XML:
        
        <Event>
          <SourceName>Microsoft-Windows-DNSServer</SourceName>
          <ProviderGuid>{EB79061A-A566-4698-9119-3ED2807060E7}
          </ProviderGuid>
          <EventID>256</EventID>
          <Version>0</Version>
          <ChannelID>16</ChannelID>
          <OpcodeValue>0</OpcodeValue>
          <TaskValue>1</TaskValue>
          <Keywords>9223372036854775809</Keywords>
          <EventTime>1640073312000</EventTime>
          <ExecutionProcessID>2476</ExecutionProcessID>
          <ExecutionThreadID>3972</ExecutionThreadID>
          <EventType>INFO</EventType>
          <SeverityValue>2</SeverityValue>
          <Severity>INFO</Severity>
          <Hostname>WIN-TEST</Hostname>
          <Domain>NT AUTHORITY</Domain>
          <AccountName>SYSTEM</AccountName>
          <UserID>S-1-2-3</UserID>
          <AccountType>User</AccountType>
          <Flags>256</Flags>
          <TCP>0</TCP>
          <InterfaceIP>198.51.100.5</InterfaceIP>
          <Source>198.51.100.0</Source>
          <RD>1</RD>
          <QNAME>www.google.com.</QNAME>
          <QTYPE>1</QTYPE>
          <XID>55835</XID>
          <Port>50843</Port>
          <BufferSize>43</BufferSize>
          <PacketData>0xDA1B0100000100000000000006766F727465780464617461096D6963726F736F667403636F6D0000010001</PacketData>
          <AdditionalInfo>.</AdditionalInfo>
          <EventReceivedTime>1640073312001</EventReceivedTime>
          <SourceModuleName>eventlog</SourceModuleName>
          <SourceModuleType>im_etw</SourceModuleType>
        </Event>
        
        

  * SYSLOG + KV:
        
        UDP question info at 00000027580C8220  Socket = 556  Remote addr 198.51.100.1, port 60766  Time Query=559415, Queued=0, Expire=0  Buf length = 0x0fa0 (4000)  Msg length = 0x0044 (68)  Message:    XID       0x49d7    Flags     0x0100      QR        0 (QUESTION)      OPCODE    0 (QUERY)      AA        0      TC        0      RD        1      RA        0      Z         0      CD        0      AD        0      RCODE     0 (NOERROR)    QCOUNT    1    ACOUNT    0    NSCOUNT   0    ARCOUNT   0    QUESTION SECTION:    Offset = 0x000c, RR count = 0    Name      \"(5)_ldap(4)_tcp(4)INMS(6)_sites(14)ForestDnsZones(8)genmills(3)com(0)\"      QTYPE   SRV (33)      QCLASS  1    ANSWER SECTION:      empty    AUTHORITY SECTION:      empty    ADDITIONAL SECTION:      empty
        

  * SYSLOG
        
        29.11.2023 14:13:11 1B14 PACKET 00000274481BF1B0 UDP Snd 198.51.100.0 14fc Q [0001 D NOERROR] A (23)win-dns(10)westeurope(8)test(5)azure(3)com(0)
        




Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-14 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-14 UTC."],[],[]] 
