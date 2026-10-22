---
url: https://docs.cloud.google.com/chrome-enterprise-premium/docs/troubleshoot-security-gateway/
title: Troubleshoot secure gateway issues \u00a0|\u00a0 Chrome Enterprise Premium \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:22.953316+00:00
---

# Troubleshoot secure gateway issues  |  Chrome Enterprise Premium  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chrome-enterprise-premium/docs/troubleshoot-security-gateway/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Chrome Enterprise Premium ](https://docs.cloud.google.com/chrome-enterprise-premium/docs)
  * [ Guides ](https://docs.cloud.google.com/chrome-enterprise-premium/docs/overview)



Send feedback 

#  Troubleshoot secure gateway issues Stay organized with collections  Save and categorize content based on your preferences. 

This document provides information about how to use Google Cloud access logs to resolve common issues with secure gateways.

Google Cloud access logs are a valuable tool for diagnosing problems. You can view the access logs in the [Logs Explorer](https://console.cloud.google.com/logs/query). To view logs for troubleshooting secure gateway problems, [configure Data Access audit logs for the `BeyondCorp Enterprise API`](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#config-console).

## End user access

Google Cloud access logs provide valuable insights into user access patterns and can help you troubleshoot access denial errors. These logs record both successful and denied access attempts, offering a comprehensive view of user interactions with your applications. In cases of denied access, the logs include detailed information about the reasons for denial, such as the specific access levels that were not met.

The logs also contain metadata, such as timestamps, user identities, and resource details, providing further context for analysis and troubleshooting. To filter the logs relevant to secure gateway access, use the following filter:
    
    
    resource.type="audited_resource"
    resource.labels.method="AuthorizeUser"
    resource.labels.service="beyondcorp.googleapis.com"
    

## Secure gateway resource issues

If you encounter issues while managing secure gateway resources, such as during creation, updating, or deletion, you can view the logs relevant to secure gateway resource management by using the following filter:
    
    
    resource.type="audited_resource"
    resource.labels.service="beyondcorp.googleapis.com"
    

## Secure gateway connection issues

If you encounter issues while connecting to secure gateway resources, you can enable [secure gateway logging](https://docs.cloud.google.com/chrome-enterprise-premium/docs/manage-security-gateway#enable-gateway-logging) and view the connection logs relevant to secure gateway resource management by using the following filter:
    
    
    resource.type="beyondcorp.googleapis.com/SecurityGateway"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
