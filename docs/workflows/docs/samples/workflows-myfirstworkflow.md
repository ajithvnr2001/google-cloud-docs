---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-myfirstworkflow/
title: Deploy your first workflow \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:02:12.276257+00:00
---

# Deploy your first workflow  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-myfirstworkflow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Deploy your first workflow Stay organized with collections  Save and categorize content based on your preferences. 

Passes the current day of the week as a search term to the Wikipedia API. A list of related Wikipedia articles is returned.

## Code sample

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Workflows quickstart using client libraries](https://docs.cloud.google.com/workflows/docs/quickstart-client-libraries). For more information, see the [Workflows Node.js API reference documentation](https://googleapis.dev/nodejs/workflows/latest/). 

To authenticate to Workflows, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
            },
            workflowId: WORKFLOW_ID,
          });
        }
      });
    
      it('should execute the quickstart', async () => {
        // Execute workflow, with long test timeout
        const result = execSync(
          `node --loader ts-node/esm ./index.ts ${PROJECT_ID} ${LOCATION_ID} ${WORKFLOW_ID}`
        );
    
        assert.strictEqual(
          result.length > 0,
          true,
          'Quickstart must return non-empty result'
        );
      }).timeout(5000);
    });
    

### YAML
    
    
    - getCurrentTime:
        call: http.get
        args:
          url: https://timeapi.io/api/Time/current/zone?timeZone=Europe/Amsterdam
        result: currentTime
    - readWikipedia:
        call: http.get
        args:
          url: https://en.wikipedia.org/w/api.php
          query:
            action: opensearch
            search: ${currentTime.body.dayOfWeek}
        result: wikiResult
    - returnResult:
        return: ${wikiResult.body[1]}

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
