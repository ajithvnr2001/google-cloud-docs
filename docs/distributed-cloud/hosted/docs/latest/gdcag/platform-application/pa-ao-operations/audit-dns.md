---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-dns/
title: Domain Name System (DNS) \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:14:05.220647+00:00
---

# Domain Name System (DNS)  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-dns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Domain Name System (DNS) Stay organized with collections  Save and categorize content based on your preferences. 

Domain Name System (DNS) audit logs in Google Distributed Cloud (GDC) air-gapped record CoreDNS zone updates along with `ManagedDNSZone` and `ResourceRecordSet` creation events. This document lists the audited operations, metadata fields, and example JSON payloads from Kubernetes audit logs for root and organization workloads.

**Workload location** |  Root and organization workloads  
---|---  
**Audit log source** |  [Kubernetes audit logs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-kubernetes)  
**Audited operations** | 

  * Update a zone
  * Create a ManagedDNSZone
  * Create a ResourceRecordSet

  
  
## Update a zone

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user.username` |  For example,
    
    
    "user":{
      "username": "dns@example.com"
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
        "uid":"08f727c9-5e3d-403f-bf35-06ef53f9832c",
        "groups":[
          "system:serviceaccounts",
          "system:serviceaccounts:dns-system",
          "system:authenticated"
          ],
        "username": "system:serviceaccount:dns-system:dns-core-controller-sa",
        "extra": {
          "authentication.kubernetes.io/pod-name":["dns-core-controller-58c4646858-z8kmr"],
          "authentication.kubernetes.io/pod-uid":["7cfc9b72-aacc-4e86-b43f-016498055230"]
          }
        },
      "userAgent":"controller-manager/v0.0.0 (linux/amd64) kubernetes/$Format",
      "verb":"update"
    }
    

## Create a ManagedDNSZone

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user.username` |  For example,
    
    
    "user":{
      "username": "system:bootstrap:xqk4xc"
      }  
  
**Target** _(Fields and values that call the API)_ | `requestURI` |  `"requestURI":"/apis/networking.global.gdc.goog/v1/namespaces/cloud-dns-2/manageddnszones?fieldManager=kubectl-create&fieldValidation=Strict"`  
**Action** _(Fields containing the performed operation)_ | `verb` |  `"verb":"create"`  
**Event timestamp** |  `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp":"2026-05-08T09:51:45.320229Z"`  
**Source of action** | `sourceIPs` |  For example, `"sourceIPs":["10.200.0.1","10.0.138.150"]`  
**Outcome** | `responseStatus.code` |  For example,
    
    
    "responseStatus":{
      "code":201
      }  
  
**Other fields** | 

  * `annotations`
  * `objectRef`

|  For example,
    
    
    "annotations":{
      "authorization.k8s.io/decision":"allow",
      "authorization.k8s.io/reason":"RBAC: allowed by ClusterRoleBinding \"e2e-test\" of ClusterRole \"cluster-admin\" to Group \"system:bootstrappers:gce-e2e\"",
      "mutation.webhook.admission.k8s.io/round_0_index_1":"{\"configuration\":\"gatekeeper-mutating-webhook-configuration\",\"webhook\":\"mutation.gatekeeper.sh\",\"mutated\":false}"
      },
    "objectRef":{
      "apiGroup":"networking.global.gdc.goog",
      "apiVersion":"v1",
      "name":"public-cf-zone-1",
      "namespace":"cloud-dns-2",
      "resource":"manageddnszones"
        }  
  
**Example log**
    
    
    {
      "_gdch_cluster": "org-1-admin",
      "_gdch_component": "user_kubectl",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-ttpfw",
      "_gdch_org_id": "org-1.zone1.google.gdch.test",
      "_gdch_org_name": "org-1",
      "_gdch_zone_id": "zone1",
      "annotations": {
        "authorization.k8s.io/decision": "allow",
        "authorization.k8s.io/reason": "RBAC: allowed by ClusterRoleBinding \"e2e-test\" of ClusterRole \"cluster-admin\" to Group \"system:bootstrappers:gce-e2e\"",
        "mutation.webhook.admission.k8s.io/round_0_index_1": "{\"configuration\":\"gatekeeper-mutating-webhook-configuration\",\"webhook\":\"mutation.gatekeeper.sh\",\"mutated\":false}"
      },
      "apiVersion": "audit.k8s.io/v1",
      "auditID": "3de6821e-4e40-4bbc-9c9c-285c59ddaa19",
      "kind": "Event",
      "level": "Request",
      "objectRef": {
        "apiGroup": "networking.global.gdc.goog",
        "apiVersion": "v1",
        "name": "public-cf-zone-1",
        "namespace": "cloud-dns-2",
        "resource": "manageddnszones"
      },
      "requestObject": {
        "apiVersion": "networking.global.gdc.goog/v1",
        "kind": "ManagedDNSZone",
        "metadata": {
          "creationTimestamp": null,
          "name": "public-cf-zone-1",
          "namespace": "cloud-dns-2"
        },
        "spec": {
          "description": "Public DNS zone for Cloud Foundry",
          "dnsName": "cf1.dns2",
          "visibility": "PUBLIC"
        }
      },
      "requestReceivedTimestamp": "2026-05-08T09:51:45.320229Z",
      "requestURI": "/apis/networking.global.gdc.goog/v1/namespaces/cloud-dns-2/manageddnszones?fieldManager=kubectl-create&fieldValidation=Strict",
      "responseStatus": {
        "code": 201,
        "metadata": {}
      },
      "sourceIPs": [
        "10.200.0.1",
        "10.0.138.150"
      ],
      "stage": "ResponseComplete",
      "stageTimestamp": "2026-05-08T09:51:45.528379Z",
      "user": {
        "groups": [
          "system:bootstrappers",
          "system:bootstrappers:gce-e2e",
          "system:authenticated"
        ],
        "username": "system:bootstrap:xqk4xc"
      },
      "userAgent": "kubectl/v1.28.3 (linux/amd64) kubernetes/a8a1abc",
      "verb": "create"
    }
    

## Create a ResourceRecordSet

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user.username` |  For example,
    
    
    "user":{
      "username": "system:serviceaccount:dns-system:dns-prober-sa"
      }  
  
**Target** _(Fields and values that call the API)_ | `requestURI` |  `"requestURI":"/apis/networking.global.gdc.goog/v1/namespaces/dns-system/resourcerecordsets"`  
**Action** _(Fields containing the performed operation)_ | `verb` |  `"verb":"create"`  
**Event timestamp** |  `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp":"2026-05-08T08:48:30.748194Z"`  
**Source of action** | `sourceIPs` |  For example, `"sourceIPs":["10.0.130.26","10.0.136.209"]`  
**Outcome** | `responseStatus.code` |  For example,
    
    
    "responseStatus":{
      "code":201
      }  
  
**Other fields** | 

  * `annotations`
  * `objectRef`

|  For example,
    
    
    "annotations":{
      "authorization.k8s.io/decision":"allow",
      "authorization.k8s.io/reason":"RBAC: allowed by RoleBinding \"dns-prober-global-prober-rolebinding/dns-system\" of Role \"dns-prober-global-prober-role\" to ServiceAccount \"dns-prober-sa/dns-system\"",
      "mutation.webhook.admission.k8s.io/round_0_index_0":"{\"configuration\":\"dns-managed-dns-v1-mutation\",\"webhook\":\"resourcerecordsets.networking.global.gdc.goog\",\"mutated\":true}",
      "mutation.webhook.admission.k8s.io/round_0_index_1":"{\"configuration\":\"gatekeeper-mutating-webhook-configuration\",\"webhook\":\"mutation.gatekeeper.sh\",\"mutated\":false}",
      "patch.webhook.admission.k8s.io/round_0_index_0":"{\"configuration\":\"dns-managed-dns-v1-mutation\",\"webhook\":\"resourcerecordsets.networking.global.gdc.goog\",\"patch\":[{\"op\":\"add\",\"path\":\"/metadata/creationTimestamp\",\"value\":null},{\"op\":\"add\",\"path\":\"/metadata/labels\",\"value\":{\"clouddns.private.gdc.goog/dnszone\":\"test.prober.private\"}},{\"op\":\"add\",\"path\":\"/metadata/annotations\",\"value\":{\"clouddns.private.gdc.goog/token\":\"synpi4vyatjbdwy2-a-pri\"}}],\"patchType\":\"JSONPatch\"}"
      },
    "objectRef":{
      "apiGroup":"networking.global.gdc.goog",
      "apiVersion":"v1",
      "name":"prober-test-rrs-zone1-private",
      "namespace":"dns-system",
      "resource":"resourcerecordsets"
        }  
  
**Example log**
    
    
    {
      "_gdch_cluster": "org-1-admin",
      "_gdch_component": "dns",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-ggwr5",
      "_gdch_org_id": "org-1.zone1.google.gdch.test",
      "_gdch_org_name": "org-1",
      "_gdch_zone_id": "zone1",
      "annotations": {
        "authorization.k8s.io/decision": "allow",
        "authorization.k8s.io/reason": "RBAC: allowed by RoleBinding \"dns-prober-global-prober-rolebinding/dns-system\" of Role \"dns-prober-global-prober-role\" to ServiceAccount \"dns-prober-sa/dns-system\"",
        "mutation.webhook.admission.k8s.io/round_0_index_0": "{\"configuration\":\"dns-managed-dns-v1-mutation\",\"webhook\":\"resourcerecordsets.networking.global.gdc.goog\",\"mutated\":true}",
        "mutation.webhook.admission.k8s.io/round_0_index_1": "{\"configuration\":\"gatekeeper-mutating-webhook-configuration\",\"webhook\":\"mutation.gatekeeper.sh\",\"mutated\":false}",
        "patch.webhook.admission.k8s.io/round_0_index_0": "{\"configuration\":\"dns-managed-dns-v1-mutation\",\"webhook\":\"resourcerecordsets.networking.global.gdc.goog\",\"patch\":[{\"op\":\"add\",\"path\":\"/metadata/creationTimestamp\",\"value\":null},{\"op\":\"add\",\"path\":\"/metadata/labels\",\"value\":{\"clouddns.private.gdc.goog/dnszone\":\"test.prober.private\"}},{\"op\":\"add\",\"path\":\"/metadata/annotations\",\"value\":{\"clouddns.private.gdc.goog/token\":\"synpi4vyatjbdwy2-a-pri\"}}],\"patchType\":\"JSONPatch\"}"
      },
      "apiVersion": "audit.k8s.io/v1",
      "auditID": "12851275-a785-41fa-8e2b-8469bd9d1f65",
      "kind": "Event",
      "level": "Request",
      "objectRef": {
        "apiGroup": "networking.global.gdc.goog",
        "apiVersion": "v1",
        "name": "prober-test-rrs-zone1-private",
        "namespace": "dns-system",
        "resource": "resourcerecordsets"
      },
      "requestObject": {
        "apiVersion": "networking.global.gdc.goog/v1",
        "kind": "ResourceRecordSet",
        "metadata": {
          "creationTimestamp": null,
          "name": "prober-test-rrs-zone1-private",
          "namespace": "dns-system"
        },
        "spec": {
          "dnsZone": "prober-test-managed-dns-private",
          "name": "prober-test-rrs-zone1-private.test.prober.private",
          "rrData": [
            "192.168.100.100"
          ],
          "ttlSeconds": 30,
          "type": "A"
        },
        "status": {
          "rollout": {
            "strategy": {
              "type": ""
            }
          }
        }
      },
      "requestReceivedTimestamp": "2026-05-08T08:48:30.748194Z",
      "requestURI": "/apis/networking.global.gdc.goog/v1/namespaces/dns-system/resourcerecordsets",
      "responseStatus": {
        "code": 201,
        "metadata": {}
      },
      "sourceIPs": [
        "10.0.130.26",
        "10.0.136.209"
      ],
      "stage": "ResponseComplete",
      "stageTimestamp": "2026-05-08T08:48:30.964607Z",
      "user": {
        "extra": {
          "__AIS_token_issuer_zone": [
            "zone1"
          ]
        },
        "groups": [
          "system:authenticated"
        ],
        "username": "system:serviceaccount:dns-system:dns-prober-sa"
      },
      "userAgent": "prober/v0.0.0 (linux/amd64) kubernetes/$Format",
      "verb": "create"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
