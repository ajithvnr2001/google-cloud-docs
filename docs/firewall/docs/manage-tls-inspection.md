---
url: https://docs.cloud.google.com/firewall/docs/manage-tls-inspection/
title: Manage TLS inspection \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:13:16.047535+00:00
---

# Manage TLS inspection  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/manage-tls-inspection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Manage TLS inspection Stay organized with collections  Save and categorize content based on your preferences. 

To enforce security controls and inspect encrypted traffic, configure Transport Layer Security (TLS) inspection policies for Cloud Next Generation Firewall (Cloud NGFW). This document describes how to manage TLS inspection policies in your project.

This document is intended for network administrators and security administrators who manage TLS inspection configurations and secure network connections.

Before managing TLS inspection policies, an existing policy must be configured in your project. For more information about core concepts of TLS inspection—such as **Certificate Authority (CA) pools** , Google-managed **Certificate Authority Service** , and **trust configs** —see the [TLS inspection overview](https://docs.cloud.google.com/firewall/docs/about-tls-inspection).

## View details for a TLS inspection policy

You can view information about the TLS inspection policy that you created in your project.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `networksecurity.firewallEndpointAssociations.list`
  * `networksecurity.gatewaySecurityPolicies.list`
  * `networksecurity.tlsInspectionPolicies.get`



**Roles**

  * `compute.securityAdmin`
  * `compute.networkAdmin`
  * `compute.networkUser`



###  Console 

  1. In the Google Cloud console, go to the **TLS inspection policies** page.

[Go to TLS inspection policies](https://console.cloud.google.com/net-security/tls/policies/list)

  2. In the project selector menu, select your project.

  3. The TLS inspection policies are listed in the **TLS inspections** section.

  4. To view the details, click the name of your TLS inspection policy.




## List all TLS inspection policies

You can list all the TLS inspection policies in a project.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `networksecurity.firewallEndpointAssociations.list`
  * `networksecurity.gatewaySecurityPolicies.list`
  * `networksecurity.locations.list`
  * `networksecurity.tlsInspectionPolicies.list`



**Roles**

  * `compute.securityAdmin`
  * `compute.networkAdmin`
  * `compute.networkUser`



###  Console 

  1. In the Google Cloud console, go to the **TLS inspection policies** page.

[Go to TLS inspection policies](https://console.cloud.google.com/net-security/tls/policies/list)

  2. In the project selector menu, select your project.

  3. The TLS inspection policies are listed in the **TLS inspections** section.




###  gcloud 

To list all TLS inspection policies, use the [`gcloud network-security tls-inspection-policies list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/tls-inspection-policies/list):
    
    
    gcloud network-security tls-inspection-policies list \
        --project PROJECT_ID \
        --location REGION
    

Replace the following:

  * `PROJECT_ID`: the project ID for the TLS inspection policy
  * `REGION`: the name of the region for which you want to list the TLS inspection policy



## Edit a TLS inspection policy

You can modify an existing TLS inspection policy in your project.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `certificatemanager.trustconfigs.list`
  * `certificatemanager.trustconfigs.use`
  * `privateca.caPools.list`
  * `privateca.caPools.use`
  * `privateca.certificateAuthorities.list`
  * `networksecurity.operations.get`
  * `networksecurity.tlsInspectionPolicies.get`
  * `networksecurity.tlsInspectionPolicies.list`
  * `networksecurity.tlsInspectionPolicies.update`



**Roles**

  * `compute.securityAdmin`
  * `compute.networkAdmin`



###  Console 

  1. In the Google Cloud console, go to the **TLS inspection policies** page.

[Go to TLS inspection policies](https://console.cloud.google.com/net-security/tls/policies/list)

  2. In the project selector menu, select your project.

  3. The TLS inspection policies are listed in the **TLS inspections** section.

  4. To edit a policy, click the name of your TLS inspection policy.

  5. Click **Edit**.

  6. Modify the required fields. For more information about each field, see [Create a TLS inspection policy](https://docs.cloud.google.com/firewall/docs/setup-tls-inspection#create-tls-inspection-policy).

  7. Click **Save**.




## Delete a TLS inspection policy

You can delete a TLS inspection policy from your project. However, if the TLS inspection policy is referenced by a firewall endpoint association, that TLS inspection policy cannot be deleted.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `networksecurity.operations.get`
  * `networksecurity.tlsInspectionPolicies.delete`



**Roles**

  * `compute.securityAdmin`
  * `compute.networkAdmin`



###  Console 

  1. In the Google Cloud console, go to the **TLS inspection policies** page.

[Go to TLS inspection policies](https://console.cloud.google.com/net-security/tls/policies/list)

  2. In the project selector menu, select your project.

  3. The TLS inspection policies are listed in the **TLS inspections** section.

  4. To delete a TLS inspection policy, select the checkbox next to its name.

  5. Click **Delete**.

  6. Click **Delete** again.




###  gcloud 

To delete a TLS inspection policy, use the [`gcloud network-security tls-inspection-policies delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/tls-inspection-policies/delete):
    
    
    gcloud network-security tls-inspection-policies delete \
        projects/PROJECT_ID/locations/REGION/tlsInspectionPolicies/TLS_INSPECTION_NAME \
        --location REGION
    

Replace the following:

  * `PROJECT_ID`: the project ID of the TLS inspection policy
  * `TLS_INSPECTION_NAME`: the name of the TLS inspection
  * `REGION`: the region where the TLS inspection policy is created



## What's next?

  * [Set up TLS inspection](https://docs.cloud.google.com/firewall/docs/setup-tls-inspection)
  * [Configure intrusion detection and prevention service](https://docs.cloud.google.com/firewall/docs/configure-intrusion-prevention)
  * [Create and manage firewall endpoints](https://docs.cloud.google.com/firewall/docs/configure-firewall-endpoints)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
