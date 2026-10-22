---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-observability-logger/
title: Observability audit logger \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:21:54.409612+00:00
---

# Observability audit logger  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-observability-logger/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Observability audit logger Stay organized with collections  Save and categorize content based on your preferences. 

## JSON representation
    
    
    {
      "auditID": string,
      "action": string,
      "time": string,
      "user":{
        object
      },
      "resource": string,
      "description": string,
      "sourceIPs": [
        string array
      ],
      "userAgent": string,
      "numBytesSent": integer,
      "numBytesReceived": integer,
      "orgAdminClusterName": string,
      "serviceName": string,
      "_gdch_service_name": string,
      "_gdch_namespace": string,
      "_gdch_tenant_id": string,
      "_gdch_cluster": string,
      "_gdch_fluentbit_pod": string
      "_gdch_org_name": string
      "_gdch_org_id": string
    }
    

Fields  
---  
`auditID` |  `string` The unique audit identification value generated for each request. For example, `"15000"`  
`action` |  `string` The action performed on the resource for the event. For example, `"create"`  
`time` |  `string` The time of the action up to milliseconds. For example, `"2022-11-30T02:14:33Z"`  
`user` |  `object` Information about the identity and issuer of the authenticated user who performed the action. For example,
    
    
    {
      "identity":"s:gpc-system:artifact-registry-services-registry-exporter",
      "issuer":"artifact.private.gdc.goog/hra"
    }  
  
`resource` |  `string` The identification value of the resource. For example, `"dataproc-service/private-cloud-devel/dataproc:3.1-dataproc-3"`  
`description` |  `string` A longer description of the nature of the access. The value might be the complete request object.  
`sourceIPs` |  `string array` The IPs from where the request originated and the intermediate proxies.  
`userAgent` |  `string` The user agent string reported by the client.  
`numBytesSent` |  `integer` The number of bytes sent in response for this request.  
`numBytesReceived` |  `integer` The number of bytes received from this request.  
`orgAdminClusterName` |  `integer` The name of the org infrastructure cluster that generated the audit log.  
`serviceName` |  `integer` A short name of the component or service that generated the audit log.  
`_gdch_service_name` |  `string` A short name of the component or service that generated the audit log.  
`_gdch_namespace` |  `string` The name of the service namespace.  
`_gdch_tenant_id` |  `string` The name of the service tenant. Possible values:

  * `"infra-obs"`
  * `"platform-obs"`

  
`_gdch_cluster` |  `string` The name of the Kubernetes cluster producing the successful event. For example, `"root-admin"`  
`_gdch_fluentbit_pod` |  `string` The name of the pod collecting audit logs. For example, `"anthos-audit-logs-forwarder-wqbg8"`  
`_gdch_org_name` |  `string` The name of the organization. For example, `"org-1"`  
`_gdch_org_id` |  `string` The ID of the organization. For example, `"org-1.zone1.google.gdch.test"`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
