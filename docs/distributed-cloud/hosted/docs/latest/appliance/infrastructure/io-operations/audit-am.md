---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations/audit-am/
title: Artifact Management audit logs \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:30:13.053114+00:00
---

# Artifact Management audit logs  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations/audit-am/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Artifact Management audit logs Stay organized with collections  Save and categorize content based on your preferences. 

Artifact Management audit logs include successful events in the container registries in the org infrastructure cluster.

## JSON representation
    
    
    {
      "auditID": string,
      "action": string,
      "time": string,
      "user":{
        object
      },
      "resource": string,
      "_gdch_service_name": string,
      "_gdch_namespace": string,
      "_gdch_service_tenant": string,
      "_gdch_cluster": string,
      "_gdch_fluentbit_pod": string
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
`_gdch_service_name` |  `string` The short name of the service collecting audit logs. The value is always `"artifactmanagement"`  
`_gdch_namespace` |  `string` The short name of the service namespace. The value is always `"harbor-system"`  
`_gdch_service_tenant` |  `string` The name of the service tenant. Possible values:

  * `"infra-obs"`
  * `"platform-obs"`

  
`_gdch_cluster` |  `string` The name of the cluster producing the successful event. For example, `"org-1-infra"`  
`_gdch_fluentbit_pod` |  `string` The name of the Fluent Bit pod collecting audit logs. For example, `"anthos-audit-logs-forwarder-wqbg8"`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
