---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/
title: gcloud beta app \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:12:50.319041+00:00
---

# gcloud beta app  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta app Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta app - manage your App Engine deployments 
SYNOPSIS
    

`gcloud beta app` `GROUP` | `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` The gcloud app command group lets you deploy and manage your Google App Engine apps. These commands replace their equivalents in the appcfg tool. 

App Engine is a platform for building scalable web applications and mobile backends. App Engine provides you with built-in services and APIs such as NoSQL datastores, memcache, and a user authentication API, common to most applications. 

More information on App Engine can be found here: <https://cloud.google.com/appengine> and detailed documentation can be found here: <https://cloud.google.com/appengine/docs/>

EXAMPLES
     To run your app locally in the development application server to simulate your application running in production App Engine with sandbox restrictions and services provided by App Engine SDK libraries, use the `dev_appserver.py` command and your app's `app.yaml` configuration file to run: 
    
    
    dev_appserver.py ~/my_app/app.yaml

For an in-depth look into using the local development server, follow this guide : <https://cloud.google.com/appengine/docs/standard/python/tools/using-local-server>

To deploy the code and configuration of your app to the App Engine server, run: 
    
    
    [gcloud beta app deploy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/deploy) ~/my_app/app.yaml

To list all versions of all services of your existing deployments, run: 
    
    
    [gcloud beta app versions list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/versions/list)

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[domain-mappings](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/domain-mappings)`
     `(BETA)` View and manage your App Engine domain mappings. 
`[firewall-rules](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/firewall-rules)`
     `(BETA)` View and manage your App Engine firewall rules. 
`[instances](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/instances)`
     `(BETA)` View and manage your App Engine instances. 
`[logs](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/logs)`
     `(BETA)` Manage your App Engine logs. 
`[migrate-config](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/migrate-config)`
     `(BETA)` Convert configuration files from one format to another. 
`[operations](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/operations)`
     `(BETA)` View and manage your App Engine Operations. 
`[regions](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/regions)`
     `(BETA)` View regional availability of App Engine runtime environments. 
`[runtimes](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/runtimes)`
     `(BETA)` List runtimes available to Google App Engine. 
`[services](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/services)`
     `(BETA)` View and manage your App Engine services. 
`[ssl-certificates](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/ssl-certificates)`
     `(BETA)` View and manage your App Engine SSL certificates. 
`[versions](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/versions)`
     `(BETA)` View and manage your App Engine versions. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[browse](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/browse)`
     `(BETA)` Open the current app in a web browser. 
`[create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/create)`
     `(BETA)` Create an App Engine app within the current Google Cloud Project. 
`[deploy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/deploy)`
     `(BETA)` Deploy the local code and/or configuration of your app to App Engine. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/describe)`
     `(BETA)` Display all data about an existing service using the beta API. 
`[gen-config](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/gen-config)`
     `(BETA)` `(DEPRECATED)` Generate missing configuration files for a source directory. 
`[migrate-to-run](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/migrate-to-run)`
     `(BETA)` Migrate a second-generation App Engine app to Cloud Run. 
`[open-console](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/open-console)`
     `(BETA)` Open the App Engine dashboard, or log viewer, in a web browser. 
`[repair](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/repair)`
     `(BETA)` Restores required App Engine features to the current application. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/update)`
     `(BETA)` Updates an App Engine application. 
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud app](https://docs.cloud.google.com/sdk/gcloud/reference/app)
    
    
    [gcloud alpha app](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/app)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
