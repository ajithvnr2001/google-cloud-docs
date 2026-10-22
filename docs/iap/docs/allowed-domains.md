---
url: https://docs.cloud.google.com/iap/docs/allowed-domains/
title: Restrict resource access to specific domains \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:27:58.642454+00:00
---

# Restrict resource access to specific domains  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/allowed-domains/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Guides ](https://docs.cloud.google.com/iap/docs/quickstarts)



Send feedback 

#  Restrict resource access to specific domains Stay organized with collections  Save and categorize content based on your preferences. 

To improve overall security, IAP by default denies access to requests that do not have a matching Server Name Indication (SNI). IAP also checks the SNI of the load balancer certificate. This allows IAP to restrict URL redirect to malicious domains. The IAP allowed domains feature provides an additional security layer for your IAP-protected resources. As a resource owner or IAP administrator, you can restrict access to IAP-protected resources to specific domains by configuring the allowed domains feature.

You can also configure IAP allowed domains in the following scenarios:

  * **Your browser or an intermediate proxy is forcing connection pooling:** In this scenario, you receive HTTP response 429 and error code [`51`](https://docs.cloud.google.com/iap/docs/faq#error_codes). To resolve the issue, an IAP admin can update the list of allowed domains to include your host name.
  * **The host name provided does not match the SSL certificate on the server:** In this scenario, you receive error code [`52`](https://docs.cloud.google.com/iap/docs/faq#error_codes). To resolve the issue, an IAP admin can update the list of allowed domains to include your host name.



## Configure allowed domains

You can use gcloud or the API to configure allowed domains settings. To configure allowed domains, use the following fields:

  * **`enable`** : Boolean. Turns the allowed domains feature on or off.
  * **`Domains`** : String. The list of allowed domains. The domains can contain wildcard prefixes, such as `*.example.com.` Domain names cannot contain a wildcard directly on a public suffix or on a top level domain. Example: `*.com`, `*.co.in`.



For more information, see [IapSettings](https://docs.cloud.google.com/iap/docs/reference/rest/v1/IapSettings#accesssettings).

To configure IAP allowed domains, complete the following steps:

###  Console 

  1. Go to the IAP page.   
[Go to Identity-Aware Proxy](https://console.cloud.google.com/security/iap/).
  2. Select a project, and then select the resource on which you want to enable the allowed domains feature.
  3. Open **Settings** for the resource. Under **Allowed domains** , select **Enable Allowed Domains**.
  4. Specify the list of allowed domains, and then click **Save**.



###  gcloud 

Following are some example commands for specifying allowed domains.

For more information, see [`gcloud iap settings set`](https://docs.cloud.google.com/sdk/gcloud/reference/iap/settings/set).

Run the following command:
    
    
    gcloud iap settings set SETTING_FILE --folder=FOLDER --organization=ORGANIZATION --project=PROJECT --resource-type=RESOURCE_TYPE --service=SERVICE --version=VERSION
    

Where `SETTING_FILE` is:
    
    
    accessSettings:
      allowed_domains_settings:
        enable: true
        domains: ["*.example.com", "*.example.net"]
    

Replace the following:

  * FOLDER: The folder ID.
  * ORGANIZATION: The organization ID.
  * PROJECT: The project ID.
  * RESOURCE_TYPE: The IAP resource type. Must be `app-engine`, `iap_web`, `compute`, `organization`, `folder`, `backend-services`, `forwarding-rule`, or `cloud-run`.
  * SERVICE: The service name. This is optional when `resource-type` is `compute` or `app-engine`.
  * VERSION: The version name. This is not applicable for `compute`, and is optional when `resource-type` is `app-engine`.



You must specify at least one of the following flags to define the scope for the settings:

  * `--organization=ORGANIZATION`
  * `--folder=FOLDER`
  * `--project=PROJECT`



###  API 

To configure allowed domains, complete the following steps. For more information about using the API to configure allowed domains, see [IapSettings](https://docs.cloud.google.com/iap/docs/reference/rest/v1/IapSettings#accesssettings).

  1. Run the following command to prepare an `iap_settings.json` file. Update the values as needed.


    
    
     {
         "access_settings":{
             "allowed_domains_settings":{
                 "enable": true
                 "domains": [
                     "*.example.com",
                     "*.exampe.net"
                 ]
             }
         }
     }
    

  1. Get the resource name by running the `gcloud iap settings get` command. Copy the name field from the output. You will need the name in the following step.


    
    
    gcloud iap settings get --organization=ORGANIZATION --folder=FOLDER --project=PROJECT --resource-type=RESOURCE_TYPE --service=SERVICE --version=VERSION
    

  1. Replace `RESOURCE_NAME` in the following command with the name from the previous step. The `IapSettings` will be updated.


    
    
    curl -X PATCH \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -d @iap_settings.json \
    "https://iap.googleapis.com/v1/RESOURCE_NAME:iapSettings?updateMask=iapSettings.accessSettings.allowedDomainsSettings.enable,iapSettings.accessSettings.allowedDomainsSettings.domains"
    

## Troubleshooting

**Allowed domains access issue**  
If you receive [Error code 53](https://docs.cloud.google.com/iap/docs/faq#error_codes), ask an IAP administrator to add your host name to the list of allowed domains.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
