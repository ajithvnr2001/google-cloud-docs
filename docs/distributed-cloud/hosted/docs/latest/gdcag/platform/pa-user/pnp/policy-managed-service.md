---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/policy-managed-service/
title: Create project network policies for managed services \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:50.191295+00:00
---

# Create project network policies for managed services  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/policy-managed-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create project network policies for managed services Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions to create project network policies for managed services in Google Distributed Cloud (GDC) air-gapped. A GDC managed service is a service that is built and maintained by Google. It is available by default to all users and can be accessed through the GDC web console or using the command line. Managed services can be either software developed by Google or open-source software that Google has integrated with GDC.

## Before you begin

To configure create project network policies for managed services, you must have the following:

  * The necessary identity and access roles. For more information, see [Prepare predefined roles and access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/pnp-overview#prepare-predefined-roles-and-access).
  * An existing project. For more information, see [Create a project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-a-project).



## Create a policy for a managed service

By default, a managed service only allows connections from the project that created the service. An operator can expose the managed service to projects other than the project that created the service by using a project network policy.

You can create a global policy for a managed service that applies to all zones in your organization. For more information on global resources in a GDC universe, see [Multi-zone overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/mz-overview).

### Create a global policy for a managed service

The following `ProjectNetworkPolicy` exposes the Database Service (DBS) as a managed service:
    
    
    kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
    apiVersion: networking.global.gdc.goog/v1
    kind: ProjectNetworkPolicy
    metadata:
      namespace: PROJECT_1
      name: allow-inbound-traffic-from-project-2-to-dbs-service
    spec:
      subject:
        subjectType: ManagedService
        managedServices:
          matchTypes:
          - 'dbs'
      ingress:
      - from:
        - projectSelector:
            projects:
              matchNames:
              - PROJECT_2
    EOF
    

Replace the following:

  * `GLOBAL_API_SERVER`: the global API server's kubeconfig path. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers). If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
  * `PROJECT_1`: the source project name.
  * `PROJECT_2` the destination project. After applying the policy, workloads in the `PROJECT_2` project can connect to workloads in the DBS managed service.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
