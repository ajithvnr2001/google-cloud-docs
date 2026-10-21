---
url: https://docs.cloud.google.com/looker/docs/updating-looker-instance/
title: Updating a customer-hosted Looker instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:36:28.680540+00:00
---

# Updating a customer-hosted Looker instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/updating-looker-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Updating a customer-hosted Looker instance Stay organized with collections  Save and categorize content based on your preferences. 

To access the latest bug fixes and new features, update your customer-hosted Looker instance by following these manual steps.

Before proceeding, be aware that rolling back to an earlier version can cause serious problems. Instead, always restore from a backup if you need to revert. If you operate a Looker cluster, update each node completely, one at a time. This process also assumes your instance includes the startup script installed during initial setup.

  1. Download the most recent release of the Looker JAR files as described on the [Downloading the Looker JAR Files](https://docs.cloud.google.com/looker/docs/downloading-looker-jar-files) documentation page.
  2. Stop the Looker process from shell, as the **looker** user:
         
         sudo su - looker
         cd /home/looker/looker
         ./looker stop
         

If you are updating a Looker cluster, repeat this process so that Looker is stopped on every node.

  3. Back up your entire Looker directory, including hidden directories (see the [Restoring backups](https://docs.cloud.google.com/looker/docs/restoring-backups) documentation page for more detail).

  4. If you have [migrated Looker's default in-memory database to an external MySQL database](https://docs.cloud.google.com/looker/docs/migrating-looker-backend-db-to-mysql), or if you are updating a Looker cluster, back up the MySQL database.

  5. Rename `looker-x.x.x.jar` to `looker.jar` and `looker-dependencies-x.x.x.jar` to `looker-dependencies.jar`. Copy `looker.jar` and `looker-dependencies.jar` to the server directory (`/home/looker/looker/looker.jar`). Both files _must_ be in the same directory.

  6. Start the Looker process from the shell as the **looker** user:

> If you are updating a Looker cluster, start the Looker process on one node only. Don't start Looker on the other nodes until the first node has completed the update process.
         
         ./looker start
         

You can also use the `java -jar` command to start Looker. The core JAR will find the dependency JAR as long as it is in the `./looker` directory along with the core JAR.

In addition, if you'd rather use a Looker-provided startup script, you can find a startup script at: <https://github.com/looker/customer-scripts>.

When you update your Looker version, Looker must also update its internal database. The database update usually takes less than five minutes, but it can sometimes take longer than the Looker startup process. If you try to start Looker while the internal database is still updating, the daemonizing process will time out in six minutes with the message "Timed out waiting for Looker to start."

During an update, the required migrations can take up to an hour, especially if you are skipping several releases. If you receive this error message, wait for the update to finish and for Looker to start. You can confirm whether the update process is still running by using the command:
         
         ps -f $(pgrep -f -- '-jar looker.jar')
         

Stopping and restarting the Looker process while the internal database updates are in progress can corrupt the internal database. If this happens, restore Looker from an existing backup and perform the update again.

  7. If you are updating a Looker cluster, wait until the first node has completed the update process before starting Looker on the other nodes.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
