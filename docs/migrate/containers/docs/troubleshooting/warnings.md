---
url: https://docs.cloud.google.com/migrate/containers/docs/troubleshooting/warnings/
title: Migration warnings \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:10.528876+00:00
---

# Migration warnings  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/troubleshooting/warnings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Guides ](https://docs.cloud.google.com/migrate/containers/docs/getting-started)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migration warnings

This page describes the warnings that you might get after you run the `analyze` command.

## Types of warnings

After you run the `analyze` command, Migrate to Containers might provide warnings specific to your migration type. There are two possible types of warnings:

  * **`MigrationBlocker` warnings:** These warnings block your migration, and you must address them. You cannot generate the artifacts of a migration while there are active `MigrationBlocker` warnings.
  * **`Normal` warnings:** These are non-blocking warnings that you can decide to address. Even though warnings of type `Normal` don't block the generation of artifacts, they might cause the migration process to fail, or cause the migrated workload to fail when run.



## How to read the warnings

If there are warnings, they appear in the `warnings.yaml` file in the output directory of the `analyze` command.

Each warning message contains the following fields:

  * **type:** The type of warning, either `MigrationBlocker` or `Normal`.
  * **reason:** The cause of the warning.
  * **mitigation:** The description of the warning and possible actions to resolve it.



For example, the following is a `FileTooBig` warning for Linux.
    
    
    - message: The source VM file-system contains file(s) which are too big to be part of the generated container image
      mitigation: Please edit the migration plan to either filter them out, or export them to a data volume
      reason: FileTooBig
      type: MigrationBlocker
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
