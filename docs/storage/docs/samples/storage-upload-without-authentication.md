---
url: https://docs.cloud.google.com/storage/docs/samples/storage-upload-without-authentication/
title: Upload a file without authentication \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:49.389858+00:00
---

# Upload a file without authentication  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-upload-without-authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Upload a file without authentication Stay organized with collections  Save and categorize content based on your preferences. 

Upload a file without authentication

## Code sample

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of your GCS bucket
    // const bucketName = 'your-unique-bucket-name';
    
    // The contents that you want to upload
    // const contents = 'these are my contents';
    
    // The new ID for your GCS file
    // const destFileName = 'your-new-file-name';
    
    // Imports the Google Cloud Node.js client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function uploadWithoutAuthentication() {
      const file = storage.bucket(bucketName).file(destFileName);
    
      // Returns an authenticated endpoint to which
      // you can make requests without credentials.
      const [location] = await file.[createResumableUpload](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/file_2.html)(); //auth required
    
      const options = {
        uri: location,
        resumable: true,
        validation: false,
    
        // Optional:
        // Set a generation-match precondition to avoid potential race conditions
        // and data corruptions. The request to upload is aborted if the object's
        // generation number does not match your precondition. For a destination
        // object that does not yet exist, set the ifGenerationMatch precondition to 0
        // If the destination object already exists in your bucket, set instead a
        // generation-match precondition using its generation number.
        preconditionOpts: {ifGenerationMatch: generationMatchPrecondition},
      };
    
      // Passes the location to file.save so you don't need to
      // authenticate this call
      await file.[save](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/file_2.html)(contents, options);
    
      console.log(`${destFileName} uploaded to ${bucketName}`);
    }
    
    uploadWithoutAuthentication().catch(console.error);

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
