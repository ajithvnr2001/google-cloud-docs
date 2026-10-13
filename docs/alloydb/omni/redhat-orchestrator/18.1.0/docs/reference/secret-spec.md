---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/reference/secret-spec/
title: Secret Custom Resource Definition \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:37:19.758022+00:00
---

# Secret Custom Resource Definition  |  AlloyDB Omni using the RPM orchestrator: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/reference/secret-spec/

This page documents AlloyDB Omni version **18.1.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/overview)
  * [ Reference ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/reference/secret-spec)



Send feedback 

#  Secret Custom Resource Definition Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://forms.gle/zxuHekMtV67Bw9Av9). 

## Spec schema

Secrets store sensitive information, for example, passwords and certificates. You use the secret reference instead of using the values directly.
    
    
    Secret:
      metadata:
        name: string
      spec:
        type: Opaque
        data:
          string: string
    

FieldType  
Required or optional |  Description  
---|---  
`type`  
`string`  
 _Optional_ |  Only the **Opaque** type is supported.   
`data`  
`object`  
 _Required_ |  Data takes a key-value pair, both of string type.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
