---
url: https://docs.cloud.google.com/vpc-service-controls/docs/identity-groups-examples/
title: Example of using identity groups and third-party identities in ingress and egress rules \u00a0|\u00a0 VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:04.985497+00:00
---

# Example of using identity groups and third-party identities in ingress and egress rules  |  VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/identity-groups-examples/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

#  Example of using identity groups and third-party identities in ingress and egress rules Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to [use identity groups and third-party identities in ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/configure-identity-groups).

This page contains the following example of using identity groups in ingress and egress rules:

  * Allow Cloud Run access to an identity group's members through the internet and to specific service accounts from an allowlisted IP address range.



## Allow Cloud Run access to an identity group's members and to specific service accounts

The following diagram shows a user from a specific identity group and from the allowlisted IP address range accesses Cloud Run inside a service perimeter:

![](https://docs.cloud.google.com/static/vpc-service-controls/images/1-access-to-group.svg)**Figure 1.** An example of providing Cloud Run access using an identity group.

Consider that you have defined the following service perimeter:
    
    
    name: accessPolicies/222/servicePerimeters/Example
    status:
      resources:
      - projects/111
      restrictedServices:
      - run.googleapis.com
      - artifactregistry.googleapis.com
      vpcAccessibleServices:
        enableRestriction: true
        allowedServices:
        - RESTRICTED_SERVICES
    title: Example
    

To find details about an existing service perimeter in your organization, [describe the service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#list-and-describe) using the gcloud CLI command.

In this example, we also assume that you have defined the following resources:

  * An identity group called `allowed-users@example.com` that has users who you want to provide access to Cloud Run inside the perimeter.
  * An access level called `CorpDatacenters` in the same access policy as the service perimeter. `CorpDatacenters` includes an allowlisted IP address range of the corporate data centers where requests from service accounts can originate from.



The following ingress policy, `ingress.yaml`, allows Cloud Run access to specific human accounts, who are part of the `allowed-users@example.com` group, and specific service accounts, that are limited to the allowlisted IP address range:
    
    
    - ingressFrom:
        identities:
        - serviceAccount:my-sa@my-project.iam.gserviceaccount.com
        sources:
        - accessLevel: accessPolicies/222/accessLevels/CorpDatacenters
      ingressTo:
        operations:
        - serviceName: run.googleapis.com
          methodSelectors:
          - method: "*"
        resources:
        - "*"
    - ingressFrom:
        identities:
        - group:allowed-users@example.com
        sources:
        - accessLevel: "*"
      ingressTo:
        operations:
        - serviceName: run.googleapis.com
          methodSelectors:
          - method: "*"
        resources:
        - "*"
    

To apply the ingress rule, run the following command:
    
    
    gcloud access-context-manager perimeters update Example --set-ingress-policies=ingress.yaml
    

## What's next

  * [Configure identity groups and third-party identities in ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/configure-identity-groups)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
