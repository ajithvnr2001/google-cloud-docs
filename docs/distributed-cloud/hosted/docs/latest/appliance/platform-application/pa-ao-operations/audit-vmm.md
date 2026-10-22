---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/audit-vmm/
title: Virtual Machine Management (VMM) \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:08.833165+00:00
---

# Virtual Machine Management (VMM)  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/audit-vmm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Virtual Machine Management (VMM) Stay organized with collections  Save and categorize content based on your preferences. 

**Workload location** |  Organization workloads  
---|---  
**Audit log source** |  [Kubernetes audit logs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/audit-kubernetes)  
**Audited operations** | 

  * Create a VM
  * List VMs
  * Update a VM
  * Delete a VM
  * Create a VM disk
  * List VM disks
  * Delete a VM disk
  * List VM types
  * Create a VM type
  * Delete a VM type
  * Update a VM type
  * Create a VM access request
  * List VM access requests
  * Delete a VM access request
  * List VM images
  * Create a VM image import
  * List VM image imports
  * Delete a VM image import
  * Create an external access policy
  * List external access policies
  * Update an external access policy
  * Delete an external access policy
  * Restart a VM
  * Review emergency access actions from an Infrastructure Operator (IO)

  
  
## Create a VM

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user": {
        "groups": [
          "system:authenticated"
        ],
        "username": "fop-myusername"
        }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` |  For example,
    
    
    "objectRef": {
        "apiGroup": "virtualmachine.gdc.goog",
        "apiVersion": "v1",
        "name": "vm1",
        "namespace": "myusername-test",
        "resource": "virtualmachines"
        }  
  
**Action** _(Fields containing the performed operation)_ | `verb` | `"verb": "create"`  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp": "2023-09-19T21:16:11.086606Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster": "org-infrastructure-cluster"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus": {
        "code": 201,
        "metadata": {}
        }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "_gdch_cluster": "org-infrastructure-cluster",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-tzdxt",
      "_gdch_org_id": "zone1.google.gdch.test",
      "_gdch_org_name": "root",
      "annotations": {
        "authorization.k8s.io/decision": "allow",
        "authorization.k8s.io/reason": "RBAC: allowed by RoleBinding \"fop-myusername-vm-admin/myusername-test\" of Role \"project-vm-admin\" to User \"fop-myusername\"",
        "mutation.webhook.admission.k8s.io/round_0_index_12": "{\"configuration\":\"gatekeeper-mutating-webhook-configuration\",\"webhook\":\"mutation.gatekeeper.sh\",\"mutated\":false}"
      },
      "apiVersion": "audit.k8s.io/v1",
      "auditID": "6b48ee52-baa4-47d1-9357-98d1bf7bee7e",
      "kind": "Event",
      "level": "Metadata",
      "objectRef": {
        "apiGroup": "virtualmachine.gdc.goog",
        "apiVersion": "v1",
        "name": "vm1",
        "namespace": "myusername-test",
        "resource": "virtualmachines"
      },
      "requestReceivedTimestamp": "2023-09-19T21:16:11.086606Z",
      "requestURI": "/apis/virtualmachine.gdc.goog/v1/namespaces/myusername-test/virtualmachines?fieldManager=kubectl-client-side-apply",
      "responseStatus": {
        "code": 201,
        "metadata": {}
      },
      "sourceIPs": [
        "10.200.0.1",
        "10.200.0.6"
      ],
      "stage": "ResponseComplete",
      "stageTimestamp": "2023-09-19T21:16:11.097294Z",
      "user": {
        "groups": [
          "system:authenticated"
        ],
        "username": "fop-myusername"
      },
      "userAgent": "kubectl/v1.23.5 (linux/amd64) kubernetes/c285e78",
      "verb": "create"
    }
    

## List VMs

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user": {
        "groups": [
          "system:authenticated"
        ],
        "username": "fop-myusername"
        }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` |  For example,
    
    
    "objectRef": {
        "apiGroup": "virtualmachine.gdc.goog",
        "apiVersion": "v1",
        "namespace": "myusername-test",
        "resource": "virtualmachines"
        }  
  
**Action** _(Fields containing the performed operation)_ | `verb` | `"verb": "list"`  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp": "2023-09-19T21:37:40.632532Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster": "org-infrastructure-cluster"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus": {
        "code": 200,
        "metadata": {}
        }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "_gdch_cluster": "org-infrastructure-cluster",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-tzdxt",
      "_gdch_org_id": "zone1.google.gdch.test",
      "_gdch_org_name": "root",
      "annotations": {
        "authorization.k8s.io/decision": "allow",
        "authorization.k8s.io/reason": "RBAC: allowed by RoleBinding \"fop-myusername-vm-admin/myusername-test\" of Role \"project-vm-admin\" to User \"fop-myusername\""
      },
      "apiVersion": "audit.k8s.io/v1",
      "auditID": "e848a3a1-da7e-4b74-8c12-f2af066dda55",
      "kind": "Event",
      "level": "Metadata",
      "objectRef": {
        "apiGroup": "virtualmachine.gdc.goog",
        "apiVersion": "v1",
        "namespace": "myusername-test",
        "resource": "virtualmachines"
      },
      "requestReceivedTimestamp": "2023-09-19T21:37:40.632532Z",
      "requestURI": "/apis/virtualmachine.gdc.goog/v1/namespaces/myusername-test/virtualmachines?limit=500",
      "responseStatus": {
        "code": 200,
        "metadata": {}
      },
      "sourceIPs": [
        "10.200.0.1",
        "10.200.0.6"
      ],
      "stage": "ResponseComplete",
      "stageTimestamp": "2023-09-19T21:37:40.639807Z",
      "user": {
        "groups": [
          "system:authenticated"
        ],
        "username": "fop-myusername"
      },
      "userAgent": "kubectl/v1.23.5 (linux/amd64) kubernetes/c285e78",
      "verb": "list"
    }
    

## Update a VM

This includes start/stop operations. A restart operation also shows up as two update operations (stop and start) by a service account.

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user":{
        "username": "fop-myname-test",
        "groups":[
          "system: authenticated"
          ]
        }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` |  For example,
    
    
    "objectRef": {
        "apiGroup": "virtualmachine.gdc.goog",
        "apiVersion": "v1",
        "name": "vm1",
        "namespace": "myusername-test",
        "resource": "virtualmachines"
        }  
  
**Action** _(Fields containing the performed operation)_ | `verb` | `"verb": "patch"`  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp": "2023-09-19T21:42:20.229318Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster": "org-infrastructure-cluster"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus": {
        "code": 415,
        "message": "the body of the request was in an unknown format - accepted media types include: application/json-patch+json, application/merge-patch+json, application/apply-patch+yaml",
        "metadata": {},
        "reason": "UnsupportedMediaType",
        "status": "Failure"
        }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "_gdch_cluster": "org-infrastructure-cluster",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-rxgp7",
      "_gdch_org_id": "zone1.google.gdch.test",
      "_gdch_org_name": "root",
      "annotations": {
        "authorization.k8s.io/decision": "allow",
        "authorization.k8s.io/reason": "RBAC: allowed by ClusterRoleBinding \"vmm-controller\" of ClusterRole \"vmm-controller\" to ServiceAccount \"vmm-controller/vm-system\""
      },
      "apiVersion": "audit.k8s.io/v1",
      "auditID": "f094a667-adc8-46cf-9ce7-e0f534b792a9",
      "kind": "Event",
      "level": "Metadata",
      "objectRef": {
        "apiGroup": "virtualmachine.gdc.goog",
        "apiVersion": "v1",
        "name": "vm1",
        "namespace": "myusername-test",
        "resource": "virtualmachines"
      },
      "requestReceivedTimestamp": "2023-09-19T21:42:20.229318Z",
      "requestURI": "/apis/virtualmachine.gdc.goog/v1/namespaces/myusername-test/virtualmachines/vm1",
      "responseStatus": {
        "code": 415,
        "message": "the body of the request was in an unknown format - accepted media types include: application/json-patch+json, application/merge-patch+json, application/apply-patch+yaml",
        "metadata": {},
        "reason": "UnsupportedMediaType",
        "status": "Failure"
      },
      "sourceIPs": [
        "10.201.64.17"
      ],
      "stage": "ResponseComplete",
      "stageTimestamp": "2023-09-19T21:42:20.230057Z",
      "user": {
        "extra": {
          "authentication.kubernetes.io/pod-name": [
            "vmm-controller-588b67d499-p7qzv"
          ],
          "authentication.kubernetes.io/pod-uid": [
            "b5bec7d9-d813-4c9d-a2c6-7c8b2ab7ae9c"
          ]
        },
        "groups": [
          "system:serviceaccounts",
          "system:serviceaccounts:vm-system",
          "system:authenticated"
        ],
        "uid": "24a689d1-aabb-4738-9576-eb3a56e5c3d4",
        "username": "system:serviceaccount:vm-system:vmm-controller"
      },
      "userAgent": "vmm-controller/v0.0.0 (linux/amd64) kubernetes/$Format",
      "verb": "patch"
    }
    

## Delete a VM

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user": {
        "groups": [
          "system:masters",
          "system:authenticated"
        ],
        "username": "kubernetes-admin"
        }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` |  For example,
    
    
    "objectRef": {
        "apiGroup": "virtualmachine.gdc.goog",
        "apiVersion": "v1",
        "name": "vm1",
        "namespace": "myusername-test",
        "resource": "virtualmachines"
        }  
  
**Action** _(Fields containing the performed operation)_ | `verb` | `"verb": "delete"`  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp": "2023-09-19T20:58:25.165020Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster": "org-infrastructure-cluster"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus": {
        "code": 200,
        "metadata": {}
        }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "_gdch_cluster": "org-infrastructure-cluster",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-tzdxt",
      "_gdch_org_id": "zone1.google.gdch.test",
      "_gdch_org_name": "root",
      "annotations": {
        "authorization.k8s.io/decision": "allow",
        "authorization.k8s.io/reason": ""
      },
      "apiVersion": "audit.k8s.io/v1",
      "auditID": "b487c3cf-3eda-4cc9-bb5f-1d9665038ee0",
      "kind": "Event",
      "level": "Metadata",
      "objectRef": {
        "apiGroup": "virtualmachine.gdc.goog",
        "apiVersion": "v1",
        "name": "vm1",
        "namespace": "myusername-test",
        "resource": "virtualmachines"
      },
      "requestReceivedTimestamp": "2023-09-19T20:58:25.165020Z",
      "requestURI": "/apis/virtualmachine.gdc.goog/v1/namespaces/myusername-test/virtualmachines/vm1",
      "responseStatus": {
        "code": 200,
        "metadata": {}
      },
      "sourceIPs": [
        "10.200.0.6"
      ],
      "stage": "ResponseComplete",
      "stageTimestamp": "2023-09-19T20:58:25.181044Z",
      "user": {
        "groups": [
          "system:masters",
          "system:authenticated"
        ],
        "username": "kubernetes-admin"
      },
      "userAgent": "kubectl/v1.23.5 (linux/amd64) kubernetes/c285e78",
      "verb": "delete"
    }
    

## Create a VM disk

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user": {
        "groups": [
          "system:authenticated"
        ],
        "username": "fop-myusername"
        }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` |  For example,
    
    
    "objectRef": {
        "apiGroup": "virtualmachine.gdc.goog",
        "apiVersion": "v1",
        "name": "vm1-boot-disk",
        "namespace": "myusername-test",
        "resource": "virtualmachinedisks"
        }  
  
**Action** _(Fields containing the performed operation)_ | `verb` | `"verb": "create"`  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp": "2023-09-19T21:16:11.056904Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster": "org-infrastructure-cluster"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus": {
        "code": 201,
        "metadata": {}
        }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "_gdch_cluster": "org-infrastructure-cluster",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-tzdxt",
      "_gdch_org_id": "zone1.google.gdch.test",
      "_gdch_org_name": "root",
      "annotations": {
        "authorization.k8s.io/decision": "allow",
        "authorization.k8s.io/reason": "RBAC: allowed by RoleBinding \"fop-myusername-vm-admin/myusername-test\" of Role \"project-vm-admin\" to User \"fop-myusername\"",
        "mutation.webhook.admission.k8s.io/round_0_index_12": "{\"configuration\":\"gatekeeper-mutating-webhook-configuration\",\"webhook\":\"mutation.gatekeeper.sh\",\"mutated\":false}"
      },
      "apiVersion": "audit.k8s.io/v1",
      "auditID": "b304923c-1df4-4184-bafd-40161210e85e",
      "kind": "Event",
      "level": "Metadata",
      "objectRef": {
        "apiGroup": "virtualmachine.gdc.goog",
        "apiVersion": "v1",
        "name": "vm1-boot-disk",
        "namespace": "myusername-test",
        "resource": "virtualmachinedisks"
      },
      "requestReceivedTimestamp": "2023-09-19T21:16:11.056904Z",
      "requestURI": "/apis/virtualmachine.gdc.goog/v1/namespaces/myusername-test/virtualmachinedisks?fieldManager=kubectl-client-side-apply",
      "responseStatus": {
        "code": 201,
        "metadata": {}
      },
      "sourceIPs": [
        "10.200.0.1",
        "10.200.0.6"
      ],
      "stage": "ResponseComplete",
      "stageTimestamp": "2023-09-19T21:16:11.071123Z",
      "user": {
        "groups": [
          "system:authenticated"
        ],
        "username": "fop-myusername"
      },
      "userAgent": "kubectl/v1.23.5 (linux/amd64) kubernetes/c285e78",
      "verb": "create"
    }
    

## List VM disks

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user": {
        "groups": [
          "system:authenticated"
        ],
        "username": "fop-myusername"
        }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` |  For example,
    
    
    "objectRef": {
        "apiGroup": "virtualmachine.gdc.goog",
        "apiVersion": "v1",
        "namespace": "myusername-test",
        "resource": "virtualmachinedisks"
        }  
  
**Action** _(Fields containing the performed operation)_ | `verb` | `"verb": "list"`  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp": "2023-09-19T21:18:43.108931Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster": "org-infrastructure-cluster"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus": {
        "code": 200,
        "metadata": {}
        }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "_gdch_cluster": "org-infrastructure-cluster",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-l7p8r",
      "_gdch_org_id": "zone1.google.gdch.test",
      "_gdch_org_name": "root",
      "annotations": {
        "authorization.k8s.io/decision": "allow",
        "authorization.k8s.io/reason": "RBAC: allowed by RoleBinding \"fop-myusername-vm-admin/myusername-test\" of Role \"project-vm-admin\" to User \"fop-myusername\""
      },
      "apiVersion": "audit.k8s.io/v1",
      "auditID": "3d71f7fd-11d0-4ed7-9d8c-a9bf9f61b46d",
      "kind": "Event",
      "level": "Metadata",
      "objectRef": {
        "apiGroup": "virtualmachine.gdc.goog",
        "apiVersion": "v1",
        "namespace": "myusername-test",
        "resource": "virtualmachinedisks"
      },
      "requestReceivedTimestamp": "2023-09-19T21:18:43.108931Z",
      "requestURI": "/apis/virtualmachine.gdc.goog/v1/namespaces/myusername-test/virtualmachinedisks?limit=500",
      "responseStatus": {
        "code": 200,
        "metadata": {}
      },
      "sourceIPs": [
        "10.200.0.1",
        "10.200.0.7"
      ],
      "stage": "ResponseComplete",
      "stageTimestamp": "2023-09-19T21:18:43.137015Z",
      "user": {
        "groups": [
          "system:authenticated"
        ],
        "username": "fop-myusername"
      },
      "userAgent": "kubectl/v1.23.5 (linux/amd64) kubernetes/c285e78",
      "verb": "list"
    }
    

## Delete a VM disk

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user":{
        "username": "fop-myname-test",
        "groups":[
          "system: authenticated"
          ]
        }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` |  For example,
    
    
    "objectRef":{
        "namespace":"foo",
        "resource":"virtualmachinedisks",
        "apiGroup":"virtualmachine.gdc.goog",
        "name":"vm1-boot-disk",
        "apiVersion":"v1"
        }  
  
**Action** _(Fields containing the performed operation)_ | `verb` | `"verb":"delete"`  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp":"2022-11-11T22:02:02.034688Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster":"org-infrastructure-cluster"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus":{
        "metadata":{},
        "code":200
        }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "_gdch_cluster":"org-infrastructure-cluster",
      "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-8z2rm",
      "_gdch_service_name":"apiserver",
      "apiVersion":"audit.k8s.io/v1",
      "auditID":"ba0344d7-283f-4d79-aabc-e083al9b053a",
      "kind":"Event",
      "level":"Metadata",
      "objectRef":{
        "namespace":"foo",
        "resource":"virtualmachinedisks",
        "apiGroup":"virtualmachine.gdc.goog",
        "apiVersion":"v1",
        "name":"vm1-boot-disk"
        },
      "requestReceivedTimestamp":"2022-11-11T22:02:02.034688Z",
      "requestURI":"/apis/virtualmachine.gdc.goog/v1/namespaces/foo/virtualmachinedisks/vm1-boot-disk",
      "responseStatus":{
        "metadata":{},
        "code":200
        },
      "sourceIPs":["10.142.5.147"],
      "stage":"ResponseComplete",
      "stageTimestamp":"2022-11-11T22:02:02.045045Z",
      "tsNs":1668204122074601081,
      "user":{
        "username": "fop-myname-test",
        "groups":[
          "system: authenticated"
          ]
        },
      "userAgent":"kubectl/v1.23.5 (linux/amd64) kubernetes/c285e78",
      "verb":"delete"
    }
    

## List VM types

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user":{
        "username": "fop-myname-test",
        "groups":[
          "system: authenticated"
          ]
        }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` |  For example,
    
    
    "objectRef":{
        "resource":"virtualmachinetypes",
        "apiGroup":"virtualmachine.gdc.goog",
        "apiVersion":"v1"
        }  
  
**Action** _(Fields containing the performed operation)_ | `verb` | `"verb":"list"`  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp":"2022-11-11T22:02:02.034688Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster":"org-infrastructure-cluster"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus":{
        "metadata":{},
        "code":200
        }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "_gdch_cluster":"org-infrastructure-cluster",
      "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-8z2rm",
      "_gdch_service_name":"apiserver",
      "annotations":{
        "authorization.k8s.io/decision":"allow",
        "authorization.k8s.io/reason":"RBAC: allowed by RoleBinding 'g-vm-admin-binding/foo' of Role 'g-vm-admin' to User 'fop-myname-test'"
        },
      "apiVersion":"audit.k8s.io/v1",
      "auditID":"ba0344d7-283f-4d79-aabc-e083al9b053a",
      "kind":"Event",
      "level":"Metadata",
      "objectRef":{
        "resource":"virtualmachinetypes",
        "apiGroup":"virtualmachine.gdc.goog",
        "apiVersion":"v1"
        },
      "requestReceivedTimestamp":"2022-11-11T22:02:02.034688Z",
      "requestURI":"/apis/virtualmachine.gdc.goog/v1/virtualmachinetypes?limit=500",
      "responseStatus":{
        "metadata":{},
        "code":200
        },
      "sourceIPs":["10.142.5.147"],
      "stage":"ResponseComplete",
      "stageTimestamp":"2022-11-11T22:02:02.045045Z",
      "tsNs":1668204122074601081,
      "user":{
        "username": "fop-myname-test",
        "groups":[
          "system: authenticated"
          ]
        },
      "userAgent":"kubectl/v1.23.5 (linux/amd64) kubernetes/c285e78",
      "verb":"list"
    }
    

## Create a VM type

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user":{
        "username": "fop-myname-test",
        "groups":[
          "system: authenticated"
          ]
        }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` |  For example,
    
    
    "objectRef":{
        "resource":"virtualmachinetypes",
        "apiGroup":"virtualmachine.gdc.goog",
        "name":"test-type",
        "apiVersion":"v1"
        }  
  
**Action** _(Fields containing the performed operation)_ | `verb` | `"verb":"create"`  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp":"2022-11-11T22:02:02.034688Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster":"org-infrastructure-cluster"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus":{
        "metadata":{},
        "code":201
        }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "_gdch_cluster":"org-infrastructure-cluster",
      "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-8z2rm",
      "_gdch_service_name":"apiserver",
      "annotations":{
        "authorization.k8s.io/decision":"allow",
        "authorization.k8s.io/reason":"RBAC: allowed by ClusterRoleBinding 'g-pa-system-binding' of ClusterRole 'g-system-cluster-admin' to User 'fop-myname-test'"
        },
      "apiVersion":"audit.k8s.io/v1",
      "auditID":"ba0344d7-283f-4d79-aabc-e083al9b053a",
      "kind":"Event",
      "level":"Metadata",
      "objectRef":{
        "resource":"virtualmachinetypes",
        "apiGroup":"virtualmachine.gdc.goog",
        "name":"test-type",
        "apiVersion":"v1"
        },
      "requestReceivedTimestamp":"2022-11-11T22:02:02.034688Z",
      "requestURI":"/apis/virtualmachine.gdc.goog/v1/virtualmachinetypes?fieldManager=kubectl-client-side-apply",
      "responseStatus":{
        "metadata":{},
        "code":201
        },
      "sourceIPs":["10.142.5.147"],
      "stage":"ResponseComplete",
      "stageTimestamp":"2022-11-11T22:02:02.045045Z",
      "tsNs":1668204122074601081,
      "user":{
        "username": "fop-myname-test",
        "groups":[
          "system: authenticated"
          ]
        },
      "userAgent":"kubectl/v1.23.5 (linux/amd64) kubernetes/c285e78",
      "verb":"create"
    }
    

## Delete a VM type

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user":{
        "username": "fop-myname-test",
        "groups":[
          "system: authenticated"
          ]
        }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` |  For example,
    
    
    "objectRef":{
        "resource":"virtualmachinetypes",
        "apiGroup":"virtualmachine.gdc.goog",
        "name":"test-type",
        "apiVersion":"v1"
        }  
  
**Action** _(Fields containing the performed operation)_ | `verb` | `"verb":"delete"`  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp":"2022-11-11T22:02:02.034688Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster":"org-infrastructure-cluster"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus":{
        "metadata":{},
        "code":200,
        "status":"Success"
        }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "_gdch_cluster":"org-infrastructure-cluster",
      "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-8z2rm",
      "_gdch_service_name":"apiserver",
      "annotations":{
        "authorization.k8s.io/decision":"allow",
        "authorization.k8s.io/reason":"RBAC: allowed by ClusterRoleBinding 'g-pa-system-binding' of ClusterRole 'g-system-cluster-admin' to User 'fop-myname-test'"
        },
      "apiVersion":"audit.k8s.io/v1",
      "auditID":"ba0344d7-283f-4d79-aabc-e083al9b053a",
      "kind":"Event",
      "level":"Metadata",
      "objectRef":{
        "resource":"virtualmachinetypes",
        "apiGroup":"virtualmachine.gdc.goog",
        "name":"test-type",
        "apiVersion":"v1"
        },
      "requestReceivedTimestamp":"2022-11-11T22:02:02.034688Z",
      "requestURI":"/apis/virtualmachine.gdc.goog/v1/virtualmachinetypes/test-type",
      "responseStatus":{
        "metadata":{},
        "code":200,
        "status":"Success"
        },
      "sourceIPs":["10.142.5.147"],
      "stage":"ResponseComplete",
      "stageTimestamp":"2022-11-11T22:02:02.045045Z",
      "tsNs":1668204122074601081,
      "user":{
        "username": "fop-myname-test",
        "groups":[
          "system: authenticated"
          ]
        },
      "userAgent":"kubectl/v1.23.5 (linux/amd64) kubernetes/c285e78",
      "verb":"delete"
    }
    

## Update a VM type

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user":{
        "username": "fop-myname-test",
        "groups":[
          "system: authenticated"
          ]
        }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` |  For example,
    
    
    "objectRef":{
        "resource":"virtualmachinetypes",
        "apiGroup":"virtualmachine.gdc.goog",
        "name":"test-type",
        "apiVersion":"v1"
        }  
  
**Action** _(Fields containing the performed operation)_ | `verb` | `"verb":"patch"`  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp":"2022-11-11T22:02:02.034688Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster":"org-infrastructure-cluster"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus":{
        "metadata":{},
        "code":200
        }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "_gdch_cluster":"org-infrastructure-cluster",
      "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-8z2rm",
      "_gdch_service_name":"apiserver",
      "annotations":{
        "authorization.k8s.io/decision":"allow",
        "authorization.k8s.io/reason":"RBAC: allowed by ClusterRoleBinding 'g-pa-system-binding' of ClusterRole 'g-system-cluster-admin' to User 'fop-myname-test'"
        },
      "apiVersion":"audit.k8s.io/v1",
      "auditID":"ba0344d7-283f-4d79-aabc-e083al9b053a",
      "kind":"Event",
      "level":"Metadata",
      "objectRef":{
        "resource":"virtualmachinetypes",
        "apiGroup":"virtualmachine.gdc.goog",
        "name":"test-type",
        "apiVersion":"v1"
        },
      "requestReceivedTimestamp":"2022-11-11T22:02:02.034688Z",
      "requestURI":"/apis/virtualmachine.gdc.goog/v1/virtualmachinetypes/test-type?fieldManager=kubectl-client-side-apply",
      "responseStatus":{
        "metadata":{},
        "code":200
        },
      "sourceIPs":["10.142.5.147"],
      "stage":"ResponseComplete",
      "stageTimestamp":"2022-11-11T22:02:02.045045Z",
      "tsNs":1668204122074601081,
      "user":{
        "username": "fop-myname-test",
        "groups":[
          "system: authenticated"
          ]
        },
      "userAgent":"kubectl/v1.23.5 (linux/amd64) kubernetes/c285e78",
      "verb":"patch"
    }
    

## Create a VM access request

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user":{
        "username": "fop-myname-test",
        "groups":[
          "system: authenticated"
          ]
        }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` |  For example,
    
    
    "objectRef":{
        "namespace":"foo",
        "resource":"virtualmachineaccessrequests",
        "apiGroup":"virtualmachine.gdc.goog",
        "apiVersion":"v1"
        }  
  
**Action** _(Fields containing the performed operation)_ | `verb` | `"verb":"create"`  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp":"2022-11-11T22:02:02.034688Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster":"org-infrastructure-cluster"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus":{
        "metadata":{},
        "code":201
        }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "_gdch_cluster":"org-infrastructure-cluster",
      "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-8z2rm",
      "_gdch_service_name":"apiserver",
      "annotations":{
        "authorization.k8s.io/decision":"allow",
        "authorization.k8s.io/reason":"RBAC: allowed by RoleBinding 'g-vm-admin-binding/foo' of Role 'g-vm-admin' to User 'fop-myname-test'"
        },
      "apiVersion":"audit.k8s.io/v1",
      "auditID":"ba0344d7-283f-4d79-aabc-e083al9b053a",
      "kind":"Event",
      "level":"Metadata",
      "objectRef":{
        "namespace":"foo",
        "resource":"virtualmachineaccessrequests",
        "apiGroup":"virtualmachine.gdc.goog",
        "apiVersion":"v1"
        },
      "requestReceivedTimestamp":"2022-11-11T22:02:02.034688Z",
      "requestURI":"/apis/virtualmachine.gdc.goog/v1/namespaces/foo/virtualmachineaccessrequests?fieldManager=kubectl-create",
      "responseStatus":{
        "metadata":{},
        "code":201
        },
      "sourceIPs":["10.142.5.147"],
      "stage":"ResponseComplete",
      "stageTimestamp":"2022-11-11T22:02:02.045045Z",
      "tsNs":1668204122074601081,
      "user":{
        "username": "fop-myname-test",
        "groups":[
          "system: authenticated"
          ]
        },
      "userAgent":"kubectl/v1.23.5 (linux/amd64) kubernetes/c285e78",
      "verb":"create"
    }
    

## List VM access requests

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user":{
        "username": "fop-myname-test",
        "groups":[
          "system: authenticated"
          ]
        }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` |  For example,
    
    
    "objectRef":{
        "namespace":"foo",
        "resource":"virtualmachineaccessrequests",
        "apiGroup":"virtualmachine.gdc.goog",
        "apiVersion":"v1"
        }  
  
**Action** _(Fields containing the performed operation)_ | `verb` | `"verb":"list"`  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp":"2022-11-11T22:02:02.034688Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster":"org-infrastructure-cluster"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus":{
        "metadata":{},
        "code":200
        }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "_gdch_cluster":"org-infrastructure-cluster",
      "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-8z2rm",
      "_gdch_service_name":"apiserver",
      "annotations":{
        "authorization.k8s.io/decision":"allow",
        "authorization.k8s.io/reason":"RBAC: allowed by RoleBinding 'g-vm-admin-binding/foo' of Role 'g-vm-admin' to User 'fop-myname-test'"
        },
      "apiVersion":"audit.k8s.io/v1",
      "auditID":"ba0344d7-283f-4d79-aabc-e083al9b053a",
      "kind":"Event",
      "level":"Metadata",
      "objectRef":{
        "namespace":"foo",
        "resource":"virtualmachineaccessrequests",
        "apiGroup":"virtualmachine.gdc.goog",
        "apiVersion":"v1"
        },
      "requestReceivedTimestamp":"2022-11-11T22:02:02.034688Z",
      "requestURI":"/apis/virtualmachine.gdc.goog/v1/namespaces/foo/virtualmachineaccessrequests?limit=500",
      "responseStatus":{
        "metadata":{},
        "code":200
        },
      "sourceIPs":["10.142.5.147"],
      "stage":"ResponseComplete",
      "stageTimestamp":"2022-11-11T22:02:02.045045Z",
      "tsNs":1668204122074601081,
      "user":{
        "username": "fop-myname-test",
        "groups":[
          "system: authenticated"
          ]
        },
      "userAgent":"kubectl/v1.23.5 (linux/amd64) kubernetes/c285e78",
      "verb":"list"
    }
    

## Delete a VM access request

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user":{
        "username": "fop-myname-test",
        "groups":[
          "system: authenticated"
          ]
        }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` |  For example,
    
    
    "objectRef":{
        "namespace":"foo",
        "resource":"virtualmachineaccessrequests",
        "apiGroup":"virtualmachine.gdc.goog",
        "name":"vm1-jdc9c",
        "apiVersion":"v1"
        }  
  
**Action** _(Fields containing the performed operation)_ | `verb` | `"verb":"delete"`  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp":"2022-11-11T22:02:02.034688Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster":"org-infrastructure-cluster"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus":{
        "metadata":{},
        "code":200
        }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "_gdch_cluster":"org-infrastructure-cluster",
      "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-8z2rm",
      "_gdch_service_name":"apiserver",
      "annotations":{
        "authorization.k8s.io/decision":"allow",
        "authorization.k8s.io/reason":"RBAC: allowed by RoleBinding 'g-vm-admin-binding/foo' of Role 'g-vm-admin' to User 'fop-myname-test'"
        },
      "apiVersion":"audit.k8s.io/v1",
      "auditID":"ba0344d7-283f-4d79-aabc-e083al9b053a",
      "kind":"Event",
      "level":"Metadata",
      "objectRef":{
        "namespace":"foo",
        "resource":"virtualmachineaccessrequests",
        "apiGroup":"virtualmachine.gdc.goog",
        "name":"vm1-jdc9c",
        "apiVersion":"v1"
        },
      "requestReceivedTimestamp":"2022-11-11T22:02:02.034688Z",
      "requestURI":"/apis/virtualmachine.gdc.goog/v1/namespaces/foo/virtualmachineaccessrequests/vm1-jdc9c",
      "responseStatus":{
        "metadata":{},
        "code":200
        },
      "sourceIPs":["10.142.5.147"],
      "stage":"ResponseComplete",
      "stageTimestamp":"2022-11-11T22:02:02.045045Z",
      "tsNs":1668204122074601081,
      "user":{
        "username": "fop-myname-test",
        "groups":[
          "system: authenticated"
          ]
        },
      "userAgent":"kubectl/v1.23.5 (linux/amd64) kubernetes/c285e78",
      "verb":"delete"
    }
    

## List VM images

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user":{
      "username": "system:serviceaccount:gatekeeper-system:gatekeeper-admin",
      "uid":"225d02e7-ee06-42c9-a561-df1945d83224",
      "groups":[
        "system:serviceaccounts",
        "system:serviceaccounts:gatekeeper-system",
        "system: authenticated"
        ]
      }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` |  For example,
    
    
    "objectRef":{
      "resource":"virtualmachineimage",
      "apiGroup":"virtualmachineview.gdc.goog",
      "apiVersion":"v1alpha1"
      }  
  
**Action** _(Fields containing the performed operation)_ | `verb` | `"verb":"list"`  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp":"2022-11-11T22:02:02.034688Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster":"org-infrastructure-cluster"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus":{
        "metadata":{},
        "code":200
        }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "_gdch_cluster":"org-infrastructure-cluster",
      "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-8z2rm",
      "_gdch_service_name":"apiserver",
      "annotations":{
        "authorization.k8s.io/decision":"allow",
        "authorization.k8s.io/reason":"RBAC: allowed by ClusterRoleBinding 'gatekeeper-manager-rolebinding' of ClusterRole 'gatekeeper-manager-role' to ServiceAccount 'gatekeeper-admin/gatekeeper-system'"
        },
      "apiVersion":"audit.k8s.io/v1",
      "auditID":"ba0344d7-283f-4d79-aabc-e083al9b053a",
      "kind":"Event",
      "level":"Metadata",
      "objectRef":{
        "resource":"virtualmachineimage",
        "apiGroup":"virtualmachineview.gdc.goog",
        "apiVersion":"v1alpha1"
        },
      "requestReceivedTimestamp":"2022-11-11T22:02:02.034688Z",
      "requestURI":"/apis/virtualmachineview.gdc.goog/v1alpha1/virtualmachineimage?limit=500",
      "responseStatus":{
        "metadata":{},
        "code":200
        },
      "sourceIPs":["10.142.5.147"],
      "stage":"ResponseComplete",
      "stageTimestamp":"2022-11-11T22:02:02.045045Z",
      "tsNs":1668204122074601081,
      "user":{
        "username": "system:serviceaccount:gatekeeper-system:gatekeeper-admin",
        "uid":"225d02e7-ee06-42c9-a561-df1945d83224",
        "groups":[
          "system:serviceaccounts",
          "system:serviceaccounts:gatekeeper-system",
          "system: authenticated"
          ]
        },
      "userAgent":"gatekeeper/v3.7.0 (linux/amd64) 3ba8e93/2021-11-15T20:59:44Z",
      "verb":"list"
    }
    

## Create a VM image import

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user":{
      "username": "kubernetes-admin",
      "groups":[
        "system:masters",
        "system: authenticated"
        ]
      }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` |  For example,
    
    
    "objectRef":{
      "namespace":"foo",
      "resource":"virtualmachineimageimports",
      "apiGroup":"virtualmachine.gdc.goog",
      "apiVersion":"v1alpha1",
      "name":"import-1"
      }  
  
**Action** _(Fields containing the performed operation)_ | `verb` | `"verb":"create"`  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp":"2022-11-11T22:02:02.034688Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster":"org-infrastructure-cluster"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus":{
        "metadata":{},
        "code":201
        }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "_gdch_cluster":"org-infrastructure-cluster",
      "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-8z2rm",
      "_gdch_service_name":"apiserver",
      "annotations":{
        "apiserver.latency.k8s.io/response-write":"1.476μs",
        "authorization.k8s.io/reason":"",
        "apiserver.latency.k8s.io/serialize-response-object":"71.971μs",
        "authorization.k8s.io/decision":"allow",
        "apiserver.latency.k8s.io/total":"7.405669466s",
        "apiserver.latency.k8s.io/validating-webhook":"7.395358418s",
        "apiserver.latency.k8s.io/transform-response-object":"2.358μs"
        },
      "apiVersion":"audit.k8s.io/v1",
      "auditID":"ba0344d7-283f-4d79-aabc-e083al9b053a",
      "kind":"Event",
      "level":"Metadata",
      "objectRef":{
        "namespace":"foo",
        "resource":"virtualmachineimageimports",
        "apiGroup":"virtualmachine.gdc.goog",
        "apiVersion":"v1alpha1",
        "name":"import-1"
        },
      "requestReceivedTimestamp":"2022-11-11T22:02:02.034688Z",
      "requestURI":"/apis/virtualmachine.gdc.goog/v1alpha1/namespaces/foo/virtualmachineimageimports?fieldManager=kubectl-client-side-apply",
      "responseStatus":{
        "metadata":{},
        "code":201
        },
      "sourceIPs":["10.142.5.147"],
      "stage":"ResponseComplete",
      "stageTimestamp":"2022-11-11T22:02:02.045045Z",
      "tsNs":1668204122074601081,
      "user":{
        "username": "kubernetes-admin",
        "groups":[
          "system:masters",
          "system: authenticated"
          ]
        },
      "userAgent":"kubectl/v1.23.5 (linux/amd64) kubernetes/c285e78",
      "verb":"create"
    }
    

## List VM image imports

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user":{
      "username": "system:serviceaccount:gatekeeper-system:gatekeeper-admin",
      "groups":[
        "system:serviceaccounts",
        "system:serviceaccounts:gatekeeper-system",
        "system: authenticated"
        ]
      }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` |  For example,
    
    
    "objectRef":{
      "resource":"virtualmachineimageimports",
      "apiGroup":"virtualmachine.gdc.goog",
      "apiVersion":"v1alpha1"
      }  
  
**Action** _(Fields containing the performed operation)_ | `verb` | `"verb":"list"`  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp":"2022-11-11T22:02:02.034688Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster":"org-infrastructure-cluster"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus":{
        "metadata":{},
        "code":201
        }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "_gdch_cluster":"org-infrastructure-cluster",
      "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-8z2rm",
      "_gdch_service_name":"apiserver",
      "apiVersion":"audit.k8s.io/v1",
      "auditID":"ba0344d7-283f-4d79-aabc-e083al9b053a",
      "kind":"Event",
      "level":"Metadata",
      "objectRef":{
        "resource":"virtualmachineimageimports",
        "apiGroup":"virtualmachine.gdc.goog",
        "apiVersion":"v1alpha1"
        },
      "requestReceivedTimestamp":"2022-11-11T22:02:02.034688Z",
      "requestURI":"/apis/virtualmachine.gdc.goog/v1alpha1/virtualmachineimageimports?limit=500",
      "responseStatus":{
        "metadata":{},
        "code":201
        },
      "sourceIPs":["10.142.5.147"],
      "stage":"ResponseComplete",
      "stageTimestamp":"2022-11-11T22:02:02.045045Z",
      "tsNs":1668204122074601081,
      "user":{
        "username": "system:serviceaccount:gatekeeper-system:gatekeeper-admin",
        "groups":[
          "system:serviceaccounts",
          "system:serviceaccounts:gatekeeper-system",
          "system: authenticated"
          ]
        },
      "userAgent":"gatekeeper/v3.7.0 (linux/amd64) 3ba8e93/2021-11-15T20:59:44Z",
      "verb":"list"
    }
    

## Delete a VM image import

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user":{
      "username": "kubernetes-admin",
      "groups":[
        "system:masters",
        "system: authenticated"
        ]
      }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` |  For example,
    
    
    "objectRef":{
      "namespace":"foo",
      "resource":"virtualmachineimageimports",
      "apiGroup":"virtualmachine.gdc.goog",
      "name":"import-1",
      "apiVersion":"v1alpha1"
      }  
  
**Action** _(Fields containing the performed operation)_ | `verb` | `"verb":"delete"`  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp":"2022-11-11T22:02:02.034688Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster":"org-infrastructure-cluster"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus":{
        "metadata":{},
        "code":200
        }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "_gdch_cluster":"org-infrastructure-cluster",
      "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-8z2rm",
      "_gdch_service_name":"apiserver",
      "apiVersion":"audit.k8s.io/v1",
      "auditID":"ba0344d7-283f-4d79-aabc-e083al9b053a",
      "kind":"Event",
      "level":"Metadata",
      "objectRef":{
        "namespace":"foo",
        "resource":"virtualmachineimageimports",
        "apiGroup":"virtualmachine.gdc.goog",
        "name":"import-1",
        "apiVersion":"v1alpha1"
        },
      "requestReceivedTimestamp":"2022-11-11T22:02:02.034688Z",
      "requestURI":"/apis/virtualmachine.gdc.goog/v1alpha1/namespaces/foo/virtualmachineimageimports/import-1",
      "responseStatus":{
        "metadata":{},
        "code":200
        },
      "sourceIPs":["10.142.5.147"],
      "stage":"ResponseComplete",
      "stageTimestamp":"2022-11-11T22:02:02.045045Z",
      "tsNs":1668204122074601081,
      "user":{
        "username": "kubernetes-admin",
        "groups":[
          "system:masters",
          "system: authenticated"
          ]
        },
      "userAgent":"kubectl/v1.23.5 (linux/amd64) kubernetes/c285e78",
      "verb":"delete"
    }
    

## Create an external access policy

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user": {
        "groups": [
          "system:masters",
          "system:authenticated"
        ],
        "username": "kubernetes-admin"
        }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` |  For example,
    
    
    "objectRef": {
        "apiGroup": "virtualmachine.gdc.goog",
        "apiVersion": "v1",
        "name": "vm1",
        "namespace": "myusername-test",
        "resource": "virtualmachineexternalaccesses"
        }  
  
**Action** _(Fields containing the performed operation)_ | `verb` | `"verb": "create"`  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp": "2023-09-20T16:58:09.485136Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster": "org-infrastructure-cluster"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus": {
        "code": 201,
        "metadata": {}
        }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "_gdch_cluster": "org-infrastructure-cluster",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-tzdxt",
      "_gdch_org_id": "zone1.google.gdch.test",
      "_gdch_org_name": "root",
      "annotations": {
        "authorization.k8s.io/decision": "allow",
        "authorization.k8s.io/reason": "",
        "mutation.webhook.admission.k8s.io/round_0_index_12": "{\"configuration\":\"gatekeeper-mutating-webhook-configuration\",\"webhook\":\"mutation.gatekeeper.sh\",\"mutated\":false}"
      },
      "apiVersion": "audit.k8s.io/v1",
      "auditID": "07306f01-f06e-44bf-ae6d-45447b14ea23",
      "kind": "Event",
      "level": "Metadata",
      "objectRef": {
        "apiGroup": "virtualmachine.gdc.goog",
        "apiVersion": "v1",
        "name": "vm1",
        "namespace": "myusername-test",
        "resource": "virtualmachineexternalaccesses"
      },
      "requestReceivedTimestamp": "2023-09-20T16:58:09.485136Z",
      "requestURI": "/apis/virtualmachine.gdc.goog/v1/namespaces/myusername-test/virtualmachineexternalaccesses?fieldManager=kubectl-create",
      "responseStatus": {
        "code": 201,
        "metadata": {}
      },
      "sourceIPs": [
        "10.200.0.6"
      ],
      "stage": "ResponseComplete",
      "stageTimestamp": "2023-09-20T16:58:09.501959Z",
      "user": {
        "groups": [
          "system:masters",
          "system:authenticated"
        ],
        "username": "kubernetes-admin"
      },
      "userAgent": "kubectl/v1.23.5 (linux/amd64) kubernetes/c285e78",
      "verb": "create"
    }
    

## List external access policies

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user": {
        "groups": [
          "system:masters",
          "system:authenticated"
        ],
        "username": "kubernetes-admin"
        }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` |  For example,
    
    
    "objectRef": {
        "apiGroup": "virtualmachine.gdc.goog",
        "apiVersion": "v1",
        "namespace": "myusername-test",
        "resource": "virtualmachineexternalaccesses"
        }  
  
**Action** _(Fields containing the performed operation)_ | `verb` | `"verb": "list"`  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp": "2023-09-20T17:06:35.634144Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster": "org-infrastructure-cluster"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus": {
        "code": 200,
        "metadata": {}
        }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "_gdch_cluster": "org-infrastructure-cluster",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-tzdxt",
      "_gdch_org_id": "zone1.google.gdch.test",
      "_gdch_org_name": "root",
      "annotations": {
        "authorization.k8s.io/decision": "allow",
        "authorization.k8s.io/reason": ""
      },
      "apiVersion": "audit.k8s.io/v1",
      "auditID": "a7396e5b-eeee-4821-9b59-c50c98de8137",
      "kind": "Event",
      "level": "Metadata",
      "objectRef": {
        "apiGroup": "virtualmachine.gdc.goog",
        "apiVersion": "v1",
        "namespace": "myusername-test",
        "resource": "virtualmachineexternalaccesses"
      },
      "requestReceivedTimestamp": "2023-09-20T17:06:35.634144Z",
      "requestURI": "/apis/virtualmachine.gdc.goog/v1/namespaces/myusername-test/virtualmachineexternalaccesses?limit=500",
      "responseStatus": {
        "code": 200,
        "metadata": {}
      },
      "sourceIPs": [
        "10.200.0.6"
      ],
      "stage": "ResponseComplete",
      "stageTimestamp": "2023-09-20T17:06:35.637132Z",
      "user": {
        "groups": [
          "system:masters",
          "system:authenticated"
        ],
        "username": "kubernetes-admin"
      },
      "userAgent": "kubectl/v1.23.5 (linux/amd64) kubernetes/c285e78",
      "verb": "list"
    }
    

## Update an external access policy

This includes start/stop operations. A restart operation also shows up as two update operations (stop and start) by a service account.

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user":{
        "groups": [
          "system:masters",
          "system:authenticated"
        ],
        "username": "kubernetes-admin"
        }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` |  For example,
    
    
    "objectRef": {
        "apiGroup": "virtualmachine.gdc.goog",
        "apiVersion": "v1",
        "name": "vm1",
        "namespace": "myusername-test",
        "resource": "virtualmachineexternalaccesses"
        }  
  
**Action** _(Fields containing the performed operation)_ | `verb` | `"verb": "patch"`  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp": "2023-09-20T17:11:00.525104Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster": "org-infrastructure-cluster"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus": {
        "code": 200,
        "metadata": {}
        }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "_gdch_cluster": "org-infrastructure-cluster",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-tzdxt",
      "_gdch_org_id": "zone1.google.gdch.test",
      "_gdch_org_name": "root",
      "annotations": {
        "authorization.k8s.io/decision": "allow",
        "authorization.k8s.io/reason": "",
        "mutation.webhook.admission.k8s.io/round_0_index_12": "{\"configuration\":\"gatekeeper-mutating-webhook-configuration\",\"webhook\":\"mutation.gatekeeper.sh\",\"mutated\":false}"
      },
      "apiVersion": "audit.k8s.io/v1",
      "auditID": "e42f6bbb-f192-4119-a674-66e0d1826dfa",
      "kind": "Event",
      "level": "Metadata",
      "objectRef": {
        "apiGroup": "virtualmachine.gdc.goog",
        "apiVersion": "v1",
        "name": "vm1",
        "namespace": "myusername-test",
        "resource": "virtualmachineexternalaccesses"
      },
      "requestReceivedTimestamp": "2023-09-20T17:11:00.525104Z",
      "requestURI": "/apis/virtualmachine.gdc.goog/v1/namespaces/myusername-test/virtualmachineexternalaccesses/vm1?fieldManager=kubectl-edit",
      "responseStatus": {
        "code": 200,
        "metadata": {}
      },
      "sourceIPs": [
        "10.200.0.6"
      ],
      "stage": "ResponseComplete",
      "stageTimestamp": "2023-09-20T17:11:00.538170Z",
      "user": {
        "groups": [
          "system:masters",
          "system:authenticated"
        ],
        "username": "kubernetes-admin"
      },
      "userAgent": "kubectl/v1.23.5 (linux/amd64) kubernetes/c285e78",
      "verb": "patch"
    }
    

## Delete an external access policy

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user": {
        "groups": [
          "system:masters",
          "system:authenticated"
        ],
        "username": "kubernetes-admin"
        }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` |  For example,
    
    
    "objectRef": {
        "apiGroup": "virtualmachine.gdc.goog",
        "apiVersion": "v1",
        "name": "vm1",
        "namespace": "myusername-test",
        "resource": "virtualmachineexternalaccesses"
        }  
  
**Action** _(Fields containing the performed operation)_ | `verb` | `"verb": "delete"`  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp": "2023-09-20T17:13:21.317256Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster": "org-infrastructure-cluster"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus": {
        "code": 200,
        "details": {
          "group": "virtualmachine.gdc.goog",
          "kind": "virtualmachineexternalaccesses",
          "name": "vm1",
          "uid": "d34ef0ad-f889-458f-804f-0086468a0674"
        },
        "metadata": {},
        "status": "Success"
        }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "_gdch_cluster": "org-infrastructure-cluster",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-tzdxt",
      "_gdch_org_id": "zone1.google.gdch.test",
      "_gdch_org_name": "root",
      "annotations": {
        "authorization.k8s.io/decision": "allow",
        "authorization.k8s.io/reason": ""
      },
      "apiVersion": "audit.k8s.io/v1",
      "auditID": "8290dc63-7aa9-4ab8-92eb-92b2ae6cabca",
      "kind": "Event",
      "level": "Metadata",
      "objectRef": {
        "apiGroup": "virtualmachine.gdc.goog",
        "apiVersion": "v1",
        "name": "vm1",
        "namespace": "myusername-test",
        "resource": "virtualmachineexternalaccesses"
      },
      "requestReceivedTimestamp": "2023-09-20T17:13:21.317256Z",
      "requestURI": "/apis/virtualmachine.gdc.goog/v1/namespaces/myusername-test/virtualmachineexternalaccesses/vm1",
      "responseStatus": {
        "code": 200,
        "details": {
          "group": "virtualmachine.gdc.goog",
          "kind": "virtualmachineexternalaccesses",
          "name": "vm1",
          "uid": "d34ef0ad-f889-458f-804f-0086468a0674"
        },
        "metadata": {},
        "status": "Success"
      },
      "sourceIPs": [
        "10.200.0.6"
      ],
      "stage": "ResponseComplete",
      "stageTimestamp": "2023-09-20T17:13:21.330032Z",
      "user": {
        "groups": [
          "system:masters",
          "system:authenticated"
        ],
        "username": "kubernetes-admin"
      },
      "userAgent": "kubectl/v1.23.5 (linux/amd64) kubernetes/c285e78",
      "verb": "delete"
    }
    

## Restart a VM

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user": {
        "groups": [
          "system:authenticated"
        ],
        "username": "fop-myusername"
        }  
  
**Target** _(Fields and values that call the API)_ | `requestURI` |  It has the following format: `"requestURI": "/apis/virtualmachineoperations.gdc.goog/v1/namespaces/namespace/virtualmachines/name/restart"` Where namespace and name identify the target object. For example, `"requestURI": "/apis/virtualmachineoperations.gdc.goog/v1/namespaces/myusername-test/virtualmachines/vm1/restart"`  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp": "2023-09-19T22:27:26.787243Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster": "org-infrastructure-cluster"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus": {
        "code": 202,
        "metadata": {}
        }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "_gdch_cluster": "org-infrastructure-cluster",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-rxgp7",
      "_gdch_org_id": "zone1.google.gdch.test",
      "_gdch_org_name": "root",
      "annotations": {
        "authorization.k8s.io/decision": "allow",
        "authorization.k8s.io/reason": "RBAC: allowed by RoleBinding \"fop-myusername-vm-admin/myusername-test\" of Role \"project-vm-admin\" to User \"fop-myusername\""
      },
      "apiVersion": "audit.k8s.io/v1",
      "auditID": "1446c6b9-f728-4f0d-9a70-aa8361749eef",
      "kind": "Event",
      "level": "Metadata",
      "objectRef": {
        "apiGroup": "virtualmachineoperations.gdc.goog",
        "apiVersion": "v1",
        "name": "vm1",
        "namespace": "myusername-test",
        "resource": "virtualmachines",
        "subresource": "restart"
      },
      "requestReceivedTimestamp": "2023-09-19T22:27:26.787243Z",
      "requestURI": "/apis/virtualmachineoperations.gdc.goog/v1/namespaces/myusername-test/virtualmachines/vm1/restart",
      "responseStatus": {
        "code": 202,
        "metadata": {}
      },
      "sourceIPs": [
        "10.200.0.1",
        "10.200.0.5"
      ],
      "stage": "ResponseComplete",
      "stageTimestamp": "2023-09-19T22:27:26.929619Z",
      "user": {
        "groups": [
          "system:authenticated"
        ],
        "username": "fop-myusername"
      },
      "userAgent": "Go-http-client/2.0",
      "verb": "update"
    }
    

## Review emergency access actions from an IO

The Infrastructure Operator (IO) has permissions to perform all the VMM audited operations described in this document on the Management API server. All their actions are audit logged automatically as part of the Kubernetes audit log.

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user": {
      "groups": [
        "system:masters",
        "system:authenticated"
        ],
      "username": "kubernetes-admin"
      }  
  
**Target** _(Fields and values that call the API)_ |  `objectRef` The VM specific resources have the following pattern for the `objectRef.apiGroup`: `"virtualmachine.gdc.goog|.*kubevirt.*|.*cdi.*"` |  For example,
    
    
    "objectRef": {
      "resource": "vmruntimes",
      "apiGroup": "virtualmachine.private.gdc.goog",
      "apiVersion": "v1"
      }  
  
**Action** _(Fields containing the performed operation)_ | `verb` | `"verb":"list"`  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp":"2022-11-30T00:47:09.472822Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster":"org-infrastructure-cluster"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus": {
      "code": 200,
      "metadata": {}
      }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "_gdch_cluster": "org-infrastructure-cluster",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-ztsnr",
      "responseStatus": {
        "code": 200,
        "metadata": {}
      },
      "kind": "Event",
      "stageTimestamp": "2022-11-30T00:47:09.475563Z",
      "annotations": {
        "authorization.k8s.io/decision": "allow",
        "authorization.k8s.io/reason": ""
      },
      "sourceIPs": [
        "10.200.1.109"
      ],
      "objectRef": {
        "resource": "vmruntimes",
        "apiGroup": "virtualmachine.private.gdc.goog",
        "apiVersion": "v1"
      },
      "apiVersion": "audit.k8s.io/v1",
      "verb": "list",
      "auditID": "fe338dca-f502-4fde-ba25-98bd29341a83",
      "level": "Metadata",
      "requestURI": "/apis/virtualmachine.private.gdc.goog/v1/vmruntimes",
      "user": {
        "groups": [
          "system:masters",
          "system:authenticated"
        ],
        "username": "kubernetes-admin"
      },
      "stage": "ResponseComplete",
      "requestReceivedTimestamp": "2022-11-30T00:47:09.472822Z",
      "userAgent": "operator/v0.0.0 (linux/amd64) kubernetes/$Format",
      "_gdch_service_name": "apiserver"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
