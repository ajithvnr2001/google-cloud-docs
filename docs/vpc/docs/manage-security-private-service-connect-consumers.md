---
url: https://docs.cloud.google.com/vpc/docs/manage-security-private-service-connect-consumers/
title: Manage security for Private Service Connect consumers \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:15.353417+00:00
---

# Manage security for Private Service Connect consumers  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/manage-security-private-service-connect-consumers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage security for Private Service Connect consumers

This page describes how service consumers can configure security for consumer organizations and VPC networks that use Private Service Connect.

_Organization policies_ let administrators broadly control which VPC networks or organizations their projects can connect to by using Private Service Connect endpoints and backends. _VPC firewall rules_ and _firewall policies_ let network administrators control network-level access to Private Service Connect resources. Organization policies and firewall rules are complementary and can be used together.

## Roles

To get the permissions that you need to manage organization policies, ask your administrator to grant you the [Organization policy administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) IAM role on the organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To get the permissions that you need to create firewall rules, ask your administrator to grant you the [Compute network administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) IAM role on the VPC network. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Consumer organization policies

You can use [organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview#organization_policy) with [list constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#list-constraint) to control the deployment of Private Service Connect endpoints or backends. If an endpoint or backend is blocked by a consumer organization policy, the creation of the resource fails.

For more information, see [Consumer-side organization policies](https://docs.cloud.google.com/vpc/docs/private-service-connect-security#consumer-side-org-policies).

### Block endpoints and backends from connecting to unauthorized service attachments

**Resources** : endpoints and backends

###  gcloud 

  1. Create a temporary file called `/tmp/policy.yaml` to store the new policy. Add the following content to the file:
         
         name: organizations/CONSUMER_ORG/policies/compute.restrictPrivateServiceConnectProducer
         spec:
           rules:
             - values:
                 allowedValues:
                 - under:organizations/PRODUCER_ORG_NUMBER
                 - under:organizations/433637338589
         

Replace the following:

     * `CONSUMER_ORG`: the [organization resource ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id) of the organization that you want to control endpoint and backend connections in.
     * `PRODUCER_ORG_NUMBER`: the numeric organization resource ID of the producer organization that you want to let endpoints and backends connect to.

To block endpoints and backends from connecting to service attachments that are owned by Google, remove the following item from the `allowedValues` section: `- under:organizations/433637338589`.

To specify additional organizations that can connect to service attachments in your project, include additional entries in the `allowedValues` section.

In addition to organizations, you can specify authorized folders and projects in the following form:

     * `under:folders/FOLDER_ID`

The `FOLDER_ID` must be the numeric ID.

     * `under:projects/PROJECT_ID`

The `PROJECT_ID` must be the string ID.

For example, the following can be used to create an organization policy that blocks endpoints and backends in `Consumer-org-1` from connecting to service attachments unless the service attachments are associated with an allowed value or a descendant of an allowed value. The allowed values are the organization `Producer-org-1`, the project `Producer-project-1`, and the folder `Producer-folder-1`.
    
    name: organizations/Consumer-org-1/policies/compute.restrictPrivateServiceConnectProducer
    spec:
        rules:
          - values:
              allowedValues:
              - under:organizations/Producer-org-1
              - under:projects/Producer-project-1
              - under:folders/Producer-folder-1
    

  2. Apply the policy.
         
         gcloud org-policies set-policy /tmp/policy.yaml
         

  3. View the policy that is in effect.
         
         gcloud org-policies describe compute.restrictPrivateServiceConnectProducer \
             --effective \
             --organization=CONSUMER_ORG
         




### Block consumers from deploying endpoints by connection type

**Resources** : endpoints

###  gcloud 

  1. Create a temporary file called `/tmp/policy.yaml` to store the new policy.

     * To block users in a consumer organization from creating endpoints that connect to Google APIs, add the following content to the file:
           
           name: organizations/CONSUMER_ORG/policies/compute.disablePrivateServiceConnectCreationForConsumers
           spec:
             rules:
               - values:
                   allowedValues:
                   - SERVICE_PRODUCERS
           

     * To block users in a consumer organization from creating endpoints that connect to published services, add the following content to the file:
           
           name: organizations/CONSUMER_ORG/policies/compute.disablePrivateServiceConnectCreationForConsumers
           spec:
             rules:
               - values:
                   allowedValues:
                   - GOOGLE_APIS
           

Replace `CONSUMER_ORG` with the name of the consumer organization for which you want to control endpoint deployment.

  2. Apply the policy.
         
         gcloud org-policies set-policy /tmp/policy.yaml
         

  3. View the policy that is in effect.
         
         gcloud org-policies describe compute.restrictPrivateServiceConnectProducer \
             --effective \
             --organization=CONSUMER_ORG
         




## Firewall rules

**Resources** : all

You can use [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls) or [firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview) to control access to Private Service Connect resources. Egress firewall rules can block or allow access from VM instances to the IP address or subnet of endpoints and backends.

For example, figure 1 describes a configuration where firewall rules control access to the subnet that the Private Service Connect endpoint is connected to.

[ ![](https://docs.cloud.google.com/static/vpc/images/psc-consumer-firewall-rules.svg)](https://docs.cloud.google.com/static/vpc/images/psc-consumer-firewall-rules.svg) Firewall rules control traffic to the endpoint-subnet. Traffic from `vm-1` can reach the endpoint-subnet, while traffic from `vm-2` is blocked (click to enlarge). 

  1. The following firewall rule denies all egress traffic to the endpoint subnet:
         
         gcloud compute firewall-rules create deny-all \
             --network=vpc-1 \
             --direction=egress \
             --action=deny \
             --destination-ranges=10.33.0.0/24
             --priority=1000
         

  2. The following higher priority firewall rule allows egress traffic to the endpoint subnet for VMs with the `allow-psc` network tag:
         
         gcloud compute firewall-rules create allow-psc \
             --network=vpc-1 \
             --direction=egress \
             --action=allow \
             --target-tags=allow-psc \
             --destination-ranges=10.33.0.0/24
             --priority=100
         




### Use firewall rules to limit access to endpoints or backends

To limit access from VMs to the subnet of an endpoint or backend, do the following.

  1. Create a firewall rule to deny egress traffic to the endpoint or backend subnet.
         
         gcloud compute firewall-rules create deny-all \
             --network=NETWORK \
             --direction=egress \
             --action=deny \
             --destination-ranges=ENDPOINT_SUBNET_RANGE \
             --priority=1000
         

Replace the following:

     * `NETWORK`: the name of the network of your endpoint or backend.
     * `ENDPOINT_SUBNET_RANGE`: the IP CIDR range of the endpoint or backend subnet that you want to control access to.
  2. Create a second firewall rule to allow egress traffic from tagged VMs to the endpoint or backend subnet.
         
         gcloud compute firewall-rules create allow-psc \
             --network=NETWORK \
             --direction=egress \
             --action=allow \
             --target-tags=allow-psc \
             --destination-ranges=ENDPOINT_SUBNET_RANGE \
             --priority=100
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
