---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/install-carbon-black-event-forwarder/
title: Install Carbon Black Event Forwarder \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:36:32.146044+00:00
---

# Install Carbon Black Event Forwarder  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/install-carbon-black-event-forwarder/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Install Carbon Black Event Forwarder

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Caution:** The Ingestion API is [deprecated](https://docs.cloud.google.com/chronicle/docs/deprecations) and will be discontinued on July 20, 2027. To ingest logs into Google SecOps, use the [Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-methods) instead. For details on how to migrate, see [Migrate from legacy SIEM API to Chronicle API](https://docs.cloud.google.com/chronicle/docs/administration/migrate-from-legacy-api-to-chronicle-api).

## Introduction

In this document, we will step through the process of configuring the Carbon Black (CB) Event Forwarder so that it sends endpoint telemetry to Google Security Operations.

## Quickstart Guide

On a high level, we will be following the quickstart guide of the official CB Event Forwarder (see [here](https://developer.carbonblack.com/reference/enterprise-response/event-forwarder/#quickstart-guide)) with a few items as follows:

  1. Install the CB Event Forwarder either directly on the CB Response server, or on another VM.
  2. Make sure that desired events to be sent to Google SecOps are configured on CB Response server.
  3. Configure a few fields in the configuration of CB Event Forwarder to enable sending events to Google SecOps



### Configure CB Response

Configure CB Response to export desired events. Please refer to [Configure CB Response](https://developer.carbonblack.com/reference/enterprise-response/event-forwarder/#configure-carbon-black) of the official CB Event Forwarder documentation for more background.

For example, if you would like to enable exporting network connection events via a CB event forwarder which also runs on the CB Response server, you will do the following:
    
    
    # If this property is not empty, it will enable publishing of incoming events from
    # sensors onto RabbitMQ PUBSUB enterprise bus (see RabbitMQ (cb-rabbitmq service)
    # settings in this file). The value of this property consists of one or more of the
    # following comma-separated event types that should be published:
    #   * procstart (or process)
    #   * procend
    #   * childproc
    #   * moduleload
    #   * module
    #   * filemod
    #   * regmod
    #   * netconn
    # If you wish to subscribe for ALL of the above events, '*' value can be specified.
    # Each event type will be published to its own topic: ingress.event.<event type>
    DatastoreBroadcastEventTypes=netconn
    

### Configure CB Event Forwarder

Configure CB Event Forwarder to export data using HTTP(S) to Chronicle Ingestion API. Please refer to [Configure the cb-event-forwarder](https://developer.carbonblack.com/reference/enterprise-response/event-forwarder/#configure-the-cb-event-forwarder) of the official CB Event Forwarder documentation for more background.

A number of flags are needed to configure the CB Event Forwarder. We will provide you with a configuration with those flags.

  1. Back up the official CB Event Forwarder configuration:


    
    
    // Go to the configuration folder.
    $ cd /etc/cb/integrations/event-forwarder
    $ cp cb-event-forwarder.conf cb-event-forwarder.conf.official
    

  1. Update the following fields in cb-event-forwarder.conf:


    
    
    // Update output_type from file to http.
    output_type=http
    
    // Configure the Ingestion API endpoint.
    httpout=https://malachiteingestion-pa.googleapis.com/v1/unstructuredlogentries?key=<api-key>
    
    // Only export the following Raw Sensor (endpoint) Events.
    events_raw_sensor=ingress.event.childproc,ingress.event.emetmitigation,ingress.event.netconn,ingress.event.process,ingress.event.processblock,ingress.event.remotethread,ingress.event.tamper,ingress.event.filemod,ingress.event.regmod
    
    // Update the following fields in the [http] section. Note that some fields with exactly the same field name appear in many sections. Make sure that you are updating the fields in the [http] section.
    
    // Do not send an empty update.
    upload_empty_files=false
    
    // Update the bundle size to 1MB.
    bundle_size_max=1048576
    
    // Update HTTP post template.
    
    
    
     
    http_post_template={"log_type": "CB_EDR", "entries":[{{range $index, $element := .Events}}{{if $index}},{{end}}{{printf "{\"log_text\":%q}" .EventText}}{{end}}]} 
    

Remember to replace ****with the Backstory Ingestion API key you were provided.

### Starting And Stopping CB Event Forwarder

Please refer to [Starting and Stopping the Service](https://developer.carbonblack.com/reference/enterprise-response/event-forwarder/#starting-and-stopping-the-service) of the official CB Event Forwarder documentation.

## How-Tos

### How To Debug If CB Event Forwarder Fails To Start Up

Start up errors will be logged to /var/log/cb/integrations/cb-event-forwarder/cb-event-forwarder.startup.log.

### How To Find Out That CB Event Forwarder Is Sending Data To Google SecOps

If CB Event Forwarder is sending data to Google SecOps, you should see the following in log. Log can be found at /var/log/cb/integrations/cb-event-forwarder/cb-event-forwarder.log
    
    
    time="2018-11-15T16:08:41-08:00" level=info msg="Enforcing minimum TLS version 1.2"
    time="2018-11-15T16:08:41-08:00" level=info msg="Raw Event Filtering Configuration:"
    time="2018-11-15T16:08:41-08:00" level=info msg="ingress.event.netconn: true"
    time="2018-11-15T16:08:41-08:00" level=info msg="cb-event-forwarder version NOT FOR RELEASE starting"
    time="2018-11-15T16:08:41-08:00" level=info msg="Interface address XXX.XXX.XXX.XXX"
    time="2018-11-15T16:08:41-08:00" level=info msg="Interface address XXXX::XXX:XXXX:XXXX:XXX"
    time="2018-11-15T16:08:41-08:00" level=info msg="Configured to capture events: [watchlist.# feed.# alert.# ingress.event.netconn binaryinfo.# binarystore.#]"
    time="2018-11-15T16:08:41-08:00" level=info msg="Rolling file /var/cb/data/event-forwarder/event-forwarder to /var/cb/data/event-forwarder/event-forwarder.2018-11-15T16:08:41.481.restart"
    time="2018-11-15T16:08:41-08:00" level=info msg="Initialized output: HTTP POST https://malachiteingestion-pa.googleapis.com/v1/unstructuredlogentries\n"
    ...
    time="2018-11-15T16:08:43-08:00" level=info msg="Successfully uploaded file /var/cb/data/event-forwarder/event-forwarder.2018-11-09T14:25:21.446 to HTTP POST https://malachiteingestion-pa.googleapis.com/v1/unstructuredlogentries."
    
    

## Contact Info

Technical Questions, including help on this instructions in this document: [forwarder@chronicle.security](mailto:forwarder@chronicle.security)

General Questions: [product@chronicle.security](mailto:product@chronicle.security)

Sales Questions: [sales@chronicle.security](mailto:sales@chronicle.security)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
