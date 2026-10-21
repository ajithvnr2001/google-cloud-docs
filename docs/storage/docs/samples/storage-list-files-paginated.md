---
url: https://docs.cloud.google.com/storage/docs/samples/storage-list-files-paginated/
title: List files in a paginated manner \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:31.147167+00:00
---

# List files in a paginated manner  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-list-files-paginated/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  List files in a paginated manner Stay organized with collections  Save and categorize content based on your preferences. 

List objects in a bucket with no autopagination, showing how to move to the next set of objects.

## Code sample

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of your GCS bucket
    // const bucketName = 'your-unique-bucket-name';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function listFilesPaginated() {
      const bucket = storage.bucket(bucketName);
      const [files, queryForPage2] = await bucket.[getFiles](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/bucket.html)({autoPaginate: false});
    
      console.log('Files:');
      files.forEach(file => {
        console.log(file.name);
      });
    
      // Page through the next set of results using "queryForPage2"
      if (queryForPage2 !== null) {
        const [files, queryForPage3] = await bucket.[getFiles](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/bucket.html)(queryForPage2);
    
        console.log('Files:');
        files.forEach(file => {
          console.log(file.name);
        });
    
        // If necessary, continue cursoring using "queryForPage3"
      }
    }
    
    listFilesPaginated().catch(console.error);

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
