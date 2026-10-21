---
url: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/saml-overview/
title: SAML overview \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:15:28.616926+00:00
---

# SAML overview  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/saml-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  SAML overview Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

SAML (Security Assertion Markup Language) is an open standard that allows an identity provider to pass authorization credentials to a service provider. By using SAML with Apigee, you can support SSO for the Apigee UI.

## How SAML works with Apigee 

The SAML specification defines three entities:

  * Principal (Apigee UI user)
  * Service provider (Google Cloud Platform) 
  * Identity provider (any third-party provider that supports SAML 2.0)



When SAML is enabled, the principal (an Apigee UI user) requests access to the service provider (Google Cloud Platform). Google Cloud Platform (in its role as a SAML service provider) then requests and obtains an identity assertion from the third-party SAML identity provider and uses that assertion to create the OAuth 2.0 token required to access the Apigee UI. The user is then redirected to the Apigee UI.

## Advantages of SAML authentication

SAML authentication offers several advantages. By using SAML you can:

  * **Take full control of user management:** Connect your company's SAML server to Apigee. When users leave your organization and are deprovisioned centrally, they are automatically denied access to Apigee.
  * **Control how users authenticate to access Apigee:** Select different authentication types for your Apigee organizations.
  * **Control authentication policies:** Your SAML provider may support authentication policies that are more in line with your enterprise standards.
  * **Monitor logins, logouts, unsuccessful login attempts and high risk activities** on your Apigee deployment.

**Note** : SAML is only used for authentication by the Apigee UI. Authorization is still controlled by Apigee user roles. See [Apigee roles](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/apigee-roles) for more.

##  Using SAML with Apigee 

To use SAML with Apigee, refer to the resources provided in the following table. 

Apigee component | More information  
---|---  
Apigee UI | 

  * Step-by-step instructions: [Set up single sign-on for managed Google Accounts using third-party identity providers](https://support.google.com/a/answer/60224?hl=en&visit_id=637284597994836724-39242969&ref_topic=6348126&rd=1)
  * Video: [Using a third-party identity provider for SSO with Google Cloud Platform](https://www.youtube.com/watch?v=1NpNPizIBIc)

  
Integrated portal | [Configure the SAML identity provider](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-identity-provider#saml)  
Drupal 8/9 portal | [Integrate simpleSAMLphp authentication](https://www.drupal.org/docs/8/modules/apigee-developer-portal-kickstart/integrate-simplesamlphp-authentication)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
