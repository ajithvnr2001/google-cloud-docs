---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/networking/networking-api-overview/
title: Overview of Networking API \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:34.009578+00:00
---

# Overview of Networking API  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/networking/networking-api-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  Overview of Networking API Stay organized with collections  Save and categorize content based on your preferences. 

The Networking API uses Kubernetes custom resources and relies on the Kubernetes Resource Model (KRM).

Create and manage networking in Google Distributed Cloud (GDC) air-gapped appliance through the Networking API using the `kubectl` CLI.

## Service endpoint

The API endpoint for the Networking API is `https://MANAGEMENT_API_SERVER_ENDPOINT/apis/networking.gdc.goog/v1`, where `MANAGEMENT_API_SERVER_ENDPOINT` is the endpoint of the Management API server.

## Discovery document

Use the `kubectl proxy` command to open a proxy to the API server on your local machine. From there, you can access the discovery document at the following URL: `http://127.0.0.1:8001/apis/networking.gdc.goog/v1`.

## Example ingress cross-project traffic policy

The following is an example of a `ProjectNetworkPolicy` object that enables workloads in the `project-1` project to permit connections from workloads in the `project-2` project, as well as the return traffic for the same flows:
    
    
    apiVersion: networking.gdc.goog/v1
    kind: ProjectNetworkPolicy
    metadata:
      namespace: project-1
      name: allow-ingress-traffic-from-project-2
    spec:
      policyType: Ingress
      subject:
        subjectType: UserWorkload
      ingress:
      - from:
        - projects:
            matchNames:
            - project-2
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
