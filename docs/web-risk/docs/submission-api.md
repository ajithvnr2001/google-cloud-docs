---
url: https://docs.cloud.google.com/web-risk/docs/submission-api/
title: Using the Submission API \u00a0|\u00a0 Web Risk \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:30:17.055739+00:00
---

# Using the Submission API  |  Web Risk  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/web-risk/docs/submission-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Web Risk ](https://docs.cloud.google.com/web-risk/docs)
  * [ Guides ](https://docs.cloud.google.com/web-risk/docs/detect-malicious-urls)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Using the Submission API

**Caution:** The Web Risk Submission API is in a formal feature freeze and closed to new orders ahead of full deprecation no later than December 31, 2027. For more information, see Key changes to the Web Risk Submission API.

This document describes how to submit URLs that you suspect are unsafe to Safe Browsing for analysis, and asynchronously check the results of these submissions. Any URLs that are confirmed to violate the [Safe Browsing Policies](https://safebrowsing.google.com/#policies) are added to the Safe Browsing service.

## Key changes to the Web Risk Submission API

  * **New orders and expansions closed** : We no longer accept new contracts or expansions for the Web Risk Submission API.
  * **Feature freeze in effect** : The API is in a formal feature freeze. We're no longer introducing new features or enhancements.
  * **Final renewals** : The final date to renew existing contracts is December 31, 2026. All renewals have a maximum term limit of one year.
  * **Service availability** : Existing services remain operational with critical bug fixes, security updates, and standard support until the end of your active contract. Full deprecation will occur no later than December 31, 2027.



## Best practices

### Read the [Safe Browsing Policies](https://safebrowsing.google.com/#policies)

The Web Risk Submission API validates that the submitted URLs render content violating Safe Browsing [policies](https://safebrowsing.google.com/#policies). API developers must ensure that the submitted URLs have clear evidence of violating these policies. The following examples show evidence of violation of policies:

  * Social engineering content that mimics a legitimate online brand (brand name, logo, look and feel), system alerts, uses deceptive URLs, or requests users to enter sensitive credentials such as a username or password.
  * A site that is hosting a known malware executable.



Don't submit the following types of URLs because they're unlikely to be added to the Safe Browsing blocklist:

  * Fake surveys, shopping sites, or other scams that don't demonstrate phishing (such as cryptocurrency scams).
  * Spam containing gambling, violence, or adult content that is not phishing or malware.



### Improve detection

We recommend using [`ThreatInfo`](https://docs.cloud.google.com/web-risk/docs/reference/rest/v1/projects.uris/submit#threatinfo) and [`ThreatDiscovery`](https://docs.cloud.google.com/web-risk/docs/reference/rest/v1/projects.uris/submit#threatdiscovery) fields to provide additional information about submissions. Doing so might help improve detection. For more information, see [Best practices for using the Submission API](https://docs.cloud.google.com/web-risk/docs/best-practices-submission).

## Taxonomy and brand targeting

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can provide more accurate and detailed abuse reports by using the following optional components in the `ThreatInfo` object: `abuseSubtype` and `targetedBrand`. These fields help Web Risk more accurately analyze the targeted entities and improve detection models.

### `abuseSubtype`

The `abuseSubtype` field provides a granular classification of the threat. Make sure that this field is set _only_ when the primary `abuseType` is `SOCIAL_ENGINEERING`; otherwise, an error is returned.

The supported `abuseSubtype` values include the following:

  * `BANK_PHISHING`: Phishing posing as a bank or trusted financial entity.
  * `CRYPTO_EXCHANGE_PHISHING`: Phishing posing as a cryptocurrency trading platform.
  * `SOCIAL_MEDIA_PLATFORM_PHISHING`: Phishing posing as a social media platform.
  * `RETAIL_PHISHING`: Phishing posing as an established retail platform.
  * `EMAIL_PROVIDER_PHISHING`: Phishing posing as an email service.
  * `ENTERTAINMENT_PHISHING`: Phishing posing as an entertainment service.
  * `GOVERNMENT_AGENCY_PHISHING`: Phishing posing as a government agency to obtain personally identifiable information (PII), such as a Social Security number or taxpayer identification number.
  * `PACKAGE_TRACKING_SCAM`: Mimicking a shipping service to obtain PII or payment details.
  * `FAKE_SUPPORT_SCAM`: Deceptive websites claiming false device problems to trick users into sharing PII or contacting scammers.
  * `GOVERNMENT_FINE_SCAM`: Deceptive content claiming an outstanding civic fine must be paid.
  * `FAKE_PRIZE_SCAM`: Deceptive pages offering unrealistic rewards or prizes.
  * `OTHER_PHISHING` / `OTHER_SCAM`: Social engineering attacks that don't belong to the other categories named here.



### `targetedBrand`

The `targetedBrand` object identifies the entity targeted by phishing and social engineering campaigns.

  * `brandName`: The recognizable name of the brand or company being impersonated (for example, `Altostrat`).
  * `domain`: The legitimate domain of the brand being impersonated (for example, `altostrat.com`).



### Important notes for preview participants

  * **Consistency in taxonomy** : Phishing remains categorized under the `SOCIAL_ENGINEERING` threat type (rather than a separate `PHISHING` parent type) to ensure consistency across the Web Risk and Safe Browsing API suite.
  * **Excluded categories** : Subcategories for `MALWARE` and `UNWANTED_SOFTWARE` are excluded from this release.
  * **Handling unlisted threats** : If your submission doesn't map to a specific subtype, use `OTHER_PHISHING` or `OTHER_SCAM`. We recommend using the `comments` field in `ThreatJustification` to describe the attack.
  * **Optional but encouraged** : Providing these fields helps Web Risk prioritize and enhance the associated threat intelligence models.
  * **Preview phase** : Enum values and behavior for this feature are subject to change.



## Submit URLs

To submit a URL, send an HTTP `POST` request to the [`projects.uris.submit`](https://docs.cloud.google.com/web-risk/docs/reference/rest/v1/projects.uris/submit) method.

  * The Submission API supports one URL per request. To check multiple URLs, you need to send a separate request for each URL.
  * The URL must be valid but it doesn't need to be canonicalized. For more information, see [RFC 2396](http://www.ietf.org/rfc/rfc2396.txt).

  * The HTTP `POST` response returns a [`long-running operation`](https://docs.cloud.google.com/web-risk/docs/reference/rpc/google.longrunning). For more information about how to retrieve the submission result and check the status of a submission, see [Long-running operations](https://docs.cloud.google.com/web-risk/docs/long-running-operations).




## Example

HTTP method and URL: 
    
    
    POST https://webrisk.googleapis.com/v1/projects/project-id/uris:submit

Request JSON body: 
    
    
    {
      "submission": {
        "uri": "https://www.example.com/login.html"
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
         "https://webrisk.googleapis.com/v1/projects/project-id/uris:submit"

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
        -Uri "https://webrisk.googleapis.com/v1/projects/project-id/uris:submit" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-number/operations/operation-id",
    }
    

### Check the submission status

Use the `project-number` and `operation-id` from the response to [check the submission status](https://docs.cloud.google.com/web-risk/docs/long-running-operations#get). The status is located in the `metadata.state` field of the returned operation.

The possible states include `RUNNING`, `SUCCEEDED`, and `CLOSED`. For more information about these states, see [Understanding Operation Status](https://docs.cloud.google.com/web-risk/docs/long-running-operations#operation-status) in the Long-running Operations guide.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
