---
url: https://docs.cloud.google.com/recaptcha/docs/implement-waf-ca/
title: Integrate with Google Cloud Armor for websites \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:50:27.969924+00:00
---

# Integrate with Google Cloud Armor for websites  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/implement-waf-ca/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Integrate with Google Cloud Armor for websites Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to integrate Google Cloud Fraud Defense for Cloud Armor on websites.

To complete the integration, you must implement one or more features of Fraud Defense for Cloud Armor and configure Cloud Armor security policies.

## Before you begin

  1. Enable the reCAPTCHA Enterprise API.

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=recaptchaenterprise.googleapis.com&redirect=https%3A//console.cloud.google.com)

  2. Plan how you want to implement the features of Fraud Defense for Cloud Armor to help protect your website.

     1. [Choose one or more WAF features](https://docs.cloud.google.com/recaptcha/docs/features-ca#features-overview) that best match your use case.
     2. Identify the pages that you want to protect and the type of Cloud Armor feature that you want to implement on those pages.



## Implement features of Fraud Defense for Cloud Armor

Depending on your requirements, you can use one or more features of Fraud Defense for Cloud Armor in a single application.

If you want to use more than one feature, then you must create a reCAPTCHA key for each of those features and use them in your application. For example, if you want to use reCAPTCHA action-tokens and reCAPTCHA challenge page, then you must create an action-token key and a challenge-page key, and use them in your application. 

### Implement reCAPTCHA action-tokens

You must have reCAPTCHA running on your web pages to generate action-tokens. After reCAPTCHA generates an action-token, you attach the action-token to a predefined request header wherever you need to protect any user action, such as `checkout`. By default, action-tokens are valid for 30 minutes, but can vary depending on the traffic. You must attach the action-token to a predefined request header before the token expires, so that the Cloud Armor can evaluate the token attributes. 

To implement a reCAPTCHA action-token, do the following:

  1. Create an action-token key for your website. 

### Cloud console

     1. In the Google Cloud console, go to the **Google Cloud Fraud Defense** page.

[Go to Google Cloud Fraud Defense](https://console.cloud.google.com/security/recaptcha)

     2. Verify that the name of your project appears in the resource selector at the top of the page.

If you don't see the name of your project, click the resource selector, then select your project.

     3. Select the **Keys** tab.
     4. Click **Create key**. 
     5. In the **Display name** field, enter a display name for the key.
     6. Depending on the platform for which you want to create reCAPTCHA keys for WAF, perform the appropriate action:
        1. For the **Application type** , select **Web**. 

The **Domain list** section appears.

        2. To protect the reCAPTCHA key for your domain and subdomains, ensure that the **Disable domain verification** toggle is turned off. 

Disabling domain verification is a security risk because there are no restrictions on the site, so your reCAPTCHA key can be accessed and used by anyone.

        3. Enter the domain name for your website:

           1. In the **Domain list** section, click **Add a domain**. 
           2. In the **Domain** field, enter the name of your domain.
           3. Optional: To add an additional domain, click **Add a domain** and enter the name of another domain in the **Domain** field. You can add up to a maximum of 250 domains.

For websites, the reCAPTCHA key is unique to the domains and subdomains that you specify. You can specify more than one domain if you serve your website from multiple domains. If you specify a domain (for example, `examplepetstore.com`), you do not need to specify its subdomains (for example, `subdomain.examplepetstore.com`). Changes to the domain list can take up to 30 minutes to take effect.

        4. In **Additional settings** , turn on the **Will you deploy this key in a Web Application Firewall (WAF)?** toggle. 
        5. From the **Feature** options, select **Action**.

        6. Optional: Turn on the **Will you use challenges?** toggle.

        7. Click **Create key**.

The newly created key is listed on the **reCAPTCHA keys** page.

### gcloud

To create reCAPTCHA keys, use the [gcloud recaptcha keys create](https://docs.cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create) command.

Before using any of the command data below, make the following replacements: 

     * INTEGRATION_TYPE: Type of integration. Specify `score` or `checkbox`. 
     * DISPLAY_NAME: Name for the key. Typically a site name. 
     * DOMAIN_NAME: Domains or subdomains of websites allowed to use the key. 

Specify multiple domains as a comma-separated list. Optional: Specify `--allow-all-domains` to disable domain verification.

Disabling domain verification is a security risk because there are no restrictions on the site, so your reCAPTCHA key can be accessed and used by anyone.

     * WAF_FEATURE: Name of the WAF feature. Specify `action-token`. 
     * WAF_SERVICE: Name of the WAF service provider. Specify `CA` for Cloud Armor. 

Execute the [gcloud recaptcha keys create](https://docs.cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create) command: 

#### Linux, macOS, or Cloud Shell
    
    gcloud recaptcha keys create \
    --web \
    --display-name=DISPLAY_NAME  \
    --integration-type=INTEGRATION_TYPE \
    --domains=DOMAIN_NAME \
    --waf-feature=WAF_FEATURE \
    --waf-service=WAF_SERVICE

#### Windows (PowerShell)
    
    gcloud recaptcha keys create `
    --web `
    --display-name=DISPLAY_NAME  `
    --integration-type=INTEGRATION_TYPE `
    --domains=DOMAIN_NAME `
    --waf-feature=WAF_FEATURE `
    --waf-service=WAF_SERVICE

#### Windows (cmd.exe)
    
    gcloud recaptcha keys create ^
    --web ^
    --display-name=DISPLAY_NAME  ^
    --integration-type=INTEGRATION_TYPE ^
    --domains=DOMAIN_NAME ^
    --waf-feature=WAF_FEATURE ^
    --waf-service=WAF_SERVICE

The response contains the newly created reCAPTCHA key. 

### REST

For API reference information about key types and integration types, see [Key](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.keys#resource:-key) and [Integration type](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.keys#integrationtype). 

Before using any of the request data, make the following replacements: 

     * INTEGRATION_TYPE: Type of integration. Specify `score` or `checkbox`. 
     * DISPLAY_NAME: Name for the key. Typically a site name. 
     * DOMAIN_NAME: Domains or subdomains of websites allowed to use the key. 

Specify multiple domains as a comma-separated list. Optional: Specify `--allow-all-domains` to disable domain verification.

Disabling domain verification is a security risk because there are no restrictions on the site, so your reCAPTCHA key can be accessed and used by anyone.

     * WAF_FEATURE: Name of the WAF feature. Specify `action-token`. 
     * WAF_SERVICE: Name of the WAF service provider. Specify `CA` for Cloud Armor. 
     * DEFAULT_SCORE_THRESHOLD: For policy-based challenge keys, this defines the universal challenge threshold for the key when a custom score threshold is not defined. This is in [preview](https://cloud.google.com/products#product-launch-stages).
     * ACTION_SCORE_THRESHOLDS: For policy-based challenge keys, this specifies the action and the corresponding threshold score between 0.0 and 1.0. For example, `login='{"scoreThreshold": "0.3"}',signup='{"scoreThreshold": "0.1"}'`. This is in [preview](https://cloud.google.com/products#product-launch-stages). **Note:** Only the final scores that are computed after any challenges are returned in assessments. The initial score computed by reCAPTCHA is compared with the threshold. 

HTTP method and URL: 
    
    POST https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/keys

Request JSON body: 
    
    {
      "displayName": "DISPLAY_NAME",
       'wafSettings': "  {
           "wafService": "WAF_SERVICE",
      
    "wafFeature": "WAF_FEATURE"
      }
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
      "name": "projects/project-id/keys/7Ldqgs0UBBBBBIn4k7YxEB-LwEh5S9-Gv6QQIWB8m",
    "displayName": "DISPLAY_NAME,
    
    "webSettings": {
      "allowAllDomains": true,
      "allowedDomains": [
        "localhost"
      ],
    
     "integrationType": "SCORE",
    
    
    },
    "wafSettings": {
      "wafService": "CA",
    
      "wafFeature": "ACTION_TOKEN"
      
    
    }
    }
    
    

  2. Integrate reCAPTCHA JavaScript on your web pages with the action-token key that you created. For instructions, refer to the document that corresponds with the integration type of your action-token key. 

     * For the `SCORE` integration type, see [Integrate score-based keys with the frontend](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages#frontend_integration_score).
     * For the `CHECKBOX` integration type, see [Render the reCAPTCHA widget on the frontend](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages-with-checkbox).
  3. After you receive the token from reCAPTCHA, attach the token to a predefined request header in the following format: 
         
         X-Recaptcha-Token: value-of-your-action-token
         

You can use languages such as XHR, Ajax, or Fetch API to attach the token to a predefined request header.

The following sample script shows how to protect the `execute` action and attach the token to a predefined request header using JavaScript + XHR:
         
         
           <script>
             src="https://www.google.com/recaptcha/enterprise.js?render=ACTION_TOKEN_KEY"></script>
         
             <script>
             function onSuccess(action_token) {
                  const xhr = new XMLHttpRequest();
                  xhr.open('GET','YOUR_URL', false);
                  // Attach the action-token to the predefined request header
                  xhr.setRequestHeader("X-Recaptcha-Token", action_token);
                  xhr.send(null);
                }
                function onError(reason) {
                  alert('Response promise rejected: ' + reason);
                grecaptcha.enterprise.ready(function () {
                  document.getElementById("execute-button").onclick = () => {
                    grecaptcha.enterprise.execute('ACTION_TOKEN_KEY', {
                    }).then(onSuccess, onError);
                  };
                });
               }
             </script>
           
           




### Implement reCAPTCHA session-tokens

The reCAPTCHA JavaScript sets a reCAPTCHA session-token as a cookie on the end user's browser after calling `execute()`. The end user's browser attaches the cookie and refreshes the cookie as long as the reCAPTCHA JavaScript remains active.

To provide a session-token as a cookie, install a session-token key on at least one of your web pages that the end user browses before the page that needs to be protected. For example, if you want to protect the checkout page, install a session-token key on the home page or product page.

To learn about how to install session-token keys on your web pages, see [Integrate score-based keys with the frontend](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages#frontend_integration_score).

You can use this cookie to protect the end user's subsequent requests and page loads on a specific domain. Session-tokens are valid for 30 minutes by default. However, if the end user stays on the page where you implemented the session-token, reCAPTCHA refreshes the session-token periodically to prevent it from expiring.

Install session-tokens on each page that needs to be protected by reCAPTCHA. We recommend that you protect every page with reCAPTCHA and use Cloud Armor rules to enforce access on all the pages, except the first page that end users browse.

The following is a sample reCAPTCHA session-token: 
    
    
       recaptcha-ca-t=value-of-your-session-token;domain=domain;expires=expiration_time

To implement a reCAPTCHA session-token, do the following:

  1. Create a session-token key for your website. 

### Cloud console

     1. In the Google Cloud console, go to the **Google Cloud Fraud Defense** page.

[Go to Google Cloud Fraud Defense](https://console.cloud.google.com/security/recaptcha)

     2. Verify that the name of your project appears in the resource selector at the top of the page.

If you don't see the name of your project, click the resource selector, then select your project.

     3. Select the **Keys** tab.
     4. Click **Create key**. 
     5. In the **Display name** field, enter a display name for the key.
     6. Depending on the platform for which you want to create reCAPTCHA keys for WAF, perform the appropriate action:
        1. For the **Application type** , select **Web**. 

The **Domain list** section appears.

        2. To protect the reCAPTCHA key for your domain and subdomains, ensure that the **Disable domain verification** toggle is turned off. 

Disabling domain verification is a security risk because there are no restrictions on the site, so your reCAPTCHA key can be accessed and used by anyone.

        3. Enter the domain name for your website:

           1. In the **Domain list** section, click **Add a domain**. 
           2. In the **Domain** field, enter the name of your domain.
           3. Optional: To add an additional domain, click **Add a domain** and enter the name of another domain in the **Domain** field. You can add up to a maximum of 250 domains.

For websites, the reCAPTCHA key is unique to the domains and subdomains that you specify. You can specify more than one domain if you serve your website from multiple domains. If you specify a domain (for example, `examplepetstore.com`), you do not need to specify its subdomains (for example, `subdomain.examplepetstore.com`). Changes to the domain list can take up to 30 minutes to take effect.

        4. In **Additional settings** , turn on the **Will you deploy this key in a Web Application Firewall (WAF)?** toggle. 
        5. From the **Feature** options, select **Session**.

        6. Optional:Turn on **Disable domain verification**. 

Disabling domain verification is a security risk because there are no restrictions on the site, so your reCAPTCHA key can be accessed and used by anyone.

        7. Click **Create key**.

The newly created key is listed on the **reCAPTCHA keys** page.

### gcloud

To create reCAPTCHA keys, use the [gcloud recaptcha keys create](https://docs.cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create) command.

Before using any of the command data below, make the following replacements: 

     * INTEGRATION_TYPE: Type of integration. Specify `score`. 
     * DISPLAY_NAME: Name for the key. Typically a site name. 
     * DOMAIN_NAME: Domains or subdomains of websites allowed to use the key. 

Specify multiple domains as a comma-separated list. Optional: Specify `--allow-all-domains` to disable domain verification.

Disabling domain verification is a security risk because there are no restrictions on the site, so your reCAPTCHA key can be accessed and used by anyone.

     * WAF_FEATURE: Name of the WAF feature. Specify `session-token`. 
     * WAF_SERVICE: Name of the WAF service provider. Specify `CA` for Cloud Armor. 

Execute the [gcloud recaptcha keys create](https://docs.cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create) command: 

#### Linux, macOS, or Cloud Shell
    
    gcloud recaptcha keys create \
    --web \
    --display-name=DISPLAY_NAME  \
    --integration-type=INTEGRATION_TYPE \
    --domains=DOMAIN_NAME \
    --waf-feature=WAF_FEATURE \
    --waf-service=WAF_SERVICE

#### Windows (PowerShell)
    
    gcloud recaptcha keys create `
    --web `
    --display-name=DISPLAY_NAME  `
    --integration-type=INTEGRATION_TYPE `
    --domains=DOMAIN_NAME `
    --waf-feature=WAF_FEATURE `
    --waf-service=WAF_SERVICE

#### Windows (cmd.exe)
    
    gcloud recaptcha keys create ^
    --web ^
    --display-name=DISPLAY_NAME  ^
    --integration-type=INTEGRATION_TYPE ^
    --domains=DOMAIN_NAME ^
    --waf-feature=WAF_FEATURE ^
    --waf-service=WAF_SERVICE

The response contains the newly created reCAPTCHA key. 

### REST

For API reference information about key types and integration types, see [Key](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.keys#resource:-key) and [Integration type](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.keys#integrationtype). 

Before using any of the request data, make the following replacements: 

     * INTEGRATION_TYPE: Type of integration. Specify `score`. 
     * DISPLAY_NAME: Name for the key. Typically a site name. 
     * DOMAIN_NAME: Domains or subdomains of websites allowed to use the key. 

Specify multiple domains as a comma-separated list. Optional: Specify `--allow-all-domains` to disable domain verification.

Disabling domain verification is a security risk because there are no restrictions on the site, so your reCAPTCHA key can be accessed and used by anyone.

     * WAF_FEATURE: Name of the WAF feature. Specify `session-token`. 
     * WAF_SERVICE: Name of the WAF service provider. Specify `CA` for Cloud Armor. 
     * DEFAULT_SCORE_THRESHOLD: For policy-based challenge keys, this defines the universal challenge threshold for the key when a custom score threshold is not defined. This is in [preview](https://cloud.google.com/products#product-launch-stages).
     * ACTION_SCORE_THRESHOLDS: For policy-based challenge keys, this specifies the action and the corresponding threshold score between 0.0 and 1.0. For example, `login='{"scoreThreshold": "0.3"}',signup='{"scoreThreshold": "0.1"}'`. This is in [preview](https://cloud.google.com/products#product-launch-stages). **Note:** Only the final scores that are computed after any challenges are returned in assessments. The initial score computed by reCAPTCHA is compared with the threshold. 

HTTP method and URL: 
    
    POST https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/keys

Request JSON body: 
    
    {
      "displayName": "DISPLAY_NAME",
       'wafSettings': "  {
           "wafService": "WAF_SERVICE",
      
    "wafFeature": "WAF_FEATURE"
      }
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
      "name": "projects/project-id/keys/7Ldqgs0UBBBBBIn4k7YxEB-LwEh5S9-Gv6QQIWB8m",
    "displayName": "DISPLAY_NAME,
    
    "webSettings": {
      "allowAllDomains": true,
      "allowedDomains": [
        "localhost"
      ],
    
     "integrationType": "SCORE",
    
    
    },
    "wafSettings": {
      "wafService": "CA",
    
      "wafFeature": "SESSION_TOKEN"
    
    
    }
    }
    
    

  2. Add the session-token key and `waf=session` to the reCAPTCHA JavaScript. 

The following sample script shows how to implement a session-token on a web page:
         
         <!DOCTYPE html>
         <html lang="en">
         <head>
          <meta charset="UTF-8">
          <title>reCAPTCHA WAF Session Token</title>
          <script src="https://www.google.com/recaptcha/enterprise.js?render=SESSION_TOKEN_KEY&waf=session" async defer></script>
          <body></body>
         </head>
         </html>




### Implement a reCAPTCHA challenge page

When you implement a reCAPTCHA challenge page, reCAPTCHA redirects to an interstitial page where it determines if it's necessary to show a CAPTCHA challenge to a user. Therefore, CAPTCHA challenges might not be visible to all users.

To implement a reCAPTCHA challenge page, create a challenge-page key for your website.

### Cloud console

  1. In the Google Cloud console, go to the **Google Cloud Fraud Defense** page.

[Go to Google Cloud Fraud Defense](https://console.cloud.google.com/security/recaptcha)

  2. Verify that the name of your project appears in the resource selector at the top of the page.

If you don't see the name of your project, click the resource selector, then select your project.

  3. Select the **Keys** tab.
  4. Click **Create key**. 
  5. In the **Display name** field, enter a display name for the key.
  6. Depending on the platform for which you want to create reCAPTCHA keys for WAF, perform the appropriate action:
     1. For the **Application type** , select **Web**. 
     2. In **Additional settings** , turn on the **Will you deploy this key in a Web Application Firewall (WAF)?** toggle. 
     3. From the **Feature** options, select **Challenge**.

     4. Turn on **Disable domain verification**. 

When you disable domain verification for challenge-page keys, Cloud Armor verifies the domain.

     5. Click **Create key**.

The newly created key is listed on the **reCAPTCHA keys** page.




### gcloud

To create reCAPTCHA keys, use the [gcloud recaptcha keys create](https://docs.cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create) command.

Before using any of the command data below, make the following replacements: 

  * INTEGRATION_TYPE: Type of integration. Specify `invisible`. 
  * DISPLAY_NAME: Name for the key. Typically a site name. 
  * DOMAIN_NAME: Domains or subdomains of websites allowed to use the key. Specify `--allow-all-domains`. 
  * WAF_FEATURE: Name of the WAF feature. Specify `challenge-page`. 
  * WAF_SERVICE: Name of the WAF service provider. Specify `CA` for Cloud Armor. 



Execute the [gcloud recaptcha keys create](https://docs.cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud recaptcha keys create \
    --web \
    --display-name=DISPLAY_NAME  \
    --integration-type=INTEGRATION_TYPE \
    --domains=DOMAIN_NAME \
    --waf-feature=WAF_FEATURE \
    --waf-service=WAF_SERVICE

#### Windows (PowerShell)
    
    
    gcloud recaptcha keys create `
    --web `
    --display-name=DISPLAY_NAME  `
    --integration-type=INTEGRATION_TYPE `
    --domains=DOMAIN_NAME `
    --waf-feature=WAF_FEATURE `
    --waf-service=WAF_SERVICE

#### Windows (cmd.exe)
    
    
    gcloud recaptcha keys create ^
    --web ^
    --display-name=DISPLAY_NAME  ^
    --integration-type=INTEGRATION_TYPE ^
    --domains=DOMAIN_NAME ^
    --waf-feature=WAF_FEATURE ^
    --waf-service=WAF_SERVICE

The response contains the newly created reCAPTCHA key. 

### REST

For API reference information about key types and integration types, see [Key](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.keys#resource:-key) and [Integration type](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.keys#integrationtype). 

Before using any of the request data, make the following replacements: 

  * INTEGRATION_TYPE: Type of integration. Specify `invisible`. 
  * DISPLAY_NAME: Name for the key. Typically a site name. 
  * DOMAIN_NAME: Domains or subdomains of websites allowed to use the key. Specify `--allow-all-domains`. 
  * WAF_FEATURE: Name of the WAF feature. Specify `challenge-page`. 
  * WAF_SERVICE: Name of the WAF service provider. Specify `CA` for Cloud Armor. 
  * DEFAULT_SCORE_THRESHOLD: For policy-based challenge keys, this defines the universal challenge threshold for the key when a custom score threshold is not defined. This is in [preview](https://cloud.google.com/products#product-launch-stages).
  * ACTION_SCORE_THRESHOLDS: For policy-based challenge keys, this specifies the action and the corresponding threshold score between 0.0 and 1.0. For example, `login='{"scoreThreshold": "0.3"}',signup='{"scoreThreshold": "0.1"}'`. This is in [preview](https://cloud.google.com/products#product-launch-stages). **Note:** Only the final scores that are computed after any challenges are returned in assessments. The initial score computed by reCAPTCHA is compared with the threshold. 



HTTP method and URL: 
    
    
    POST https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/keys

Request JSON body: 
    
    
    
    {
      "displayName": "DISPLAY_NAME",
       'wafSettings': "  {
           "wafService": "WAF_SERVICE",
      
    "wafFeature": "WAF_FEATURE"
      }
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
      "name": "projects/project-id/keys/7Ldqgs0UBBBBBIn4k7YxEB-LwEh5S9-Gv6QQIWB8m",
    "displayName": "DISPLAY_NAME,
    
    "webSettings": {
      "allowAllDomains": true,
      "allowedDomains": [
        "localhost"
      ],
    
      "integrationType": "INVISIBLE",
     
    
    },
    "wafSettings": {
      "wafService": "CA",
    
      "wafFeature": "CHALLENGE_PAGE"
      
    
    }
    }
    
    

**Important:** You shouldn't delete the challenge-page key while it is being used in a security policy. If the challenge-page key is not available when the reCAPTCHA challenge page is rendered, the reCAPTCHA challenge page shows an error, and that users cannot pass the assessment. Therefore, you must disassociate the key from the security policy before deleting it. For details, see [Configure rules for bot management](https://docs.cloud.google.com/armor/docs/configure-bot-management).

## Configure Cloud Armor security policies

After implementing the features of Fraud Defense for Cloud Armor, you must configure Cloud Armor security policies for bot management.

If you implemented a reCAPTCHA challenge page, then you must do the following:

  1. Associate the challenge-page key with your security policy.
  2. Configure a security policy rule to redirect a request for reCAPTCHA assessment.



If you implemented reCAPTCHA action tokens or session tokens, then you must configure a security policy rule that evaluates reCAPTCHA tokens.

Before configuring the Cloud Armor security policies, understand the [reCAPTCHA token attributes for Cloud Armor](https://docs.cloud.google.com/recaptcha/docs/token-attr-ca).

To learn how to configure Cloud Armor security policies and use the reCAPTCHA keys for WAF with your security policies, see [Configure rules for bot management](https://docs.cloud.google.com/armor/docs/configure-bot-management).

## Get reCAPTCHA scores

For reCAPTCHA action-tokens and session-tokens, you can get reCAPTCHA scores from the `X-Recaptcha-Wafdata` header. Based on these scores, you can configure any custom action that needs to be taken for user requests.

The following example shows a sample `X-Recaptcha-Wafdata` header:
    
    
    X-Recaptcha-Wafdata: waf_service="Google Cloud Armor", action_token;score=0.9, session_token;score=0.8\r\n
    

You can also view reCAPTCHA scores in the [Google Cloud Armor logs](https://docs.cloud.google.com/armor/docs/request-logging#requests).

## What's next

  * [Examples of integration with Google Cloud Armor](https://docs.cloud.google.com/recaptcha/docs/examples-ca).
  * Learn how to [implement Fraud Defense for Cloud Armor features](https://codelabs.developers.google.com/codelabs/cloud-armor-recaptcha-bot-management).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
