---
url: https://docs.cloud.google.com/vpc/docs/manage-security-private-service-connect-producers/
title: Manage security for Private Service Connect producers \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:12.304022+00:00
---

# Manage security for Private Service Connect producers  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/manage-security-private-service-connect-producers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage security for Private Service Connect producers

This page describes how service producers can implement security for producer organizations and projects that use Private Service Connect.

_Consumer accept lists_ let service owners specify networks or projects that can connect to individual [service attachments](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#service-attachments). _Organization policies_ also control access to service attachments, but they let network administrators broadly control access to all service attachments in an organization.

Consumer accept lists and organization policies are complementary and can be used together. In this case, a Private Service Connect connection is only created if it is authorized by both of these security mechanisms.

## Roles

To get the permissions that you need to manage organization policies, ask your administrator to grant you the [Organization policy administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) IAM role on the organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Producer organization policies

You can use [organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview#organization_policy) with the `compute.restrictPrivateServiceConnectConsumer` [list constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#list-constraint) to control which endpoints and backends can connect to Private Service Connect service attachments. If an endpoint or backend is rejected by a producer organization policy, the creation of the resource succeeds, but the connection enters the rejected state.

For more information, see [Producer-side organization policies](https://docs.cloud.google.com/vpc/docs/private-service-connect-security#producer-side-org-policies).

### Reject connections from unauthorized endpoints and backends

**Resources** : endpoints and backends

###  gcloud 

  1. Create a temporary file called `/tmp/policy.yaml` to store the new policy. Add the following content to the file:
         
         name: organizations/PRODUCER_ORG/policies/compute.restrictPrivateServiceConnectConsumer
         spec:
           rules:
             - values:
                 allowedValues:
                 - under:organizations/CONSUMER_ORG_NUMBER
         

Replace the following:

     * `PRODUCER_ORG`: the [organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id) of the producer organization that you want to control consumer Private Service Connect access to.
     * `CONSUMER_ORG_NUMBER`: the numeric resource ID of the consumer organization that you want to let connect to service attachments in the producer organization.

To specify additional organizations that can connect to service attachments in your project, include additional entries in the `allowedValues` section.

In addition to organizations, you can specify authorized folders and projects in the following form:

     * `under:folders/FOLDER_ID`

The `FOLDER_ID` must be the numeric ID.

     * `under:projects/PROJECT_ID`

The `PROJECT_ID` must be the string ID.

For example, the following file shows an organization policy configuration that rejects connections from endpoints or backends to service attachments in `Producer-org-1` unless they are associated with an allowed value or a descendant of an allowed value. The allowed values are the organization `Consumer-org-1`, the project `Consumer-project-1`, and the folder `Consumer-folder-1`.
    
    name: organizations/Producer-org-1/policies/compute.restrictPrivateServiceConnectConsumer
    spec:
    rules:
      - values:
          allowedValues:
          - under:organizations/Consumer-org-1
          - under:projects/Consumer-project-1
          - under:folders/Consumer-folder-1
    

  2. Apply the policy.
         
         gcloud org-policies set-policy /tmp/policy.yaml
         

  3. View the policy that is in effect.
         
         gcloud org-policies describe compute.restrictPrivateServiceConnectConsumer \
             --effective \
             --organization=PRODUCER_ORG
         




## Consumer accept and reject lists

**Resources** : endpoints and backends

Consumer accept and reject lists are associated with service attachments. These lists let you explicitly accept or deny connections from consumer projects or networks.

For more information, see [Consumer accept and reject lists](https://docs.cloud.google.com/vpc/docs/private-service-connect-security#consumer-lists).

## Interaction between accept lists and organization policies

Both consumer accept lists and organization policies control whether a connection can be established between two Private Service Connect resources. Connections are blocked if either an accept list or an organization policy denies the connection.

For example, a policy with the `restrictPrivateServiceConnectConsumer` constraint can be configured to block connections from outside of the producer's organization. Even if a service attachment is configured to automatically accept all connections, the organization policy still blocks connections from outside of the producer's organization. We recommend using both accept lists and organization policies together to help provide layered security.

## Configure accept and reject lists

For information about how to create a new service attachment that has consumer accept or reject lists, see [Publish a service with explicit project approval](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#publish-service-explicit).

For information about how to update consumer accept or reject lists, see [Manage requests for access to a published service](https://docs.cloud.google.com/vpc/docs/manage-private-service-connect-services#access).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
