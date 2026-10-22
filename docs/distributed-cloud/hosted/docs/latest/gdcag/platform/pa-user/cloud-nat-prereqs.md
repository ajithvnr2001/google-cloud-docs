---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cloud-nat-prereqs/
title: Before you begin with Cloud NAT \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:58:27.602790+00:00
---

# Before you begin with Cloud NAT  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cloud-nat-prereqs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Before you begin with Cloud NAT Stay organized with collections  Save and categorize content based on your preferences. 

This page covers prerequisite steps before you can begin setting up a Cloud NAT gateway. This includes steps for getting the necessary permissions,setting up your network policy, enabling egress, and creating subnets.

### Add IAM Roles

The default resource model is designed around the Platform Administrator persona creating the project, project network policy, and the external subnets that contain the egress Internet Protocol (IP) addresses. The Application Operator persona manages project-scoped Cloud NAT gateways. The Infrastructure Operator persona has comprehensive permissions for debugging Cloud NAT and related network resources.

You can grant permissions by assigning the Cloud NAT Identity and Access Management (IAM) roles in the following list.

  * **Cloud NAT Developer (`cloud-nat-developer`)**: This role provides the necessary permissions for application operators to Create, Read, Update, and Delete (CRUD) Cloud NAT objects within their assigned projects. It focuses purely on the operational aspects of Cloud NAT configuration, without granting access to foundational network infrastructure.
  * **Cloud NAT Viewer (`cloud-nat-viewer`)**: This role offers read-only access to Cloud NAT resources. It is intended for application operators and other users who need to monitor Cloud NAT configurations and status without the ability to make any modifications.
  * **Cloud NAT Debugger (`cloud-nat-debugger`)**: This specialized role, assigned to infrastructure operators, provides comprehensive permissions for debugging Cloud NAT and related network resources. This role grants full control over Cloud NAT resources, along with elevated permissions to inspect and troubleshoot underlying network components that directly impact Cloud NAT functionality.

**Note:** **Cloud NAT Manager (`cloud-nat-manager`)** provides the same permissions as `cloud-nat-developer`, but has been deprecated, and will be removed in a future release.

### Set up Project and Project Network Policy

Before creating a Cloud NAT gateway, create a project by following [the instructions for creating a project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-a-project).

By default, Google Distributed Cloud (GDC) air-gapped blocks workloads in a project from going out of the organization. Workloads can exit the organization if your Platform Administrator (PA) has disabled data exfiltration protection for the project. PAs can do so by attaching the label `networking.gdc.goog/enable-default-egress-allow-to-outside-the-org: "true"` to the project, or by [disabling data exfiltration protection from the console](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/data-exfiltration#disable-data-exfiltration-protection).

An example project, with egress traffic enabled:
    
    
    apiVersion: resourcemanager.gdc.goog/v1
    kind: Project
    metadata:
      namespace: platform
      name: project-1
      labels:
        networking.gdc.goog/enable-default-egress-allow-to-outside-the-org: "true"
    

An example network policy, that allows all egress:
    
    
    apiVersion: networking.gdc.goog/v1alpha1
    kind: ProjectNetworkPolicy
    metadata:
      namespace: project-1
      name: allow-egress-traffic
    spec:
      policyType: Egress
      subject:
        subjectType: UserWorkload
      egress:
      - to:
        - ipBlock:
            cidr: 0.0.0.0/0
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
