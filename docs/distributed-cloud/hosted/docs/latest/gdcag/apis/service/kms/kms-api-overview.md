---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/kms/kms-api-overview/
title: Key Management Service API overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:13:27.768686+00:00
---

# Key Management Service API overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/kms/kms-api-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  Key Management Service API overview Stay organized with collections  Save and categorize content based on your preferences. 

The Key Management Service (KMS) API uses Kubernetes custom resources to manage the lifecycle of the crypto keys.

To use the KMS API, use the GDC console. If your application uses your own libraries to call the API, adopt the example service endpoint in the following section, and the full API definitions to build your requests:

  * [kms.gdc.goog](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/kms/v1/kms-v1)
  * [kms.global.gdc.goog](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/kms/v1/global-kms-v1)



## Service endpoint and discovery document

The KMS APIs are provided in two packages depending on zonal deployment or global deployment.

The API endpoints for the zonal and global KMS APIs are the following, respectively:

  * `https://MANAGEMENT_API_SERVER_ENDPOINT/apis/kms.gdc.goog/v1`
  * `https://MANAGEMENT_API_SERVER_ENDPOINT/apis/kms.global.gdc.goog/v1`



The `MANAGEMENT_API_SERVER_ENDPOINT` variable is the endpoint of the Management API server.

Using the `kubectl proxy` command, access the URL in your browser to obtain the discovery document for the KMS API. The `kubectl proxy` command opens up a proxy on `127.0.0.1:8001` to the Kubernetes API server on your local machine. After that command is running, access the documents at the following URLs:

  * `http://127.0.0.1:8001/apis/kms.gdc.goog/v1`
  * `http://127.0.0.1:8001/apis/kms.global.gdc.goog/v1`



## Example resources

The following are sample resources. The namespace is a project namespace. For more information on creating and managing `AEADKey` and `SigningKey` resources in a project namespace, see [Create and delete keys](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/kms/create-delete-keys).

### AEADKey resource
    
    
    apiVersion: "kms.gdc.goog/v1"
    kind: AEADKey
    metadata:
      name: my-test-key
      namespace: user-kms-project
    spec:
      algorithm: AES_256_GCM
    

### SigningKey resource
    
    
    apiVersion: "kms.gdc.goog/v1"
    kind: SigningKey
    metadata:
      name: my-test-key
      namespace: user-kms-project
    spec:
      algorithm: EC_SIGN_P384_SHA384
    

### KeyImport resource
    
    
    apiVersion: "kms.gdc.goog/v1"
    kind: KeyImport
    metadata:
      name: my-test-key-import
      namespace: user-kms-project
    spec:
      context:
        mechanism: ECDH_P521_AES256
    

### KeyExport resource
    
    
    apiVersion: "kms.gdc.goog/v1"
    kind: KeyExport
    metadata:
      name: my-test-key-export
      namespace: user-kms-project
    spec:
      context:
        mechanism: ECDH_P521_AES256
        publicKey: pub_key_from_import
      keyToExport:
        kind: AEADKey
        name: key_name_to_export
    

### RotationJob resource
    
    
    apiVersion: "kms.gdc.goog/v1"
    kind: RotationJob
    metadata:
      name: my-test-rotate-job
    spec:
      rootKeyResourceName: namespaces/kms-system/secrets/kms-key-ctm-root
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
