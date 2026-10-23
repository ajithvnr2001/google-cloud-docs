---
url: https://docs.cloud.google.com/translate/docs/samples/translate-text-with-model-beta/
title: Translate text with model (V3 Beta) \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:55.725444+00:00
---

# Translate text with model (V3 Beta)  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/samples/translate-text-with-model-beta/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Samples ](https://docs.cloud.google.com/translate/docs/samples)



#  Translate text with model (V3 Beta) Stay organized with collections  Save and categorize content based on your preferences. 

Translate text with model.

## Code sample

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Node.js API reference documentation](https://googleapis.dev/nodejs/translate/latest/index.html). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const location = 'global';
    // const modelId = 'YOUR_MODEL_ID';
    
    // Imports the Google Cloud Translation library
    const {TranslationServiceClient} = require('[@google-cloud/translate](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)').v3beta1;
    const automl = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)');
    
    // Instantiates a client
    const translationClient = new [TranslationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)();
    const autoMLClient = new automl.[AutoMlClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    async function translateTextWithModel() {
      const model = autoMLClient.modelPath(projectId, location, modelId);
      // Construct request
      const request = {
        parent: translationClient.locationPath(projectId, location),
        contents: [text],
        mimeType: 'text/plain', // mime types: text/plain, text/html
        sourceLanguageCode: 'en-US',
        targetLanguageCode: 'ja',
        model: model,
      };
    
      // Run request
      const [response] = await translationClient.translateText(request);
    
      for (const translation of response.translations) {
        console.log(`Translated Content: ${translation.translatedText}`);
      }
    }
    
    translateTextWithModel();

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudtranslation). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
