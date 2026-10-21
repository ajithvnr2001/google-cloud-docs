---
url: https://docs.cloud.google.com/vision/docs/samples/vision-detect-document/
title: Label detection on a local file \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:22.481486+00:00
---

# Label detection on a local file  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/samples/vision-detect-document/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Samples ](https://docs.cloud.google.com/vision/docs/samples)



#  Label detection on a local file Stay organized with collections  Save and categorize content based on your preferences. 

Performs label detection on a local document file.

## Code sample

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client libraries
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)').v1p1beta1;
    
    // Creates a client
    const client = new vision.[ImageAnnotatorClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment the following line before running the sample.
     */
    // const fileName = 'Local image file, e.g. /path/to/image.png';
    
    // Performs label detection on the local file
    const [result] = await client.textDetection(fileName);
    const pages = result.fullTextAnnotation.pages;
    pages.forEach(page => {
      page.blocks.forEach(block => {
        const blockWords = [];
        block.paragraphs.forEach(paragraph => {
          paragraph.words.forEach(word => blockWords.push(word));
          console.log(`Paragraph confidence: ${paragraph.confidence}`);
        });
    
        let blockText = '';
        const blockSymbols = [];
        blockWords.forEach(word => {
          word.symbols.forEach(symbol => blockSymbols.push(symbol));
          let wordText = '';
          word.symbols.forEach(symbol => {
            wordText = wordText + symbol.text;
            console.log(`Symbol text: ${symbol.text}`);
            console.log(`Symbol confidence: ${symbol.confidence}`);
          });
          console.log(`Word text: ${wordText}`);
          console.log(`Word confidence: ${word.confidence}`);
          blockText = blockText + ` ${wordText}`;
        });
    
        console.log(`Block text: ${blockText}`);
        console.log(`Block confidence: ${block.confidence}`);
      });
    });

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudvision). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
