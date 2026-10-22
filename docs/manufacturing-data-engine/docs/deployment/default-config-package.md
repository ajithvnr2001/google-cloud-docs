---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/deployment/default-config-package/
title: Default configuration package \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:49.207731+00:00
---

# Default configuration package  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/deployment/default-config-package/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Default configuration package

The standard Manufacturing Data Engine (MDE) deployment doesn't apply any configuration settings by default, which are needed to ingest data.

Applying the default configuration package lets you to start quickly ingesting data Manufacturing Connect edge (MCe) and other data sources.

#### Before you begin

The `curl` deployment option requires that you perform the following:

  * Install the [`curl` utility](https://everything.curl.dev/install/index.html) on your workstation.
  * Configure [SSH tunneling over IAP](https://docs.cloud.google.com/manufacturing-data-engine/docs/deployment/step-three-configure-access#ssh-tunneling-over-IAP) or otherwise have established connectivity between your client and the MDE APIs.



#### Steps

  1. Open a tunnel to the `mde-proxy` by executing using the following command:
         
         export MDE_PROXY_ZONE=$(gcloud compute instances list --filter="mde-proxy" --format="value(zone)")
         
         gcloud compute ssh mde-proxy \
         --zone "$MDE_PROXY_ZONE" --tunnel-through-iap  \
         -- -N -L 8080:api.mde.cloud.google.com:80
         

  2. Download the default configuration package [shell script](https://storage.mtls.cloud.google.com/gc-imde/assets/default_config_package_1.1.1.sh).

  3. Execute the shell script `sh default-package.sh`.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
