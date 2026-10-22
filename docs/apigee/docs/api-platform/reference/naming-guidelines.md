---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/naming-guidelines/
title: Naming guidelines \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:08.129943+00:00
---

# Naming guidelines  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/naming-guidelines/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Resources ](https://docs.cloud.google.com/apigee/docs/release-notes)



Send feedback 

#  Naming guidelines Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The following table lists naming guidelines for common Apigee components:

Named Item | Maximum characters | Allowed characters  
---|---|---  
[API key](https://docs.cloud.google.com/apigee/docs/api-platform/security/api-keys) | 255 | Alphanumeric and the following: `_ -`  
[API product](https://docs.cloud.google.com/apigee/docs/api-platform/publish/create-api-products) | 100(1) | Alphanumeric, space, and the following: `_ - . # $ %`  
[App: developer and company](https://docs.cloud.google.com/apigee/docs/api-platform/publish/creating-apps-surface-your-api) |  | Alphanumeric, space, and the following: `_ - . # $ %`. Must begin with an alpha character or digit  
[Developer (username, first name, last name)](https://docs.cloud.google.com/apigee/docs/api-platform/publish/adding-developers-your-api-product) | 64 | Alphanumeric, space, and special characters (any character except line breaks)  
Email ID |  | Valid email address syntax. (Hybrid only) lower case only  
[Environment name](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environmentgroups-working-with) | 32 | Alphanumeric, space, and the following: `_ - .`  
[Instance name](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/instances) | 32 | Lowercase alphanumeric, hyphens, and numbers. Must begin with an alpha character; cannot end with a hyphen. Follows the pattern `/^[a-z0-9\-]+$/`  
[Key value map (KVM) name](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps) |  | Alphanumeric, space, and the following: `_ - . # $ %`  
Key value map (KVM) key name |  | Alphanumeric, space, and the following: `_ - . $`  
[Organization name](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/organization-structure) | 32 | Lowercase letters only; it shouldn't contain spaces, underscores, or periods.  
Password for Apigee administrators | >=8, <= 100 | Alphanumeric, special characters. The password must have at least one lowercase character, one uppercase character, one number, and one special character.  
[Policy name (or step definition)](https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-and-configuring-policies-management-ui) | 237 | Alphanumeric, space, and the following: `_ - .`  
[Proxy name](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-apis-and-api-proxies) | 2048(2) | Alphanumeric, space, and special characters. Long names with many special characters might cause rendering or other issues and should be avoided.  
[Resource file names](https://docs.cloud.google.com/apigee/docs/api-platform/develop/resource-files) | 255 | Alphanumeric, space, and the following: `: / \ ! @ # $ % ^ & { } [ ] ( ) _ + - = , . ~ '`  
[Resource file types](https://docs.cloud.google.com/apigee/docs/api-platform/develop/resource-files) | 255 | Alphanumeric and the following: `_ - .`  
  
**(1)** Total length including organization name and product display name, in this form: `<org_name>@@@<display_name>`. For example, "MyOrg1@@@API Product Name".

**(2)** Including http:// or https://.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
