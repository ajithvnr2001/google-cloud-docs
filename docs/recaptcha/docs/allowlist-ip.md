---
url: https://docs.cloud.google.com/recaptcha/docs/allowlist-ip/
title: Configure an IP address allowlist \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:59.247737+00:00
---

# Configure an IP address allowlist  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/allowlist-ip/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Configure an IP address allowlist Stay organized with collections  Save and categorize content based on your preferences. 

To exclude trusted IP addresses from Fraud Defense enforcement, create an allowlist for a reCAPTCHA key that is associated with your site. Then, add the IP addresses and the subnets to this allowlist.

You can also remove IP addresses or subnets from the allowlist and view the IP addresses and subnets in the allowlist.

## Before you begin

Before you begin, ensure that you do the following:

  * Gather all IP addresses and subnets that you want to add to the allowlist.

  * Identify the IP addresses and subnets that you want to remove from the allowlist.

  * Ensure that you have the following Identity and Access Management role: reCAPTCHA Enterprise Admin (`roles/recaptchaenterprise.admin`).




## Add an IP address or subnet to the allowlist

When you add an IP address or a subnet to the allowlist, Fraud Defense skips the verification and always gives a score of `0.9` to the requests coming from that IP address or subnet. You can add a maximum of 1000 IP addresses and subnets to an allowlist.

### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Before using any of the command data below, make the following replacements: 

     * KEY: The reCAPTCHA key associated with your site.
     * IP_ADDRESS_OR_SUBNET: The IP address or subnet that needs to be added to the allowlist.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud recaptcha keys add-ip-override
    KEY \
    --ip=IP_ADDRESS_OR_SUBNET \
    --override=ALLOW

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud recaptcha keys add-ip-override
    KEY `
    --ip=IP_ADDRESS_OR_SUBNET `
    --override=ALLOW

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud recaptcha keys add-ip-override
    KEY ^
    --ip=IP_ADDRESS_OR_SUBNET ^
    --override=ALLOW




### REST

Before using any of the request data, make the following replacements: 

  * KEY: The reCAPTCHA key associated with your site.
  * IP_ADDRESS_OR_SUBNET: The IP address or subnet that needs to be added to the allowlist.
  * PROJECT_ID: Your Google Cloud project ID



HTTP method and URL: 
    
    
    POST https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/keys/KEY:addIpOverride

Request JSON body: 
    
    
    
    {
      "ip_override_data": {
        "ip": "IP_ADDRESS_OR_SUBNET",
        "override_type": "ALLOW"
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
         "https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/keys/KEY:addIpOverride"

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
        -Uri "https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/keys/KEY:addIpOverride" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

After you add an IP address or a subnet to the allowlist, the changes take effect within a few minutes.

## Validate your allowlist configuration

To confirm that your IP allowlist is working as expected, complete the following steps:

  1. Verify that you added the IP address or subnet to the allowlist for the specific reCAPTCHA key.

  2. Initiate a complete Fraud Defense transaction from a machine or environment that is using the IP address that is on the allowlist.

  3. Inspect the assessment result. If the allowlist is active for the originating IP, the `riskAnalysis.score` in the JSON response is `0.9`.


**Important:** The IP allowlist mechanism checks the actual source IP address of the traffic where the reCAPTCHA token was generated. It doesn't use the `event.userIpAddress` field, which you can optionally send in a request to create an assessment. The `event.userIpAddress` field provides end-user IP information for separate risk analysis, not for allowlist enforcement.

## Remove an IP address or subnet from the allowlist

### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Before using any of the command data below, make the following replacements: 

     * KEY: The reCAPTCHA key associated with your site.
     * IP_ADDRESS_OR_SUBNET: The IP address or subnet that needs to be added to the allowlist.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud recaptcha keys remove-ip-override
    KEY \
    --ip=IP_ADDRESS_OR_SUBNET \
    --override=ALLOW

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud recaptcha keys remove-ip-override
    KEY `
    --ip=IP_ADDRESS_OR_SUBNET `
    --override=ALLOW

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud recaptcha keys remove-ip-override
    KEY ^
    --ip=IP_ADDRESS_OR_SUBNET ^
    --override=ALLOW




### REST

Before using any of the request data, make the following replacements: 

  * KEY: The reCAPTCHA key associated with your site.
  * IP_ADDRESS_OR_SUBNET: The IP address or subnet that needs to be added to the allowlist.
  * PROJECT_ID: Your Google Cloud project ID



HTTP method and URL: 
    
    
    POST https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/keys/KEY:removeIpOverride

Request JSON body: 
    
    
    
    {
      "ip_override_data": {
        "ip": "IP_ADDRESS_OR_SUBNET",
        "override_type": "ALLOW"
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
         "https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/keys/KEY:removeIpOverride"

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
        -Uri "https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/keys/KEY:removeIpOverride" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

After you remove an IP address or a subnet from the allowlist, the changes take effect within a few minutes.

## List all IP addresses from the allowlist

### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Before using any of the command data below, make the following replacements: 

     * KEY: The reCAPTCHA key associated with your site.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud recaptcha keys list-ip-overrides KEY --format=json

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud recaptcha keys list-ip-overrides KEY --format=json

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud recaptcha keys list-ip-overrides KEY --format=json




### REST

Before using any of the request data, make the following replacements: 

  * KEY: The reCAPTCHA key associated with your site.
  * PROJECT_ID: Your Google Cloud project ID



HTTP method and URL: 
    
    
    GET https://recaptchaenterprise.googleapis.com/v1/projects//keys/:listIpOverrides

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://recaptchaenterprise.googleapis.com/v1/projects//keys/:listIpOverrides"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://recaptchaenterprise.googleapis.com/v1/projects//keys/:listIpOverrides" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    
    {
      "ipOverrides": [
        {
          "ip": "1.2.3.4",
          "overrideType": "ALLOW"
        }
      ],
      "nextPageToken": ""
    }
    
    
    

## What's next

  * [Create assessments for websites](https://docs.cloud.google.com/recaptcha/docs/create-assessment-website)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
