---
url: https://docs.cloud.google.com/armor/docs/armor-enterprise-using/
title: Set up Cloud Armor Enterprise \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:56.382671+00:00
---

# Set up Cloud Armor Enterprise  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/armor-enterprise-using/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Guides ](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)



Send feedback 

#  Set up Cloud Armor Enterprise Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage your subscription to Google Cloud Armor Enterprise and enroll your projects. By subscribing and enrolling your projects, you gain access to advanced security features and distributed denial-of-service (DDoS) mitigation capabilities that help protect your services against denial-of-service and web attacks. For a product overview, see the [Cloud Armor Enterprise overview](https://docs.cloud.google.com/armor/docs/armor-enterprise-overview).

## Required IAM permissions

To enroll a project into the Cloud Armor Enterprise subscription, you must have the following IAM permissions:

IAM permission | API methods | Roles  
---|---|---  
`billing.accounts.update` | N/A | [Billing Account Administrator (`roles/billing.admin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin)  
`compute.projects.setCloudArmorTier` | `Projects setCloudArmorTier` | [Compute Admin (`roles/compute.admin`)](https://docs.cloud.google.com/iam/docs/understanding-roles#compute.admin)  
  
To learn more about billing permissions, see [Cloud Billing access control and permissions](https://docs.cloud.google.com/billing/docs/how-to/billing-access).

## Subscribe to Cloud Armor Enterprise Annual

To subscribe to Cloud Armor Enterprise Annual and enroll the current project, follow these steps.

###  Console 

#### Subscribe to Cloud Armor Enterprise Annual

  1. In the Google Cloud console, go to the **Cloud Armor Service Tier** page. If your subscription is active, then the billing account is already subscribed.

[Go to Cloud Armor Service Tier](https://console.cloud.google.com/net-security/securitypolicies/servicetier)

  2. Click **Subscribe and enroll** in the **Google Cloud Armor Enterprise Annual** pane. You see a confirmation dialog.




**Note:** We strongly recommend that you enroll your projects in Cloud Armor Enterprise as soon as possible because activation can take up to one hour. During this period, you can continue to enroll projects.

## Enroll projects to Cloud Armor Enterprise

**Note:** If you create a hierarchical security policy in a project that isn't enrolled in Cloud Armor Enterprise, your project is automatically enrolled in Cloud Armor Enterprise Paygo. For more information about hierarchical security policy automatic enrollment behavior, see [Hierarchical security policies](https://docs.cloud.google.com/armor/docs/armor-enterprise-overview#hierarchical).

To enroll projects to Cloud Armor Enterprise Annual or Paygo, follow these steps. If your project is already enrolled, you can change your enrollment tier by enrolling in the new enrollment tier. For example, if your project is enrolled in Cloud Armor Enterprise Annual, you can enroll to Cloud Armor Enterprise Paygo to change the enrollment tier.

###  Console 

#### Enroll a project to Cloud Armor Enterprise Annual

**Note:** Before you can enroll a project to Cloud Armor Enterprise Annual, you must subscribe the billing account.

  1. In the Google Cloud console, go to the **Cloud Armor Service Tier** page.

[Go to Cloud Armor Service Tier](https://console.cloud.google.com/net-security/securitypolicies/servicetier)

  2. In the **Google Cloud Armor Enterprise Annual** pane, click **Enroll**.




#### Enroll a project to Cloud Armor Enterprise Paygo

  1. In the Google Cloud console, go to the **Cloud Armor Service Tier** page.

[Go to Cloud Armor Service Tier](https://console.cloud.google.com/net-security/securitypolicies/servicetier)

  2. In the **Google Cloud Armor Enterprise Paygo** pane, click **Enroll**.




###  gcloud 

#### Enroll a project to Cloud Armor Enterprise Annual

**Note:** Before you can enroll a project to Cloud Armor Enterprise Annual, you must subscribe the billing account.

Use the following command to enroll a project in Cloud Armor Enterprise Annual:
    
    
    gcloud compute project-info update --cloud-armor-tier CA_ENTERPRISE_ANNUAL
    

#### Enroll a project to Cloud Armor Enterprise Paygo

Use the following command to enroll a project in Cloud Armor Enterprise Paygo:
    
    
    gcloud compute project-info update --cloud-armor-tier CA_ENTERPRISE_PAYGO
    

**Note:** We strongly recommend that you enroll your projects in Cloud Armor Enterprise as soon as possible because activation can take up to one hour. During this period, you can continue to enroll projects.

## Remove a project from Cloud Armor Enterprise

Before you remove your project from Cloud Armor Enterprise, we recommend that you familiarize yourself with [Downgrading from Cloud Armor Enterprise](https://docs.cloud.google.com/armor/docs/armor-enterprise-overview#downgrade). After you unenroll a project from Cloud Armor Enterprise, up to twelve hours might elapse before the change takes effect. You can continue to unenroll (or enroll) other projects during this period.

**Note:** If Global Front End Enterprise was enabled in your project, Google Cloud doesn't restore the previous Google Cloud Armor tier when you disable Global Front End Enterprise. You must immediately and manually designate a Cloud Armor billing tier (either Cloud Armor Standard or Cloud Armor Enterprise PayGo) to prevent security policy degradation or unexpected billing. For more information, see [Disabling Global Front End Enterprise](https://docs.cloud.google.com/armor/docs/armor-enterprise-overview#disable-gfe) and the [Global Front End overview](https://docs.cloud.google.com/docs/networking/cross-cloud-network/global-front-end/gfee-overview).

To unenroll a project from Cloud Armor Enterprise, follow these steps.

###  Console 

#### Unenroll a project from Cloud Armor Enterprise Annual

  1. In the Google Cloud console, go to the **Cloud Armor Service Tier** page.

[Go to Cloud Armor Service Tier](https://console.cloud.google.com/net-security/securitypolicies/servicetier)

  2. In the **Google Cloud Armor Standard** pane, click **Enroll**.




#### Unenroll a project from Cloud Armor Enterprise Paygo

  1. In the Google Cloud console, go to the **Cloud Armor Service Tier** page.

[Go to Cloud Armor Service Tier](https://console.cloud.google.com/net-security/securitypolicies/servicetier)

  2. In the **Google Cloud Armor Standard** pane, click **Enroll**.




###  gcloud 

#### Unenroll a project from Cloud Armor Enterprise Annual
    
    
    gcloud compute project-info update --cloud-armor-tier CA_STANDARD
    

#### Unenroll a project from Cloud Armor Enterprise Paygo
    
    
    gcloud compute project-info update --cloud-armor-tier CA_STANDARD
    

## View your enrollment information

Use the following sections to view your current Cloud Armor Enterprise enrollment tier, or to view the number of resources covered by your enrollment.

### View current Cloud Armor Enterprise enrollment tier

Use these instructions to view your current Cloud Armor Enterprise enrollment tier.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Armor Service Tier** page.

[Go to Cloud Armor Service Tier](https://console.cloud.google.com/net-security/securitypolicies/servicetier)

  2. You see the available Cloud Armor Enterprise service tiers, including Cloud Armor Enterprise Annual and Cloud Armor Enterprise Paygo. Your current Cloud Armor Enterprise enrollment tier is highlighted, and has the status "Enrolled" in the **Project** field.




###  gcloud 

To view your current Cloud Armor Enterprise enrollment tier, check the `cloudArmorTier` value by using the [`gcloud compute project-info describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/project-info/describe):
    
    
    gcloud compute project-info describe
    

### View the number of backend services and backend buckets covered by an enrollment

Each project that is enrolled in Cloud Armor Enterprise shows the number of backend services and backend buckets covered on the **Cloud Armor Enterprise** page. The number that you see is the total number of backend services and backend buckets covered by the enrollment.

If the project is enrolled in Cloud Armor Enterprise Standard, which is the default tier, this count isn't displayed.

## Unsubscribe a billing account from Cloud Armor Enterprise Annual

A Cloud Armor Enterprise Annual subscription is a one-year commitment that's renewed automatically. To prevent renewal at the end of the one-year term, you must disable automatic renewal. After automatic renewal is disabled, your current one-year subscription period continues to the end. At the end of the subscription period, your Cloud Armor Enterprise subscription isn't renewed. If your project has effective hierarchical security policies, your project is downgraded to Cloud Armor Enterprise Paygo. Otherwise, all projects in the billing account that are enrolled in Cloud Armor Enterprise Annual revert to Cloud Armor Enterprise Standard.

To cancel Cloud Armor Enterprise Annual auto-renewal, follow these steps.

###  Console 

  1. When you are signed in to the subscribed billing account, in the Google Cloud console, go to the **Cloud Armor Service Tier** page.

[Go to Cloud Armor Service Tier](https://console.cloud.google.com/net-security/securitypolicies/servicetier)

  2. Click **Auto-Renew (off)**. Your Cloud Armor Enterprise subscription is not renewed when your current subscription expires. At that time, projects enrolled in Cloud Armor Enterprise are no longer enrolled. They still receive the DDoS protection provided in Cloud Armor Enterprise Standard.




## Open a DDoS response support case

To engage DDoS response support, you open a support case through the Google Cloud console. For customers that meet the [eligibility requirements](https://docs.cloud.google.com/armor/docs/armor-enterprise-overview#ddos-response-support), your case is escalated to the Cloud Armor DDoS Response Team for support, triage, and potential mitigation.

To open a DDoS response support case, see [Get support for a DDoS case](https://docs.cloud.google.com/armor/docs/getting-support#ddos-case).

## Engage DDoS bill protection

To file a claim for DDoS Bill Protection, your project must be enrolled in Cloud Armor Enterprise Annual, and you must prepare the following information:

  * The billing account associated with the targeted project.
  * The project number of the project containing the targeted resource.
  * The internet-facing IP address of the targeted resource.
  * The time that the attack started.
  * The time that the attack concluded.
  * Normal traffic volumes for the impacted service.
  * Attack volumes for the impacted service.



You can initiate a chat or contact billing support through the Google Cloud console. For more information on contacting Cloud Billing Support, see [How to contact Cloud Billing Support](https://docs.cloud.google.com/support/billing#how_to_contact_support).

### Cross-project referencing requirements

If you use [cross-project service referencing](https://docs.cloud.google.com/load-balancing/docs/https#cross-project) and you want to take advantage of the Cloud Armor Enterprise pricing, both the frontend and backend service projects must be enrolled in Cloud Armor Enterprise Annual.

### Qualified Attacks

For regional external passthrough Network Load Balancers, protocol forwarding, and public IP addresses (VMs), an attack is considered a Qualified Attack (as described in the Cloud Armor [terms and limitations](https://docs.cloud.google.com/armor/docs/armor-enterprise-overview#terms-and-limitations)) only if advanced DDoS protection was already enabled for the region with the attacked endpoint at the start of the attack.

## Use Google Threat Intelligence

To use [Google Threat Intelligence](https://docs.cloud.google.com/armor/docs/armor-enterprise-overview#nti), you configure a security policy using the `evaluateThreatIntelligence` match expression, providing a feed name based on the category that you want to allow or block. If Google Threat Intelligence incorrectly blocks an IP address, you can add the IP address to the exclusion list to allow traffic.

## Troubleshooting Cloud Armor Enterprise

This section provides information to help you resolve any issues with Cloud Armor Enterprise.

### You subscribed to Cloud Armor Enterprise Annual, but your bill continues to be pay-as-you-go

If you subscribed to Cloud Armor Enterprise and you are still being billed on a pay-as-you-go basis, check whether you enrolled your projects in Cloud Armor Enterprise.

### The `Subscribe` button is unavailable

If you are unable to subscribe to Cloud Armor Enterprise Annual because the **Subscribe** button is unavailable, ensure that the user who is trying to subscribe has the `billing.accounts.update` permission, which is required to subscribe at the billing account level.

### You unsubscribed from Google Cloud Armor Enterprise Annual, but were automatically enrolled in Paygo

If you unsubscribe your billing account from Google Cloud Armor Enterprise Annual while your project has effective hierarchical security policies, your project is downgraded to Cloud Armor Enterprise Paygo. This is because hierarchical security policies require an active Google Cloud Armor Enterprise enrollment. To unenroll from Paygo, you must first [delete your hierarchical security policies](https://docs.cloud.google.com/armor/docs/hierarchical-policies-using#delete-policy).

### Your project was automatically enrolled to Cloud Armor Enterprise

Projects that are covered by a hierarchical security policy are automatically enrolled to the highest Cloud Armor Enterprise tier for which they are eligible. For more information, see [Cloud Armor Enterprise enrollment and billing behavior](https://docs.cloud.google.com/armor/docs/hierarchical-policies-overview#enrollment).

### Billing discrepancies

If these troubleshooting tips don't resolve the problems that you are experiencing, contact the [Google Cloud billing support team](https://docs.cloud.google.com/support/billing).

## What's next

  * [Troubleshoot issues](https://docs.cloud.google.com/armor/docs/troubleshooting)
  * [Use the custom rules language reference](https://docs.cloud.google.com/armor/docs/rules-language-reference)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
