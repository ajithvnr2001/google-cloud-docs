---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/obfuscate-userdata-for-analytics/
title: Obfuscate user data for analytics \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:57:01.038135+00:00
---

# Obfuscate user data for analytics  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/obfuscate-userdata-for-analytics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Obfuscate user data for analytics Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.12 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.12 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/obfuscate-userdata-for-analytics.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/obfuscate-userdata-for-analytics.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/obfuscate-userdata-for-analytics.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/obfuscate-userdata-for-analytics.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/obfuscate-userdata-for-analytics.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/obfuscate-userdata-for-analytics.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/obfuscate-userdata-for-analytics.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/obfuscate-userdata-for-analytics.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/obfuscate-userdata-for-analytics.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/obfuscate-userdata-for-analytics.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/obfuscate-userdata-for-analytics.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/obfuscate-userdata-for-analytics.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/obfuscate-userdata-for-analytics.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/obfuscate-userdata-for-analytics.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/obfuscate-userdata-for-analytics.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/obfuscate-userdata-for-analytics.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/obfuscate-userdata-for-analytics.html)



This feature allows you to obscure data before sending it as part of the analytics payload. With this feature, Apigee uses SHA512 to hash the original value before sending data from the runtime plane to the control plane. 

For additional information on using data obfuscation, including information on enabling the feature in environments, see [ Obfuscate user data for Apigee API Analytics](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/obfuscate-user-data-for-analytics).

## Set the salt value in Apigee hybrid

You can set the salt value for the hash with the [`axHashSalt`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/config-prop-ref#axhashsalt) property in the `overrides.yaml` file. The `axHashSalt` property specifies a value used as a salt when computing SHA512 hashes to obfuscate sensitive analytics data. Apigee recommends using the same value across different clusters that host the same Apigee organization. Apply the value with the `apigee-org` chart with the following command:
    
    
      helm upgrade ORG_NAME apigee-org/ \
        --namespace apigee \
        --atomic \
        -f overrides.yaml
      

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
