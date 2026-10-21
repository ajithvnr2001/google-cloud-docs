---
url: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/build-integrated-portal/
title: Building your integrated portal \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:57:21.893576+00:00
---

# Building your integrated portal  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/build-integrated-portal/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Building your integrated portal Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Apigee delivers a simple-to-use, integrated portal to document and manage access to your APIs, and foster your app developer community.

All users of Apigee have access to the integrated portal development tools enabling them to build their own developer portal quickly, providing an alternative to the [Drupal-based portal development](https://docs.cloud.google.com/apigee/docs/api-platform/publish/drupal/open-source-drupal-8). For a feature comparison, see [Comparison of developer portal features](https://docs.cloud.google.com/apigee/docs/api-platform/publish/intro-portals#feature-comparison).

## Key features and benefits

The integrated portal provides you with the following key features and benefits: Feature | Benefits  
---|---  
Portal content development | Develop your portal content quickly and easily. 

  * Create pages using the simple-to-use page editor
  * Use Markdown and HTML to compose content
  * Add menus for navigating your portal

  
Portal look-and-feel | Fully customize the look-and-feel of your portal using SCSS style sheets and personalized branding.  
API documentation | Auto-generate API reference documentation based on your OpenAPI Specifications.  
Self-service registration | Provide self-service registration for developers to build apps using your APIs.  
Audience management | Control who can access the portal content and APIs  
Analytics | Configure Google Analytics and custom analytics tracking.  
Advanced customizations | Perform advanced portal customizations, including:

  * Customize your domain
  * Add custom registration fields
  * Extend your portal using scripts
  * Configure your email

  
  
##  How Apigee addresses security in the integrated portal 

The following table describes how Apigee addresses security through built-in features in the integrated portal.

**Important** : While Apigee monitors for and addresses newly emerging security features as required, it is important to note that Apigee integrated portals are not [FedRAMP](https://www.fedramp.gov/) authorized.Feature  | Addresses   
---|---  
Requires HTTPS and transport layer security (TLS)  | Enforces encrypted communication   
Includes `apigee.io` domain registration with [Public Suffix List](https://publicsuffix.org/) | Disallows "supercookies" from being set on subdomains of `apigee.io`  
Requires: 

  * Sanitization of form input 
  * Site-wide JavaScript injection restricted to administrators 

| Guards against HTML, SQL, or backend injection attacks   
Includes `x-content-type-options: nosniff` XSS header  | Disallows browsers from trying to guess MIME types   
Includes `x-frame-options: deny` XSS header  | Disallows embedding portal content into an iFrame   
Includes `x-xss-protection: 1` XSS header  | Disallows pages from loading when they detect reflected cross-site scripting (XSS) attacks   
Uses CSRF tokens  | Guards against cross-site request forgery   
Leverages: 

  * [Google Cloud data encryption at rest](https://cloud.google.com/security/encryption/default-encryption/)
  * [Google user data and retention policies](https://cloud.google.com/security/deletion)
  * Log and debug data retention (6 weeks)

| Customer data protections   
  
## How the integrated portal communicates with Apigee

A majority of the information used by the developer portal is stored on Apigee. The portal acts as a client to Apigee. As necessary, the developer portal sends an HTTP or HTTPS REST request to retrieve information from or send information to Apigee. For example, when a portal user registers a new app on the portal, the portal sends a request to Apigee to store information about the app.

All interactions between the developer portal and Apigee are initiated by the portal. Apigee does not make requests to the portal, it only responds to requests made from the portal. 

The following sections provide more detail.

### Where app registration and API keys are stored

When a portal user completes the app registration process on the integrated portal, the portal sends information about the app to Apigee, including the app name and the API products associated with the app. If Apigee registers the app successfully, Apigee returns a single API key to the portal. The portal user uses that API key to access the API products associated with the app.

Information about the apps and API keys is stored on Apigee only; it is not stored on the portal. When a portal user uses the portal to view information about an app, via the My Apps page for example, the portal makes a request to Apigee with the API key to access the information.

Similarly, when a portal user adds, removes, or modifies an app, the portal sends the modifications to Apigee to be stored.

Because all information about apps and API keys is stored on Apigee, an Apigee administrator can modify the information by using the Apigee UI or management API. For example, an administrator can:

  * Add, remove, or modify a developer app
  * Approve or revoke an API key for a developer app



For more information, see [Controlling access to your APIs by registering apps](https://docs.cloud.google.com/apigee/docs/api-platform/publish/creating-apps-surface-your-api).

### Where app developer account information is stored

Developer account information is stored on Apigee, as follows:

  * Using the [built-in identity provider](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-identity-provider#built-in), when a portal user **[creates an account](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-interact#register)** , the information is stored in the identity provider and is displayed on the [Users page](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/api-portal-users#explore_the_users_page).
  * Using the [SAML identity provider](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-identity-provider#saml), when a portal user **[signs in to the portal](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-interact#saml-auth)** , a shadow record of the information is stored in the identity provider and is displayed on the [Users page](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/api-portal-users#explore_the_users_page).
  * After a portal user [**registers a developer app**](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-interact#register-apps), the user account information is synced to and available on Apigee on the [Developers page](https://docs.cloud.google.com/apigee/docs/api-platform/publish/adding-developers-your-api-product#ui).

Note the following: 

  * Although it is possible to create accounts on behalf of portal users manually using the Apigee UI, as described in [Registering app developers](https://docs.cloud.google.com/apigee/docs/api-platform/publish/adding-developers-your-api-product), this is not recommended to ensure that the user accounts on the integrated portal and Apigee stay in sync.
  * When you [delete a user](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/api-portal-users#delete), the associated app developer is not deleted from the Developers page on Apigee. Similarly, when you [delete a developer](https://docs.cloud.google.com/apigee/docs/api-platform/publish/adding-developers-your-api-product#deletingadeveloper) from Apigee, the user account information is not deleted from the identity provider.



The following user account information is stored on Apigee:

  * First and last name
  * Email address
  * Username
  * Portal account status (active or inactive)
  * Portal role (authenticated user, administrator, other)
  * Role-based permissions
  * Teams to which the portal user is a member (if you have [enrolled in the Preview release of the teams feature](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/developer-teams#enroll))



The email address is the primary key used by Apigee to identify the developer and each must be unique. From the primary key, Apigee generates a unique developer ID for each organization to which the developer belongs.

For more information, see [Register app developers](https://docs.cloud.google.com/apigee/docs/api-platform/publish/adding-developers-your-api-product).

### Where developer team information is stored (Preview)

**Note:** You must [enroll in the Preview release of the teams feature](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/developer-teams#enroll).

When a developer team is created on the portal by a portal user, the developer team information is stored on Apigee, including:

  * Developer team name and description
  * Developer team members and their roles
  * Apps to which the developer team is assigned
  * Audiences assigned to the developer team
  * Time the developer team was created



A unique, auto-generated email address is generated for the developer team and serves as the primary key used by Apigee to identify the developer team.

For more information, see [Share responsibility for an app using developer teams (Preview)](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-interact#teams) and [Manage developer teams](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/developer-teams).

## About the sample portal

When you create a new portal, a set of starter pages is provided for you to use as a jump-off point. The starter pages contain demo content to help inspire your own portal development as you replace the text and images with your unique content. The sample portal theme uses [material design theming](https://material.angular.io/guide/theming) and [SCSS](https://sass-lang.com/).

The following shows the home page of the sample portal.

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/sample-portal.png)

The starter pages provided with the sample portal include:

Page | Description  
---|---  
Home | Portal home page that describes the APIs that are showcased. Serves as default home page for your portal (index.html). Demonstrates use of [angular material](https://material.angular.io/) components, as described in [Add angular material components](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/page-editor#angular-material).  
Get Started | Sample content page. Learn how to edit this page and add it to the top navigation by [stepping through the tutorial](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/get-started/overview).  
APIs | List of available APIs. When you [generate interactive API reference documentation](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/publish-apis), links to the content are added to this page automatically.   
  
**Note:** The contents of this page are auto-generated based on the APIs that you publish to your portal. You cannot edit the contents of this page directly; it does not appear in the pages list. You can modify the styling of the page using the [portal theme editor](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/api-portal-themes).  
My Apps | List of registered apps for an authorized user. See [How portal users interact with your portal](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-interact).  
  
**Note:** The contents of this page are auto-generated based on the registered user apps. You cannot edit the contents of the page directly; it does not appear in the pages list. You can modify the styling of the page using the [theme editor](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/api-portal-themes).  
Sign in | Sign in page for registered users. New users can register from this page by clicking **Create an account**. See [How portal users interact with your portal](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-interact).  
  
**Note:** The Sign In page is included in your portal automatically. You can [customize the logo](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/configure-register-sign-in#manage_company_information) on the Sign In page and [add custom registration fields](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/configure-register-sign-in#custom_registration_fields) to the Create Account page. You cannot edit the contents of the page directly; it does not appear in the pages list. "  
Terms and Conditions | Sample terms and conditions page.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
