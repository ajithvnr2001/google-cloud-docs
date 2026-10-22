---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/audit-storage/
title: Storage \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:52.471805+00:00
---

# Storage  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/audit-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Storage Stay organized with collections  Save and categorize content based on your preferences. 

## Platform Administrator logs

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user.identity` |  For example,
    
    
    "user":{
      "identity":"root-admin-client-cert"
    }  
  
**Target Resource** _(Details of the resource being accessed)_ | `resource` |  For example,
    
    
    "resource": {
      "Application": "ontapi",
      "Hostname": "aa-aa-stge01-02",
      "StorageVirtualMachine": "root-admin"
    }

_(Note: This was parsed from the original JSON string value)_  
**Action** _(Fields containing the performed operation)_ | `action` |  For example (partial view):
    
    
    <netapp xmlns="http://www.netapp.com/filer/admin" version="1.21" vfiler="root-admin">
      <ems-autosupport-log>
        <app-version>1</app-version>
        <auto-support>false</auto-support>
        <category>heartbeat</category>
        <computer-name>gpc-adhoc-d0c087e7vm-admin-node0-zone1</computer-name>
        <event-description>{"version":"23.10.0-custom+601b7ce938be9b603524454285ddbf1b2918c33c","backendUUID":"5dee53d1-ab72-4e4e-9177-3fceddfe2eb2","platform":"kubernetes","platformVersion":"v1.30.5-gke.200","plugin":"ontap-san","svm":"root-admin","storagePrefix":"trident_"}</event-description>
        <event-id>1</event-id>
        <event-source>trident</event-source>
        ...
      </ems-autosupport-log>
    </netapp>

_(Note: This was an XML string in the original log)_  
**Event timestamp** |  `time` |  For example, `"time": "2024-12-01T15:24:07Z"`  
**Source of action** | `sourceIPs` |  For example, `"sourceIPs": ["10.200.0.2"]`  
**Outcome/Response** | `response` |  For example, `"response": "pending"`  
**Audit ID** | `auditID` |  For example, `"auditID": "8589957281"`  
**Other fields** | _See full log._ | _Includes host, ident, and _gdch_org._  
  
**Example log**
    
    
    {
      "time": "2024-12-01T15:24:07Z",
      "auditID": "8589957281",
      "user": {
        "identity": "root-admin-client-cert"
      },
      "resource": "{\"Application\":\"ontapi\",\"Hostname\":\"aa-aa-stge01-02\",\"StorageVirtualMachine\":\"root-admin\"}",
      "action": "<netapp xmlns=\"[http://www.netapp.com/filer/admin](http://www.netapp.com/filer/admin)\" version=\"1.21\" vfiler=\"root-admin\">         <ems-autosupport-log>     <app-version>1</app-version>     <auto-support>false</auto-support>     <category>heartbeat</category>     <computer-name>gpc-adhoc-d0c087e7vm-admin-node0-zone1</computer-name>     <event-description>{\"version\":\"23.10.0-custom+601b7ce938be9b603524454285ddbf1b2918c33c\",\"backendUUID\":\"5dee53d1-ab72-4e4e-9177-3fceddfe2eb2\",\"platform\":\"kubernetes\",\"platformVersion\":\"v1.30.5-gke.200\",\"plugin\":\"ontap-san\",\"svm\":\"root-admin\",\"storagePrefix\":\"trident_\"}</event-description>     <event-id>1</event-id>     <event-source>trident</...",
      "sourceIPs": [
        "10.200.0.2"
      ],
      "response": "pending",
      "_gdch_org": "root-admin",
      "host": "storage",
      "ident": "storage",
      "pid": "-",
      "msgid": "-",
      "extradata": "-",
      "message": "{\"time\":\"2024-12-01T15:24:07Z\",\"auditID\":\"8589957281\",\"user\":{\"identity\":\"root-admin-client-cert\"},\"resource\":\"{\\\"Application\\\":\\\"ontapi\\\",\\\"Hostname\\\":\\\"aa-aa-stge01-02\\\",\\\"StorageVirtualMachine\\\":\\\"root-admin\\\"}\",\"action\":\"\\u003cnetapp xmlns=\\\"[http://www.netapp.com/filer/admin](http://www.netapp.com/filer/admin)\\\" version=\\\"1.21\\\" vfiler=\\\"root-admin\\\"\\u003e              \\u003cems-autosupport-log\\u003e      \\u003capp-version\\u003e1\\u003c/app-version\\u003e      \\u003cauto-support\\u003efalse\\u003c/auto-support\\u003e      \\u003ccategory\\u003eheartbeat\\u003c/category\\u003e      \\u003ccomputer-name\\u003egpc-adhoc-d0c087e7vm-admin-node0-zone1\\u003c/computer-name\\u003e      \\u003cevent-description\\u003e{\\u0026#34;version\\u0026#34;:\\u0026#34;23.10.0-custom+601b7ce938be9b603524454285ddbf1b2918c33c\\u0026#34;,\\u0026#34;backendUUID\\u0026#34;:\\u0026#34;5dee53d1-ab72-4e4e-9177-3fceddfe2eb2\\u0026#34;,\\u0026#34;platform\\u0026#34;:\\u0026#34;kubernetes\\u0026#34;,\\u0026#34;platformVersion\\u0026#34;:\\u0026#34;v1.30.5-gke.200\\u0026#34;,\\u0026#34;plugin\\u0026#34;:\\u0026#34;ontap-san\\u0026#34;,\\u0026#34;svm\\u0026#34;:\\u0026#34;root-admin\\u0026#34;,\\u0026#34;storagePrefix\\u0026#34;:\\u0026#34;trident_\\u0026#34;}\\u003c/event-description\\u003e      \\u003cevent-id\\u003e1\\u003c/event-id\\u003e      \\u003cevent-source\\u003etrident\\u003c/...\",\"sourceIPs\":[\"10.200.0.2\"],\"response\":\"pending\",\"_gdch_org\":\"root-admin\"}"
    }
    

## Infrastructure Operator logs

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user.identity` |  For example,
    
    
    "user":{
      "identity":"root-admin-client-cert"
    }  
  
**Target Resource** _(Details of the resource being accessed)_ | `resource` |  For example,
    
    
    "resource": {
      "Application": "ontapi",
      "Hostname": "aa-aa-stge01-02",
      "StorageVirtualMachine": "root-admin"
    }

_(Note: This was parsed from the original JSON string value)_  
**Action** _(Fields containing the performed operation)_ | `action` |  For example:
    
    
    <netapp xmlns="http://www.netapp.com/filer/admin" version="1.21" vfiler="root-admin">
      <volume-size>
        <volume>trident_pvc_ae2f25d7_51f3_4cc1_b24b_650ff25ca96c</volume>
      </volume-size>
    </netapp>

_(Note: This was an XML string in the original log)_  
**Event timestamp** |  `time` |  For example, `"time": "2024-11-27T00:15:12Z"`  
**Source of action** | `sourceIPs` |  For example, `"sourceIPs": ["10.200.0.3"]`  
**Outcome/Response** | `response` |  For example, `"response": "pending"`  
**Audit ID** | `auditID` |  For example, `"auditID": "8589956251"`  
**Other fields** | _See full log._ | _Includes host, ident, and _gdch_org._  
  
**Example log**
    
    
    {
      "time": "2024-11-27T00:15:12Z",
      "auditID": "8589956251",
      "user": {
        "identity": "root-admin-client-cert"
      },
      "resource": "{\"Application\":\"ontapi\",\"Hostname\":\"aa-aa-stge01-02\",\"StorageVirtualMachine\":\"root-admin\"}",
      "action": "<netapp xmlns=\"[http://www.netapp.com/filer/admin](http://www.netapp.com/filer/admin)\" version=\"1.21\" vfiler=\"root-admin\">         <volume-size>     <volume>trident_pvc_ae2f25d7_51f3_4cc1_b24b_650ff25ca96c</volume> </volume-size>         </netapp>",
      "sourceIPs": [
        "10.200.0.3"
      ],
      "response": "pending",
      "_gdch_org": "root-admin",
      "host": "storage",
      "ident": "storage",
      "pid": "-",
      "msgid": "-",
      "extradata": "-",
      "message": "{\"time\":\"2024-11-27T00:15:12Z\",\"auditID\":\"8589956251\",\"user\":{\"identity\":\"root-admin-client-cert\"},\"resource\":\"{\\\"Application\\\":\\\"ontapi\\\",\\\"Hostname\\\":\\\"aa-aa-stge01-02\\\",\\\"StorageVirtualMachine\\\":\\\"root-admin\\\"}\",\"action\":\"\\u003cnetapp xmlns=\\\"[http://www.netapp.com/filer/admin](http://www.netapp.com/filer/admin)\\\" version=\\\"1.21\\\" vfiler=\\\"root-admin\\\"\\u003e              \\u003cvolume-size\\u003e      \\u003cvolume\\u003etrident_pvc_ae2f25d7_51f3_4cc1_b24b_650ff25ca96c\\u003c/volume\\u003e  \\u003c/volume-size\\u003e           \\u003c/netapp\\u003e\",\"sourceIPs\":[\"10.200.0.3\"],\"response\":\"pending\",\"_gdch_org\":\"root-admin\"}"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
