---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-compute-health-checks-create-http/
title: gdcloud compute health-checks create http \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:24:32.301817+00:00
---

# gdcloud compute health-checks create http  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-compute-health-checks-create-http/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  gdcloud compute health-checks create http Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud compute health-checks create http - Create an HTTP health check for a load balancer.

## SYNOPSIS
    
    
    gdcloud compute health-checks create http HEALTH_CHECK_NAME [flags]
    

### EXAMPLES
    
    
    To create a global HTTP health check named "http-health-check", run:
    
        gdcloud compute health-checks create http http-health-check \
          --port=80 \
          --global
    
    To create a zonal HTTP health check named "http-health-check", run:
    
        gdcloud compute health-checks create http http-health-check \
          --port=80
    

### OPTIONAL FLAGS
    
    
          --check-interval int        Time (in seconds) from the start of one probe to the start of the next one. (default 5)
          --global                    If set, the global health check object is created.
          --healthy-threshold int     Number of sequential probes that must succeed for the endpoint to be considered healthy. (default 2)
          --host string               Value of the host header in the HTTPS health check request. If left empty (default value), the host header is set to the destination IP address to which health check packets are sent.
          --port int                  Port number on which to perform the health check. (default 80)
          --request-path string       Request path of the HTTPS health check request. This field does not support query parameters. Must comply with RFC 3986. (default "/")
          --response string           Creates a content-based HTTPS health check. In addition to the required 200 status code, you can configure the health check to pass only when the backend sends this specific ASCII response string within the first 1024 bytes of the HTTP response body.
          --timeout int               Time (in seconds) to wait before claiming failure. (default 5)
          --unhealthy-threshold int   Number of sequential probes that must fail for the endpoint to be considered unhealthy. (default 2)
          --zone string               Zone to use for this invocation. To preset the zone flag for all commands that require it, run: "gdcloud config set core/zone ZONE". The zone flag is available only in multi-zone environments.
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
