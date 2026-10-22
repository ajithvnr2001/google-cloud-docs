---
url: https://docs.cloud.google.com/channel/docs/guides/create-verified-accounts/
title: Create verified Google Workspace and Google Chrome accounts \u00a0|\u00a0 Channel Services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:50.780990+00:00
---

# Create verified Google Workspace and Google Chrome accounts  |  Channel Services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/channel/docs/guides/create-verified-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Channel Services ](https://docs.cloud.google.com/channel/docs)
  * [ Guides ](https://docs.cloud.google.com/channel/docs/overview)



Send feedback 

#  Create verified Google Workspace and Google Chrome accounts Stay organized with collections  Save and categorize content based on your preferences. 

This page helps you use the Cloud Channel API create email- and domain-verified customers for Google Workspace and Chrome accounts. Verification offers [additional account security](https://support.google.com/a/answer/60216) and unlocks extra features for the account. 

For more information on what features you can unlock after verifying an account, see [About email-verified and domain-verified accounts](https://support.google.com/chrome/a/answer/10435184).

To create a new verified customer account, use the following POST request.
    
    
    POST https://cloudchannel.googleapis.com/v1/accounts/customers
    

Google Workspace and Chrome offer two kinds of customers: domain verified and email verified.

Country code restrictions apply. Confirm that the customer's country is approved for resale.

## Create domain customers

Domain verified customers have full admin access to their domain. When you create a verified customer, set [`customerType`](https://docs.cloud.google.com/channel/docs/reference/rest/v1/CloudIdentityInfo#CustomerType) to `domain`.

Your JSON request body should resemble the following:
    
    
    {
      "customerType": "domain",
      "alternateEmail": "dani@example.com",
      "phoneNumber": "(949) 555-1234",
      "languageCode": "en-US",
    }
    

A successful response returns an HTTP `200` status code and the following information:
    
    
      "customerType": "domain",
      "primaryDomain": "example.com"
      "isDomainVerified": true,
      "alternateEmail": "dani@example.com",
      "phoneNumber": "(949) 555-1234",
      "languageCode": "en-US",
      "adminConsoleUri": "altostrat.com"
    

## Create email customers

Email verified customers don't own or manage their domain. Set [`customerType`](https://docs.cloud.google.com/channel/docs/reference/rest/v1/CloudIdentityInfo#CustomerType) to `team` when you create this kind of customer.

Your JSON request body should resemble the following:
    
    
    {
      "customerType": "team",
      "alternateEmail": "dani@example.com",
      "phoneNumber": "(949) 555-1234",
      "languageCode": "en-US",
    }
    

A successful response returns an HTTP `200` status code and the following information:
    
    
      "customerType": "team",
      "alternateEmail": "dani@example.com",
      "phoneNumber": "(949) 555-1234",
      "languageCode": "en-US",
      "adminConsoleUri": "altostrat.com"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
