---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/haveibeenpwned/
title: Have I Been Pwned \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:36.311331+00:00
---

# Have I Been Pwned  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/haveibeenpwned/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Have I Been Pwned

This document provides guidance on how to integrate Have I Been Pwned with Google SecOps.

## Configure Have I Been Pwned to work with Google Security Operations

### Credentials

An API Key needs to be purchased in order to make necessary configurations for the HaveIBeenPwned integration.

**Note:** For more detailed information, see [Have I Been Pwned API Documentation](https://haveibeenpwned.com/API/v3).

### Network

Function | Default Port | Direction | Protocol  
---|---|---|---  
API | Multivalues | Outbound | apikey  
  
## Configure HaveIBeenPwned integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Check Account

#### Description

Check if you have an account that has been compromised in a data breach.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the User entity.

#### Action Results

##### Entity Enrichment

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
Breaches | Returns if it exists in JSON result  
Pastes | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
pwned_emails | N/A | N/A  
  
##### JSON Result
    
    
    [
        {
            "EntityResult":
            {
                "breaches": [
                    {
                        "PwnCount": 37217682,
                        "IsRetired": false,
                        "Description": "In March 2012, the music website <a href=\\\"https://techcrunch.com/2016/09/01/43-million-passwords-hacked-in-last-fm-breach/\\\" target=\\\"_blank\\\" rel=\\\"noopener\\\">Last.fm was hacked</a> and 43 million user accounts were exposed. Whilst <a href=\\\"http://www.last.fm/passwordsecurity\\\" target=\\\"_blank\\\" rel=\\\"noopener\\\">Last.fm knew of an incident back in 2012</a>, the scale of the hack was not known until the data was released publicly in September 2016. The breach included 37 million unique email addresses, usernames and passwords stored as unsalted MD5 hashes.",
                        "DataClasses": ["Email addresses",
                                        "Passwords",
                                        "Usernames"
                                       ],
                        "IsSensitive": false,
                        "Domain": "last.fm",
                        "IsSpamList": false,
                        "BreachDate": "2012-03-22",
                        "IsFabricated": false,
                        "ModifiedDate": "2016-09-20T20:00:49Z",
                        "Title": "Last.fm",
                        "Name": "Lastfm",
                        "AddedDate": "2016-09-20T20:00:49Z",
                        "IsVerified": true,
                        "LogoPath": "https://haveibeenpwned.com/Content/Images/PwnedLogos/Lastfm.png"
                    }],
                "pastes": [
                    {
                        "Date": null,
                        "Source": "AdHocUrl",
                        "EmailCount": 36959,
                        "Id": "http://siph0n.in/exploits.php?id=1",
                        "Title": "BuzzMachines.com 40k+"
                    }]
            },
            "Entity": "john_doe@example.com"
        }
    ]
    

### Ping

#### Description

Check connectivity.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_connect | True/False | is_connect:False  
  
##### JSON Result
    
    
    N/A
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
