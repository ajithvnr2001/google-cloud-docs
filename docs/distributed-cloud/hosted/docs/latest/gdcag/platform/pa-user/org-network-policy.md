---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/org-network-policy/
title: Create organization network policies \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:50.070325+00:00
---

# Create organization network policies  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/org-network-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create organization network policies Stay organized with collections  Save and categorize content based on your preferences. 

An organization network policy defines the network access control for organization-level managed services exposed through Google Distributed Cloud (GDC) air-gapped. You can define these access controls using the [`OrganizationNetworkPolicy`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/networking/v1/networking-v1#organizationnetworkpolicy) resource from the [Networking API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/networking/networking-api-overview).

To get the permissions you need to configure the organization network policy, ask your Organization Identity and Access Management (IAM) Admin to grant you the Org Network Policy Admin (`org-network-policy-admin`) role.

You can define an organization network policy for access controls for the following GDC managed services:

  * All services
  * GDC console
  * [Distributed Cloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview)
  * [Global API server](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers)
  * [Identity and Access Management (IAM)](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/set-up-role-bindings)
  * [Key Management Systems (KMS)](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/kms/kms)
  * [Object storage](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/storage#object_storage)
  * [System Artifact Registry (SAR)](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/infrastructure/io-operations-30/sar-overview)
  * [Vertex AI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vertex-pre-trained-apis)
    * Services within Vertex AI that a policy supports include the [Optical Character Recognition API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/quickstart-ocr), [Speech-to-Text API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/quickstart-stt), [Translation API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/quickstart-translation), and [Workbench](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-workbench-intro).
  * [Virtual Machine Management (VMM)](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/vm-introduction)



## Default policy

By default, the following GDC managed services have the following principles:

GDC service | Principle  
---|---  
All services | `allow-all`  
GDC console | `allow-all`  
gdcloud CLI | `allow-all`  
Global API server | `deny-by-default`  
IAM | `deny-by-default`  
KMS | `deny-by-default`  
Object storage | `deny-by-default`  
SAR | `allow-all`  
Vertex AI and supported services | `deny-by-default`  
VMM | `deny-by-default`  
  
## Example organization network policy

The following is an example of an `OrganizationNetworkPolicy` resource that allows traffic from an IP address to access a GDC managed service.
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f - <<EOF
    apiVersion: networking.gdc.goog/v1
    kind: OrganizationNetworkPolicy
    metadata:
      name: POLICY_NAME
      namespace: platform
    spec:
      subject:
        services:
          matchTypes:
          - "SERVICE_NAME"
      ingress:
        - from:
          - ipBlock:
              cidr: CIDR
          - ipBlock:
              cidr: CIDR
    EOF
    

Replace the following variables:

Variable | Description  
---|---  
MANAGEMENT_API_SERVER | The zonal API server's kubeconfig path. If you have not yet generated a kubeconfig file for the API server in your targeted zone, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.  
POLICY_NAME | The name to give the policy.   
  
For example, `allow-ui-access`.  
SERVICE_NAME | The name of the service to apply the policy. Use the following values for each service:   


  * **All services** : `all`
  * **GDC console** : `ui-console`
  * **gdcloud CLI** : `api-server`
  * **Global API server** : `global-api-server`
  * **IAM** : `iam`
  * **KMS** : `kms`
  * **Object storage** : `object-storage`
  * **SAR** : `system-artifact-registry`
  * **Vertex AI** : `ai`
  * **VMM** : `vmm`

  
CIDR | The IP address range in CIDR notation from which to allow access, such as `10.251.0.0/24`. You can add multiple `ipBlock` entries to allow access from multiple ranges.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
