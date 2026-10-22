---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-iam/
title: Identity and access management (IAM) \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:49:25.188602+00:00
---

# Identity and access management (IAM)  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-iam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Identity and access management (IAM) Stay organized with collections  Save and categorize content based on your preferences. 

## Key exchange for STS token

**Log schema** : Istio

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `identity` | 
    
    
    \"user\":{\"identity\":\"system:serviceaccount:iam-test:service-account\"}  
  
**Target** _(Fields and values that call the API)_ | `resource` | 
    
    
    \"resource\":\"service-accounts.zone1.google.gdch.test\"  
  
**Action** _(Fields containing the performed operation)_ | _Not applicable_ |   
**Event timestamp** | `time` | 
    
    
    "time": "2022-11-23T18:25:54Z"  
  
**Source of action** | _Not applicable_ |   
**Outcome** | _Not applicable_ |   
**Other fields** | _Not applicable_ |   
  
## Audit logs CRUD operations on Kubernetes resources including creation of service accounts, and access control management.

**Log schema** : KRM API

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user/username` | 
    
    
    "user": {
        "groups": [
          "system:authenticated"
        ],
        "username": "fop-platform-admin@example.com"
      }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` | 
    
    
    "objectRef": {
        "resource": "projectserviceaccounts",
        "apiGroup": "resourcemanager.gdc.goog",
        "name": "service-accountt",
        "apiVersion": "v1alpha1",
        "namespace": "iam-test"
    }  
  
**Action** _(Fields containing the performed operation)_ | `verb` | 
    
    
    "verb": "create"  
  
**Event timestamp** | `requestReceivedTimestamp` | 
    
    
    "requestReceivedTimestamp": "2022-11-23T18:24:26.514173Z"  
  
**Source of action** | `sourceIPs` | 
    
    
    "sourceIPs": [
        "10.200.0.2"
      ]  
  
**Outcome** | `responseStatus` | 
    
    
    "responseStatus": {
        "code": 201,
        "metadata": {}
      }  
  
**Other fields** | `annotations/authorization.k8s.io/reason` | 
    
    
    "annotations": {
        "authorization.k8s.io/reason": "RBAC: allowed by RoleBinding \"platform-admin-project-iam-admin/iam-test\" of Role \"project-iam-admin\" to User \"fop-platform-admin@example.com\"",
        "authorization.k8s.io/decision": "allow"
      }  
  
## Audit Log when a user logs out

**Log schema** : Custom AIS format.

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `payload.user` | 
    
    
    "payload": {
          "expirationTime": "2023-08-29T12:42:36.848454939+00:00",
          "groups": [],
          "id": "7a5bea7a-0821-45d8-b4a0-69f24d30ab3f",
          "issuer": "Google OIDC",
          "user": "test-user"
        }  
  
**Target** _(Fields and values that call the API)_ | _Not applicable_ |   
**Action** _(Fields containing the performed operation)_ | `operation` | 
    
    
    "operation": "revoke"  
  
**Event timestamp** | `metadata.timestamp` | 
    
    
    "timestamp": "2023-08-29T00:42:40.000544813+00:00"  
  
**Source of action** | _Not applicable_ |   
**Outcome** | _Not applicable_ |   
**Other fields** | `expirationTime` | 
    
    
    "expirationTime": "2023-08-29T12:42:36.848454939+00:00"  
  
## Audit Log when a user logs in

**Log schema** : Custom AIS format.

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `payload.user` | 
    
    
    "payload": {
          "expirationTime": "2023-08-29T05:22:13.350779831+00:00",
          "groups": [],
          "id": "dcb7c5d9-c171-4f5b-84b6-5c92bfffb0e0",
          "issuer": "Azure AD SAML",
          "user": "test-ais-e2e-saml@byoidcloudaccountgoogle.onmicrosoft.com"
        }  
  
**Target** _(Fields and values that call the API)_ | _Not applicable_ |   
**Action** _(Fields containing the performed operation)_ | `operation` | 
    
    
    "operation": "create"  
  
**Event timestamp** | `metadata.timestamp` | 
    
    
    "timestamp": "2023-08-28T17:22:13.351713088+00:00"  
  
**Source of action** | _Not applicable_ |   
**Outcome** | _Not applicable_ |   
**Other fields** | `expirationTime` | 
    
    
    "expirationTime": "2023-08-29T05:22:13.350779831+00:00"  
  
## Audit Log when PA revokes sessions for a user

**Log schema** : Custom AIS format.

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `payload.admin / payload.user` | 
    
    
    "payload": {
          "admin": "test-user-1@gdch.com",
          "numSessionsAffected": 1,
          "peerWorkloadIdentity": "system:serviceaccount:anthos-identity-service:default",
          "peerWorkloadIdentityIssuer": "https://kubernetes.default.svc.cluster.local",
          "user": "test-user-2@gdch.com"
        }  
  
**Target** _(Fields and values that call the API)_ | `resource` | 
    
    
    "resource": "session"  
  
**Action** _(Fields containing the performed operation)_ | `operation` | 
    
    
    "operation": "revoke"  
  
**Event timestamp** | `metadata.timestamp` | 
    
    
    "timestamp": "2023-08-28T17:22:24.043644569+00:00"  
  
**Source of action** | _Not applicable_ |   
**Outcome** | _Not applicable_ |   
**Other fields** | `numSessionsAffected` | 
    
    
    "numSessionsAffected": 1  
  
## Example log IAM
    
    
    {
      "pri": "46",
      "_gdch_flbProcessedTimestamp": 1669227957.340494,
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-vk6vx",
      "time": "2022-11-23T18:25:54Z",
      "message": "{\"time\":\"2022-11-23T18:25:54.257503516Z\",\"auditID\":\"d1c33645-bed0-47dc-8180-06b752673109\",\"user\":{\"identity\":\"system:serviceaccount:iam-test:service-accountt\"},\"resource\":\"service-accounts.zone1.google.gdch.test\",\"description\":\"{\\\"keyID\\\":\\\"f9540561-84d5-4113-983f-fd8868501596\\\",\\\"expirationTime\\\":\\\"2022-11-24T06:25:53Z\\\"}\"}",
      "ident": "/service-identity-server",
      "pid": "1",
      "msgid": "audit-log",
      "extradata": "-",
      "_gdch_cluster": "root-admin",
      "host": "serviceidentity-sa-server-55544bd9f5-nwg8m",
      "_gdch_service_name": "service-identity-audit-logs"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
