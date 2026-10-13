---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-compute-health-checks-create-tcp/
title: gdcloud compute health-checks create tcp \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:01:16.806914+00:00
---

# gdcloud compute health-checks create tcp  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-compute-health-checks-create-tcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  gdcloud compute health-checks create tcp Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud compute health-checks create tcp - Create TCP health check for a load balancer.

## SYNOPSIS
    
    
    gdcloud compute health-checks create tcp HEALTH_CHECK_NAME [flags]
    

### EXAMPLES
    
    
    To create a global TCP health check "tcp-health-check", run:
    
        gdcloud compute health-checks create tcp tcp-health-check \
          --port=8080 \
          --global
    
        To create a zonal TCP health check "tcp-health-check", run:
    
        gdcloud compute health-checks create tcp tcp-health-check \
          --port=8080
    

### OPTIONAL FLAGS
    
    
          --check-interval int        Amount of time in seconds from the start of one probe to the start of the next one. Defaults to 5. (default 5)
          --global                    If set, the global health check object is created.
          --healthy-threshold int     Number of sequential probes that must succeed for the endpoint to be considered healthy. Defaults to 2. (default 2)
          --port int                  Port to use for the health check. If not specified, the backend service's port is used.
          --timeout int               Time (in seconds) to wait before claiming failure. Defaults to 5. (default 5)
          --unhealthy-threshold int   Number of sequential probes that must fail for the endpoint to be considered unhealthy. Defaults to 2. (default 2)
          --zone string               Zone to use for this invocation. To preset the zone flag for all commands that require it, run: "gdcloud config set core/zone ZONE". The zone flag is available only in multi-zone environments.
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
