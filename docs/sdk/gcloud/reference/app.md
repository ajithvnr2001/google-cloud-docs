---
url: https://docs.cloud.google.com/sdk/gcloud/reference/app/
title: gcloud app \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:34:28.787772+00:00
---

# gcloud app  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/app/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud app Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud app - manage your App Engine deployments 
SYNOPSIS
    

`gcloud app` `GROUP` | `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     The gcloud app command group lets you deploy and manage your Google App Engine apps. These commands replace their equivalents in the appcfg tool. 

App Engine is a platform for building scalable web applications and mobile backends. App Engine provides you with built-in services and APIs such as NoSQL datastores, memcache, and a user authentication API, common to most applications. 

More information on App Engine can be found here: <https://cloud.google.com/appengine> and detailed documentation can be found here: <https://cloud.google.com/appengine/docs/>

EXAMPLES
     To run your app locally in the development application server to simulate your application running in production App Engine with sandbox restrictions and services provided by App Engine SDK libraries, use the `dev_appserver.py` command and your app's `app.yaml` configuration file to run: 
    
    
    dev_appserver.py ~/my_app/app.yaml

For an in-depth look into using the local development server, follow this guide : <https://cloud.google.com/appengine/docs/standard/python/tools/using-local-server>

To deploy the code and configuration of your app to the App Engine server, run: 
    
    
    [gcloud app deploy](https://docs.cloud.google.com/sdk/gcloud/reference/app/deploy) ~/my_app/app.yaml

To list all versions of all services of your existing deployments, run: 
    
    
    [gcloud app versions list](https://docs.cloud.google.com/sdk/gcloud/reference/app/versions/list)

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[domain-mappings](https://docs.cloud.google.com/sdk/gcloud/reference/app/domain-mappings)`
     View and manage your App Engine domain mappings. 
`[firewall-rules](https://docs.cloud.google.com/sdk/gcloud/reference/app/firewall-rules)`
     View and manage your App Engine firewall rules. 
`[instances](https://docs.cloud.google.com/sdk/gcloud/reference/app/instances)`
     View and manage your App Engine instances. 
`[logs](https://docs.cloud.google.com/sdk/gcloud/reference/app/logs)`
     Manage your App Engine logs. 
`[operations](https://docs.cloud.google.com/sdk/gcloud/reference/app/operations)`
     View and manage your App Engine Operations. 
`[regions](https://docs.cloud.google.com/sdk/gcloud/reference/app/regions)`
     View regional availability of App Engine runtime environments. 
`[runtimes](https://docs.cloud.google.com/sdk/gcloud/reference/app/runtimes)`
     List runtimes available to Google App Engine. 
`[services](https://docs.cloud.google.com/sdk/gcloud/reference/app/services)`
     View and manage your App Engine services. 
`[ssl-certificates](https://docs.cloud.google.com/sdk/gcloud/reference/app/ssl-certificates)`
     View and manage your App Engine SSL certificates. 
`[versions](https://docs.cloud.google.com/sdk/gcloud/reference/app/versions)`
     View and manage your App Engine versions. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[browse](https://docs.cloud.google.com/sdk/gcloud/reference/app/browse)`
     Open the current app in a web browser. 
`[create](https://docs.cloud.google.com/sdk/gcloud/reference/app/create)`
     Create an App Engine app within the current Google Cloud Project. 
`[deploy](https://docs.cloud.google.com/sdk/gcloud/reference/app/deploy)`
     Deploy the local code and/or configuration of your app to App Engine. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/app/describe)`
     Display all data about an existing service. 
`[open-console](https://docs.cloud.google.com/sdk/gcloud/reference/app/open-console)`
     Open the App Engine dashboard, or log viewer, in a web browser. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/app/update)`
     Updates an App Engine application. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha app](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/app)
    
    
    [gcloud beta app](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
