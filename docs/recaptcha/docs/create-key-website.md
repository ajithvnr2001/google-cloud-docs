---
url: https://docs.cloud.google.com/recaptcha/docs/create-key-website/
title: Create reCAPTCHA keys for websites \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:43:53.439995+00:00
---

# Create reCAPTCHA keys for websites  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/create-key-website/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Create reCAPTCHA keys for websites Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to create reCAPTCHA keys to verify user interactions on your web pages.

reCAPTCHA keys represent how reCAPTCHA is configured for a website. The configuration includes important options such as whether to show CAPTCHA challenges.

## Before you begin

  * [Prepare your environment for Google Cloud Fraud Defense](https://docs.cloud.google.com/recaptcha/docs/prepare-environment). 
  * Ensure that you have the following Identity and Access Management role: reCAPTCHA Enterprise Admin (`roles/recaptchaenterprise.admin`).
  * [Choose the key type that is best for your use case](https://docs.cloud.google.com/recaptcha/docs/choose-key-type).



## Create a reCAPTCHA key

There is no limit on the number of reCAPTCHA keys that you can create for a Google Cloud project. It is best to create one reCAPTCHA key per website.

We recommend creating separate reCAPTCHA keys for staging and production environments. Otherwise, you risk polluting reCAPTCHA risk analysis with data from your test environment.

The simplest way to create a reCAPTCHA key is through the reCAPTCHA Admin console. Alternatively, you can use the Google Cloud console, reCAPTCHA Enterprise API, or the Google Cloud CLI.

### Admin console

  1. Go to the Google Cloud Fraud Defense Admin console.

[Go to Fraud Defense admin console](https://www.google.com/recaptcha/admin/create)

  2. In the **Label** field, enter a name that you can use to identify your site.
  3. If you want to create a score-based key, select **Score based (v3)**. If you want to create a checkbox key, select **Challenge (v2)**.
  4. To add a domain, enter your domain name and click  add . 

To add an additional domain, you can repeat this step. You can add up to a maximum of 250 domains.

  5. If you are new to the Google Cloud console, then read the terms of service, and select the checkbox.
  6. Click **Submit**.



If you are new to the Google Cloud console, then a Google Cloud project is created and the necessary APIs are enabled for you to get started. If you already have a Google Cloud project, then the necessary APIs are enabled for your project to get started.

### Cloud console

  1. In the Google Cloud console, go to the **Google Cloud Fraud Defense** page.

[Go to Google Cloud Fraud Defense](https://console.cloud.google.com/security/recaptcha)

  2. Verify that the name of your project appears in the resource selector at the top of the page.

If you don't see the name of your project, click the resource selector, then select your project.

  3. Select the **Keys** tab.
  4. Click **Create key**. 
  5. In the **Display name** field, enter a display name for the key.
  6. For the **Application type** , select **Web**. 

The **Domain list** section appears.

  7. To protect the reCAPTCHA key for your domain and subdomains, ensure that the **Disable domain verification** toggle is turned off. 

Disabling domain verification is a security risk because there are no restrictions on the site, so your reCAPTCHA key can be accessed and used by anyone.

  8. Enter the domain name for your website:

     1. In the **Domain list** section, click **Add a domain**. 
     2. In the **Domain** field, enter the name of your domain.
     3. Optional: To add an additional domain, click **Add a domain** and enter the name of another domain in the **Domain** field. You can add up to a maximum of 250 domains.

For websites, the reCAPTCHA key is unique to the domains and subdomains that you specify. You can specify more than one domain if you serve your website from multiple domains. If you specify a domain (for example, `examplepetstore.com`), you do not need to specify its subdomains (for example, `subdomain.examplepetstore.com`). Changes to the domain list can take up to 30 minutes to take effect.

To use a key on more than 250 domains, click the **Disable domain verification** toggle. Google Cloud Fraud Defense will then ignore the domain list. You need to perform domain verification yourself by examining the `[tokenProperties.hostname](https://docs.cloud.google.com/recaptcha/docs/reference/rpc/google.cloud.recaptchaenterprise.v1#tokenproperties)` field in the assessments you create.

  9. Depending on the type of reCAPTCHA key you want to create for your website, perform the appropriate action:

#### Create score-based reCAPTCHA keys

**Note:** Creating a score-based key is the default option in the Google Cloud console. 
     1. If you want to allow the score-based key to work with Accelerated Mobile Pages (AMP) using the [`amp-recaptcha-input`](https://amp.dev/documentation/components/amp-recaptcha-input/) component, turn on the **Allow this key to work with AMP pages** toggle.
     2. For your non-production environment, if you want to specify a score you want the key to return when any assessments are created for it, do the following: 

        1. Click **Next Step (optional)**
        2. In the Additional settings step, click the **Are you creating this key for testing purposes only?** toggle.
        3. Use the **Set score** slider to specify a score between 0 to 1.0.
     3. Click **Create key**.

The newly created key is listed on the **reCAPTCHA keys** page.

#### Create checkbox reCAPTCHA keys

We do not recommend using checkbox keys because they increase user friction and don't significantly improve accuracy.
     1. Click **Next Step (optional)**.
     2. In the Additional settings step, turn on the **Will you use challenges?** toggle. 
     3. Select the appropriate **Challenge security** option. 

The challenge security option controls the probability of a user being prompted for a secondary challenge in which users are prompted to select images based on an identified category (example, select the pictures with a motorcycle, or stairs).

If you want to ensure the best anti-fraud protection, select **Hard**.

If you select **Easy** , users are less likely to be prompted with the visual challenge.

     4. For your non-production environment, if you want to specify a score you want the key to return when any assessments are created for it, do the following: 

        1. Click the **Are you creating this key for testing purposes only?** toggle.
        2. Use the **Set score** slider to specify a score between 0 to 1.0.
        3. Select the appropriate **Challenge type** option. 
           * **Auto** pops up the challenge sometimes.
           * **No CAPTCHA** does not show a challenge. 
           * **Unsolvable challenge** shows the images but the challenge is not passed.
        4. Click **Create key**. 

The newly created key is listed on the **reCAPTCHA keys** page.

#### Create policy-based challenge reCAPTCHA keys

     1. Click **Next Step (optional)**.
     2. In the Additional settings step, turn on the **Will you use challenges?** toggle. 
     3. Select the appropriate **Challenge security** option. 

The challenge security option defines the complexity and the frequency of the CAPTCHA challenges shown to the user.

If you want to ensure the best anti-fraud protection, select **Hard**.

If you select **Easy** , users are less likely to be prompted with fewer, less complex CAPTCHA challenges.

     4. For your non-production environment, if you want to specify a score for the key to return when any assessments are created for it, do the following: 

        1. Click the **Are you creating this key for testing purposes only?** toggle.
        2. Use the **Set score** slider to specify a score between 0 to 1.0.
     5. Select the score threshold for triggering CAPTCHA challenges, which is applicable to all actions.
     6. Click **Create key**.

The newly created key is listed on the **reCAPTCHA keys** page.




### gcloud

To create reCAPTCHA keys, use the [gcloud recaptcha keys create](https://docs.cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create) command.

Before using any of the command data below, make the following replacements: 

  * INTEGRATION_TYPE: Type of integration. Depending on the type of keys, specify the following values: 
    * `score` for score-based keys.
    * `checkbox` for checkbox keys.
    * `policy-based-challenge` for policy-based challenge keys.
**Note:** We do not recommend using `CHECKBOX` because it increases user friction and doesn't significantly improve accuracy. For more information, see the [FAQs](https://docs.cloud.google.com/recaptcha/docs/faq#id_like_to_use_the_score_from_to_show_a_challenge_checkbox_widget_how_can_i_do_this). 
  * DISPLAY_NAME: Name for the key. Typically a site name. 
  * DOMAIN_NAME: Domains or subdomains of websites allowed to use the key. 

Specify multiple domains as a comma-separated list. 

To use a key on more than 250 domains, specify `--allow-all-domains` to disable domain verification. Google Cloud Fraud Defense will then ignore the domain list. You need to perform domain verification yourself by examining the `[tokenProperties.hostname](https://docs.cloud.google.com/recaptcha/docs/reference/rpc/google.cloud.recaptchaenterprise.v1#tokenproperties)` field in the assessments you create.

Disabling domain verification is a security risk because there are no restrictions on the site, so your reCAPTCHA key can be accessed and used by anyone.

**Note:** The reCAPTCHA key is unique to the domains and subdomains that you specify. You can specify more than one domain if you serve your website from multiple domains. If you specify a domain (for example, `examplepetstore.com`), you do not need to specify its subdomains (for example, `subdomain.examplepetstore.com`). Changes to the domain list can take up to 30 minutes to take effect. 
  * DEFAULT_SCORE_THRESHOLD: For policy-based challenge keys, this defines the universal challenge threshold for the key when a custom score threshold is not defined.
  * ACTION_SCORE_THRESHOLDS: For policy-based challenge keys, this specifies the action and the corresponding threshold score between 0.0 and 1.0. For example, `login='{"scoreThreshold": "0.3"}',signup='{"scoreThreshold": "0.1"}'`. **Note:** Only the final scores that are computed after any challenges are returned in assessments. The initial score computed by Fraud Defense is compared with the threshold. 



Execute the [gcloud recaptcha keys create](https://docs.cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud recaptcha keys create \
            --web \
            --display-name=DISPLAY_NAME  \
            --integration-type=INTEGRATION_TYPE \
            --domains=DOMAIN_NAME \

#### Windows (PowerShell)
    
    
    gcloud recaptcha keys create `
            --web `
            --display-name=DISPLAY_NAME  `
            --integration-type=INTEGRATION_TYPE `
            --domains=DOMAIN_NAME `

#### Windows (cmd.exe)
    
    
    gcloud recaptcha keys create ^
            --web ^
            --display-name=DISPLAY_NAME  ^
            --integration-type=INTEGRATION_TYPE ^
            --domains=DOMAIN_NAME ^

The response contains the newly created reCAPTCHA key. 

### REST

For API reference information about key types and integration types, see [Key](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.keys#resource:-key) and [Integration type](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.keys#integrationtype). 

Before using any of the request data, make the following replacements: 

  * INTEGRATION_TYPE: Type of integration. Depending on the type of keys, specify the following values: 
    * `SCORE` for score-based keys.
    * `CHECKBOX` for checkbox keys.
    * `POLICY_BASED_CHALLENGE` for policy-based challenge keys. 
**Note:** We do not recommend using `CHECKBOX` because it increases user friction and doesn't significantly improve accuracy. For more information, see the [FAQs](https://docs.cloud.google.com/recaptcha/docs/faq#id_like_to_use_the_score_from_to_show_a_challenge_checkbox_widget_how_can_i_do_this). 
  * DISPLAY_NAME: Name for the key. Typically a site name. 
  * DOMAIN_NAME: Domains or subdomains of websites allowed to use the key. 

Specify multiple domains as a comma-separated list. 

To use a key on more than 250 domains, specify `--allow-all-domains` to disable domain verification. Google Cloud Fraud Defense will then ignore the domain list. You need to perform domain verification yourself by examining the `[tokenProperties.hostname](https://docs.cloud.google.com/recaptcha/docs/reference/rpc/google.cloud.recaptchaenterprise.v1#tokenproperties)` field in the assessments you create.

Disabling domain verification is a security risk because there are no restrictions on the site, so your reCAPTCHA key can be accessed and used by anyone.

**Note:** The reCAPTCHA key is unique to the domains and subdomains that you specify. You can specify more than one domain if you serve your website from multiple domains. If you specify a domain (for example, `examplepetstore.com`), you do not need to specify its subdomains (for example, `subdomain.examplepetstore.com`). Changes to the domain list can take up to 30 minutes to take effect. 
  * DEFAULT_SCORE_THRESHOLD: For policy-based challenge keys, this defines the universal challenge threshold for the key when a custom score threshold is not defined.
  * ACTION_SCORE_THRESHOLDS: For policy-based challenge keys, this specifies the action and the corresponding threshold score between 0.0 and 1.0. For example, `login='{"scoreThreshold": "0.3"}',signup='{"scoreThreshold": "0.1"}'`. **Note:** Only the final scores that are computed after any challenges are returned in assessments. The initial score computed by Fraud Defense is compared with the threshold. 
  * DEFAULT_SCORE_THRESHOLD: For policy-based challenge keys, this defines the universal challenge threshold for the key when a custom score threshold is not defined. This is in [preview](https://cloud.google.com/products#product-launch-stages).
  * ACTION_SCORE_THRESHOLDS: For policy-based challenge keys, this specifies the action and the corresponding threshold score between 0.0 and 1.0. For example, `login='{"scoreThreshold": "0.3"}',signup='{"scoreThreshold": "0.1"}'`. This is in [preview](https://cloud.google.com/products#product-launch-stages). **Note:** Only the final scores that are computed after any challenges are returned in assessments. The initial score computed by reCAPTCHA is compared with the threshold. 



HTTP method and URL: 
    
    
    POST https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/keys

Request JSON body: 
    
    
    
    {
      "displayName": "DISPLAY_NAME",
      "webSettings": {
        "allowedDomains": "DOMAINS",
        "integrationType": "INTEGRATION_TYPE"
      }
    }
    
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/keys"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/keys" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-id/keys/6Ldqgs0UAAAAAIn4k7YxEB-LwEh5S9-Gv6IIWB8m",
      "displayName": "DISPLAY_NAME",
      "webSettings": {
        "allowAllDomains": false,
        "allowedDomains": [
          DOMAINS
        ],
        "allowAmpTraffic": false,
        "integrationType": "SCORE",
        "challengeSecurityPreference": "CHALLENGE_SECURITY_PREFERENCE_UNSPECIFIED"
      }
    }
    

**Note:** After creating reCAPTCHA keys, you can edit or delete them. You cannot recover deleted keys. Also, you cannot migrate reCAPTCHA keys from one Google Cloud project to another.

## (Optional) Find a legacy reCAPTCHA secret key

If you want to integrate with a third-party application that does not use the reCAPTCHA Enterprise API, you need the legacy secret key.

For every site key that you create, reCAPTCHA creates a legacy reCAPTCHA secret key (legacy secret key), which you can use with your third-party application.

**Note:** Third-party applications or plugins often refer to this legacy secret key as a **private key** or **secret key**.

If you need the secret key for a reCAPTCHA Classic key, then [migrate the key to reCAPTCHA on Google Cloud](https://docs.cloud.google.com/recaptcha/docs/migrate-recaptcha) and find the legacy secret key.

**Note:** We don't recommend using a legacy secret key on your frontend because it will be visible to your users and attackers can abuse your application.

To find the legacy secret key, do the following:

  1. In the Google Cloud console, go to the **Fraud Defense** page.

[Go to Fraud Defense](https://console.cloud.google.com/security/recaptcha)

  2. Select the **Keys** tab.

  3. In the **reCAPTCHA Keys** section, find the reCAPTCHA key that you created and click the key.

![](https://docs.cloud.google.com/static/recaptcha/images/legacy-key1.png)![](https://docs.cloud.google.com/static/recaptcha/images/legacy-key1.png)

  4. On the **Key Details** page, under the **Integration** tab, click **Use Legacy Key**. A dialog opens with instructions on how to use the legacy secret key.

![](https://docs.cloud.google.com/static/recaptcha/images/legacy-key-location.png)![](https://docs.cloud.google.com/static/recaptcha/images/legacy-key-location.png)




## What's next

  * [Install score-based keys on your web pages](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages).
  * [Install checkbox keys on your web pages](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages-with-checkbox).
  * [Install policy-based challenge keys on your web pages](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages-policy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
