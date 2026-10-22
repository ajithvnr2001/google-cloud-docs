---
url: https://docs.cloud.google.com/apigee/docs/api-security/best-practices/
title: Advanced API Security best practices \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:31:56.822492+00:00
---

# Advanced API Security best practices  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-security/best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Advanced API Security best practices Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page describes some best practices for working with Advanced API Security.

## Configure client IP resolution

If the [default client IP resolution algorithm](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/client-ip-resolution#default-client-ip-address-resolution) does not work for your use case, it can be customized per environment. See [client IP resolution](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/client-ip-resolution). Configuring this setting allows Advanced API Security to find and use the appropriate client IP address for each API request, and ensures consistent client IP address resolution across your environment.

In order to use client IP resolution, you'll also need to Preserve X-Forwarded-For request headers.

## Preserve X-Forwarded-For request headers

The X-Forwarded-For (XFF) request header is a standard header for identifying the originating IP addresses of clients connecting to a web server through a proxy server. Many platforms provide the ability to strip off XFF headers from incoming requests for security purposes. However, this is not recommended if you are using Advanced API Security, because the machine learning algorithms it uses need the IP address information to identify abuse traffic, and to calculate security scores.

### How to determine if your platform is stripping off XFF headers

To determine if your platform is stripping off XFF headers, make an API call like the following:
    
    
    curl https://apigee.googleapis.com/v1/organizations/ORG/environments/ENV/stats/x_forwarded_for_ip?select=avg\(total_response_time\)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
     -H "Authorization: Bearer $TOKEN"
    

where ORG is your organization and ENV is an environment in the organization.

If your platform is stripping off XFF headers, this returns a response in which the first line will be
    
    
     "name": "(not set)",

The `(not set)` in the response means your platform is stripping off XFF headers.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
