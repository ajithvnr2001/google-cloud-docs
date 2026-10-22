---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-syslog/
title: System logging protocol (syslog) audit logs \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:22:16.241681+00:00
---

# System logging protocol (syslog) audit logs  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-syslog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  System logging protocol (syslog) audit logs Stay organized with collections  Save and categorize content based on your preferences. 

Various components in GDC produce their audit logs using a standard syslog format according to the RFC-5424 specification. For more information, see <https://datatracker.ietf.org/doc/html/rfc5424>.

**JSON representation**
    
    
    {
      "pid": string,
      "pri": string,
      "hostname": string,
      "ident": string,
      "msgid": string,
      "extradata": string,
      "message": string
    }
    

Fields  
---  
`pid` |  `string` The process ID of the application that originated the message. For example, `"1"`  
`pri` |  `string` Priority value. For example, `"46"`  
`hostname` |  `string` The component that originally sent the syslog message. For example, `"anthos-audit-logs-forwarder-2kbnd"`  
`ident` |  `string` The device or application that originated the message. For example, `"/logging-prober-sidecar"`  
`msgid` |  `string` The type of message. For example, `"audit-log"`  
`extradata` |  `string` Additional custom information. For example, `"[exampleSDID@20224 iut=\"3\" eventSource=\"Application\" eventID=\"11211\"]"`  
`message` |  `string` A free-form message that provides information about the event. For example,
    
    
    "{\"time\":\"2024-01-24T17:24:55.076954537Z\",\"auditID\":\"7ab3bf57-67cb-4373-bbf6-b3ad0835cc65\",\"user\":{\"identity\":\"audit-log-writer\"},\"resource\":\"41075\",\"action\":\"-\",\"description\":\"This is a prober testing the functionality of the syslog endpoint\",\"userAgent\":\"audit-log-prober\",\"response\":\"-\",\"_gdch_org\":\"-\",\"_gdch_service\":\"audit-log-prober\"}"  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
