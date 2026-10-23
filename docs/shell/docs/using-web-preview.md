---
url: https://docs.cloud.google.com/shell/docs/using-web-preview/
title: Preview web apps \u00a0|\u00a0 Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:46:40.340148+00:00
---

# Preview web apps  |  Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/shell/docs/using-web-preview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Shell ](https://docs.cloud.google.com/shell/docs)



Send feedback 

#  Preview web apps Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use the web preview feature in Cloud Shell. This feature lets you run web applications on the Cloud Shell virtual machine instance and preview them from the [Google Cloud console](https://console.cloud.google.com/).

The Web Preview button ![Web Preview Button](https://docs.cloud.google.com/static/shell/docs/images/web_preview.svg) can be found on the top right of the Cloud Shell taskbar.

## Start the web application

You can run any web application that listens to HTTP requests on the Cloud Shell virtual machine. The web application must listen for HTTP requests on ports within the permitted range 2000 to 65000. These ports are only available to the secure Cloud Shell proxy service, which restricts access over HTTPS to your user account only.

### Simple server example

To start a simple Python HTTP server from the Cloud Shell command prompt:
    
    
    cd `mktemp -d` \
        && echo '<html><body>Hello World</body></html>' >./index.html \
        && python -m http.server 8080
    

## Preview the application

Click the **Web Preview** button ![Web Preview Button](https://docs.cloud.google.com/static/shell/docs/images/web_preview.svg) and then select the port number from the displayed menu. Cloud Shell opens the preview URL on its proxy service in a new browser window.

You can also access the preview URL by combining the port with the environment variable `WEB_HOST` in the Cloud Shell terminal using the format `https://$PORT-$WEB_HOST`, or by using the [Cloud Shell API](https://docs.cloud.google.com/shell/docs/reference/rpc/google.cloud.shell.v1#environment).

## Accessing Streamlit applications

Web preview in Cloud Shell works through a series of HTTP proxies. Streamlit applications require [additional arguments](https://github.com/streamlit/streamlit/issues/6305) to function when running behind an HTTP proxy. When running these applications, make sure you specify `--browser.serverAddress=localhost --server.enableCORS=false --server.enableXsrfProtection=false` on the command line.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
