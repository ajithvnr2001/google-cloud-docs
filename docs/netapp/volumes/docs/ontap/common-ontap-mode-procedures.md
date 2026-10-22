---
url: https://docs.cloud.google.com/netapp/volumes/docs/ontap/common-ontap-mode-procedures/
title: Common ONTAP-mode procedures \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:45.858177+00:00
---

# Common ONTAP-mode procedures  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/ontap/common-ontap-mode-procedures/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Common ONTAP-mode procedures Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the common procedures required for ONTAP-mode tasks. Because many Flex Unified ONTAP-mode storage pool tasks use the same Google Cloud CLI and API prerequisites, you only need to complete this setup once before proceeding to your specific task.

## Before you begin

Complete the following steps:

  1. Run command examples in a Unix-like environment: Linux, macOS, or Windows Subsystem for Linux (WSL). The `ontap_execute` shell function and other bash examples require bash. If your workstation doesn't provide a Unix-like shell, use Google Cloud Shell, which includes bash and the Google Cloud CLI.

  2. Install Google Cloud CLI version 559.0.0 or later and authenticate:
         
         gcloud auth login
         gcloud config set project PROJECT_ID
         

  3. Collect the following values for each pool that you administer:

     * `POOL_NAME`: the storage pool name.

     * `LOCATION`: the location for the pool.

     * `PROJECT_ID`: the project ID, which is optional if you have set it in your Google Cloud CLI configuration.


**Note:** Use a zone for zonal pools (for example, `us-central1-a`) or a region for regional pools (for example, `us-central1`).

## Set up ontap_execute

Set `POOL_NAME` and `LOCATION`, then define a shell function to run ONTAP commands through the [Google Cloud CLI ONTAP CLI proxy](https://docs.cloud.google.com/netapp/volumes/docs/ontap/manage-ontap#use-gcloud-ontap-cli-proxy). The function validates variables on each call. The `PROJECT_ID` uses the default from your Google Cloud CLI configuration.

To define the `ontap_execute` function:
    
    
     export POOL_NAME="mypool"
     export LOCATION="us-central1-a"
    
     ontap_execute() {
       : "${POOL_NAME:?Set POOL_NAME to your ONTAP-mode storage pool name}"
       : "${LOCATION:?Set LOCATION to the pool zone (for example us-central1-a) or region (for example us-central1)}"
    
       local project="${PROJECT_ID:-$(gcloud config get-value project 2>/dev/null)}"
    
       if [[ -z "${project}" ]]; then
         echo "Set PROJECT_ID or run: gcloud config set project PROJECT_ID" >&2
         return 1
       fi
    
       gcloud netapp storage-pools execute "${POOL_NAME}" "$1" \
         --project="${project}" \
         --location="${LOCATION}"
     }
    

The following examples use `ontap_execute "ONTAP-COMMAND"` to run the specified ONTAP command on the pool identified by `POOL_NAME` and `LOCATION`. Replace the placeholder values such as `SVM_NAME` before you run each command.

When a procedure involves more than one pool, change `POOL_NAME` and `LOCATION` before each `ontap_execute` call.

## Run ONTAP CLI commands by using the proxy

The ONTAP CLI proxy provides access to most ONTAP commands for your storage pool. The proxy isn't interactive, so commands that prompt for a passphrase, password, or other input will fail.

Use `ontap_execute` for routine non-interactive commands, as shown in the Procedures section.

## Use the REST API proxy for interactive steps

When an ONTAP command requires interactive input, use the [Google proxy API for ONTAP REST API calls](https://docs.cloud.google.com/netapp/volumes/docs/ontap/manage-ontap#use_a_google_proxy_api_for_ontap_rest_api_calls) instead. This document includes Python examples. REST requests through the proxy use a `body` envelope around the ONTAP API payload.

## Look up cluster and SVM names

To look up the cluster and SVM names on an ONTAP-mode pool:
    
    
     ontap_execute "cluster identity show"
     ontap_execute "vserver show"
     ontap_execute "network interface show -role intercluster"
    

Note the cluster name from `cluster identity show` and the data SVM name from `vserver show`. IC-LIFs for intercluster traffic are in IPspace `Gcnv`. The `Vserver` column for IC-LIFs shows `Gcnv`. IC-LIF names are `intercluster-1`, `intercluster-2`, and similar, with one name per node.

**Note:** The ONTAP CLI proxy doesn't support `-fields` on `network interface show` or `vserver peer show`. Use the default command output.

## Procedures

The following procedures include routine non-interactive commands:

  * [Join an ONTAP-mode pool to Active Directory](https://docs.cloud.google.com/netapp/volumes/docs/ontap/join-ontap-mode-pool-to-ad)

  * [Peer clusters and SVMs](https://docs.cloud.google.com/netapp/volumes/docs/ontap/peer-clusters-svms)




## What's next

  * [Join an ONTAP-mode pool to Active Directory](https://docs.cloud.google.com/netapp/volumes/docs/ontap/join-ontap-mode-pool-to-ad).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
