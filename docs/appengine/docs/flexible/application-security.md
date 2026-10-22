---
url: https://docs.cloud.google.com/appengine/docs/flexible/application-security/
title: Overview of app security \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:45:11.524771+00:00
---

# Overview of app security  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/application-security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Overview of app security Stay organized with collections  Save and categorize content based on your preferences. 

### Region ID

The `REGION_ID` is an abbreviated code that Google assigns based on the region you select when you create your app. The code does not correspond to a country or province, even though some region IDs may appear similar to commonly used country and province codes. For apps created after February 2020, `REGION_ID.r` is included in App Engine URLs. For existing apps created before this date, the region ID is optional in the URL.

Learn more [about region IDs](https://docs.cloud.google.com/appengine/docs/flexible/python/how-requests-are-routed#region-id). 

OK

Security is a core feature of the Google Cloud, but there are still steps you should take to protect your App Engine app and identify vulnerabilities.

Use the following features to ensure that your App Engine app is secure. To learn more about the Google Security Model and the available steps that you can take to secure your Google Cloud projects, see [Google Cloud Platform Security](https://docs.cloud.google.com/security).

## HTTPS requests

Use HTTPS requests to access to your App Engine app securely. Depending on how your app is configured, you have the following options:

`appspot.com` domains
    

  * Use the `https` URL prefix to send HTTPS request to the `default` service of your Google Cloud project, for example:  
`https://PROJECT_ID.REGION_ID.r.appspot.com`


  * To target specific resources in your App Engine app, use the `-dot-` syntax to separate each resource you want to target, for example:  
`https://VERSION-dot-SERVICE-dot-PROJECT_ID.REGION_ID.r.appspot.com`

  * To convert an HTTP URL to an HTTPS URL, replace the periods between each resource with `-dot-`, for example:  
`http://SERVICE_ID.PROJECT_ID.REGION_ID.r.appspot.com`  
`https://SERVICE_ID-dot-PROJECT_ID.REGION_ID.r.appspot.com`




For more information about HTTPS URLs and targeting resources, see [How Requests are Routed](https://docs.cloud.google.com/appengine/docs/flexible/how-requests-are-routed).

Custom domains
    

To send HTTPS requests with your custom domain, you can use the managed SSL certificates that are provisioned by App Engine. For more information, see [Securing Custom Domains with SSL](https://docs.cloud.google.com/appengine/docs/flexible/securing-custom-domains-with-ssl).

## Access control

In each Google Cloud project, set up access control to determine who can access the services within the project, including App Engine. You can assign different roles to different accounts to ensure each account has only the permissions it needs to support your app. For details see, [Setting Up Access Control](https://docs.cloud.google.com/appengine/docs/flexible/access-control).

## App Engine firewall

The [App Engine firewall](https://docs.cloud.google.com/appengine/docs/flexible/creating-firewalls) enables you to control access to your App Engine app through a set of rules that can either allow or deny requests from the specified ranges of IP addresses. You are not billed for traffic or bandwidth that is blocked by the firewall. Create a firewall to:

Allow only traffic from within a specific network
    Ensure that only a certain range of IP addresses from specific networks can access your app. For example, create rules to allow only the range of IP addresses from within your company's private network during your app's testing phase. You can then create and modify your firewall rules to control the scope of access throughout your release process, allowing only certain organizations, either within your company or externally, to access your app as it makes its way to public availability.
Allow only traffic from a specific service
    Ensure that all the traffic to your App Engine app is first proxied through a specific service. For example, if you use a third-party Web Application Firewall (WAF) to proxy requests directed at your app, you can create firewall rules to deny all requests except those that are forwarded from your WAF.
Block abusive IP addresses
    While Google Cloud has many mechanisms in place to prevent attacks, you can use the App Engine firewall to block traffic to your app from IP addresses that present malicious intent or shield your app from denial of service attacks and similar forms of abuse. You can add IP addresses or subnetworks to a denylist, so that requests routed from those addresses and subnetworks are denied before they reach your App Engine app.

For details about creating rules and configuring your firewall, see [Controlling App Access with Firewalls](https://docs.cloud.google.com/appengine/docs/flexible/creating-firewalls).

## Ingress controls

You can use Ingress controls to restrict inbound traffic to your App Engine app. By default, your App Engine app accepts traffic from all network origins. To modify the default settings, and edit and view the available settings, see [Specify ingress settings](https://docs.cloud.google.com/appengine/docs/flexible/ingress-settings).

## Security scanner

The Google Cloud [Web Security Scanner](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview) discovers vulnerabilities by crawling your App Engine app, following all that links within the scope of your starting URLs, and attempting to exercise as many user inputs and event handlers as possible.

In order to use the security scanner, you must be an owner of the Google Cloud project. For more information on assigning roles, see [Setting Up Access Control](https://docs.cloud.google.com/appengine/docs/flexible/access-control).

You can run security scans from the Google Cloud console to identify security vulnerabilities in your App Engine app. For details about running the Security Scanner, see the [Using Web Security Scanner](https://docs.cloud.google.com/security-command-center/docs/how-to-use-web-security-scanner).

## VPC Service Controls

[Not supported](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#appengine) in the App Engine flexible environment.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
