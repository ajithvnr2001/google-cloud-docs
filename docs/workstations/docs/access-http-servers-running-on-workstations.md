---
url: https://docs.cloud.google.com/workstations/docs/access-http-servers-running-on-workstations/
title: Connect to HTTP servers running on a workstation \u00a0|\u00a0 Cloud Workstations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:23.258116+00:00
---

# Connect to HTTP servers running on a workstation  |  Cloud Workstations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/access-http-servers-running-on-workstations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  Connect to HTTP servers running on a workstation Stay organized with collections  Save and categorize content based on your preferences. 

By default you can connect to HTTP ports `80` and ports `1024` to `65535` on your workstations from your browser. You can restrict the ports you can connect to on your workstations by setting `allowedPorts` in the workstation configuration.

Running workstations have a `host` property that you can use to connect using HTTP from a remote browser. You can find the `host` property by getting details for a running workstation through the API, Google Cloud CLI, the Google Cloud console, or by printing the `$WEB_HOST` environment variable, which is automatically set inside your workstation. The URL connects on port `80` by default.

## Default workstation URL format

The `host` property URL uses the following format by default:
    
    
    https://PORT-WORKSTATION_NAME.CLUSTER_ID.cloudworkstations.dev
    

The placeholders represent the following:

  * `PORT`: the port number, which is port `80` by default.
  * `WORKSTATION_NAME`: the workstation name.
  * `CLUSTER_ID`: the randomly generated cluster identifier
  * `cloudworkstations.dev`: the default domain name for a workstation.

URLs for custom domains use a different format. For more about setting up custom domains in Cloud Workstations, see [Set up custom domains for Cloud Workstations](https://docs.cloud.google.com/workstations/docs/set-up-custom-domains-for-cloud-workstations).




## Connect to a different port by changing the URL

In order to connect on a different port, specify a different port number as a prefix. For example, the following URL connects to port `9900`:
    
    
    https://9900-myworkstation.cluster-12345abcde.cloudworkstations.dev
    

In this example, note the following:

  * `9900`: represents the port number.
  * `myworkstation`: represents the workstation ID.
  * `cluster-12345abcde`: represents the cluster identifier.
  * `cloudworkstations.dev`: represents the default domain name for a workstation.



These URLs require user authentication. To open these URLs, you must be logged in and must have the Cloud Workstations User IAM role, `roles/workstations.user`, or the `workstations.workstations.use` permission.

## Connect to an HTTP app from Google Cloud console

You can connect to an HTTP app running on a workstation from the Google Cloud console.

For any running workstation that you have permissions to use, you see a **Launch** button. By default, this button connects on port `80`. You can click the arrow_drop_downexpander arrow next to **Launch** to see alternative connecting options. The **Connect to web app on port** option lets you specify a different port to connect to.

## Connect to an HTTP app from the base editor

To connect to an app running on your workstation from the Cloud Workstations base editor, follow either of these instructions:

  * Click localhost links in the terminal. The base editor automatically redirects localhost links to the right URLs.

    1. To open a terminal window, click menu **Menu** > **Terminal** > **New Terminal**. Alternatively, press `Control+Shift+`` (or `Command+Shift+`` on macOS).

    2. At the command prompt, run the following command to display the localhost link:
           
           echo http://localhost:PORT
           

Replace `PORT` with a port number such as `80` or `8080`.

    3. Hold `Control` (or `Command` on macOS) and then click the localhost link.   
This opens `PORT-WORKSTATION-HOSTNAME` in your browser.

  * Use the browser window: navigate to `https://PORT-WORKSTATION-HOSTNAME`, where `PORT` is the port number and `WORKSTATION-HOSTNAME` is your workstation hostname.




## Restrict port access for a workstation

To restrict the ports that can be connected to on a workstation, set the `allowedPorts` in the workstation configurations.

To restrict a single port, set the [`PortRange`](https://docs.cloud.google.com/workstations/docs/reference/rest/v1/projects.locations.workstationClusters.workstationConfigs#PortRange) `first` and `last` fields to the same port number.

By default ports `22`, `80` and `1024`to`65535` are allowed.

To create a workstation configuration with restricted port access to `80` and `8080` to `8100`, run the following Google Cloud CLI command:
    
    
        gcloud workstations configs create CONFIG \
            --cluster=CLUSTER_ID \
            --region=REGION \
            --project=PROJECT \
            --allowed-ports=first=80,last=80 \
            --allowed-ports=first=8080,last=8100
    

## CORS preflight requests

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

By default, Cloud Workstations makes sure that all HTTP/HTTPS requests to the workstation are [authenticated](https://docs.cloud.google.com/workstations/docs/authentication#http) by using a cookie or authentication header.

Cross-Origin Resource Sharing (CORS) preflight requests don't include cookies or custom headers, and so are considered unauthenticated and blocked by Cloud Workstations. Administrators can optionally allow unauthenticated CORS preflight requests through to the workstation, where it becomes the responsibility of the destination server in the workstation to validate the request.

To allow unauthenticated CORS preflight requests, run the following Google Cloud CLI command:
    
    
        gcloud beta workstations configs update CONFIG \
            --cluster=CLUSTER_ID \
            --region=REGION \
            --project=PROJECT \
            --allow-unauthenticated-cors-preflight-requests
    

## Disable localhost replacement in HTTP responses

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To allow apps under development to run properly on the workstation, Cloud Workstations replaces references to localhost, 127.0.0.1, and 0.0.0.0 with the workstation's hostname in HTTP responses from the workstation.

This might interfere with some applications. To disable this behavior, run the following Google Cloud CLI command:
    
    
        gcloud beta workstations configs update CONFIG \
            --cluster=CLUSTER_ID \
            --region=REGION \
            --project=PROJECT \
            --disable-localhost-replacement
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
