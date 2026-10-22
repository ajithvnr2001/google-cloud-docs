---
url: https://docs.cloud.google.com/alloydb/docs/samples/alloydb-quickstart/
title: List supported database flags \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:27.680677+00:00
---

# List supported database flags  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/samples/alloydb-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Samples ](https://docs.cloud.google.com/alloydb/docs/samples)



#  List supported database flags Stay organized with collections  Save and categorize content based on your preferences. 

This snippet shows how to list the database flags that are supported by the service. You can use this to learn which flags are available to configure on your clusters.

## Code sample

### Node.js

To authenticate to AlloyDB, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. The name of the parent resource. The required format is:
     *   * projects/{project}/locations/{location}
     *  Regardless of the parent specified here, as long it is contains a valid
     *  project and location, the service will return a static list of supported
     *  flags resources. Note that we do not yet support region-specific
     *  flags.
     */
    // const parent = 'abc123'
    /**
     *  Requested page size. Server may return fewer items than requested.
     *  If unspecified, server will pick an appropriate default.
     */
    // const pageSize = 1234
    /**
     *  A token identifying a page of results the server should return.
     */
    // const pageToken = 'abc123'
    
    // Imports the Alloydb library
    const {AlloyDBAdminClient} = require('[@google-cloud/alloydb](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)').v1alpha;
    
    // Instantiates a client
    const alloydbClient = new [AlloyDBAdminClient](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)();
    
    async function callListSupportedDatabaseFlags() {
      // Construct request
      const request = {
        parent,
      };
    
      // Run request
      const iterable =
        await alloydbClient.listSupportedDatabaseFlagsAsync(request);
      for await (const response of iterable) {
        console.log(response);
      }
    }
    
    callListSupportedDatabaseFlags();

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=alloydbforpostgresql). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
