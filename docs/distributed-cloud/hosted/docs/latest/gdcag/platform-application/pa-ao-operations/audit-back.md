---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-back/
title: Backup and Restore (BACK) \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:20:07.343937+00:00
---

# Backup and Restore (BACK)  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-back/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Backup and Restore (BACK) Stay organized with collections  Save and categorize content based on your preferences. 

**Audit log source** |  [KRM API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-kubernetes)  
---|---  
**Audited operations** | 

  * Backup
  * BackupPlan
  * Restore
  * RestorePlan
  * ManualBackupRequest
  * ManualRestoreRequest
  * DeleteBackupRequest
  * BackupRepository
  * BackupRepositoryManager
  * VirtualMachineBackupPlan
  * VirtualMachineBackup
  * VirtualMachineRestore
  * MachineBackupPlanTemplate
  * VirtualMachineBackupRequest
  * VirtualMachineRestoreRequest
  * VirtualMachineDeleteBackupRequest

  
  
## Backup

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user": {
      "extra":{
        "authentication.kubernetes.io/pod-name": ["gpcbackup-controlplane-controller-8557fdb956-47zjb"],
        "authentication.kubernetes.io/pod-uid": ["f3aa711d-b09e-4863-90d6-3d6e7122f4a3"]
      },
      "username": "system:serviceaccount:gpc-backup-system:gpcbackup-controlplane-manager-sa",
      "groups": ["system:serviceaccounts","system:serviceaccounts:gpc-backup-system","system:authenticated"],"uid":"e77ab07e-a987-4ba3-ad7d-b3bf002125eb"
    }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` | 
    
    
    "objectRef": {
      "apiGroup":"backup.gdc.goog",
      "resource":"backups",
      "apiVersion":"v1",
      "name":"backup-test-2",
      "namespace":"default"
    }  
  
**Action** _(Fields containing the performed operation)_ | `verb` |  `"verb":"create"`  
**Event timestamp** |  `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp": "2023-08-21T14:56:43.549191Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster": "root-admin"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus": {
      "code":201,
      "metadata":{}
    }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
## BackupPlan

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user": {
      "groups":["system:masters","system:authenticated"],
      "username":"kubernetes-admin"
    }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` | 
    
    
    "objectRef": {
      "apiGroup":"backup.gdc.goog",
      "resource":"backupplans",
      "apiVersion":"v1",
      "name":"backupplan-test-2",
      "namespace":"default"
    }  
  
**Action** _(Fields containing the performed operation)_ | `verb` |  `"verb":"create"`  
**Event timestamp** |  `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp": "2023-08-21T14:56:43.549191Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster": "root-admin"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus": {
      "code":201,
      "metadata":{}
    }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
## Restore

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user": {
      "uid":"e77ab07e-a987-4ba3-ad7d-b3bf002125eb",
      "username":"system:serviceaccount:gpc-backup-system:gpcbackup-controlplane-manager-sa",
      "extra":{
        "authentication.kubernetes.io/pod-uid":["f3aa711d-b09e-4863-90d6-3d6e7122f4a3"],
        "authentication.kubernetes.io/pod-name":["gpcbackup-controlplane-controller-8557fdb956-47zjb"]
      },
      "groups":["system:serviceaccounts", "system:serviceaccounts:gpc-backup-system", "system:authenticated"]
    }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` | 
    
    
    "objectRef": {
      "apiGroup":"backup.gdc.goog",
      "apiVersion":"v1",
      "name":"restore-test-2",
      "resource":"restores",
      "namespace":"default"
    }  
  
**Action** _(Fields containing the performed operation)_ | `verb` |  `"verb":"create"`  
**Event timestamp** |  `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp": "2023-08-21T14:56:43.549191Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster": "root-admin"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus": {
      "code":201,
      "metadata":{}
    }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
## RestorePlan

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user": {
      "groups":["system:masters","system:authenticated"],
      "username":"kubernetes-admin"
    }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` | 
    
    
    "objectRef": {
      "namespace":"default",
      "apiGroup":"backup.gdc.goog",
      "resource":"restoreplans",
      "apiVersion":"v1",
      "name":"restoreplan-test-2"
    }  
  
**Action** _(Fields containing the performed operation)_ | `verb` |  `"verb":"create"`  
**Event timestamp** |  `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp": "2023-08-21T14:56:43.549191Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster": "root-admin"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus": {
      "code":201,
      "metadata":{}
    }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
## ManualBackupRequest

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user": {
      "groups":["system:masters","system:authenticated"],
      "username":"kubernetes-admin"
    }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` | 
    
    
    "objectRef": {
      "resource":"manualbackuprequests",
      "namespace":"default",
      "apiGroup":"backup.gdc.goog",
      "name":"manualbackuprequest-test-2",
      "apiVersion":"v1"
    }  
  
**Action** _(Fields containing the performed operation)_ | `verb` |  `"verb":"create"`  
**Event timestamp** |  `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp": "2023-08-21T14:56:43.549191Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster": "root-admin"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus": {
      "code":201,
      "metadata":{}
    }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
## ManualRestoreRequest

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user": {
      "groups":["system:masters","system:authenticated"],
      "username":"kubernetes-admin"
    }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` | 
    
    
    "objectRef": {
      "resource":"manualrestorerequests",
      "apiGroup":"backup.gdc.goog",
      "apiVersion":"v1",
      "name":"manualrestorerequest-test-2",
      "namespace":"default"
    }  
  
**Action** _(Fields containing the performed operation)_ | `verb` |  `"verb":"create"`  
**Event timestamp** |  `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp": "2023-08-21T14:56:43.549191Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster": "root-admin"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus": {
      "code":201,
      "metadata":{}
    }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
## DeleteBackupRequest

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user": {
      "groups":["system:masters","system:authenticated"],
      "username":"kubernetes-admin"
    }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` | 
    
    
    "objectRef": {
      "apiGroup":"backup.gdc.goog",
      "resource":"deletebackuprequests",
      "apiVersion":"v1",
      "name":"deletebackuprequest-test-2",
      "namespace":"default"
    }  
  
**Action** _(Fields containing the performed operation)_ | `verb` |  `"verb":"create"`  
**Event timestamp** |  `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp": "2023-08-21T14:56:43.549191Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster": "root-admin"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus": {
      "code":201,
      "metadata":{}
    }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
## BackupRepository

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user": {
      "groups":["system:masters","system:authenticated"],
      "username":"kubernetes-admin"
    }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` | 
    
    
    "objectRef": {
      "apiGroup":"backup.gdc.goog",
      "name":"default",
      "resource":"backuprepositories",
      "apiVersion":"v1"
    }  
  
**Action** _(Fields containing the performed operation)_ | `verb` |  `"verb":"create"`  
**Event timestamp** |  `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp": "2023-08-21T14:56:43.549191Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster": "root-admin"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus": {
      "code":201,
      "metadata":{}
    }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
## BackupRepositoryManager

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user": {
      "username":"kubernetes-admin",
      "groups":["system:masters","system:authenticated"]
    }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` | 
    
    
    "objectRef": {
      "name":"default",
      "resource":"backuprepositorymanagers",
      "apiVersion":"v1",
      "apiGroup":"backup.gdc.goog"
    }  
  
**Action** _(Fields containing the performed operation)_ | `verb` |  `"verb":"create"`  
**Event timestamp** |  `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp": "2023-08-21T14:56:43.549191Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster": "org-1-admin"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus": {
      "code":201,
      "metadata":{}
    }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
## VirtualMachineBackupPlan

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user": {
      "groups":["system:masters","system:authenticated"],
      "username":"kubernetes-admin"
    }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` | 
    
    
    "objectRef": {
      "apiGroup":"virtualmachine.gdc.goog",
      "apiVersion":"v1",
      "name":"vmbpt-vm-vm",
      "namespace":"default",
      "resource":"virtualmachinebackupplans"
    }  
  
**Action** _(Fields containing the performed operation)_ | `verb` |  `"verb":"create"`  
**Event timestamp** |  `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp": "2023-08-21T14:56:43.549191Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster": "org-1-system"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus": {
      "code":201,
      "metadata":{}
    }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
## VirtualMachineBackup

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user": {
      "groups":["system:masters","system:authenticated"],
      "username":"kubernetes-admin"
    }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` | 
    
    
    "objectRef": {
      "apiGroup":"virtualmachine.gdc.goog",
      "apiVersion":"v1",
      "name":"vm-backup-test",
      "namespace":"default",
      "resource":"virtualmachinebackups"
    }  
  
**Action** _(Fields containing the performed operation)_ | `verb` |  `"verb":"create"`  
**Event timestamp** |  `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp": "2023-08-21T14:56:43.549191Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster": "org-1-system"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus": {
      "code":201,
      "metadata":{}
    }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
## VirtualMachineRestore

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user": {
      "groups":["system:masters","system:authenticated"],
      "username":"kubernetes-admin"
    }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` | 
    
    
    "objectRef": {
      "apiGroup":"virtualmachine.gdc.goog",
      "apiVersion":"v1",
      "name":"vm-restore-test",
      "namespace":"default",
      "resource":"virtualmachinerestores"
    }  
  
**Action** _(Fields containing the performed operation)_ | `verb` |  `"verb":"create"`  
**Event timestamp** |  `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp": "2023-08-21T14:56:43.549191Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster": "org-1-system"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus": {
      "code":201,
      "metadata":{}
    }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
## MachineBackupPlanTemplate

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user": {
      "groups":["system:masters","system:authenticated"],
      "username":"kubernetes-admin"
    }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` | 
    
    
    "objectRef": {
      "apiGroup":"virtualmachine.gdc.goog",
      "apiVersion":"v1",
      "name":"vmbpt",
      "namespace":"default",
      "resource":"virtualmachinebackupplantemplates"
    }  
  
**Action** _(Fields containing the performed operation)_ | `verb` |  `"verb":"create"`  
**Event timestamp** |  `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp": "2023-08-21T14:56:43.549191Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster": "org-1-system"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus": {
      "code":201,
      "metadata":{}
    }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
## VirtualMachineBackupRequest

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user": {
      "groups":["system:masters","system:authenticated"],
      "username":"kubernetes-admin"
    }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` | 
    
    
    "objectRef": {
      "apiGroup":"virtualmachine.gdc.goog",
      "apiVersion":"v1",
      "name":"vmbr-test",
      "namespace":"default",
      "resource":"virtualmachinebackuprequests"
    }  
  
**Action** _(Fields containing the performed operation)_ | `verb` |  `"verb":"create"`  
**Event timestamp** |  `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp": "2023-08-21T14:56:43.549191Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster": "org-1-system"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus": {
      "code":201,
      "metadata":{}
    }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
## VirtualMachineRestoreRequest

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user": {
      "groups":["system:masters","system:authenticated"],
      "username":"kubernetes-admin"
    }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` | 
    
    
    "objectRef": {
      "apiGroup":"virtualmachine.gdc.goog",
      "apiVersion":"v1",
      "name":"vmrr-test",
      "namespace":"default",
      "resource":"virtualmachinerestorerequests"
    }  
  
**Action** _(Fields containing the performed operation)_ | `verb` |  `"verb":"create"`  
**Event timestamp** |  `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp": "2023-08-21T14:56:43.549191Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster": "org-1-system"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus": {
      "code":201,
      "metadata":{}
    }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
## VirtualMachineDeleteBackupRequest

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user": {
      "groups":["system:masters","system:authenticated"],
      "username":"kubernetes-admin"
    }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` | 
    
    
    "objectRef": {
      "apiGroup":"virtualmachine.gdc.goog",
      "apiVersion":"v1",
      "name":"vmdbr",
      "namespace":"default",
      "resource":"virtualmachinedeletebackuprequests"
    }  
  
**Action** _(Fields containing the performed operation)_ | `verb` |  `"verb":"create"`  
**Event timestamp** |  `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp": "2023-08-21T14:56:43.549191Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster": "org-1-system"`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus": {
      "code":201,
      "metadata":{}
    }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
## Example log
    
    
    {
      "api_group": "backup.gdc.goog",
      "cluster": "root-admin",
      "fluentbit_pod": "anthos-audit-logs-forwarder-h89tv",
      "service_name": "apiserver",
      "Time": 1692629803549,
      "_gdch_cluster": "root-admin",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-h89tv",
      "_gdch_org_id": "root.zone1.google.gdch.test",
      "_gdch_org_name": "root",
      "_gdch_service_name": "apiserver",
      "_gdch_tenant_id": "infra-obs",
      "annotations": {
        "authorization.k8s.io/decision":"allow","mutation.webhook.admission.k8s.io/round_0_index_2":"{\"configuration\":\"gatekeeper-mutating-webhook-configuration\",\"webhook\":\"mutation.gatekeeper.sh\",\"mutated\":false}","authorization.k8s.io/reason":"RBAC: allowed by ClusterRoleBinding \"gpcbackup-controlplane-manager-role\" of ClusterRole \"gpcbackup-controlplane-manager-role\" to ServiceAccount \"gpcbackup-controlplane-manager-sa/gpc-backup-system\""
      },
      "apiVersion": "audit.k8s.io/v1",
      "auditID": "856f47ac-f022-467f-82ea-55aa08d948e1",
      "kind": "Event",
      "level": "Metadata",
      "objectRef": {
        "apiGroup":"backup.gdc.goog",
        "resource":"backups",
        "apiVersion":"v1",
        "name":"backup-test-2",
        "namespace":"default"
      },
      "requestReceivedTimestamp": "2023-08-21T14:56:43.549191Z",
      "requestURI": "/apis/backup.gdc.goog/v1/namespaces/default/backups",
      "responseStatus": {
        "code":201,
        "metadata":{}
      },
      "sourceIPs": ["10.200.0.3"],
      "stage": "ResponseComplete",
      "stageTimestamp": "2023-08-21T14:56:43.560200Z",
      "tsNs": 1692629803549191000,
      "user": {
        "extra":{
          "authentication.kubernetes.io/pod-name":["gpcbackup-controlplane-controller-8557fdb956-47zjb"],
          "authentication.kubernetes.io/pod-uid":["f3aa711d-b09e-4863-90d6-3d6e7122f4a3"]
        },
        "username":"system:serviceaccount:gpc-backup-system:gpcbackup-controlplane-manager-sa",
        "groups":["system:serviceaccounts","system:serviceaccounts:gpc-backup-system","system:authenticated"],"uid":"e77ab07e-a987-4ba3-ad7d-b3bf002125eb"
      },
      "userAgent": "manager/v0.0.0 (linux/amd64) kubernetes/$Format",
      "verb": "create"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
