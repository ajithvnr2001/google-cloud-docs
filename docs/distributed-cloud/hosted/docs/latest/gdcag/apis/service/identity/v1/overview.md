---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/identity/v1/overview/
title: Identity and Access Management API overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:10.310601+00:00
---

# Identity and Access Management API overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/identity/v1/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  Identity and Access Management API overview Stay organized with collections  Save and categorize content based on your preferences. 

The Identity and Access Management (IAM) API uses Kubernetes custom resources to manage the control access for identity providers.

To use the IAM API, use the GDC console. If your application uses your own libraries to call the API, adopt the example service endpoint in the following section, and the full API definitions to build your requests:

  * [iam.gdc.goog](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/identity/v1/identity-v1)
  * [iam.global.gdc.goog](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/identity/v1/global-identity-v1)



## Service endpoint and discovery document

The IAM APIs are provided in two packages depending on zonal deployment or global deployment.

The API endpoints for the zonal and global IAM APIs are the following, respectively:

  * `https://MANAGEMENT_API_SERVER_ENDPOINT/apis/iam.gdc.goog/v1`
  * `https://MANAGEMENT_API_SERVER_ENDPOINT/apis/iam.global.gdc.goog/v1`



The `MANAGEMENT_API_SERVER_ENDPOINT` variable is the endpoint of the Management API server.

Using the `kubectl proxy` command, access the URL in your browser to obtain the discovery document for the IAM API. The `kubectl proxy` command opens up a proxy on `127.0.0.1:8001` to the Kubernetes API server on your local machine. After that command is running, access the documents at the following URLs:

  * `http://127.0.0.1:8001/apis/iam.gdc.goog/v1`
  * `http://127.0.0.1:8001/apis/iam.global.gdc.goog/v1`



## Example resources

The following is a sample `IdentityProviderConfig` resource:
    
    
    apiVersion: iam.gdc.goog/v1
    kind: IdentityProviderConfig
    metadata:
      name: example-provider
      namespace: platform
    spec:
      - oidc:
        clientID: clientID
        clientSecret: clientSecret
        groupPrefix: example-
        groupsClaim: groups
        issuerURI: https://test-oidc-provider.example.com
        scopes: openid,email,profile
        userClaim: user-email@example.com
        userPrefix: example-
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
