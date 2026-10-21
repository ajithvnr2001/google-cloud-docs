---
url: https://docs.cloud.google.com/appengine/docs/flexible/reference/dispatch-yaml/
title: dispatch.yaml Configuration File \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:02:51.288777+00:00
---

# dispatch.yaml Configuration File  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/reference/dispatch-yaml/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/flexible/apis)



Send feedback 

#  dispatch.yaml Configuration File Stay organized with collections  Save and categorize content based on your preferences. 

Go Java Node.js PHP Python Ruby .NET Custom

### Region ID

The `REGION_ID` is an abbreviated code that Google assigns based on the region you select when you create your app. The code does not correspond to a country or province, even though some region IDs may appear similar to commonly used country and province codes. For apps created after February 2020, `REGION_ID.r` is included in App Engine URLs. For existing apps created before this date, the region ID is optional in the URL.

Learn more [about region IDs](https://docs.cloud.google.com/appengine/docs/flexible/python/how-requests-are-routed#region-id). 

OK

The `dispatch.yaml` allows you to override [routing rules](https://docs.cloud.google.com/appengine/docs/flexible/how-requests-are-routed#routing_via_url). You can use the `dispatch.yaml` to send incoming requests to a specific service (formerly known as modules) based on the path or hostname in the URL.

For more information, see [How Requests are Routed](https://docs.cloud.google.com/appengine/docs/flexible/how-requests-are-routed).

An app can have only one `dispatch.yaml` file, and the routing rules in that file apply to all of the app's services and versions. 

## Deploying the dispatch file

To deploy and apply the configuration settings from your dispatch file to your App Engine environment:
    
    
    gcloud app deploy dispatch.yaml
    

## Syntax

The root element in the `dispatch.yaml` file is `dispatch:` and contains a list of routing definitions that are specified by the following subelements.

The rules that you define in your dispatch file must use HTTP URL patterns that include the "`.`" notation for separating subdomains. URLs defined with the HTTPS "`-dot-`" notation are not supported.

Dispatch rules are order dependent, and only the first rule that matches a URL will be applied.

Element | Description  
---|---  
` service` |  Specifies the name of the service that will handle the requests that match the `url` pattern. Note that services were previously called modules.   
`url` |  In the `url` element, you define the URL pattern within quotes, which can include the host name and URL path that are no longer than 100 characters.  For the `service` element, you specify the name of the service that you want handling any incoming requests that match the URL pattern of the `url` element.  Tip: You can include glob patterns like the `*` wildcard character in the `url` element; however, those patterns can be used only before the host name and at the end of the URL path.  URL paths that begin with `/_ah/` are not routed by the dispatch file.   
  
## Example

The following is a sample dispatch file that routes requests to `https://simple-sample.uc.r.appspot.com` and requests like `https://simple-sample.uc.r.appspot.com/favicon.ico` to the `default` service. All static content is served from the `default` service. Mobile requests like `https://simple-sample.uc.r.appspot.com/mobile/` are routed to a mobile frontend, and worker requests like `https://simple-sample.uc.r.appspot.com/work/` are routed to a static backend.

Example:
    
    
    dispatch:
      # Default service serves the typical web resources and all static resources.
      - url: "*/favicon.ico"
        service: default
    
      # Default service serves simple hostname request.
      - url: "simple-sample.uc.r.appspot.com/"
        service: default
    
      # Send all mobile traffic to the mobile frontend.
      - url: "*/mobile/*"
        service: mobile-frontend
    
      # Send all work to the one static backend.
      - url: "*/work/*"
        service: static-backend
    

If you prefer general routing rules that match many possible requests, you can define rules with wider scopes.

Example:
    
    
    # Send any path that begins with “simple-sample.uc.r.appspot.com/mobile” to the mobile-frontend service.
    - url: "simple-sample.uc.r.appspot.com/mobile*"
      service: mobile-frontend
    
    # Send any domain/sub-domain with a path that starts with “work” to the static backend service.
    - url: "*/work*"
      service: static-backend
    

You can also write expressions that are more strict.

Example:
    
    
    # Matches the path "/fun", but not "/fun2" or "/fun/other"
    - url: "*/fun"
      service: mobile-frontend
    
    # Matches the hostname 'customer1.myapp.com', but not '1.customer1.myapp.com.
    - url: "customer1.myapp.com/*"
      service: static-backend
    

You can create rules to re-direct your incoming domain requests to a service. The following rules route incoming requests from "customer1.myapp.com" to the default service and incoming requests from subdomains to a static backend service.

Example:
    
    
    # Matches the domain name 'customer1.myapp.com' and directs all the request to default service 
    - url: "customer1.myapp.com/*"
      service: default
    
    # Matches all the subdomains of 'customer1.myapp.com' and directs all the request to static-backend service
    - url: "*.customer1.myapp.com/*"
      service: static-backend
    
    

## Limits

The dispatch file can contain up to 20 routing rules. When specifying the URL string, neither the hostname nor the path can be longer than 100 characters.

## Deleting all dispatch rules

To delete all dispatch rules:

  1. Edit the contents of the `dispatch.yaml` file to:
         
         dispatch: []
         

  2. Deploy the `dispatch.yaml` file to App Engine.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
