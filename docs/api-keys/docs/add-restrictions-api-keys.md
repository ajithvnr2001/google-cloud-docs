---
url: https://docs.cloud.google.com/api-keys/docs/add-restrictions-api-keys/
title: Adding restrictions to API keys \u00a0|\u00a0 API Keys API Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:05.082245+00:00
---

# Adding restrictions to API keys  |  API Keys API Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-keys/docs/add-restrictions-api-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Service Usage ](https://docs.cloud.google.com/service-usage/docs)
  * [ API Keys API Documentation ](https://docs.cloud.google.com/api-keys/docs)
  * [ Guides ](https://docs.cloud.google.com/api-keys/docs/how-to)



Send feedback 

#  Adding restrictions to API keys Stay organized with collections  Save and categorize content based on your preferences. 

API keys identify your application or website to Google Cloud. API key restrictions ensure that only your apps and websites can use your keys. For security reasons, we recommend that you add restrictions that specify:

  * Which clients or websites can use your API keys.
  * The Google Cloud APIs that your application can call using your API keys.



If a client uses a restricted API key to issue a request that doesn't satisfy the API key restrictions, then the request fails. For example, if an API key requires HTTP requests to be issued from a specific domain but an HTTP request is received from a different domain, the request will be rejected with an error.

You can add restrictions when you create an API key with the `CreateKey` method, or you can add the restrictions after the key is created using the `UpdateKey` method. This page describes the restrictions that you can add to an API key, and it shows you how to add those restrictions.

## Adding client restrictions

Client restrictions specify which websites, IP addresses, or apps can use an API key. You add client restrictions based on the type of client that calls your API. You can specify one of the following types of client restrictions:

  * `browserKeyRestrictions`: The HTTP referrers (websites) that are allowed to use the key.
  * `serverKeyRestrictions`: The IP addresses of callers that are allowed to use the key.
  * `androidKeyRestrictions`: The Android apps that are allowed to use the key.
  * `iosKeyRestrictions`: The iOS apps that are allowed to use the key.

**Note:** You can set only one type of client restrictions per API key. For example, if you have both Android apps and iOS apps using your API, you must create separate API keys with the restrictions for each type of client app.

### Adding browser restrictions

The following example shows how to call the `UpdateKey` method to restrict the HTTP referrer to `www.example.com`:
    
    
    curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d '{
              "restrictions" : {
                "browserKeyRestrictions": {
                  "allowedReferrers": "www.example.com"
                }
              },
              "etag": "ETAG"
            }' \
         'https://apikeys.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/keys/KEY_ID?updateMask=restrictions'

When the response from `operations.get` contains `"done": true`, the `response` contains the updated `Key` with the restrictions.

The following example shows how to create a new API key that only allows HTTP requests from a list of specific URLs.
    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d '{
              "displayName" : "API key with browser restrictions",
              "restrictions" : {
                "browserKeyRestrictions": {
                  "allowedReferrers": ["www.example.com", "www.example-2.com"]
                }
              }
            }' \
         'https://apikeys.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/keys'

The following table shows some example scenarios and browser restrictions:

**Scenario** | **Restrictions**  
---|---  
Allow any URL in your site | You must set two URLs in the `allowedReferers` list.  


  1. URL for the domain, without a subdomain, and with a wildcard for the path. For example:  
`example.com/*`
  2. A second URL that includes a wildcard for the subdomain and a wildcard for the path. For example:  
`*.example.com/*`

  
Allow a specific URL | Add a URL with an exact path. For example:  
`www.example.com/path`  
`www.example.com/path/path`  
Allow any URL in a single subdomain or naked domain | You must set two URLs in the `allowedReferers` list to allow an entire domain.  


  1. URL for the domain, without a trailing slash. For example:  
`www.example.com`  
`sub.example.com`  
`example.com`  

  2. A second URL for the domain that includes a wildcard for the path. For example:  
`www.example.com/*`  
`sub.example.com/*`  
`example.com/*`

  
  
### Adding server restrictions

You can specify one or more IP addresses of the callers, for example web servers or cron jobs, that are allowed to use your API key. You can specify the IP addresses in any of the following formats:

  * IPv4 (`198.51.100.1`)
  * IPv6 (`2001:db8::1`)
  * A subnet using CIDR notation (`198.51.100.0/24`, `2001:db8::/64`)



The following example shows how to create an API key with a list of `allowedIps`:
    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d '{
              "displayName" : "API key with server restrictions with IPv4, IPv6 and CIDR",
              "restrictions" : {
                "serverKeyRestrictions": {
                  "allowedIps": ["198.51.100.1","198.51.100.0/24","2001:db8::1","2001:db8::/64"]
                }
              }
            }' \
         'https://apikeys.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/keys'

### Adding Android restrictions

You can restrict usage of an API key to only your Android apps. When you create or update an API key, provide the package name and the 20 byte [SHA-1 fingerprint](https://developer.android.com/studio/publish/app-signing#certificates-keystores) for each app.

For example, assume that you ran the [`keytool` utility](https://developers.google.com/android/guides/client-auth) and it created the following fingerprint:
    
    
      Certificate fingerprint: SHA1: DA:39:A3:EE:5E:6B:4B:0D:32:55:BF:EF:95:60:18:90:AF:D8:07:09
    

The following example shows how to create an API key with the fingerprint and and package name to the `androidKeyRestrictions`:
    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d '{
              "displayName" : "API key with Android restrictions",
              "restrictions" : {
                "androidKeyRestrictions": {
                  "allowedApplications": [
                    {
                      "sha1Fingerprint": "DA:39:A3:EE:5E:6B:4B:0D:32:55:BF:EF:95:60:18:90:AF:D8:07:09",
                      "packageName": "com.example.my.app"
                    }
                  ]
                }
              }
            }' \
         'https://apikeys.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/keys'

### Adding iOS restrictions

You can restrict usage of an API key to only your iOS apps by providing the bundle ID of each app when you create or update a key. The following example shows how to set the `iosKeyRestrictions` when creating an API key:
    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d '{
              "displayName" : "API key with iOS restrictions",
              "restrictions" : {
                "iosKeyRestrictions": {
                  "allowedBundleIds": ["com.example.my.app1", "com.example.my.app2"]
                }
              }
            }' \
         'https://apikeys.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/keys'

## Adding API restrictions

API restrictions allow you to specify which Google Cloud APIs can be called using the API key. We recommend that you add both client and API restrictions to all your API keys.

You can specify one or more services in the API restrictions. The following example shows how to restrict the usage of a new API key to only the services `translate.googleapis.com` and `datastore.googleapis.com`:
    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d '{
              "displayName" : "API key with API restrictions",
              "restrictions": {
                "api_targets": [
                  {
                    "service": "translate.googleapis.com"
                  },
                  {
                    "service" : "datastore.googleapis.com"
                  }
                ]
              },
            }' \
            'https://apikeys.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/keys'

To get a list of services that are enabled in your Google Cloud project, use the [`gcloud services list`](https://docs.cloud.google.com/sdk/gcloud/reference/services/list) command.

In addition to restricting the API key for use to specific services, you can optionally specify the methods in each service to further restrict the API key. The following example shows how to restrict the previous key to only allowed methods of `translate.googleapis.com`:
    
    
    curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d '{
              "restrictions": {
                "api_targets": [
                  {
                    "service": "translate.googleapis.com",
                    "methods": [
                      "Get*",
                      "DetectLanguage"
                    ]
                  },
                  {
                    "service" : "datastore.googleapis.com"
                  }
                ]
              },
              "etag": "ETAG"
            }' \
         'https://apikeys.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/keys/KEY_ID?updateMask=restrictions'

## What's next

  * [Viewing Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit)
  * [Troubleshooting](https://docs.cloud.google.com/api-keys/docs/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
