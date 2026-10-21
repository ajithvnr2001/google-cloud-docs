---
url: https://docs.cloud.google.com/recaptcha/docs/policy-engine/
title: Set up Policy Engine with a Universal key \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:11.074557+00:00
---

# Set up Policy Engine with a Universal key  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/policy-engine/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Set up Policy Engine with a Universal key Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how you can configure Policy Engine on your website using a Universal key. Universal key is a new Google Cloud Fraud Defense key which supports creation of rules within the Policy Engine.

With Policy Engine, Fraud Defense can deterministically trigger CAPTCHA challenges based on [custom policy rules](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/Policy) that you configure. These rules might decide when to show a Fraud Defense challenge based on risk scores, IP addresses, user agents, ASNs, or verified bot (AI agent) identities.

The Fraud Defense Policy Engine configuration provides two main features:

  * **AutoExecute integration (`protected_endpoint_group`)**: Simplifies the frontend JavaScript integration by automatically inspecting outgoing asynchronous network requests and attaching reCAPTCHA tokens to them, so that only a script tag is needed on your frontend.
  * **Challenge policies (`challenge_rule_groups`)**: Determines whether to show a challenge across different user actions and configures the associated challenge difficulty levels (`USABILITY`, `BALANCE`, `SECURITY`) using custom CEL-based rules.



## Before you begin

  1. [Prepare your environment for Google Cloud Fraud Defense](https://docs.cloud.google.com/recaptcha/docs/prepare-environment). 

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

A linked and enabled billing account is required to use Policy Engine. You can enable billing by using either a credit card or an existing Google Cloud project billing ID. If you need help with billing, contact [Cloud Billing support](https://cloud.google.com/support/billing).




## Create a Universal key

Depending on your preferred interface, choose the appropriate option to create a Universal key:

### Console

  1. In the Google Cloud console, go to the **Google Cloud Fraud Defense** page.

[Go to Google Cloud Fraud Defense](https://console.cloud.google.com/security/recaptcha)

  2. Verify that the name of your project appears in the resource selector at the top of the page.

If you don't see the name of your project, click the resource selector, then select your project.

  3. Select the **Keys** tab.
  4. Click **Create key**. 
  5. In the **Display name** field, enter a display name for the key.
  6. For the **Application type** , select **Universal**.
  7. Click **Create key**.



The newly created key is listed on the **reCAPTCHA keys** page.

### gcloud

To create a Universal key using the Google Cloud CLI, use the [`gcloud recaptcha keys create`](https://docs.cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create) command with the `--universal` flag:
    
    
    gcloud recaptcha keys create --universal --display-name=DISPLAY_NAME
    

The response contains the newly created Universal key.

### REST API

To create a Universal key using the REST API, use the [`projects.keys.create`](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.keys/create) method and specify `universalSettings`:
    
    
    POST https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/keys
    
    {
      "displayName": "DISPLAY_NAME",
      "universalSettings": {}
    }
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID
  * `DISPLAY_NAME`: a display name for your key, typically your website name



The response contains the newly created Universal key.

## Configure domains for Policy Engine

**Note:** For websites, the reCAPTCHA key is unique to the domains and subdomains that you specify. You can specify more than one domain if you serve your website from multiple domains. If you specify a domain (for example, `examplepetstore.com`), you don't need to specify its subdomains (for example, `subdomain.examplepetstore.com`).

Depending on your preferred interface, choose the appropriate option to configure allowed domains for your Universal key:

### Console

  1. In the Google Cloud console, go to the **Fraud Defense** page.

[Go to Fraud Defense](https://console.cloud.google.com/security/recaptcha)

  2. Check that the name of your project appears in the resource selector at the top of the page.

If you don't see the name of your project, click the resource selector, and then select your project.

  3. Click the **Keys** tab.

  4. Identify the Universal key that you want to configure, and click the key.

  5. On the **Key details** page, click **Edit key**.

  6. Identify the **Key usage settings** section.

To protect the reCAPTCHA key for your domain and subdomains, ensure that the **Disable domain verification** toggle is turned off. 

Disabling domain verification is a security risk because there are no restrictions on the site, so your reCAPTCHA key can be accessed and used by anyone.

Enter the domain name for your website:

     1. In the **Domain list** section, click **Add a domain**.
     2. In the **Domain** field, enter the name of your domain.
     3. Optional: To add an additional domain, click **Add a domain** and enter the name of another domain in the **Domain** field. You can add up to 250 domains.
  7. Click **Save changes**.


**Note:** To use a policy on more than 250 domains, click the **Disable domain verification** toggle. When domain verification is disabled, Fraud Defense ignores the domain list, and you must perform domain verification yourself by examining the [`tokenProperties.hostname`](https://docs.cloud.google.com/recaptcha/docs/reference/rpc/google.cloud.recaptchaenterprise.v1#tokenproperties) field in the assessments you create.

### gcloud

To update the allowed domains for your Universal key using the Google Cloud CLI, use the [`gcloud alpha recaptcha policies update`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/recaptcha/policies/update) command and specify the domains in a policy configuration file (for example, `POLICY.yaml`):
    
    
    gcloud alpha recaptcha policies update --key=KEY_ID --policy=POLICY.yaml
    

**Note:** The `gcloud alpha recaptcha policies update` command updates the entire policy. Any existing `protected_endpoint_group` or `challenge_rule_groups` must be included in the `POLICY.yaml` file to avoid deleting them.

The `POLICY.yaml` file must specify the allowed domains under `clientSettings`:
    
    
    clientSettings:
      allowedDomains:
        - DOMAIN_NAME_1
        - DOMAIN_NAME_2
    

Alternatively, to allow all domains and disable domain verification, set `allowAllDomains` to `true` in your `POLICY.yaml` file:
    
    
    clientSettings:
      allowAllDomains: true
    

Replace the following:

  * `KEY_ID`: the ID or full resource name of your Universal key
  * `DOMAIN_NAME_1`, `DOMAIN_NAME_2`: the domain names of websites allowed to use the key

**Note:** When `allowAllDomains` is set to `true`, Fraud Defense ignores the domain list, and you must perform domain verification yourself by examining the [`tokenProperties.hostname`](https://docs.cloud.google.com/recaptcha/docs/reference/rpc/google.cloud.recaptchaenterprise.v1#tokenproperties) field in the assessments you create.

### REST API

To update the allowed domains for your Universal key using the REST API, use the [`projects.keys.updatePolicy`](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.keys/updatePolicy) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID
  * KEY_ID: the ID of your Universal key
  * DOMAIN_NAME_1, DOMAIN_NAME_2: the domain names of websites allowed to use the key



HTTP method and URL: 
    
    
    PATCH https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/keys/KEY_ID/policy?updateMask=clientSettings.allowedDomains,clientSettings.allowAllDomains

Request JSON body: 
    
    
    {
    "clientSettings": {
      "allowedDomains": [
        "DOMAIN_NAME_1",
        "DOMAIN_NAME_2"
      ],
      "allowAllDomains": false
    }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/keys/KEY_ID/policy?updateMask=clientSettings.allowedDomains,clientSettings.allowAllDomains"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/keys/KEY_ID/policy?updateMask=clientSettings.allowedDomains,clientSettings.allowAllDomains" | Select-Object -Expand Content

If successful, the request returns the updated policy configuration. **Note:** To use a policy on more than 250 domains, set `allowAllDomains` to `true` in the request body. When `allowAllDomains` is set to `true`, Fraud Defense ignores the domain list, and you must perform domain verification yourself by examining the [`tokenProperties.hostname`](https://docs.cloud.google.com/recaptcha/docs/reference/rpc/google.cloud.recaptchaenterprise.v1#tokenproperties) field in the assessments you create.

## What's next

  * [Install Universal keys on web pages](https://docs.cloud.google.com/recaptcha/docs/install-universal-keys-web-pages).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
