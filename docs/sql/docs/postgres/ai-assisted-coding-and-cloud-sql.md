---
url: https://docs.cloud.google.com/sql/docs/postgres/ai-assisted-coding-and-cloud-sql/
title: Build vibe-coded applications with AI Studio and Cloud SQL \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:42.060049+00:00
---

# Build vibe-coded applications with AI Studio and Cloud SQL  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/ai-assisted-coding-and-cloud-sql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Build vibe-coded applications with AI Studio and Cloud SQL Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

This page provides an overview of capabilities offered by Cloud SQL for PostgreSQL to help you build [vibe-coded](https://cloud.google.com/discover/what-is-vibe-coding) applications.

[Google AI Studio](https://ai.google.dev/aistudio) supports full-stack, AI-assisted development enabling you to build applications that have rich functionality like persistent data storage and secure authentication. Using build mode in Google AI Studio, with a single prompt and a few clicks, you can create a rich application using Cloud SQL for PostgreSQL as the database. This enables your application to leverage the power of open source PostgreSQL and the enterprise readiness of Cloud SQL.

**Important:** Your ability to integrate with Google AI Studio might be blocked if your account and projects are part of an organization that has [domain-restricted sharing](https://docs.cloud.google.com/organization-policy/restrict-domains) enabled. Domain-restricted sharing is an organization policy that's enabled by default for all Google Cloud organizations created on or after May 3, 2024. It uses the `iam.allowedPolicyMemberDomains` legacy-managed constraint that only allows principals from projects in your organization to be granted roles in other projects belonging to your organization. We don't recommend disabling domain-restricted sharing because that can weaken your security posture.

## Get started with Google AI Studio and Cloud SQL

You can create an application with Cloud SQL using Google AI Studio at no cost by completing the following steps.

  1. Describe the application.

     1. Open [Google AI Studio](https://ai.google.dev/aistudio).
     2. To open build mode, click **Try it out**.
     3. If this is your first time using Google AI Studio, and you don't already have a Google Cloud account, then a **Welcome to AI Studio** window appears.

Review the Google Cloud Starter Tier terms of service, accept the terms of the agreement, and select any notifications you want to receive.

Click **Continue**.

     4. In the prompt field, enter a prompt describing your application.

For example, you can enter the following text. For best results, explicitly ask the agent to use Cloud SQL or a relational database:
            
            Build an expense tracker app using Cloud SQL
            

     5. Click **Build**.

  2. To confirm the creation of Cloud SQL for your application, the **Enable Database** card appears in the Google AI Studio chat. You can either use the default project and location settings of the card or change the settings.

The project and location you choose for your first integrated feature automatically applies to all other Google Cloud services and products that you later add to your app, including the following:

     * [Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/introduction)
     * [Firestore](https://firebase.google.com/docs/ai-assistance/ai-studio-integration#understand-shared-quota)
     * [Firebase Authentication](https://firebase.google.com/docs/ai-assistance/ai-studio-integration)
     * [Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)
**Note:** Once set, you can't change the location of resources you set up using Google AI Studio.

To use Cloud SQL default settings, do the following:

     1. In the **Enable database** card, click **Enable Cloud SQL**.

To select your own project and data storage location, do the following:

     1. In the **Enable database** card, click settings **Settings**.

     2. In the **Cloud SQL and Auth** window that appears, click the **Select a Google Cloud project to connect to Cloud SQL** menu.

        * If you have a Google Cloud account, select **Import project** to import a project you already use. The project must have billing enabled. Standard billing rates apply.
     3. In the **Your data will be stored in** menu, choose the region you want to use. We recommend choosing a region geographically close to you.

     4. Click **Enable Cloud SQL**.

The agent automatically deploys the Cloud SQL for PostgreSQL instance, creates the schema needed for your application, connects your application to the instance, and generates any necessary code.

  3. In the Preview panel, scroll through the design templates and choose the design you want to use. When you find the one you want, click **Select this design**.

  4. In the **Gemini** chat panel, click arrow_upward **Send prompt**.

  5. Iterate on the application.

     1. Once the initial version of the application is created, you can make modifications to the app, such as adding new features, using prompts. Here is an example:
            
            I want to add a custom description for each expense
            

The agent automatically makes the necessary code changes and updates the schema to add necessary columns to the Cloud SQL database.

     2. Optional: Next to the **Untitled** text, click edit **Edit app name and description** to rename the app. Alternatively, you can give Google AI Studio a prompt to rename the app.

  6. Publish the application.

     1. When the application is ready, click **Publish**.

     2. In the **Publish your app** panel, enter a description for your application and a support email for users to contact you.

     3. Click **Publish your app** to deploy the application using Cloud Run.

**Important:** Publishing the application exposes it publicly to the internet. Make sure to follow [security best practices](https://ai.google.dev/gemini-api/docs/aistudio-fullstack#best-practices) before you publish.



## Understand Cloud SQL quota for Google AI Studio

New Google AI Studio users can begin with [Google Cloud Starter Tier](https://docs.cloud.google.com/docs/starter-tier#supported-products), which provides a limited set of [supported resources](https://docs.cloud.google.com/docs/starter-tier#supported-products) for application deployment. This tier offers the core capabilities necessary to build and deploy your apps without requiring any billing details.

Deploying an application with Cloud SQL in Google Cloud Starter Tier automatically provisions all required infrastructure within a fully-managed Google Cloud Starter Tier project.

Because Google handles project management and configuration, you can use these services without a billing account.

Within Google Cloud Starter Tier, users are permitted to develop and publish 2 applications with Cloud SQL.

To expand your resource limits to build additional applications with Cloud SQL, you can upgrade your Google Cloud Starter Tier project to a standard Google Cloud project.

A standard Google Cloud project supports up to 10 applications with Cloud SQL per user per region.

You can scale up your Cloud SQL instance once you have upgraded to a standard Google Cloud project.

## Cloud SQL configuration in Google Cloud Starter Tier

When Google AI Studio builds an application that needs a relational database in Google Cloud Starter Tier, the agent creates a Cloud SQL for PostgreSQL developer edition instance.

Developer edition instances provide the following capabilities:

  * Supports 0.5 vCPU and 2 GB of memory with 1 GB of storage.
  * Creates instances in a fully-managed Google Cloud Starter Tier project.
  * Supports Cloud SQL for PostgreSQL instances created in version PostgreSQL 18.

**Note:** In Google Cloud Starter Tier, you can build 2 applications with Cloud SQL. You can't change instance configuration when using Google Cloud Starter Tier.

## Cloud SQL configuration when using an existing project

If you have a Google Cloud account and you enable Cloud SQL integration for an application, then you can optionally select an existing Google Cloud project that you own:

  1. In the **Enable database** card, click settings **Settings**.

     1. In the **Cloud SQL and Auth** window that appears, click the **Select a Google Cloud project to connect to Cloud SQL** menu.

        * Select **Import project** to import a project you already use. This project must have billing enabled.
  2. Click **Enable Cloud SQL**.




When you choose a project, the following actions occur:

  * A new Cloud SQL for PostgreSQL developer edition instance is instantly provisioned into that project.
  * The instance uses a limited free monthly quota. Any excess usage is charged as per the charges for compute and storage. For more information, see Google Cloud Starter Tier tier and pricing.



Cloud SQL for PostgreSQL developer edition can be created only when using Google AI Studio. You can't create a developer edition instance from the Google Cloud console or using Cloud SQL Admin API, [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) or Terraform. The Cloud SQL for PostgreSQL developer edition instance comes with the following features:

  * Google Cloud Starter Tier to start building applications at no cost. 
    * When using your Google Cloud project to build and deploy Google AI Studio applications with Cloud SQL, you get 50 compute units and 10 GB of Cloud Storage per month per billing account at no charge. For more information, see Google Cloud Starter Tier and pricing.
  * Instant provisioning for a seamless [vibe coding](https://cloud.google.com/discover/what-is-vibe-coding) experience. 
    * Cloud SQL instance is provisioned within seconds and ready for Google AI Studio to build the application.
  * Pauses the database instance automatically when the application is inactive. 
    * "Scale to zero" capability pauses an instance automatically when there are no active connections. Paused instances don't accrue VM or storage cost. Instance capacity limitations apply.
  * Scale up to 2 vCPU and 8 GB of RAM and 20 GB of storage. 
    * As compute and storage needs of the application grows, you can update the instance to 1 vCPU and 4 GB or 2 vCPU and 8 GB configuration. You can also update the storage to up to 20 GB.



You can only upgrade an instance when it is in a standard Google Cloud project. You can't scale up an instance using Google Cloud Starter Tier.

For more information, see [Upgrade your Google Cloud Starter Tier project to a standard Google Cloud project](https://docs.cloud.google.com/docs/starter-tier#upgrade).

**Important:** Developer edition doesn't support Cloud SQL Enterprise edition or Cloud SQL Enterprise Plus edition features like high availability, replicas, private networks, customer managed encryption keys or backup and recovery.

## Operations on the instance

When a Google AI Studio application uses a Cloud SQL instance as the database, you can interact with the instance from Google AI Studio through natural language prompts. For example, if you want to see the schema, then you can ask the agent the following:
    
    
    Show me the schema in the database.
    

The agent returns all information about the schema.

Similarly, if you want to execute a `CRUD` operation on the database, for example, to insert rows, then you can ask the agent to run that operation.

## Upgrade from Google Cloud Starter Tier for more quota and capabilities

After you've deployed your app using Google AI Studio, you can get more quota for your Cloud SQL instance and access other Google Cloud services by first upgrading from a Google Cloud Starter Tier project to a standard Google Cloud project.

To upgrade your Google Cloud Starter Tier project to a standard Google Cloud project:

  1. In Google AI Studio, click settings **Settings**.
  2. In the **Chat settings** window that appears, in the **Free requests** section, click settings **Select an API Key**.
  3. In the **Upgrade to unlock more** window, click **Gemini API**.
  4. Click **Continue with pay per request**.
  5. In the **Link a paid API Key** window, click **Set up billing**.
  6. In the **Set up your Google Cloud billing account** window, review the **Google Cloud Billing** terms of service and click **Agree and continue**.
  7. In the **Add your billing account details** window, enter your contact information and payment method and click **Submit**.



Now you are ready to get higher quotas for your application services. For more information, see Understand Cloud SQL quota for Google AI Studio.

### Update your Cloud SQL instance

After you have upgraded to a standard Google Cloud project, you can use the Google Cloud console to increase the instance size by updating the vCPU and disk size of the Cloud SQL instance.

To update your Cloud SQL instance in the Google Cloud console:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of the instance, click the name of the instance. Any instance created using Google AI Studio has the **Cloud SQL edition** type listed as **Developer** and an instance ID prefix of **ai-studio-**.
  3. Click **Edit**.
  4. In the **Instance ID** panel, update your configurations:

     1. **Machine configuration** : select the vCPU and amount of RAM you want to use.
     2. **Storage** : Select the amount of storage you want to use.

For more information, see [Editable settings](https://docs.cloud.google.com/sql/docs/postgres/instance-settings).

  5. Click **Save**.




## Google Cloud Starter Tier and pricing

Cloud SQL for PostgreSQL developer edition is charged only for usage beyond Google Cloud Starter Tier usage and for the time the instance is running. The instance is not charged when inactive or "scaled to zero".

Cloud SQL developer edition is charged based on compute units. A compute unit refers to 1 vCPU and 4 GB of memory. You are given 50 compute units and 10 GB of storage at no charge every month.

Google Cloud Starter Tier usage is aggregated across all [Google Cloud projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) by [Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/manage-billing-account) and resets every month; you are billed only for usage past the limited free tier.

If you are deploying applications using Cloud SQL across multiple Google Cloud projects and all projects use the same billing account, the usage limit is aggregated across all projects.

## Compute and storage pricing

The following is an example of per unit pricing in the region of South Carolina (`us-east1`).

Hourly pricing |   
---|---  
South Carolina (`us-east1`) | Region (USD)  
Compute unit | $0.10 / 1 hour  
Storage | $0.000157534 / 1 gibibyte hour  
**Note:** Cloud SQL for PostgreSQL developer edition is not eligible for committed used discounts or product-specific discounts.

For detailed pricing information, see [Cloud SQL pricing](https://cloud.google.com/sql/pricing).

## Google Cloud Starter Tier example

If you have a Google Account, you can start the Google AI Studio journey using the limited free quota for Cloud SQL in [Google Cloud Starter Tier](https://docs.cloud.google.com/docs/starter-tier#upgrade).

You can build 2 applications at no charge using Google Cloud Starter Tier. After that quota is exceeded, you can upgrade to use a standard Google Cloud project to get more quota to build and publish additional Google AI Studio apps.

If you upgrade your Google Cloud Starter Tier project to a standard Google Cloud project, or if you create a standard Google Cloud project to explore other Google Cloud products, then you can use the Google Cloud [Free Trial](https://docs.cloud.google.com/free/docs/free-cloud-features) to access a limited free quota of 50 compute units and 10 GB of storage per month. If your usage exceeds that quota during the month for a particular billing account, then you will be charged for the additional usage based on the previous pricing table.

For example, say you are building Google AI Studio applications in a Google Cloud project called `Test`. You use a billing account and credit card for that project. Your Google AI Studio usage of Cloud SQL across all applications exceeds 50 compute units and by the end of the month you use 100 compute units. You will be charged the excess 50 compute units at $0.10 per hour and charged $5 for the month.

## Limitations

  * Database instances with up to 1 GB of storage and up to 0.5 vCPU of compute capacity pause automatically, or "scale to zero," if there are no active connections. This capability is not supported for instances that exceed either of these storage and compute limits.

  * Ability to integrate with Google AI Studio might be blocked if your organization has [domain-restricted sharing](https://docs.cloud.google.com/organization-policy/restrict-domains) enabled.




## What's next

  * [Learn about Google AI Studio](https://ai.google.dev/aistudio)
  * [Learn about Google Cloud Starter Tier](https://docs.cloud.google.com/docs/starter-tier#supported-products)
  * [Edit your Cloud SQL instance](https://docs.cloud.google.com/sql/docs/postgres/edit-instance)
  * [Work with vector embeddings](https://docs.cloud.google.com/sql/docs/postgres/work-with-vectors)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
