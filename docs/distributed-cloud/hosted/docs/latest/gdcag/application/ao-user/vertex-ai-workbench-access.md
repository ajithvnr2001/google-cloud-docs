---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-workbench-access/
title: Control access to Vertex AI Workbench \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:29:57.429641+00:00
---

# Control access to Vertex AI Workbench  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-workbench-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Control access to Vertex AI Workbench Stay organized with collections  Save and categorize content based on your preferences. 

You can grant and restrict access to Vertex AI Workbench for an organization or a project. To do so, you define an organization policy using the `GDCHRestrictedService` policy type, which lets you restrict which service you can use on Google Distributed Cloud (GDC) air-gapped. When applied, the policy prevents the use of the APIs that it references.

For example, you can use this policy type to restrict the use of Vertex AI Workbench to specific projects. Only non-restricted organizations or projects can create or update JupyterLab notebooks. You can also use the policy to completely restrict access to the Vertex AI Workbench service because you want to run tests before allowing your teams to use it.

This page describes how to grant and restrict access to Vertex AI Workbench using the `GDCHRestrictedService` policy type. To learn more about organization policies and how to edit the `GDCHRestrictedService` organization policy, see [Configure organization policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/org-policy).

## Before you begin

  * To get the permissions you need to grant or restrict access to Vertex AI Workbench for an organization or a project, ask your IAM Org Admin to grant you the GDC Restricted Service Policy Admin (`gdchrestrictedservice-policy-admin`) cluster role. This role is not bound to a namespace. For more information about this role, see [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-ao-permissions).

  * Define the path to your management API server kubeconfig:
        
        export KUBECONFIG=MANAGEMENT_API_SERVER_KUBECONFIG
        




## Create restrictions

The following sections describe how to create, update, delete, and view restrictions for specific services within your project namespaces.

### Create or update restrictions

  * To create or update restrictions for your organization, run:
        
        kubectl --kubeconfig=${KUBECONFIG} apply -f  - <<EOF
        apiVersion: constraints.gatekeeper.sh/v1beta1
        kind: GDCHRestrictedService
        metadata:
          name: NAME
        spec:
          match:
            scope: "Namespaced"
            namespaces: PROJECT_NAMESPACE
            kinds:
            - apiGroups:
              - "aiplatform.gdc.goog"
              kinds:
              - Notebook
        EOF
        




### Delete a restriction

  * To delete restrictions, run:
        
        kubectl delete GDCHRestrictedService NAME 
        




### Describe a restriction

  * To describe restrictions, run:
        
        kubectl describe GDCHRestrictedService NAME 
        




## Restrict access to Vertex AI Workbench for your organization

To restrict access to Vertex AI Workbench for your organization, edit the `GDCHRestrictedService` policy type by adding the `aiplatform.gdc.goog` API group and the `Notebook` kind to the `kinds` field of the policy.

The following example shows how the `kinds` field looks in the `GDCHRestrictedService` policy type when you restrict access to Vertex AI Workbench for your entire organization:
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: GDCHRestrictedService
    metadata:
      name: restrict-notebook-for-organization
    spec:
      match:
        scope: "Namespaced"
        kinds:
        - apiGroups:
          - "aiplatform.gdc.goog"
          kinds:
          - Notebook
    
    [...]
    

To restore an organization's access to Vertex AI Workbench, see Grant access to Vertex AI Workbench for your organization.

## Restrict access to Vertex AI Workbench for a project

To restrict access to Vertex AI Workbench for a project, edit the `GDCHRestrictedService` policy type by adding the `aiplatform.gdc.goog` API group and the `Notebook` kind to the `kinds` field of the policy for the project namespace.

The difference with restricting access for an organization is that you must specify the namespace that the policy should impact. Add the `namespaces` field to the policy with your project namespace.

The following example shows how the `kinds` field looks in the `GDCHRestrictedService` policy type when you restrict access to Vertex AI Workbench for a project:
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: GDCHRestrictedService
    metadata:
      name: restrict-notebook-for-organization
    spec:
      match:
        scope: "Namespaced"
        namespaces: [PROJECT_NAMESPACE]
        kinds:
        - apiGroups:
          - "aiplatform.gdc.goog"
          kinds:
          - Notebook
    
    [...]
    

Replace `PROJECT_NAMESPACE` with the namespace of the project where you want to restrict access to Vertex AI Workbench.

## Grant access to Vertex AI Workbench for your organization

By default, Distributed Cloud organizations have access to Vertex AI Workbench. However, if you restricted access to Vertex AI Workbench for your organization, you can grant access again.

Follow these steps to grant access to Vertex AI Workbench for all the projects in your organization:

  1. Identify the `GDCHRestrictedService` policy type in your organization.

  2. Find the `aiplatform.gdc.goog` API group and the `Notebook` kind in the policy.

  3. If the `aiplatform.gdc.goog` API group and the `Notebook` kind are the only content in the `kinds` field of the policy, delete the `GDCHRestrictedService` resource.

  4. If the `GDCHRestrictedService` policy contains other restricted services, remove the `aiplatform.gdc.goog` API group and the `Notebook` kind from the `kinds` field and save the changes to the policy.


**Note:** The `kinds` field must always contain a value.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
