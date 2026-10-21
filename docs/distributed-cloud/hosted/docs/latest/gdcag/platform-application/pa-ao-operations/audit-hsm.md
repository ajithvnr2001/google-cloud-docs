---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-hsm/
title: Hardware Security Module (HSM) \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:44:07.144285+00:00
---

# Hardware Security Module (HSM)  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-hsm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Hardware Security Module (HSM) Stay organized with collections  Save and categorize content based on your preferences. 

**Workload location** |  Hardware  
---|---  
**Audit log source** |  [Syslog format](https://datatracker.ietf.org/doc/html/rfc5424)  
**Audited operations** | 

  * Create Hewlett Packard Enterprise Integrated Lights-Out (HPE iLO) tenant key
  * Create NetApp ONTAP tenant key

  
  
## Create HPE iLO tenant key

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | _Not applicable_ | _Not applicable_  
**Target** _(Fields and values that call the API)_ | _Not applicable_ | _Not applicable_  
**Action** _(Fields containing the performed operation)_ |  `message.action` |  For example,
    
    
    "message":{
      "action":"Create Key"
      }  
  
**Event timestamp** |  `time` |  For example, `"time":"2022-11-14T14:55:53.051642Z"`  
**Source of action** | `message.sourceIPs` |  For example,
    
    
    "message":{
      "sourceIPs":["10.142.0.27"]
      }  
  
**Outcome** | `message.response` |  Either `success` or `failure`. For example,
    
    
    "message":{
      "response":"success"
      }  
  
**Other fields** | The `message.description` field contains the complete log message retrieved directly from the HSM. |  For more information, see the **Example log**.  
  
**Example log**
    
    
    {
      "pri":"14",
      "time":"2022-11-14T14:55:53.051642Z",
      "host":"hsmcluster",
      "ident":"hsmcluster",
      "pid":"-",
      "msgid":"-",
      "extradata":"-",
      "message":{
        "time":"2022-11-14T14:55:53.051642Z",
        "auditID":"bda22019-e565-4781-9c81-7a148cd1dfec",
        "user":{},
        "resource":"gpc-system/8b06-ddef1a-d643-469c-8a96-2339b1c",
        "action":"Create Key",
        "description":{
          "account":"kylo:kylo-ddb1c-f5a5:admin:accounts:kylo-ddadef1a-d643-23c",
          "application":"ncryptify:gemalto:admin:apps:kylo",
          "client_ip":"10.142.0.27",
          "createdAt":"2022-11-14T14:55:53.051642Z",
          "details":{
            "algorithm":"AES",
            "aliases":[{
              "alias":"ontap-admin-org-1-e09a731927eca3c",
              "index":0,
              "type":"string"
              }],
            "domain":"ddadef1a-d643-469c-8a96-23333e169b1c",
            "id":"8b0aec4f428354248f766",
            "name":"ontap-admin-org-1-e09a731927eca3c",
            "objectType":"Symmetric Key",
            "ownerId":"local|2620af75-cfd5-4279-88f1-c7977a317224",
            "size":256,
            "uri":"kylo:kylo-ddadef1a-d643-469c-8a96-233e16b1c:vault:keys:ontap-admin-org-1-e09a731927eca3c-v0",
            "usageMask":12
            },
          "devAccount":"ncryptify:gemalto:admin:accounts:gemalto",
          "id":"e352167a-60ce-4054-be1a-5cd09f2c64f4",
          "message":"Create Key",
          "principal":{
            "acc":"kylo/ddadef1a-d643-469c-8a96-23333e169b1c",
            "acct":"kylo:kylo-ddadefe169b1c:admin:accounts:kylo-ddadef1a-d643-469c-8a96-23333e169b1c",
            "iss":"kylo",
            "sub":"local|2620af75-cfd5-4279-88f1-c7977a317224"
            },
          "service":"minerva",
          "severity":"info",
          "source":"ciphertrust",
          "success":true,
          "requestId":"b0e2bc 72-63e3-446e-80d3-2d2dc8987915",
          "uri":"kylo:kylo-ddadef1a-d643-469c-8a96-233339b1c:audit:records:e3567a-60ce-4054-be1a-5cdf4",
          "username":"admin"
          },
        "sourceIPs":["10.142.0.27"],
        "response":"success",
        "_gdch_org":"org-1-admin",
        "_gdch_service":"hsm"
        },
      "_gdch_cluster":"org-1-admin",
      "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-ttg7r",
      "_gdch_service_name":"admin-audit-logs"
    }
    

## Create NetApp ONTAP tenant key

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | _Not applicable_ | _Not applicable_  
**Target** _(Fields and values that call the API)_ | _Not applicable_ | _Not applicable_  
**Action** _(Fields containing the performed operation)_ |  `message.action` |  For example,
    
    
    "message":{
      "action":"Create Key"
      }  
  
**Event timestamp** |  `time` |  For example, `"time":"2022-11-14T14:55:53.051642Z"`  
**Source of action** | `message.sourceIPs` |  For example,
    
    
    "message":{
      "sourceIPs":["10.142.0.27"]
      }  
  
**Outcome** | `message.response` |  Either `success` or `failure`. For example,
    
    
    "message":{
      "response":"success"
      }  
  
**Other fields** | The `message.description` field contains the complete log message retrieved directly from the HSM. |  For more information, see the **Example log**.  
  
**Example log**
    
    
    {
      "pri":"14",
      "time":"2022-11-14T14:55:53.051642Z",
      "host":"hsmcluster",
      "ident":"hsmcluster",
      "pid":"-",
      "msgid":"-",
      "extradata":"-",
      "message":{
        "time":"2022-11-14T14:55:53.051642Z",
        "auditID":"bda22019-e565-4781-9c81-7a148cd1dfec",
        "user":{},
        "resource":"gpc-system/8b06-ddef1a-d643-469c-8a96-2339b1c",
        "action":"Create Key",
        "description":{
          "account":"kylo:kylo:admin:accounts:kylo",
          "application":"ncryptify:gemalto:admin:apps:kylo",
          "client_ip":"10.142.0.27",
          "createdAt":"2022-11-14T14:55:53.051642Z",
          "details":{
            "algorithm":"AES",
            "aliases":[{
              "alias":"ten-user-org-1",
              "index":0,
              "type":"string"
              }],
            "domain":"root",
            "id":"8b0aec4f428354248f766",
            "name":"ten-user-org-1",
            "objectType":"Symmetric Key",
            "ownerId":"",
            "size":256,
            "uri":"kylo:kylo:vault:keys:ten-user-org-1-v0",
            "usageMask":4194303
            },
          "devAccount":"ncryptify:gemalto:admin:accounts:gemalto",
          "id":"e352167a-60ce-4054-be1a-5cd09f2c64f4",
          "message":"Create Key",
          "principal":{
            "acc":"kylo",
            "acct":"kylo:kylo:admin:accounts:kylo",
            "iss":"kylo",
            "sub":"local|2620af75-cfd5-4279-88f1-c7977a317224"
            },
          "service":"minerva",
          "severity":"info",
          "source":"ciphertrust",
          "success":true,
          "requestId":"b0e2bc 72-63e3-446e-80d3-2d2dc8987915",
          "uri":"kylo:kylo:audit:records:e3567a-60ce-4054-be1a-5cdf4",
          "username":"admin"
          },
        "sourceIPs":["10.142.0.27"],
        "response":"success",
        "_gdch_org":"org-1-admin",
        "_gdch_service":"hsm"
        },
      "_gdch_cluster":"org-1-admin",
      "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-ttg7r",
      "_gdch_service_name":"admin-audit-logs"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
