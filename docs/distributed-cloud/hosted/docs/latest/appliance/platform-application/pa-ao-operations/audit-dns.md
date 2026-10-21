---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/audit-dns/
title: Domain Name System (DNS) \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:21:50.590231+00:00
---

# Domain Name System (DNS)  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/audit-dns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Domain Name System (DNS) Stay organized with collections  Save and categorize content based on your preferences. 

**Workload location** |  Root and organization workloads  
---|---  
**Audit log source** |  [Kubernetes audit logs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/audit-kubernetes)  
**Audited operations** | 

  * Update a zone
  * Create or delete a DNSSEC key
  * Change a DNSSEC key (ZSK or KSK) for signing records in a DNS zone

  
  
## Update a zone

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user.username` |  For example,
    
    
    "user":{
      "username": "fop-dns@example.com"
      }  
  
**Target** _(Fields and values that call the API)_ | `requestURI` |  `"requestURI":"/api/v1/namespaces/dns-system/configmaps/gpc-coredns-external-zonefile"`  
**Action** _(Fields containing the performed operation)_ | `verb` |  `"verb":"update"`  
**Event timestamp** |  `ts` |  For example, `"ts":2022-11-11T22:02:02.074Z`  
**Source of action** | `sourceIPs` |  For example, `"sourceIPs":["10.142.5.147"]`  
**Outcome** | `responseStatus.code` |  For example,
    
    
    "responseStatus":{
      "code":200
      }  
  
**Other fields** | 

  * `annotations`
  * `objectRef`

|  For example,
    
    
    "annotations":{
      "authorization.k8s.io/decision":"allow"
      },
    "objectRef":{
      "resourceVersion":"697063",
      "uid":"aed2e6f7-ca03-4bcd-9c07-167ccd4da88e",
      "apiVersion":"v1",
      "resource":"configmaps",
      "apiGroup":"UNKNOWN",
      "namespace":"dns-system",
      "name":"gpc-coredns-external-zonefile"
        }  
  
**Example log**
    
    
    {
      "_gdch_cluster":"root-admin",
      "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-7s769",
      "_gdch_service_name":"apiserver",
      "annotations":{
        "authorization.k8s.io/decision":"allow",
        "authorization.k8s.io/reason": "RBAC: allowed by ClusterRoleBinding \"dns-core-controllers-rolebinding\" of ClusterRole \"dns-core-controllers-role\" to ServiceAccount \"dns-core-controller-sa/dns-system\"",
        },
      "apiVersion":"audit.k8s.io/v1",
      "auditID":"ba0344d7-283f-4d79-aabc-e083al9b053a",
      "kind":"Event",
      "level":"Metadata",
      "objectRef":{
        "resourceVersion":"697063",
        "uid":"aed2e6f7-ca03-4bcd-9c07-167ccd4da88e",
        "apiVersion":"v1",
        "resource":"configmaps",
        "apiGroup":"UNKNOWN",
        "namespace":"dns-system",
        "name":"gpc-coredns-external-zonefile"
        },
      "requestReceivedTimestamp":"2022-11-11T22:02:02.034688Z",
      "requestURI":"/api/v1/namespaces/dns-system/configmaps/gpc-coredns-external-zonefile",
      "responseStatus":{
        "metadata":{},
        "code":200
        },
      "sourceIPs":["10.142.5.147"],
      "stage":"ResponseComplete",
      "stageTimestamp":"2022-11-11T22:02:02.045045Z",
      "ts":2022-11-11T22:02:02.074Z,
      "tsNs":1668204122074601081,
      "user":{
        "uid":"08f727c9-5e3d-403f-bf35-06ef53f9709c",
        "groups":[
          "system:serviceaccounts",
          "system:serviceaccounts:dns-system",
          "system:authenticated"
          ],
        "username": "system:serviceaccount:dns-system:dns-core-controller-sa",
        "extra": {
          "authentication.kubernetes.io/pod-name":["dns-core-controller-58c4646858-z8kmr"],
          "authentication.kubernetes.io/pod-uid":["17d9392a-bc27-4d6c-bab7-ff076a5457eb"]
          }
        },
      "userAgent":"controller-manager/v0.0.0 (linux/amd64) kubernetes/$Format",
      "verb":"update"
    }
    

## Create or delete a DNSSEC key

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user.username` |  For example,
    
    
    "user":{
      "username": "fop-dns@example.com"
      }  
  
**Target** _(Fields and values that call the API)_ | `requestURI` |  `"requestURI":"/api/v1/namespaces/dns-system/secrets/gpc-coredns-external-ksks"`  
**Action** _(Fields containing the performed operation)_ | `verb` |  `"verb":"update"`  
**Event timestamp** |  `ts` |  For example, `"ts":2022-11-11T22:02:02.074Z`  
**Source of action** | `sourceIPs` |  For example, `"sourceIPs":["10.142.5.147"]`  
**Outcome** | `responseStatus.code` |  For example,
    
    
    "responseStatus":{
      "code":200
      }  
  
**Other fields** | 

  * `annotations`
  * `objectRef`

|  For example,
    
    
    "annotations":{
      "authorization.k8s.io/decision":"allow"
      },
    "objectRef":{
      "resource": "secrets",
      "namespace":"dns-system",
      "uid":"9a9c16ca-3601-4bc9-8683-629a61ea5634",
      "apiVersion":"v1",
      "resourceVersion":"825911",
      "apiGroup":"UNKNOWN",
      "name":"gpc-coredns-external-ksks"
      }  
  
**Example log**
    
    
    {
      "_gdch_cluster":"root-admin",
      "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-t15kb",
      "_gdch_service_name":"apiserver",
      "annotations":{
        "authorization.k8s.io/decision":"allow",
        "authorization.k8s.io/reason":"RBAC: allowed by RoleBinding 'fop-dns@example.com-dns-key-manager/dns-system' of Role 'dns-key-manager' to User 'fop-dns@example.com'"
        },
      "apiVersion":"audit.k8s.io/v1",
      "auditID":"87d3d836-b5a2-487a-8480-bc8078c5b248",
      "kind":"Event",
      "level":"Metadata",
      "objectRef":{
        "resource": "secrets",
        "namespace":"dns-system",
        "uid":"9a9c16ca-3601-4bc9-8683-629a61ea5634",
        "apiVersion":"v1",
        "resourceVersion":"825911",
        "apiGroup":"UNKNOWN",
        "name":"gpc-coredns-external-ksks"
        },
      "requestReceivedTimestamp":"2022-11-11T22:02:02.034688Z",
      "requestURI":"/api/v1/namespaces/dns-system/secrets/gpc-coredns-external-ksks",
      "responseStatus":{
        "metadata":{},
        "code":200
        },
      "sourceIPs":["10.142.5.147"],
      "stage":"ResponseComplete",
      "stageTimestamp":"2022-11-11T22:02:02.045045Z",
      "ts":2022-11-11T22:02:02.074Z,
      "tsNs":1668204122074601081,
      "user":{
        "groups":[
          "system: authenticated"
          ],
        "username": "fop-dns@example.com"
        },
      "userAgent":"gdcloud/v0.0.0 (linux/amd64) kubernetes/$Format",
      "verb":"update"
    }
    

## Change a DNSSEC key

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user.username` |  For example,
    
    
    "user":{
      "username": "fop-dns@example.com"
      }  
  
**Target** _(Fields and values that call the API)_ | `requestURI` |  `"requestURI":"/api/v1/namespaces/dns-system/configmaps/gpc-coredns-external-corefile"`  
**Action** _(Fields containing the performed operation)_ | `verb` |  `"verb":"update"`  
**Event timestamp** |  `ts` |  For example, `"ts":2022-11-11T22:02:02.074Z`  
**Source of action** | `sourceIPs` |  For example, `"sourceIPs":["10.142.5.147"]`  
**Outcome** | `responseStatus.code` |  For example,
    
    
    "responseStatus":{
      "code":200
      }  
  
**Other fields** | 

  * `annotations`
  * `objectRef`

|  For example,
    
    
    "annotations":{
      "authorization.k8s.io/decision":"allow"
      },
    "objectRef":{
      "resourceVersion":"758987",
      "resource":"configmaps",
      "apiGroup":"UNKNOWN",
      "name":"gpc-coredns-external-corefile",
      "apiVersion":"v1",
      "namespace":"dns-system",
      "uid":"d831c851-4fa3-4£30-92f6-c68cb36b0c62"
      }  
  
**Example log**
    
    
    {
      "_gdch_cluster":"root-admin",
      "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-8z2rm",
      "_gdch_service_name":"apiserver",
      "annotations":{
        "authorization.k8s.io/decision":"allow",
        "authorization.k8s.io/reason":"RBAC: allowed by RoleBinding 'fop-dns@example.com-dns-key-manager/dns-system' of Role 'dns-key-manager' to User 'fop-dns@example.com'"
        },
      "apiVersion":"audit.k8s.io/v1",
      "auditID":"ba0344d7-283f-4d79-aabc-e083al9b053a",
      "kind":"Event",
      "level":"Metadata",
      "objectRef":{
        "resourceVersion":"758987",
        "resource":"configmaps",
        "apiGroup":"UNKNOWN",
        "name":"gpc-coredns-external- corefile",
        "apiVersion":"v1",
        "namespace":"dns-system",
        "uid":"d831c851-4fa3-4£30-92f6-c68cb36b0c62"
        },
      "requestReceivedTimestamp":"2022-11-11T22:02:02.034688Z",
      "requestURI":"/api/v1/namespaces/dns-system/configmaps/gpc-coredns-external-corefile",
      "responseStatus":{
        "metadata":{},
        "code":200
        },
      "sourceIPs":["10.142.5.147"],
      "stage":"ResponseComplete",
      "stageTimestamp":"2022-11-11T22:02:02.045045Z",
      "ts":2022-11-11T22:02:02.074Z,
      "tsNs":1668204122074601081,
      "user":{
        "groups":[
          "system: authenticated"
          ],
        "username": "fop-dns@example.com"
        },
      "userAgent":"gdcloud/v0.0.0 (linux/amd64) kubernetes/$Format",
      "verb":"update"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
