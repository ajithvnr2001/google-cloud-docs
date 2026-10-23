---
url: https://docs.cloud.google.com/stackdriver/docs/instrumentation/opentelemetry-collector-troubleshooting/
title: Troubleshoot the Google-Built OpenTelemetry Collector \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:09:37.126579+00:00
---

# Troubleshoot the Google-Built OpenTelemetry Collector  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/instrumentation/opentelemetry-collector-troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Troubleshoot the Google-Built OpenTelemetry Collector Stay organized with collections  Save and categorize content based on your preferences. 

This document describes troubleshooting steps and common issues with using an OpenTelemetry Collector such as the Google-Built OpenTelemetry Collector to send data to Google Cloud Observability.

## Troubleshoot data collection

This section describes strategies you can use to troubleshoot issues with data collection.

### Use the `debug` exporter

The [`debug` exporter](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.163.1/exporter/debugexporter) is the best way to view the data at the OpenTelemetry Collector level. The exporter takes whatever data it receives and writes it to stdout in a human-readable format. This is most useful when you need to verify that any transformations in your pipeline are producing the intended result.

The `debug` exporter is included in the Google-Built OpenTelemetry Collector. You can configure the `debug` exporter with `verbosity: detailed` to see the entire telemetry payload.
    
    
    exporters:
      debug:
        verbosity: detailed
    

You can include the exporter in your pipeline:
    
    
    service:
      pipelines:
        metrics:
          receivers: [
            # ...
          ]
          processors: [
            # ...
          ]
          exporters: [
            debug, # can be added alongside any other configured exporters
            # ...
          ]
    

### Test OpenTelemetry Transformation Language (OTTL) online with the OTTL Playground

The [OTTL Playground](https://ottl.run/) is a community-developed tool that lets you interactively develop an OpenTelemetry Transformation Language pipeline. You start by providing OTLP JSON as input, write your pipeline using the same configuration as you would for your OpenTelemetry Collector, and visually inspect the results.

The best way to get OTLP JSON from a pipeline is to put a [`file` exporter](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.163.1/exporter/fileexporter) at the spot before where your transformation processor would be. Start by configuring a `file` exporter:
    
    
    exporters:
      file:
        path: example.json
    

If you had a pipeline like this:
    
    
    service:
      pipelines:
        metrics:
          receivers: [hostmetrics]
          processors: [
            memorylimiter,
            groupbyattrs,
            transform, # where your OTTL pipeline will go
            cumulativetodelta,
            metricstarttime,
          ]
          exporters: [
            otlp,
          ]
    

You could temporarily modify your pipeline to export the data as it will look going into the `transform` processor you are working on.
    
    
    service:
      pipelines:
        metrics:
          receivers: [hostmetrics]
          processors: [
            memorylimiter,
            groupbyattrs,
            # transform,
            # cumulativetodelta,
            # metricstarttime,
          ]
          exporters: [
            # otlp,
            file,
          ]
    

The `file` exporter will write each payload it receives to a line in the file. You can use a single line of data as input to the OTTL Playground.

## Known issues

This section describes known issues with the OpenTelemetry Collector/Google-Built OpenTelemetry Collector and how to work around them where possible.

### Excessive `connect: network is unreachable` errors when using the `otlp` exporter

NOTE: This issue only applies to the gRPC `otlp` exporter, not the HTTP equivalent exporter called `otlphttp`.

NOTE: This issue has only been directly observed in Compute Engine environments so far, but due to the nature of the issue we can't confirm that it is truly limited to Compute Engine.

Starting in Google-Built OpenTelemetry Collector version 0.147.0 and upstream OpenTelemetry Collector version 0.145.0, the `otlp` exporter will start to default to the [client-side load balancing](https://grpc.io/docs/guides/custom-load-balancing/#implementing-your-own-policy) strategy `round_robin`, where previously it was `pick_first`. When the exporter previously used the `pick_first` strategy, it also had fully functioning IPV4 fallback in a scenario where IPV6 wouldn't work. The `round_robin` strategy does not have this property, and will repeatedly attempt to send to all addresses that it resolves at exporter start time, even when they don't work.

As a result, if you are using the `otlp` exporter to send data to the Telemetry API, you may see error messages like this:
    
    
    2026-02-13T20:50:00.665Z        warn    grpc@v1.78.0/clientconn.go:1526 [core] [Channel #1 SubChannel #18] grpc: addrConn.createTransport failed to connect to {Addr: "[2607:f8b0:4001:c62::5f]:443", ServerName: "telemetry.googleapis.com:443", }. Err: connection error: desc = "transport: Error while dialing: dial tcp [2607:f8b0:4001:c62::5f]:443: connect: network is unreachable"   {"resource": {"service.instance.id": "feb467f0-ecc6-4a0c-b1e2-90c908131fdd", "service.name": "otelcol-google", "service.version": "v0.147.0"}, "grpc_log": true}
    

Isolating the actual error of the log:
    
    
    transport: Error while dialing: dial tcp [2607:f8b0:4001:c62::5f]:443: connect: network is unreachable
    

To work around this error, you can either switch to the `otlphttp` exporter (see our [OTLP metrics user guide](https://docs.cloud.google.com/stackdriver/docs/otlp-metrics/deploy-collector) for an example) or you can manually configure the `pick_first` balancer on the `otlp` exporter:
    
    
    exporters:
      otlp:
        # ...
        balancer_name: pick_first
        # ...
    

If the error persists after either workaround, then it is likely that this error message is a symptom of actual network connectivity problems, so you will need to ensure that your collector can actually reach the network.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
