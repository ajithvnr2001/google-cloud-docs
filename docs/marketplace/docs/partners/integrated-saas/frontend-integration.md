---
url: https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/frontend-integration/
title: Integrate your app's frontend \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:59.423675+00:00
---

# Integrate your app's frontend  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/frontend-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Integrate your app's frontend Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to integrate your app's frontend with Cloud Marketplace to give your customers a smooth experience when they go from Cloud Marketplace to your product.

At a high level, you must provide a sign up URL to handle creating users' accounts, which are then managed in your web console. You also must provide a URL for users to log in. Optionally, you can integrate single sign-on (SSO).

## Use Producer Portal to integrate your app's frontend

To access all of the information you need to integrate your app's frontend with Cloud Marketplace from one location, you can use the **Frontend integration** section of Producer Portal.

The direct link to Producer Portal is:
    
    
    https://console.cloud.google.com/producer-portal?project=YOUR_PROJECT_ID
    

**Note:** If you don't see the link, or can't access the URL, verify that you've selected the correct project. If you still can't access the URL, use the [Partner Support Desk](https://g.co/cloud/psd-partner) to request assistance, and include the word "Marketplace" in your description. For more information about Partner Support Desk, visit [Request assistance with Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/get-support).

To access the **Frontend integration** section:

  1. In the list of products, click the name of your product.

  2. On the **Overview** page of your product, go to the **Technical integration** section and click on **Frontend integration**.




## Add your sign up URL

When users purchase your product from Cloud Marketplace, you must create an account with your product for them. To do this, you must create a sign up page to set up and approve users' accounts in your system. You can set up the page as a registration page where users sign up for an account in your system, or as a page that approves accounts automatically.

**Caution:** When you set up your sign up page, ensure that users can access the page without first entering a username and password.

After you've created the sign up page, add it in Producer Portal:

  1. In the list of products, click the name of your product.

  2. On the **Overview** page of your product, go to the **Technical integration** section and click on **Frontend integration**.

  3. Enter the URL for your sign up page into the **Sign up URL** field.




### Verify the user's sign up information

If a user hasn't yet established an account in your system, they must click the **Register with` YOUR_COMPANY_NAME`** button in Cloud Marketplace. When they click the button, Google Cloud sends an `HTTP POST` request to your sign up page, with a [JSON Web Token (JWT)](https://jwt.io/) in the `x-gcp-marketplace-token` parameter. The JWT contains the user's _procurement account ID_ , which identifies them as a Google Cloud user, and an _obfuscated ID_ , which represents their Google account ID. You must use both the procurement account ID and the obfuscated ID to link the user's Google account to their account in your system.

**Note:** It's possible for a single user to have multiple procurement account IDs, or for multiple users to share a common procurement account ID, depending on how they or their organization have configured their usage of Google Cloud.

After verifying the JWT, your sign up page must send an account approval request to the Partner Procurement API, described in the [backend integration steps](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/backend-integration).

For detailed information about the JWT payload and how to verify it, refer to Verify the JWT below.

If you're new to working with JWTs, refer to the [JWT introduction](https://jwt.io/introduction/).

## Add your login URL

You must specify the URL for your app's login page.

To enter the URL for your app's login page in Producer Portal:

  1. In the list of products, click the name of your product.

  2. On the **Overview** page of your product, go to the **Technical integration** section and click **Frontend integration**.

  3. Enter the URL for your app's login page into the **Login URL** field.




### (Optional) Enable single sign-on (SSO) for your customers

To enable SSO in Producer Portal:

  1. In the list of products, click the name of your product.

     1. On the **Overview** page of your product, go to the **Technical integration** section and click on **Frontend integration**.

     2. Under **Enable SSO login?** , select **Yes**.




#### Verify your customers' SSO login information

When customers log into your app by using SSO, Google Cloud sends an `HTTP POST` request to your app's login page, with a [JSON Web Token (JWT)](https://www.rfc-editor.org/rfc/rfc7519) of the same format as the JWT sent when users first sign up for your app.

For detailed information about the JWT payload and how to verify it, refer to Verify the JWT below.

## Verify the JWT

Some processes, such as signing up a new customer or logging in a customer with SSO, involve sending you an `HTTP POST` request with a [JSON Web Token (JWT)](https://jwt.io/) that you might need to verify.

The following table lists:

  * Events which involve sending an HTTP request with a JWT.
  * The type of HTTP request involved.
  * Whether or not you must verify the JWT.

Event | HTTP request type | JWT verification required  
---|---|---  
Sign up a new customer |  POST |  Yes  
Customer login, without SSO |  GET |  No  
Customer login, with SSO |  POST |  Yes  
  
### The JWT payload

The JWT payload is in the following format:

**Header**
    
    
    {
      "alg": "RS256",
      "kid": "KEY_ID"
    }

Where:

  * `alg` is always `RS256`.
  * `kid` indicates the key ID that was used to secure the JWT. Use the key ID to look up the key from the JSON object in the `iss` attribute in the payload.



**Payload**
    
    
    {
      "iss": "https://www.googleapis.com/robot/v1/metadata/x509/cloud-commerce-partner@system.gserviceaccount.com",
      "iat": CURRENT_TIME,
      "exp": CURRENT_TIME + 5 minutes,
      "aud": "PARTNER_DOMAIN_NAME",
      "sub": "PROCUREMENT_ACCOUNT_ID",
      "google": {
        "roles": [GCP_ROLE],
        "user_identity": USER_ID
      }
    }

Where:

  * `sub` is the user's Google account ID. You must use this ID to link the user's Google account to their account in your system.
  * `iss` identifies the sender of the JWT. The URL in the `iss` claim links to a public key from Google.
  * `exp` indicates when the token expires, and is set to 5 minutes after the token is sent.
  * `aud` is the domain that hosts your product, such as `example.com`.
  * `roles` is an array of strings representing the user's roles. It can be either:

    * `account_admin`, which indicates that the user is a [Billing Account Administrator (Order Administrator)](https://docs.cloud.google.com/marketplace/docs/access-control) of the billing account that purchased the product, or

    * `project_editor`, which indicates that the user is an Editor (Entitlement Manager), but not a Billing Administrator, of the project under that billing account.

**Note:** If you've enabled single sign-on (SSO), users with the `account_admin` role must also have the `project_editor` role.
  * `user_identity` is an obfuscated user reference, which can be used as a `login_hint` to initiate an OAuth 2.0 consent flow. For more details, see Initiate Google sign-in with `login_hint`.




**Payload for multiple orders of the same product**

If you've enabled multiple orders of the same product, then the payload includes an additional `orders` object. This includes the unique order ID corresponding to the entitlement ID for each order. Make sure that your app's login page can respond to this new `orders` field.
    
    
    {
      "iss": "https://www.googleapis.com/robot/v1/metadata/x509/cloud-commerce-partner@system.gserviceaccount.com",
      "iat": CURRENT_TIME,
      "exp": CURRENT_TIME + 5 minutes,
      "aud": "PARTNER_DOMAIN_NAME",
      "sub": "PROCUREMENT_ACCOUNT_ID",
      "google": {
        "roles": [GCP_ROLE],
        "user_identity": USER_ID,
        "orders": [ORDER_ID1, ORDER_ID2]
      }
    }

Where:

  * `ORDER_ID` is a list of unique order IDs for each entitlement ID that indicates the different offers on the same product. This field is available only if multiple orders of the same product is enabled.



For more information about turning multiple orders of the same product on, see [Turn on multiple orders of the same product](https://docs.cloud.google.com/marketplace/docs/partners/offers/multiple-offers).

### Verify the payload

When you receive the JWT, you must verify the following:

  1. Verify that the JWT signature is using [the public key from Google](https://www.googleapis.com/robot/v1/metadata/x509/cloud-commerce-partner@system.gserviceaccount.com).

  2. Verify that the JWT hasn't expired, by checking the `exp` claim.

  3. Verify that the `aud` claim is the correct domain for your product.

  4. Verify that the `iss` claim is `https://www.googleapis.com/robot/v1/metadata/x509/cloud-commerce-partner@system.gserviceaccount.com`.

  5. Verify that `sub` is not empty.


**Note:** Because we might add new fields to the JWT, you shouldn't consider a JWT invalid just because it contains new fields that you haven't yet encountered.

## Initiate Google sign-in with `login_hint`

If you want your users to go through an OAuth 2.0 consent flow with your site, you can use the identity information from the payload to initialize that flow on the Google account they were using for Google Cloud before the redirect. To do this, you supply the `user_identity` provided in the JWT as the `login_hint`. For more information, visit the [Google OAuth 2.0 documentation](https://developers.google.com/identity/protocols/oauth2/web-server#handlingresponse).

After the user completes the OAuth 2.0 flow with your site, you should verify that they're the user you expected to complete the OAuth flow. You do this by using the OAuth 2.0 access token to call the Google UserInfo API to fetch their basic user information. This returns an ID that's expected to match the `user_identity` field from the JWT.

## Create service accounts for your customers

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

If your product requires a service account, you can work with a partner engineer to:

  * Provision service accounts for your customers, and
  * Set up a _service account management page_ for your customers to grant the required Identity and Access Management (IAM) roles to the service accounts.



You must provide the link to this service account page to your customers, usually through your product's management console.

### Provision the service accounts

To provision the service accounts, contact your partner engineer and include the following information:

  * **Service name** : This is a unique product ID that differentiates your product from other products. We recommend using the service name that you created when you [onboarded your product](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/set-up-environment#adding_product_details).

  * **Project ID** : The ID of the project in which you create the service accounts that access your customers' resources. You must create all service accounts that your product uses within a single project.

  * **IAM roles and reasoning** : The IAM roles required for the service accounts, and the reason why the roles are necessary. This is shared with your customer and can impact whether your customer grants access to the service account.




If you want your customer to return to your site after they grant access to the service account, send the **domain name** of your console to your partner engineer. You can send multiple domain names, including subdomains, such as `staging.example.com`.

### Integrate the service account management page into your product's console

The partner engineer creates a service account management page to allow your customers to grant access to the service accounts. You then link to the page from your console.

After your partner engineer notifies you that the service account management page is ready, add parameters to the URL, and then link to the page from your console.

You must add two parameters to the URL:

  * `service-name`: This is the service name you provided to your partner engineer.

  * `service-account-email`: This is the email address of the service account you created for your customer. Each customer has a unique service account.




The following example shows a URL with the required parameters:
    
    
    https://console.cloud.google.com/marketplace-saas/service-account/service-name/service-account-email
    

You can add additional parameters depending on your customers' needs. For example:
    
    
    https://console.cloud.google.com/marketplace-saas/service-account/service-name/service-account-email;single=true;redirect=https%3A%2F%2Fexample.com
    

The parameters of the URL indicate that your product requires access to a single Google Cloud project and that the customer can return to your console.

#### List of URL parameters

The following is a list of the URL parameters that you can send to the service account management page:

Parameter| Description| `service-name`| This is required. This is the service name you provided to your partner engineer.  
---|---  
`service-account-email`| This is required. This is the email address of the service account you created for your customer.  
`single`| When true, this indicates that your product requires access to a single project.  
`hints=project-id-1`| Sets the project that you want the service account to access. Use commas to separate projects.  
`filter=role1`| Limits the roles granted to the service account to a subset of the roles you provided to your partner engineer. Exclude the `roles/` when using the filter.  
`redirect`| Provides a link for the customer to return to your management console. The **domain name** must be registered with your partner engineer to use this parameter.  
  
[ Previous arrow_back  Integrate your app  ](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/technical-integration-setup)

[ Next Track your products' associated consumption  arrow_forward  ](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/partner-consumption-tracking)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
