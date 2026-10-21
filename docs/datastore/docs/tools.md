---
url: https://docs.cloud.google.com/datastore/docs/tools/
title: Using the gcloud Tool to Test Applications and Manage Indexes \u00a0|\u00a0 Firestore in Datastore mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:31:48.013556+00:00
---

# Using the gcloud Tool to Test Applications and Manage Indexes  |  Firestore in Datastore mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastore/docs/tools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)
  * [ Guides ](https://docs.cloud.google.com/datastore/docs/concepts/overview)



Send feedback 

#  Using the gcloud Tool to Test Applications and Manage Indexes Stay organized with collections  Save and categorize content based on your preferences. 

You can use the Google Cloud CLI to test your application locally and to manage indexes for your production Firestore in Datastore mode instance. This page describes the typical workflow for these activities.

**Note:** This discussion assumes that you have already [enabled](https://docs.cloud.google.com/datastore/docs/activate) the Datastore API for your project; [downloaded](https://docs.cloud.google.com/sdk) the Google Cloud CLI, which contains the gcloud CLI; and set up the gcloud CLI using [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init).

The gcloud CLI supports the following workflow:

  1. Create local support for a Datastore instance, including directory, required files, and project ID.
  2. Start up the Datastore emulator, which provides local emulation of the production Datastore environment.
  3. Generate index definitions from your application's queries to the emulator.
  4. Upload manually created or generated index definitions to your production database instance.
  5. Delete unused indexes from your production database instance.



## The development workflow using the command-line tool

The following is the typical workflow using the gcloud CLI:

  1. [Start the Datastore emulator](https://docs.cloud.google.com/datastore/docs/tools/datastore-emulator#starting_the_emulator).

  2. [Set environment variables](https://docs.cloud.google.com/datastore/docs/tools/datastore-emulator#setting_environment_variables) so your application knows it is using the emulator.

  3. Start your application and test it against the emulator. You need to run the queries your application uses against the emulator in order to generate indexes for your production database instance.

  4. Upload the generated indexes with the [`indexes create`](https://docs.cloud.google.com/sdk/gcloud/reference/datastore/indexes/create) command, passing in the path to your local `index.yaml` file, as in the following example:
         
         gcloud datastore indexes create ~/.config/gcloud/emulators/datastore/WEB-INF/index.yaml
         

The example path assumes you have not set a specific directory for the [`data-dir`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/emulators/datastore/start#FLAGS) option. If you have set a specific directory, modify the path to use the path to your `index.yaml` file.

  5. [Remove environment variables](https://docs.cloud.google.com/datastore/docs/tools/datastore-emulator#removing_environment_variables) so your application knows it is using the production database instance.

  6. Run your application against your production database instance.

  7. Over time, you might no longer use some of the indexes. You can delete unused indexes from your production database instance by removing them from your local `index.yaml` file and then invoking the [`indexes cleanup`](https://docs.cloud.google.com/sdk/gcloud/reference/datastore/indexes/cleanup) command:
         
         gcloud datastore indexes cleanup ~/.config/gcloud/emulators/datastore/WEB-INF/index.yaml
         

If you have set a specific directory for the [`data-dir`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/emulators/datastore/start#FLAGS) option, modify the path in the example to use the path to your `index.yaml` file.




## What's next

  * Learn more about the [emulator](https://docs.cloud.google.com/datastore/docs/tools/datastore-emulator).
  * Get details about [Index configuration](https://docs.cloud.google.com/datastore/docs/tools/indexconfig).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
