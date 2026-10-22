---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/org-policy/org-policy-api-overview/
title: Organization Policy API overview \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:33.851738+00:00
---

# Organization Policy API overview  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/org-policy/org-policy-api-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  Organization Policy API overview Stay organized with collections  Save and categorize content based on your preferences. 

The Organization Policy API uses Kubernetes custom resources and relies on the Kubernetes Resource Model (KRM). It is used to manage the lifecycle of organization policies such as creating, updating, deleting.

To use the Organization Policy API, we recommend that you use the Kubernetes CLI `kubectl`. If your application needs to use its own libraries to call this API, use the following example, the [full API definition](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/org-policy/org-policy-krm-api), and the dedicated [policy match page](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/org-policy/policy-match-section) to build your requests.

**Warning:** While organization policies leverage an open-source API that's marked as beta (`constraints.gatekeeper.sh/v1beta1`), the organization policy system itself is in alpha. Additional APIs may be introduced in the future to facilitate the management of organisation policies.

## Service endpoint and discovery document

The API endpoint for the Organization Policy API is: `https://MANAGEMENT_API_SERVER_ENDPOINT/apis/constraints.gatekeeper.sh/v1beta1` where `MANAGEMENT_API_SERVER_ENDPOINT` is the endpoint of the Management API server.

Using the `kubectl proxy` command, you can access that URL in your browser or with a tool such as `curl` to get the discovery document for the Organization Policy API. The `kubectl proxy` command opens up a proxy to the Kubernetes API server on your local machine. Once that command is running, you can access the document at the following URL: `http://127.0.0.1:8001/apis/constraints.gatekeeper.sh/v1beta1`.

## Example KRM

The following example is a `GDCHRestrictedServices` object in the Organization Policy API to restrict the use of the Database Service to projects that have the label `owner: dba-team`.
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: GDCHRestrictedService
    metadata:
      name: db-restricted-to-dbas
    spec:
      match:
        scope: Namespaced
        namespaceSelector:
          matchExpressions:
          # We are restricting the use of the service in namespaces that
          # DON'T have the owner: dba-team label
          - key: owner
            operator: NotIn
            values:
            - dba-team
        kinds:
        - apiGroups:
          - "postgresql.ods.anthosapis.com"
          kinds:
          - Dbclusters
          - Backupplans
          - Imports
          - Restores
        - apiGroups:
          - "oracle.ods.anthosapis.com"
          kinds:
          - Dbclusters
          - Backupplans
          - Imports
      parameters:
        disabledOperations:
          - "UPDATE"
          - "CREATE"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
