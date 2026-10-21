---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace/run-use-cases/
title: Run use cases from the Content Hub \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:26:00.995901+00:00
---

# Run use cases from the Content Hub  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace/run-use-cases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Run use cases from the Content Hub

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

In Google Security Operations, a _use case_ is a pre-packaged deployment unit designed to accelerate workflow implementation. Each package acts as a functional blueprint, providing the necessary assets to model, ingest, and automate security operations.

Google Security Operations provides a repository of use cases that you can deploy in your environment. These use cases are available for download from the Content Hub. 

## Use case components

Each use case includes the following components you need to run a complete workflow:

  * A [test case](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/create-a-test-case) designed to trigger the workflow for validation.
  * [Mapping and modeling](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/ontology/create-entities-mapping--modeling) schemas to support data normalization.
  * The underlying [integration](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations) packages required for the workflow.
  * Predefined [connectors](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/connectors) for external log sources or APIs.
  * [Playbooks](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/whats-on-the-playbooks-screen) that define the automated logic and response actions.



You can find all legacy use case packages in the Google SecOps Content Hub home page. Each use case lists exactly what's included and typically comes with a video that shows how to get the use case running with either mock or live data. For a more updated experience, explore the **Content Packs** tab.

Once everything is set up, you can run the test cases from the **Cases** page.

## Example: Run the zero to hero use case

This example demonstrates how to run the basic phishing (zero to hero) use case from the Google SecOps Content Hub.

  1. Go to the **Google SecOps Content Hub**. 
  2. On the Home page, click **Go to legacy use cases**. 
  3. Filter for the **Zero to Hero** use case, and click **Run Use Case**. 
  4. Click **Run Use Case**. **Note** : We recommend that you watch the embedded five-minute technical walkthrough before proceeding with the wizard. 
  5. On the **overview** page, verify the specific integrations, playbooks, and test cases to bundle. Note the two provided email samples (malicious and non-malicious) available for ingestion by way of the Email Connector. Click **Next** when you're ready. 
  6. On the **Install Use Case items** page, verify the asset list (integrations, playbooks, and simulation cases) and click **Install**. 
  7. When the installation is complete, click **Next**.  
[ ![runusecases1](https://docs.cloud.google.com/static/chronicle/images/soar/runusecases1.png)](https://docs.cloud.google.com/static/chronicle/images/soar/runusecases1.png) Install use case  

  8. Make sure that you correctly define all the relevant fields and parameters to configure the integrations. When you've completed and tested the configuration, click **Next**. 
  9. Select the alert for simulation and click **Next** to automatically simulate the case. If you don't select the alert for simulation, go to **Cases** in the link, click  add **Add** , and select **Simulate Cases**. 
  10. When you see the **Congratulations** notification, review the next steps, click **Finish** and go to the **Cases** page. Then, continue to the last step in this procedure.   
[ ![runusecases2](https://docs.cloud.google.com/static/chronicle/images/soar/runusecases2.png)](https://docs.cloud.google.com/static/chronicle/images/soar/runusecases2.png) Confirmation of deployment  

  11. Select the **Zero to Hero** use case and click **Create**. 
  12. Select the default environment and click **Simulate**. 
  13. Click **Refresh**. A new case is created in Google SecOps, with a playbook attached within the alert. 



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
