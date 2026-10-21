---
url: https://docs.cloud.google.com/composer/docs/samples/composer-list-image-versions/
title: List Composer Image Versions \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:28:25.589769+00:00
---

# List Composer Image Versions  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/samples/composer-list-image-versions/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Samples ](https://docs.cloud.google.com/composer/docs/samples)



#  List Composer Image Versions Stay organized with collections  Save and categorize content based on your preferences. 

Lists image versions for Cloud Composer

## Code sample

### Node.js

To authenticate to Managed Airflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    
    // remove this line after package is released
    // eslint-disable-next-line node/no-missing-require
    const {ImageVersionsClient} = require('[@google-cloud/orchestration-airflow](https://docs.cloud.google.com/nodejs/docs/reference/orchestration-airflow/latest/overview.html)');
    
    // TODO(developer): replace with your prefered project ID.
    // const projectId = 'my-project'
    
    // Creates a client
    // eslint-disable-next-line no-unused-vars
    const client = new [ImageVersionsClient](https://docs.cloud.google.com/nodejs/docs/reference/orchestration-airflow/latest/overview.html)();
    
    async function listImageVersions() {
      const [versions] = await client.listImageVersions({
        parent: `projects/${projectId}/locations/${location}`,
      });
      console.info(versions);
    }
    listImageVersions();

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=composer). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
