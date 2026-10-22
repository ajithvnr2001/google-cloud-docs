---
url: https://docs.cloud.google.com/confidential-computing/confidential-space/docs/vpc-service-controls/
title: VPC Service Controls \u00a0|\u00a0 Confidential Space \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:06.048026+00:00
---

# VPC Service Controls  |  Confidential Space  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/confidential-computing/confidential-space/docs/vpc-service-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Confidential Space ](https://docs.cloud.google.com/confidential-computing/confidential-space/docs)
  * [ Guides ](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-overview)



Send feedback 

#  VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

To validate its attestation token, Confidential Space needs to download certificates from Cloud Storage buckets. If these buckets reside outside your perimeter, you must configure the following egress rule: 
    
    
    - egressTo:
        operations:
          - serviceName: storage.googleapis.com
            methodSelectors:
              - method: google.storage.objects.get
        resources:
          - projects/870449385679
          - projects/180376494128
      egressFrom:
        identityType: ANY_IDENTITY
    

The following table lists the projects containing the necessary certificates:

Project ID | Project number | Description  
---|---|---  
cloud-shielded-ca-prod | 870449385679 | Project containing attestation certificates  
cloud-shielded-ca-prod-root | 180376494128 | Project containing root certificates  
  
If the Compute Engine API is restricted by your service perimeter, you must create the following egress rule:
    
    
    - egressTo:
        operations:
          - serviceName: compute.googleapis.com
            methodSelectors:
              - method: InstancesService.Insert
        resources:
          - projects/30229352718
      egressFrom:
        identityType: ANY_IDENTITY
    

The following table lists the project necessary to fetch Confidential Space VM images:

Project ID | Project number | Description  
---|---|---  
confidential-space-images | 30229352718 | Project containing Confidential Space VM images  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
