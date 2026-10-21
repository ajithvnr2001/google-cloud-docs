---
url: https://docs.cloud.google.com/apigee/docs/api-security/incidents-api/
title: Incidents API \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:24:59.655613+00:00
---

# Incidents API  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-security/incidents-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Incidents API Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**Preview — Advanced API Security Incidents API**

This feature is covered by the [Pre-GA Offerings Terms](https://cloud.google.com/terms/service-terms#1) of the Google Cloud Terms of Service. Pre-GA features may have limited support, and changes to pre-GA features may not be compatible with other pre-GA versions. For more information, see the [ launch stage descriptions](https://cloud.google.com/products#product-launch-stages).

Support for the Preview launch of Advanced API Security Incidents API is available through the [ Apigee - Google Cloud Community](https://www.googlecloudcommunity.com/gc/Apigee/bd-p/cloud-apigee) forum. 

The Incidents API lets you view statistics for security incidents related to [abuse detection](https://cloud.google.com/apigee/docs/api-security/abuse-detection).

## Parameters in example API calls

The following sections give examples of API calls that use the Incidents API. The API calls contain the following variable parameters:

  * ORG is your organization.
  * ENV is the environment in which you want scores to be calculated.
  * `INCIDENT_UUID` is the UUID for the incident.
  * `$TOKEN` is the environment variable for an [OAuth access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). 



## List incidents and get their details

The following examples show how to list incidents and get their details.

### Example: List all incidents for an environment

To list all incidents for an environment, send the following request:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG/environments/ENV/securityIncidents" \
           -H 'Content-type: application/json' \
           -H "Authorization: Bearer $TOKEN"

See the [ `SecurityIncident`](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityIncidents#SecurityIncident) reference page for descriptions of the request and response.

### Example: Get details for a specific incident

To get the details for a specific incident, send a request like the following:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG/environments/ENV/securityIncidents/INCIDENT_UUID" \
           -H 'Content-type: application/json' \
           -H "Authorization: Bearer $TOKEN"

where `INCIDENT_UUID` is the UUID for the incident, which is returned in the `name` field by the call shown in Example: List all incidents for an environment.

See the [ `SecurityIncident`](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityIncidents#SecurityIncident) reference page for descriptions of the request and response.

## Archiving incidents

To help you distinguish between the incidents you have already investigated from those that you haven't, you can archive the incidents that no longer require you attention. Archiving incidents has the following effects: 

  * In the Apigee UI, archived incidents are not displayed in the [ **Environment details > Incidents**](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection#environment-details) list (provided that **Include archived incidents** is not selected).
  * In the API, when you make a call to list all incidents, archived incidents have the following line: 
        
        "observability": "ARCHIVED"

You can use the `"observability"` field to to filter out archived incidents from a list of incidents.

The possible values for `"observability"` are:

    * `ACTIVE`
    * `ARCHIVED`



Archived incidents are not deleted: you can always unarchive them, which changes the incident's `"observability"` to `ACTIVE`.

The following examples show how to archive and unarchive incidents.

### Archive an incident

To archive an incident, send a request like the following:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG/environments/ENV/securityIncidents/INCIDENT_UUID?updateMask=observability" \
           -X POST \
           -H "Authorization: Bearer $TOKEN" \
           -H "Content-Type: application/json" \
           -d '{"name": "organizations/ORG/environments/ENV/securityIncidents/INCIDENT_UUID",
                "observability": "ARCHIVED"}' \
           -X PATCH

This returns a response like the following:
    
    
    {
        "name": "INCIDENT_UUID",
        "displayName": "Multi type attack from US",
        "firstDetectedTime": "2023-04-04T17:00:00Z",
        "lastDetectedTime": "2023-09-12T03:10:00Z",
        "detectionTypes": [
          "Advanced Anomaly Detection",
          "OAuth Abuser"
        ],
        "trafficCount": "4052130",
        "containsMlAbuses": false,
        "riskLevel": "MODERATE",
        "observability": "ARCHIVED"
    }

The last line, `"observability": "ARCHIVED"`, shows that the incident has been archived.

### Unarchive an incident

To unarchive an incident, use the same call as in the previous section, but use the line 
    
    
    "observability": "ACTIVE"

### Filter incidents by archive status

The next example filters the results of a call to list incidents so that only active incidents are returned.
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG/environments/ENV/securityIncidents?filter=observability=\"ACTIVE\"" \
           -X POST \
           -H "Authorization: Bearer $TOKEN" \
           -H "Content-Type: application/json"

This returns a result like the following.
    
    
    {
      "securityIncidents": [
        {
          "name": "1850fbb9-53a9-44e7-8893-f0b0c987d55e",
          "displayName": "Multi type attack from US",
          "firstDetectedTime": "2023-04-04T17:00:00Z",
          "lastDetectedTime": "2023-09-12T03:10:00Z",
          "detectionTypes": [
            "Advanced Anomaly Detection",
            "OAuth Abuser"
          ],
          "trafficCount": "4052130",
          "containsMlAbuses": false,
          "riskLevel": "MODERATE",
          "observability": "ACTIVE"
        }
      ],
      "nextPageToken": "ClAKAjUwEj1saXN0U2VjdXJpdHlJbmNpZGVudC9hcGlzZWN1cml0eS1tbHRlc3QtYXV0b3B1c2gvZGVmYXVsdC1wcm9kGgsI_KW1qQYQ6fqSDg"
    }

### Archive or unarchive multiple security incidents

To archive or unarchive more than one security incident, enter a command like the following:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG/environments/ENV/securityIncidents:batchUpdate" \
           -X POST \
           -d '{"requests": 
            [{"security_incident": {"name": "organizations/apisecurity-mltest-autopush/environments/default-prod/securityIncidents/INCIDENT_UUID1", "observability": "ARCHIVE"}, "update_mask": "observability"}, 
             {"security_incident": {"name": "organizations/apisecurity-mltest-autopush/environments/default-prod/securityIncidents/INCIDENT_UUID2", "observability": "ARCHIVE"}, "update_mask": "observability"}]}'

## Limitations on the Security Incidents API

The Security Incidents API has the following limitations:

  * Incidents are stored for a maximum of 14 months.
  * `ListIncidents` supports filters only for the following: 
    * `first_detected_time`
    * `last_detected_time`
    * `apiproxy`
  * When you first [enable Advanced API for an organization](https://docs.cloud.google.com/apigee/docs/api-security/enable-security#enable-advanced-api-security), or later re-enable it, there will be a delay while events are clustered into incidents. After that, incidents are recalculated periodically.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
