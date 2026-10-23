---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-use-vpcsc/
title: Use VPC Service Controls \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:00.156996+00:00
---

# Use VPC Service Controls  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-use-vpcsc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  Use VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

To secure your Network Connectivity Center (NCC) configuration, use VPC Service Controls.

VPC Service Controls provides additional security for Google APIs and services, including your NCC configuration. In addition to IAM, VPC Service Controls limits the source systems that can make NCC configuration changes.

This page describes a common use case and an example configuration to allow access between an NCC hub and VPC spokes separated by service perimeters.

For comprehensive documentation, see the [VPC Service Controls overview](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

## Example: Cross-project VPC spoke proposals across service perimeters

If your configuration requires that an NCC hub and its VPC spokes reside in different projects that belong to separate VPC Service Controls perimeters, you must configure [ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) in both perimeters. This lets spoke administrators [propose a VPC spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-propose-a-spoke) referencing the hub, and lets hub administrators [accept proposed spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-review-proposed-spokes).

The example on this page assumes that the hub administrator and spoke administrators belong to separate organizations.

The following table summarizes the rules required for this example:

Perimeter | Rule | Purpose  
---|---|---  
Spoke perimeter  
(spoke project) | Ingress rule 1 | Allow the spoke administrator to initiate a spoke proposal by creating a spoke in the spoke project (if managing from outside `SpokePerimeter`)  
Egress rule 1 | Allow the outbound spoke proposal to initiate attachment to the hub in the hub project, which includes verifying the backing VPC network  
Hub perimeter  
(hub project) | Ingress rule 1 | Allow the hub administrator to manage the hub in the hub project, including accepting or rejecting spoke proposals (if managing the hub from outside `HubPerimeter`)  
Ingress rule 2 | Allow the inbound spoke proposal to initiate attachment to the hub  
Egress rule 1 | Allow the inbound spoke proposal to call back to the spoke project to complete linking the spoke to the hub, which includes verifying the backing VPC network  
  
### Spoke perimeter rules

To enable spoke creation and management, the spoke administrator configures the following ingress and egress rules:

Rule | Details  
---|---  
Ingress rule 1: Spoke creation |  When a spoke administrator initiates a spoke proposal by issuing the creation command from outside the perimeter (such as from an administrator workstation, Cloud Shell, or the Google Cloud console), VPC Service Controls evaluates the call as an ingress request to the spoke project. `SpokePerimeter` must allow ingress from the spoke administrator's identity and network origin for the NCC API.   
  
This rule isn't needed if spoke management is performed exclusively from within a VPC network protected by `SpokePerimeter`.   
Egress rule 1: Hub attachment and network verification |  When a spoke administrator proposes a spoke, the request initiates attachment to the hub in the hub project. As part of the request, the NCC API also verifies the backing VPC network by using the Compute Engine API. `SpokePerimeter` must allow egress from the spoke administrator for both the NCC and Compute Engine APIs.   
  
#### Spoke perimeter definition

The ingress and egress rule examples in the following sections are based on the following perimeter definition.

For more information about service perimeters, see [Service perimeter details and configuration](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters).
    
    
    # Spoke perimeter definition
    name: accessPolicies/2345678901/servicePerimeters/SpokePerimeter
    status:
      resources:
      - projects/222222222222
      restrictedServices:
      - networkconnectivity.googleapis.com
      - compute.googleapis.com
    title: SpokePerimeter
    

#### Spoke ingress rule

This section provides an example that implements the ingress rule for the spoke perimeter as described in Spoke perimeter rules. This rule is required only if managing spokes from outside `SpokePerimeter`.

For details about rule syntax, see the [ingress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules-reference). To apply rules, see [Configuring ingress and egress policies](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies).
    
    
    echo """
    # Rule 1: Allow the spoke administrator to initiate a spoke proposal by creating
    # a spoke in the spoke project (if managing from outside SpokePerimeter)
    - ingressFrom:
        identities:
        # Specify the principal identifier for the spoke administrator or deployment pipeline:
        - serviceAccount:spoke-admin-sa@spoke-project.iam.gserviceaccount.com
        # - group:spoke-admins@example.org
        # - user:spoke-admin@example.org
        sources:
        - accessLevel: accessPolicies/2345678901/accessLevels/SpokeAdminAccessLevel
        # Alternatively, specify a management project or VPC network if managing
        # from a VPC network outside the perimeter:
        # - resource: projects/MANAGEMENT_PROJECT_NUMBER
      ingressTo:
        operations:
        - serviceName: networkconnectivity.googleapis.com
          methodSelectors:
          - method: "*"
        resources:
        - projects/222222222222
    """ > spoke-ingress.yaml
    

As a best practice, define ingress rules that are as specific as possible:

  * `identities`: Specify only the principal identifier needed for your environment rather than broad identity types. In this example, Rule 1 specifies a service account for an automated deployment pipeline. Alternatively, you can specify a Google group for team administration, or an individual user account. For details, see [Supported identities for ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/supported-identities).

  * `sources`: Restrict origins to known access levels. This example specifies an access level from the access policy managing `SpokePerimeter` to authorize external sources such as administrator workstations, Cloud Shell, or the Google Cloud console. Alternatively, you can allow access from a management VPC network outside the perimeter by using the `- resource:` attribute to specify the project or VPC network. For details, see [Allow access from outside a perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels) and [Context-aware access with ingress rules](https://docs.cloud.google.com/vpc-service-controls/docs/context-aware-access).

  * `operations`: Restrictions for `networkconnectivity.googleapis.com` are enforced at the service level, requiring `method: "*"`. More granular methods aren't available for this service.

  * `resources`: Specify the exact spoke project number in `resources`. Avoid wildcards (`*`).




#### Spoke egress rule

This section provides an example that implements the egress rule for the spoke perimeter as described in Spoke perimeter rules.

For details about rule syntax, see the [egress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#egress-rules-reference).
    
    
    echo """
    # Rule 1: Allow the outbound spoke proposal to initiate attachment to the hub in
    # the hub project, which includes verifying the backing VPC network
    - egressTo:
        operations:
        - serviceName: networkconnectivity.googleapis.com
          methodSelectors:
          - method: "*"
        - serviceName: compute.googleapis.com
          methodSelectors:
          - method: NetworksService.Get
        resources:
        - projects/111111111111
      egressFrom:
        identities:
        # Specify the principal identifier for the spoke administrator or deployment pipeline:
        - serviceAccount:spoke-admin-sa@spoke-project.iam.gserviceaccount.com
        # - group:spoke-admins@example.org
        # - user:spoke-admin@example.org
    """ > spoke-egress.yaml
    

As a best practice, define egress rules that are as specific as possible:

  * `identities`: Specify only the principal identifier needed for your environment rather than broad identity types. In this example, Rule 1 specifies a service account for an automated deployment pipeline. Alternatively, you can specify a Google group for team administration or an individual user account. For details, see [Supported identities for ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/supported-identities).

  * `operations`: Restrictions for `networkconnectivity.googleapis.com` are enforced at the service level, requiring `method: "*"`. For `compute.googleapis.com`, specify `method: NetworksService.Get` to grant permission to verify the backing VPC network when initiating attachment to the hub.

  * `resources`: Specify the exact hub project number in `resources`. Avoid wildcards (`*`).




### Hub perimeter rules

To enable hub administration and allow incoming spoke proposals, the hub administrator configures the following ingress and egress rules:

Rule | Details  
---|---  
Ingress rule 1: Hub management |  When a hub administrator manages the hub from outside the perimeter (such as from an administrator workstation, Cloud Shell, or the Google Cloud console), VPC Service Controls evaluates the call as an ingress request to the hub project. This rule allows the hub administrator to review proposed spokes and accept them (transitioning the spoke to `ACTIVE`) or reject them (transitioning the spoke to `REJECTED`). `HubPerimeter` must allow ingress from the hub administrator's identity and network origin.   
  
This rule isn't needed if hub management is performed exclusively from within a VPC network protected by `HubPerimeter`.   
Ingress rule 2: Hub attachment |  When a spoke administrator proposes a spoke, the request initiates attachment to the hub in the hub project. `HubPerimeter` must allow ingress from the spoke administrator's identity and network origin for the NCC API across service perimeters.   
Egress rule 1: Spoke linking and network verification |  When a spoke administrator proposes a spoke, the request calls back to the spoke project to complete linking the spoke to the hub and put the spoke into a `PENDING_REVIEW` state. As part of the request, the NCC API also verifies the backing VPC network by using the Compute Engine API. `HubPerimeter` must allow egress from the spoke administrator for both the NCC and Compute Engine APIs.   
  
#### Hub perimeter definition

The ingress and egress rule examples in the following sections are based on the following perimeter definition.

For more information about service perimeters, see [Service perimeter details and configuration](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters).
    
    
    # Hub perimeter definition
    name: accessPolicies/1234567890/servicePerimeters/HubPerimeter
    status:
      resources:
      - projects/111111111111
      restrictedServices:
      - networkconnectivity.googleapis.com
      - compute.googleapis.com
    title: HubPerimeter
    

#### Hub ingress rules

This section provides an example that implements the ingress rules for the hub perimeter as described in Hub perimeter rules.

For details about rule syntax, see the [ingress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules-reference). To apply rules, see [Configuring ingress and egress policies](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies).
    
    
    echo """
    # Rule 1: Allow the hub administrator to manage the hub in the hub project
    # (if managing from outside HubPerimeter)
    - ingressFrom:
        identities:
        # Specify the principal identifier for the hub administrator:
        - group:hub-admins@example.com
        # - user:hub-admin@example.com
        # - serviceAccount:hub-admin-sa@hub-project.iam.gserviceaccount.com
        sources:
        - accessLevel: accessPolicies/1234567890/accessLevels/HubAdminAccessLevel
        # Alternatively, specify a management project or VPC network if managing
        # from a VPC network outside the perimeter:
        # - resource: projects/MANAGEMENT_PROJECT_NUMBER
      ingressTo:
        operations:
        - serviceName: networkconnectivity.googleapis.com
          methodSelectors:
          - method: "*"
        resources:
        - projects/111111111111
    
    # Rule 2: Allow the inbound spoke proposal to initiate attachment to the hub
    - ingressFrom:
        identities:
        # Specify the principal identifier for the spoke administrator or deployment pipeline:
        - serviceAccount:spoke-admin-sa@spoke-project.iam.gserviceaccount.com
        # - group:spoke-admins@example.org
        # - user:spoke-admin@example.org
        sources:
        # Specify an access level defined in the hub organization's access policy if
        # the spoke administrator manages spokes from the Google Cloud console or
        # external networks:
        - accessLevel: accessPolicies/1234567890/accessLevels/SpokeAdminAccessLevel
        # Alternatively, specify the spoke project if the spoke administrator
        # manages from a VPC network in the spoke project:
        # - resource: projects/222222222222
      ingressTo:
        operations:
        - serviceName: networkconnectivity.googleapis.com
          methodSelectors:
          - method: "*"
        resources:
        - projects/111111111111
    """ > hub-ingress.yaml
    

As a best practice, define ingress rules that are as specific as possible:

  * `identities`: Specify only the principal identifier needed for your environment rather than broad identity types:

    * In Rule 1, this example specifies a hub administrator Google group for team administration. Alternatively, you can specify an individual user account or service account. This rule is required only if managing the hub from outside `HubPerimeter`.
    * In Rule 2, this example specifies a spoke administrator service account for an automated deployment pipeline. Alternatively, you can specify a Google group for team administration or an individual user account.

For more information, see [Supported identities for ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/supported-identities).

  * `sources`: Restrict origins to known access levels or projects:

    * In Rule 1, this example specifies an access level for hub administrators from the access policy managing `HubPerimeter` to authorize external sources such as administrator workstations, Cloud Shell, or the Google Cloud console. Alternatively, you can allow access from a management VPC network outside the perimeter by using the `- resource:` attribute to specify the project or VPC network. For details, see [Allow access from outside a perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels) and [Context-aware access with ingress rules](https://docs.cloud.google.com/vpc-service-controls/docs/context-aware-access).
    * In Rule 2, this example specifies an access level for spoke administrators from the access policy managing `HubPerimeter` to authorize external sources such as administrator workstations, Cloud Shell, or the Google Cloud console. Alternatively, you can allow access from a VPC network in the spoke project by using the `- resource:` attribute to specify the spoke project number (such as for an automated deployment pipeline).
  * `operations`: Restrictions for `networkconnectivity.googleapis.com` are enforced at the service level, requiring `method: "*"`. More granular methods aren't available for this service.

  * `resources`: Specify the exact hub project number in `resources`. Avoid wildcards (`*`).




#### Hub egress rule

This section provides an example that implements the egress rule for the hub perimeter as described in Hub perimeter rules.

For details about rule syntax, see the [egress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#egress-rules-reference).
    
    
    echo """
    # Rule 1: Allow the inbound spoke proposal to call back to the spoke project to
    # complete linking the spoke to the hub, which includes verifying the backing
    # VPC network
    - egressTo:
        operations:
        - serviceName: networkconnectivity.googleapis.com
          methodSelectors:
          - method: "*"
        - serviceName: compute.googleapis.com
          methodSelectors:
          - method: NetworksService.Get
        resources:
        - projects/222222222222
      egressFrom:
        identities:
        # Specify the principal identifier for the spoke administrator or deployment pipeline:
        - serviceAccount:spoke-admin-sa@spoke-project.iam.gserviceaccount.com
        # - group:spoke-admins@example.org
        # - user:spoke-admin@example.org
    """ > hub-egress.yaml
    

As a best practice, define egress rules that are as specific as possible:

  * `identities`: Specify the principal identifier for the spoke administrator (such as a deployment pipeline service account, group, or user account). When a spoke administrator proposes a spoke, `HubPerimeter` evaluates egress under the spoke administrator's identity to complete linking the spoke to the hub in the spoke project, which includes verifying the backing VPC network.

For details, see [Supported identities for ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/supported-identities).

  * `operations`: Restrictions for `networkconnectivity.googleapis.com` are enforced at the service level, requiring `method: "*"`. For `compute.googleapis.com`, specify `method: NetworksService.Get` to grant permission to verify the backing VPC network when completing the link to the spoke project.

  * `resources`: Specify the exact spoke project number in `resources`. Avoid wildcards (`*`).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
