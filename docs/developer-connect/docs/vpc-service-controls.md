---
url: https://docs.cloud.google.com/developer-connect/docs/vpc-service-controls/
title: Use VPC Service Controls \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:33:34.066535+00:00
---

# Use VPC Service Controls  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/vpc-service-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Guides ](https://docs.cloud.google.com/developer-connect/docs/overview)



Send feedback 

#  Use VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls) is a Google Cloud feature that lets you set up a service perimeter to guard against data exfiltration.

VPC Service Controls in Developer Connect don't guard against possible exfiltration to external source code management systems. This guide shows further controls that use Custom Org Policies to help block these scenarios. SCMSs

See [Set up a service perimeter by using VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-service-perimeter) for more information on how to use VPC Service Controls.

  * Create a custom org policy that restricts what your developers can create connections to.

  * Create a custom org policy that allows your developers to create and update connections only through a specific Service Directory resource.

  * Review Limitations for Developer Connect insights.




## Before you begin

To use the command-line examples in this guide, install and configure the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk).

**Note:** If you've installed gcloud CLI previously, make sure you have the latest available version by running `gcloud components update`.

### Required roles

To get the permissions that you need to create or edit a custom organization policy, ask your administrator to grant you the [Organization Policy Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) IAM role on the organization resource. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a constraint to limit the SCMSs to which your team can create connections

One way to mitigate the possibility of data exfiltration to an SCMS is to limit which SCMSs are allowed for connections. You can create a custom organization policy that allows connections to one or more specified SCMSs.

The following organization policy limits repository connections to allow connections to GitHub Enterprise only:
    
    
    name: organizations/ORGANIZATION_ID/customConstraints/CONSTRAINT_NAME
    resourceTypes:
    - developerconnect.googleapis.com/Connection
    methodTypes:
    - CREATE
    - UPDATE
    condition: |
      resource.githubEnterpriseConfig.hostUri=="https://github.mycompany.net"
    actionType: ALLOW
    displayName: Connection GitHub Enterprise Host Constraint
    description: |
      Allows creation/update of Developer Connect connections only to GitHub Enterprise host github.mycompany.net
    

## Create a constraint to require connections through Service Directory

You can mitigate the possibility of data exfiltration by creating a custom organization policy that allows connections only to a specified [Service Directory](https://docs.cloud.google.com/service-directory/docs/overview) endpoint.

The following organization policy allows connections to a specific Service Directory endpoint only:
    
    
    name: organizations/ORGANIZATION_ID/customConstraints/CONSTRAINT_NAME
    resourceTypes:
    - developerconnect.googleapis.com/Connection
    methodTypes:
    - CREATE
    - UPDATE
    condition: |
      resource.gitlabEnterpriseConfig.serviceDirectoryConfig.service=="projects/my-project/locations/us-central1/namespaces/ns/services/myendpoint"
    actionType: ALLOW
    displayName: Connection GitLab Enterprise Service Directory endpoint
    description: |
      Allows creation/update of Developer Connect connections only through a specific Service Directory resource
    

## Limitations for Developer Connect insights

When using [Developer Connect insights](https://docs.cloud.google.com/developer-connect/docs/insights) (`InsightsConfig`) with VPC Service Controls, consider the following known limitations and configuration requirements:

  * **App Hub API reliance** : Developer Connect insights relies on the [App Hub API](https://docs.cloud.google.com/app-hub/docs/using-vpc-service-controls). For applications using a folder management boundary, VPC Service Controls restrictions at the folder level aren't applied to descendent projects; App Hub can discover services and workloads for all descendent projects even if they aren't in the same perimeter as the management project.

  * **Resource metadata available through App Topology** : When using Developer Connect insights, enriched resource metadata is made available through [App Topology](https://docs.cloud.google.com/hub/docs/app-topology#vpc-sc), if the App Topology API is also enabled. We recommend you restrict both the Developer Connect insights API (`developerconnect.googleapis.com`) and App Topology API(`apptopology.googleapis.com`) in perimeters if using both services.

  * **App Hub application feeds and IAM access control** : When an `InsightsConfig` tracks insights for an App Hub application, Developer Connect creates Cloud Asset Inventory [real-time feeds](https://docs.cloud.google.com/asset-inventory/docs/monitor-asset-changes) in the App Hub application's management folder or project boundary. Data from these feeds is published directly to the Developer Connect service, but is only consumed by Developer Connect service agents allowed to read asset metadata from these folders or projects. In addition to using [IAM roles](https://docs.cloud.google.com/developer-connect/docs/set-up-insights#iam-roles) to restrict which Developer Connect service agents are given this access, the project hosting the `InsightsConfig` resource and the project where data is published from must reside in the same VPC Service Controls perimeter, or configured [ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) must be added for the Developer Connect service agent to allow access.

  * **Project scoped feeds and IAM access control** : When an `InsightsConfig` is scoped to a project, Developer Connect creates Cloud Asset Inventory [real-time feeds](https://docs.cloud.google.com/asset-inventory/docs/monitor-asset-changes) directly in the target project(s). Data from these feeds is published directly to the Developer Connect service, but is only consumed by Developer Connect service agents allowed to read asset metadata from these projects. In addition to using [IAM roles](https://docs.cloud.google.com/developer-connect/docs/set-up-insights#iam-roles) to restrict which Developer Connect service agents are given this access, the project hosting the `InsightsConfig` resource and the project where data is published from must reside in the same VPC Service Controls perimeter, or configured [ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) must be added for the Developer Connect service agent to allow access.

  * **Perimeter alignment for artifact metadata and provenance** : The project hosting the `InsightsConfig` resource and any project containing artifact metadata or provenance must reside in the same VPC Service Controls perimeter, or configured [ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) must be added for the Developer Connect service agent to allow access.

  * **Perimeter alignment for deployment logging** : The project hosting the `InsightsConfig` resource and any project containing deployments must be in the same VPC Service Controls perimeter, or configured [ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) must be added for the Developer Connect service agent to allow access.




## What's next

  * [Learn more](https://docs.cloud.google.com/developer-connect/docs/custom-constraints) about creating custom organization policies.

  * [Learn more](https://docs.cloud.google.com/vpc-service-controls/docs/overview) about VPC Service Controls.

  * [Learn more](https://docs.cloud.google.com/service-directory/docs/overview) about Service Directory.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
