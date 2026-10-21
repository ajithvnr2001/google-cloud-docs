---
url: https://docs.cloud.google.com/looker/docs/archiving-log-files/
title: Archiving Looker log files \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:09:57.907595+00:00
---

# Archiving Looker log files  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/archiving-log-files/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Archiving Looker log files Stay organized with collections  Save and categorize content based on your preferences. 

Looker automatically rotates [log files](https://docs.cloud.google.com/looker/docs/creating-backups#directory_structure) daily. However, once the log is rotated and date stamped, Looker does not perform any further actions to compress or delete the logs. To preserve disk space on a customer-hosted Looker instance, we recommend you archive and delete older log files.

For the most basic configuration, we recommend setting up archive jobs in the Looker user's crontab. Add the following `cron` entries to leave the previous 7 days of log files uncompressed and the 21 days of log files prior to that gzipped in your log directory:
    
    
    ##zip Looker logs
    9 1 * * * find $HOME/looker/log -name 'looker.log.????????' -mtime +7 -exec gzip '{}' \; > /dev/null
    ##delete Looker logs
    33 1 * * * find $HOME/looker/log -name 'looker.log.????????.gz' -mtime +28 -exec rm -f '{}' \; > /dev/null
    

To leave fewer uncompressed logs, change the `7` in the first entry to a lower number. To store fewer compressed logs, change the `28` in the second crontab entry to a lower number.

For more information on how to use `cron`, see <https://help.ubuntu.com/community/CronHowto>.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
