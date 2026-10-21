---
url: https://docs.cloud.google.com/apigee/docs/api-security/security-feedback-api/
title: Security feedback API \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:47:20.878248+00:00
---

# Security feedback API  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-security/security-feedback-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Security feedback API Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The security feedback API lets you specify and manage lists of attributes to exclude from abuse detection and incident reporting. For additional information, see [Exclude traffic from abuse detection](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection#exclude-traffic-from-abuse-detection).

This page provides an example of setting up an exclusion list. See the [ `SecurityFeedback`](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityFeedback) API reference page for information on all of the options and responses available with this API.

## Example: Exclude traffic from abuse detection using an exclusion list

The following example adds a CIDR range, `192.168.1.0/24`, and an IP address, `10.0.0.1`, to a new exclusion list so that the traffic from those addresses will not be included in detections and incident reports.

For the example ORG is your Apigee organization.
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG/securityFeedback" \
           -H "Authorization: Bearer $TOKEN" \
           -X POST \
           -H "Content-Type: application/json" \
           -d '{
           "displayName": "My Feedback List",
           "feedbackContexts": [
             {
               "attribute": "ATTRIBUTE_IP_ADDRESS_RANGES",
               "values": ["192.168.1.0/24", "10.0.0.1"]
             },
             {
               "attribute": "ATTRIBUTE_ENVIRONMENTS",
               "values": ["prod"]
             }
           ],
           "feedbackType": "EXCLUDED_DETECTION",
           "reason": "PENETRATION_TEST",
           "comment": "Testing feedback API"
        }'

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
