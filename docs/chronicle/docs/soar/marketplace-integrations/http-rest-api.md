---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/http-rest-api/
title: HTTP REST API \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:28.078973+00:00
---

# HTTP REST API  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/http-rest-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# HTTP REST API

Integration version: 10.0

## Configure HTTP REST API integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Get Data

#### Description

Send an HTTP and get a request.

#### Parameters

Parameters | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
URL | String | N/A | Yes | The URL to send the request to.  
Username | String | N/A | No | N/A  
Password | String | N/A | No | N/A  
SSL Verification | Checkbox | Unchecked | No | Whether to verify the SSL certificate of the destination server.  
Headers JSON | String | N/A | No | A JSON object of the HTTP headers to be sent with the request.  
Ignore HTTP Error Codes | Checkbox | Unchecked | No | If enabled, the action should ignore 4xx or 5xx HTTP error codes and not return error.  
  
#### Use cases

N/A

#### Run On

This action runs on the URL entity.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
response_data | N/A | N/A  
  
##### JSON Result
    
    
    {
      "redirects": [
        "http://blank.org/"
      ],
      "response_code": 200,
      "data": "<html>\n\n<head>\n<title>\nblank\n</title>\n</head>\n\n<body bgcolor=#ffffff text=#2222ff link=#ff0000 vlink=#880000 alink=#00ff00>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<center>\n<a style=\"text-decoration:none\" href=\"blank.html\">.</a>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n</center>\n</body>\n</html>\n"
    }
    

### Get URL Data

#### Description

Send HTTP GET requests to URL entities.

#### Parameters

Parameters | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Username | String | N/A | No | Username for basic authentication. Optional.  
Password | String | N/A | No | Password for basic authentication. Optional.  
SSL Verification | Checkbox | N/A | No | Whether to verify the SSL certificate of the destination server.  
  
#### Use cases

N/A

#### Run On

This action runs on the URL entity.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult": {
                "redirects": ["http://blank.org/"],
                "data": "<html>\\n\\n<head>\\n<title>\\nblank\\n</title>\\n</head>\\n\\n<body bgcolor=#ffffff text=#2222ff link=#ff0000 vlink=#880000 alink=#00ff00>\\n<br>\\n<br>\\n<br>\\n<br>\\n<br>\\n<br>\\n<br>\\n<br>\\n<br>\\n<br>\\n<br>\\n<br>\\n<br>\\n<br>\\n<br>\\n<br>\\n<br>\\n<br>\\n<br>\\n<br>\\n<br>\\n<br>\\n<br>\\n<br>\\n<center>\\n<a style=\\\"text-decoration:none\\\" href=\\\"blank.html\\\">.</a>\\n<br>\\n<br>\\n<br>\\n<br>\\n<br>\\n<br>\\n<br>\\n<br>\\n<br>\\n<br>\\n<br>\\n<br>\\n<br>\\n</center>\\n</body>\\n</html>\\n"
            },
            "Entity": "http://blank.org/"
        }
    ]
    

### Ping

#### Description

Test Connectivity.

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
is_succeed | True/False | is_succeed:False  
  
##### JSON Result
    
    
    N/A
    

### Post Data

#### Description

Send HTTP and post requests.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
URL | String | N/A | Yes | The URL to send the request to.  
Data | String | N/A | Yes | The data to send with the request.  
Username | String | N/A | No | N/A  
Password | String | N/A | No | N/A  
SSL Verification | Checkbox | N/A | Unchecked | Whether to verify the SSL certificate of the destination server.  
Headers JSON | String | N/A | No | A JSON object of the HTTP headers to be sent with the request.  
Content Type | String | N/A | No | Content type. If set to application or JSON, the input data must be JSON string.  
  
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
response_data | N/A | N/A  
  
##### JSON Result
    
    
    {
      "redirects": [
        "http://blank.org/"
      ],
      "data": "<html>\n\n<head>\n<title>\nblank\n</title>\n</head>\n\n<body bgcolor=#ffffff text=#2222ff link=#ff0000 vlink=#880000 alink=#00ff00>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<center>\n<a style=\"text-decoration:none\" href=\"blank.html\">.</a>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n<br>\n</center>\n</body>\n</html>\n"
    }
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
