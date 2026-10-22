---
url: https://docs.cloud.google.com/application-design-center/docs/three-tier-web-app/
title: Three-tier web app template \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:46.143136+00:00
---

# Three-tier web app template  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/three-tier-web-app/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Guides ](https://docs.cloud.google.com/application-design-center/docs/overview)



Send feedback 

#  Three-tier web app template Stay organized with collections  Save and categorize content based on your preferences. 

Accelerate your organization's digital transformation by providing a high-availability, production-ready foundation for modern web applications. This guide helps you understand the _Three-tier web app_ application template, which helps you quickly deploy a three-tier web application to Google Cloud.

For example, you might implement this template to address the following business needs:

Example | Business need | Implementation  
---|---|---  
Ecommerce platform | A retail company needs a web presence that can handle sudden spikes in traffic during seasonal sales while maintaining low latency for product searches and purchases. | Use the Cloud Run tier for the storefront to scale automatically based on request volume. The middle tier handles inventory logic, and Memorystore for Redis caches product catalogs to reduce database load and latency.  
Tech support ticketing system | An enterprise IT department needs an internal portal where employees report hardware issues and track software requests. | Use the Cloud Run frontend to input employee requests. The frontend communicates with an API layer to manage ticket routing logic and priority assignments. The Cloud SQL database contains employee data and resolution audit trails.  
  
## Architecture

The following image shows the components and connections in the application:

![A three-tier web application in the design canvas. The application includes frontend, backend, and database components.](https://docs.cloud.google.com/static/application-design-center/images/google-three-tier.png)

The following is the request processing flow of the application:

  1. A [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview) frontend receives external requests and distributes traffic to the Cloud Load Balancing backend.
  2. The Cloud Load Balancing backend distributes traffic to the [Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run) service.
  3. A web-based Cloud Run frontend service renders an HTML client in the user's browser.
  4. The frontend service sends requests to an API layer, which is also deployed as a Cloud Run service.
  5. [Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview) caches and serves frequently read data.
  6. The API layer sends requests that it can't serve from the in-memory Redis cache to a [Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/introduction) database.



## What's next

  * To learn how to duplicate and customize templates, see [Quickstart: Customize and deploy a Google template](https://docs.cloud.google.com/application-design-center/docs/quickstart-deploy-google-template).
  * Define your own configurations by [designing application templates](https://docs.cloud.google.com/application-design-center/docs/design-application-templates).
  * Identify general architectural best practices with the [Google Cloud Architecture Framework](https://docs.cloud.google.com/architecture/framework).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
