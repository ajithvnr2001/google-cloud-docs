---
url: https://docs.cloud.google.com/access-context-manager/docs/create-cba-access-levels/
title: Create access levels for certificate-based access \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:46:19.778408+00:00
---

# Create access levels for certificate-based access  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/create-cba-access-levels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/access-context-manager/docs/create-access-level)



Send feedback 

#  Create access levels for certificate-based access Stay organized with collections  Save and categorize content based on your preferences. 

To secure your resources with certificate-based access, create an access level that requires certificates when determining access to resources. To create access levels, see [Creating a custom access level](https://docs.cloud.google.com/access-context-manager/docs/create-custom-access-level).

The values you use when creating a custom access level can be whatever makes sense for you, but the expression for the custom access level must be:
    
    
    certificateBindingState(origin, device) == CertificateBindingState.CERT_MATCHES_EXISTING_DEVICE
    

For example, you can use the gcloud CLI to create your custom access level by running the following command:
    
    
    gcloud access-context-manager levels create LEVEL_NAME \
      --title=TITLE \
      --custom-level-spec=FILE \
      --description=DESCRIPTION \
      --policy=POLICY_NAME
    

The content of the .yaml file referenced by `FILE` is the following custom expression:
    
    
    expression: "certificateBindingState(origin, device) == CertificateBindingState.CERT_MATCHES_EXISTING_DEVICE"
    
    

## What's next

  * [Enable CBA with VPC Service Controls](https://docs.cloud.google.com/access-context-manager/docs/enable-cba-vpcsc)
  * [Enable CBA with user groups](https://docs.cloud.google.com/access-context-manager/docs/enable-cba-user-groups)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
