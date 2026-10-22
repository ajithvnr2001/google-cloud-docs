---
url: https://docs.cloud.google.com/apigee/docs/support/service-requests/provisioning-req/
title: Provisioning requests \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:27:00.459934+00:00
---

# Provisioning requests  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/support/service-requests/provisioning-req/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Provisioning requests Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/service-requests/provisioning-req) documentation._

_Provisioning****_ refers to the process of installing and configuring an organization in Apigee X. The provisioning requests involve operations such as creation and deletion of organizations, environments, environment groups, etc. 

**Note:** Provisioning requests apply only to Apigee X users. Apigee hybrid users can perform these tasks themselves, as they have full access to their respective environments. 

## Eval org

An _eval_ (evaluation) organization is a​​ temporary, self-service organization that is generally created for testing Apigee. These organizations are time-limited and lack the scalability and flexibility of production organizations. 

Service request description | Can I do this myself? | How to perform this operation?  
---|---|---  
Create a new Apigee X eval organization | Yes | You can create an Apigee X eval organization using one of the following methods: **Provisioning wizard**

  * [Provisioning an eval org](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/eval-orgs)

**Command line**

  * [ Provisioning an eval org](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-eval) (`gcloud`)

  
Delete an existing Apigee X eval organization | Yes | You can delete an eval org using the command line: [ Delete an eval org using command line](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/organizations/delete)  
  
## Paid org

A paid organization, also referred to as a _production_ organization, is a permanent organization with full scalability. A paid organization can use either Subscription or Pay-as-you-go pricing. For more information, see [Apigee pricing](https://docs.cloud.google.com/apigee/pricing).

Service request description | Can I do this myself? | How to perform this operation?  
---|---|---  
Create a new Apigee X paid (Subscription or Pay-as-you-go) organization | Yes | **Prerequisite** Ensure that you have the required entitlements for creating a paid organization based on your chosen pricing model: 

  * See [Subscription entitlements](https://docs.cloud.google.com/apigee/docs/support/service-requests/apigee/docs/api-platform/reference/subscription-entitlements) for paid Subscription organizations. If needed, follow the instructions in [ Entitlement requests](https://docs.cloud.google.com/apigee/docs/support/service-requests/entitlement-req) to get the required entitlements.
  * See [Pay-as-you-go entitlements](https://docs.cloud.google.com/apigee/docs/support/service-requests/apigee/docs/api-platform/reference/pay-as-you-go-entitlements) for paid Pay-as-you-go organizations.

**Creating Apigee X paid organization** You can create an Apigee X paid organization using one of the following methods: **Provisioning wizard**

  * [Provisioning a paid org](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/overview)

**Command line**

  * [Provisioning a paid org using command line](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli)

  
Delete an existing Apigee X paid (Subscription) organization | Yes | You can delete an existing Apigee X paid Subscription organization using the API. See [ Delete an Apigee organization](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/delete). To delete an existing Apigee X paid Subscription organization _and entitlement_ , or to reconfigure an existing entitlement, file a support ticket with Apigee and including the following information:

  * Google Cloud Project ID 
  * Apigee X organization name

  
Delete an existing Apigee X paid (Pay-as-you-go) organization | Yes | You can delete an existing Apigee X paid Pay-as-you-go organization using the API. See [ Delete an Apigee organization](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/delete).  To stop billing for Apigee Pay-as-you-go services, make sure to delete all environments in your Pay-as-you-go organization before deleting your org. You can delete an environment from an existing Apigee Pay-as-you-go organization using one of the following methods: 

  * [Delete an environment with the Apigee UI](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-working-with?hl=en_US#deleting-an-environment-with-the-apigee-ui)
  * [Delete an environment with the Apigee API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/delete)

  
Expand an existing Apigee X paid (Subscription or Pay-as-you-go) organization to multiple regions | Yes | You can manage regions for an Apigee X paid organization following the instructions in [ Using multiple regions](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/multi-region). **Note:** There's a limit on the number of regions you can have per organization as documented in the [ Limits](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits#environment-and-organization) page.   
Decommission a region in Apigee X | Yes | You can decommission a region by deleting the instance in the specific region by following the instructions in [ Delete an existing instance](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/instances#deleting-an-existing-instance).  
  
## Eval and paid (Subscription or Pay-as-you-go) orgs

The following table has some requests that are common to both Apigee X eval and paid organizations: 

Service request description | Can I do this myself? | How to perform this operation?  
---|---|---  
Create new environments in an existing Apigee X organization | Yes | You can create an environment in an existing Apigee X eval or paid (Subscription or Pay-as-you-go) organization using one of the following methods: **Apigee X UI**

  * [ Create a new environment in the UI](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-working-with#creating-a-new-environment-in-the-ui)

**Apigee API**

  * [ Create a new environment with the Apigee API](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-working-with#creating-a-new-environment-with-the-apigee-api)

  
Delete environments from an existing Apigee X organization | Yes | You can delete an environment from an existing Apigee X eval or paid organization using one of the following methods: **Apigee X UI**

  * [ Delete an environment with the Apigee UI](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-working-with#deleting-an-environment-with-the-apigee-ui)

**Apigee API**

  * [ Delete an environment with the Apigee API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/delete)

  
Create new environment group in an existing Apigee X organization | Yes | You can create an environment group in an existing Apigee X eval or paid organization using one of the following methods: **Apigee X UI**

  * [ Create an environment group in the UI](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environmentgroups-working-with#creating-an-environment-group-in-the-ui)

**Apigee API**

  * [ Create an environment group with the Apigee API](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environmentgroups-working-with#creating-an-environment-group-with-the-apigee-api)

  
Delete environment group from an existing Apigee X organization | Yes | [ Delete an environment group with the Apigee API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups/delete)  
Add environment to environment group in an existing Apigee X organization | Yes | You can create an environment group in an existing Apigee X eval or paid organization using one of the following methods: **Apigee X UI**

  * [ Add an environment to a group using the Apigee UI](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environmentgroups-working-with#adding-an-environment-to-a-group-using-the-apigee-ui)

**Apigee API**

  * [ Add an environment to a group using the Apigee API](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environmentgroups-working-with#adding-an-environment-to-a-group-using-the-apigee-api)

  
Remove environment from an environment group in an existing Apigee X organization | Yes | [ Remove an environment from an environment group with the Apigee API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups.attachments/delete)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
