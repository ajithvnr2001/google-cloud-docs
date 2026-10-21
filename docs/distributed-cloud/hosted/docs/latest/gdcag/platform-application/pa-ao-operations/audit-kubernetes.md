---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-kubernetes/
title: Kubernetes audit logs \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:40:18.651966+00:00
---

# Kubernetes audit logs  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-kubernetes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Kubernetes audit logs Stay organized with collections  Save and categorize content based on your preferences. 

Audit logs in Google Distributed Cloud (GDC) air-gapped record a chronological, security-relevant sequence of API requests across your Kubernetes clusters. This document extracts the JSON schema and field definitions from the public upstream specification. For the full Go reference, see [`type Event` of the audit package](https://pkg.go.dev/k8s.io/apiserver/pkg/apis/audit#Event). 

**JSON representation**
    
    
    {
      "kind": string,
      "apiVersion": string,
      "level": string,
      "auditID": string,
      "stage": string,
      "requestURI": string,
      "verb": string,
      "user": {
        object
      },
      "sourceIPs": [
        string array
      ],
      "userAgent": string,
      "objectRef": {
        object
      },
      "requestReceivedTimestamp": string,
      "stageTimestamp": string,
      "hostname": string
    }
    

Fields  
---  
`kind` |  `string` The Kubernetes object type that is automatically generated in response to changes with other resources. For example, `"Event"`  
`apiVersion` |  `string` The version of the API group that contains the referred object. For example, `"audit.k8s.io/v1"`  
`level` |  `string` The audit level at which the event occurred. For example, `"Metadata"`  
`auditID` |  `string` The unique audit identification value, generated for each request. For example, `"c5f48f91-d4da-4659-97eb-56bdbcd0817c"`  
`stage` |  `string` The stage of the request handling when the event instance was generated. For example, `"RequestReceived"`  
`requestURI` |  `string` The request URI that the client sends to a server. For example, `"/apis/fleet.gpc.gke.io/v1/namespaces/gpc-system/fleets/root?fieldManager=kubectl-edit"`  
`verb` |  `string` The Kubernetes verb associated with the request. For non-resource requests, this value is the lower-cased HTTP method.

  * `"verb": "create"`
  * `"verb": "delete"`
  * `"verb": "get"`
  * `"verb": "list"`
  * `"verb": "patch"`
  * `"verb": "update"`
  * `"verb": "watch"`

  
`user` |  `object` Information about username and groups of the authenticated user. For example,
    
    
    {
      "username": "kubernetes-admin",
      "groups": [
        "system:masters",
        "system:authenticated"
      ]
    }  
  
`sourceIPs` |  `string array` Array of IPs from where the request originated and all the intermediate proxies. The source IPs are presented in the following ordered list:

  1. X-Forwarded-For request header IPs
  2. X-Real-IP header, if not present in the X-Forwarded-For list
  3. The remote address for the connection, if it doesn't match the last IP in the list up to here

All but the last IP can be arbitrarily set by the client. For example, `["10.200.0.3"]`  
`userAgent` |  `string` The user agent string that the client reports. For example, `"kubectl/v1.19.4 (linux/amd64) kubernetes/d360454"`  
`objectRef` |  `object` Information about the object reference that the request targets. For example,
    
    
    {
      "resource": "fleets",
      "namespace": "gpc-system",
      "name": "root",
      "apiGroup": "fleet.gpc.gke.io",
      "apiVersion": "v1"
    }  
  
`requestReceivedTimestamp` |  `string` The time when the request reached the Kubernetes apiserver. For example, `"2022-05-05T05:38:57.155218Z"`  
`stageTimestamp` |  `string` The time when the request reached the current audit stage. For example, `"2022-05-05T05:38:57.155218Z"`  
`hostname` |  `string` The name of the audit log host. For example, `"audit-logs-forwarder-2k4d9"`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
