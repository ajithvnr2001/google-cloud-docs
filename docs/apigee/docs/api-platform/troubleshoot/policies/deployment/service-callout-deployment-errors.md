---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/service-callout-deployment-errors/
title: Service Callout policy deployment error troubleshooting \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:22:29.008750+00:00
---

# Service Callout policy deployment error troubleshooting  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/service-callout-deployment-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Service Callout policy deployment error troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/policies/deployment/service-callout-deployment-errors) documentation._

Was this troubleshooting playbook helpful? Please let us know by clicking [ Send Feedback ](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/service-callout-deployment-errors/).

## URLMissing

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision [**_revision_number_**]
    URL is missing in Step [**_policy_name_**]
    

**Example error message**
    
    
    Error Saving Revision 2
    URL is missing in Step ExecuteGeocodingRequest.
    

**Example screenshot**

![Error saving revision 2.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/sc-deploy-error-2.png)

### Cause

If the `<URL>` element in the Service Callout policy is missing or left blank, then the deployment of the API proxy fails.

### Diagnosis

Examine the `<URL>` element in the Service Callout policy named in the error message. If there is no URL declared within the element, then that is the cause of the error. For example, the following Service Callout policy has an empty `<URL>` element:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <ServiceCallout name="ExecuteGeocodingRequest">
        <Request variable="GeocodingRequest"/>
        <Response>GeocodingResponse</Response>
        <HTTPTargetConnection>
            <URL></URL>
        </HTTPTargetConnection>
    </ServiceCallout>
    

Because the `<URL>` element is empty, the deployment of the API proxy fails.

### Resolution

Ensure that the `<URL>` element in the Service Callout policy has a valid URL. For example:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <ServiceCallout name="ExecuteGeocodingRequest">
        <Request variable="GeocodingRequest"/>
        <Response>GeocodingResponse</Response>
        <HTTPTargetConnection>
            <URL>http://maps.googleapis.com/maps/api/geocode/json</URL>
        </HTTPTargetConnection>
    </ServiceCallout>
    

## ConnectionInfoMissing

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision [**_revision_number_**]
    Connection information is missing in Step [**_policy_name_**]
    

**Example error message**
    
    
    Error Saving Revision 1
    Connection information is missing in Step ExecuteGeocodingRequest.
    

**Example screenshot**

![Error saving revision 1.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/sc-deploy-error-3.png)

### Cause

If the Service Callout Policy does not have either the `<HTTPTargetConnection>` or `<LocalTargetConnection>` element, then the deployment of the API proxy fails.

### Diagnosis

Determine whether the Service Callout policy has `<HTTPTargetConnection>` or `<LocalTargetConnection>` element defined. For example:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <ServiceCallout name="ExecuteGeocodingRequest">
        <Request variable="GeocodingRequest"/>
        <Response>GeocodingResponse</Response>
    </ServiceCallout>
    

Notice that there is no `<HTTPTargetConnection>` or `<LocalTargetConnection>` element defined in the policy.

### Resolution

Ensure that the Service Callout policy has either the `<HTTPTargetConnection>` or `<LocalTargetConnection>` element. For example:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <ServiceCallout name="ExecuteGeocodingRequest">
        <Request variable="GeocodingRequest"/>
        <Response>GeocodingResponse</Response>
        <HTTPTargetConnection>
            <URL>http://maps.googleapis.com/maps/api/geocode/json</URL>
        </HTTPTargetConnection>
    </ServiceCallout>
    

## InvalidTimeoutValue

### Error message

Deployment of API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision [**_revision_number_**]
    Invalid Timeout value [**_0 or negative_number_**].
    

**Example error message**
    
    
    Error Saving Revision 1
    Invalid Timeout value -1.
    

**Example screenshot**

![Error saving revision 1.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/sc-deploy-error-1.png)

### Cause

If the `<Timeout>` element in the Service Callout policy has a **zero or negative value** specified, then the deployment of the API proxy fails.

### Diagnosis

Examine the `<Timeout>` element in the Service Callout policy. If the value is zero or a negative number, then that is the cause for the error. For example:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <ServiceCallout name="ExecuteGeocodingRequest">
        <Request variable="GeocodingRequest"/>
        <Response>GeocodingResponse</Response>
        <Timeout>0</Timeout>
        <HTTPTargetConnection>
            <URL>http://maps.googleapis.com/maps/api/geocode/json</URL>
        </HTTPTargetConnection>
    </ServiceCallout>
    

Because the `<Timeout>` element has a value of zero, the proxy fails to deploy.

### Resolution

Ensure that the value specified for the `<Timeout>` element is a non-zero or non-negative number. For example:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <ServiceCallout name="ExecuteGeocodingRequest">
        <Request variable="GeocodingRequest"/>
        <Response>GeocodingResponse</Response>
        <Timeout>10</Timeout>
        <HTTPTargetConnection>
            <URL>http://maps.googleapis.com/maps/api/geocode/json</URL>
        </HTTPTargetConnection>
    </ServiceCallout>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
