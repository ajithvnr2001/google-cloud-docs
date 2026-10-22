---
url: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-extensible-template-udf/
title: Create UDF for an extensible template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:39.408647+00:00
---

# Create UDF for an extensible template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-extensible-template-udf/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Samples ](https://docs.cloud.google.com/dataflow/docs/samples)



#  Create UDF for an extensible template Stay organized with collections  Save and categorize content based on your preferences. 

Creates a UDF that extends the Pub/Sub Topic to BigQuery template.

## Code sample

### Node.js

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * User-defined function (UDF) to transform events
     * as part of a Dataflow template job.
     *
     * @param {string} inJson input Pub/Sub JSON message (stringified)
     */
     function process(inJson) {
        const obj = JSON.parse(inJson);
        const includePubsubMessage = obj.data && obj.attributes;
        const data = includePubsubMessage ? obj.data : obj;
    
        if (!data.hasOwnProperty('url')) {
          throw new Error("No url found");
        } else if (data.url !== "https://beam.apache.org/") {
          throw new Error("Unrecognized url");
        }
    
        return JSON.stringify(obj);
      }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=dataflow). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
