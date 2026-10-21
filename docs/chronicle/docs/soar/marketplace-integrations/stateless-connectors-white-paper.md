---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/stateless-connectors-white-paper/
title: Stateless Connectors - White Paper \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:10.376743+00:00
---

# Stateless Connectors - White Paper  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/stateless-connectors-white-paper/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Stateless Connectors - White Paper

This white paper will detail the new and significant updates to our connectors, and to the connectors' infrastructure.

## Background

Google Security Operations connectors are the main data sources of the SOAR platform. Every connector is the main ark of ingestion into the platform. To track this component's proper functioning, the Google SecOps Content Hub department is using metadata files to store the connector's state. Up until now - these files were saved in the connector's running folder.

### Why are files no longer necessary

There is no need to store files when offering a SAAS solution, as we are providing stateless support for the main functionalities of the Google SecOps system.

Files are not sustainable and can get lost. When thinking of scaling up or down, and taking full advantage of the micro-services architecture, working with local files is no longer relevant.

To improve our state track mechanism, and to improve one of our most important procedures in the system, we have come up with the following solution.

### Solution Overview

The solution is to store everything related to the connector's state within the Google SecOps instance. Every connector has its own storage place, within the Google SecOps instance, where all of the data is be kept.

A new concept of "Connector-Context" will be introduced.

### Some Issues to Look out For

**Map.json File**

Customers using the map.json file, for advanced environment mapping within Google SecOps, now have to migrate to a newer version of the environment mapping capabilities - Environment Aliases. For further instructions, please visit our documentation site right here.

**Connector Upgrade process**

When updating the connector, the connector's state is not transferred from the file system to the connector's context. Which means, the connector's first run in the new solution is considered the first run. Therefore, cases of duplications can happen around the update time.

**Size Limitation**

Some of our connectors maintain a backward tracking capability, to better fit to the API of the product we are integrating with. This behavior was represented in the connector's configuration parameters, usually called "Padding Period" or "Fetch Backwards Time Interval" or similar. Now, we are going to have another limitation which is the actual size of the data stored. By default, the limitation is 3 million characters. This limitation should be sufficient for most cases.

If, by any chance, this limitation is reached, we will log it and will try to maintain maximum functionality within the limitation.

## Next Steps

  1. Make sure you are using the Environment Aliases for advanced environment mapping and not the map.json file.
  2. Make sure the update is done at a time where duplicates shouldn't be an issue for you.
  3. Go over your "Fetch Backwards Time Interval" parameters in the connectors, and make sure they are not trying to keep a long time (between 1 day to 1 week is recommended).

**Note:** Logs for now are still being written to the same place. Once that is changes, we will update here with the appropriate explanation and guidance.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
