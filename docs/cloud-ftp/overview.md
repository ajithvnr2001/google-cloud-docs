---
url: https://docs.cloud.google.com/cloud-ftp/overview/
title: Cloud FTP overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:14:44.880662+00:00
---

# Cloud FTP overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-ftp/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud FTP ](https://docs.cloud.google.com/cloud-ftp)
  * [ Guides ](https://docs.cloud.google.com/cloud-ftp/overview)



Send feedback 

#  Cloud FTP overview Stay organized with collections  Save and categorize content based on your preferences. 

Cloud FTP provides a managed, cloud-based solution to securely move data in and out of Google Cloud by using SSH File Transfer Protocol (SFTP).

You use Cloud FTP to create a managed SFTP server for users who need to securely transfer files to and from Cloud Storage. Then, your users can upload or download data in Cloud Storage buckets by using SFTP commands and standard SFTP clients like Cyberduck, FileZilla, or WinSCP.

## Use cases

Cloud FTP supports common scenarios like the following:

  * **Sharing data with external partners** : enterprises in a range of industries, including finance, healthcare, media, and retail, use managed file transfer solutions to exchange different types of data with external partners.

  * **Sharing data among coworkers** : employees who need to access and transfer storage data can do these tasks by using standard SFTP commands, without having to learn Identity and Access Management (IAM) concepts or use the Google Cloud CLI.

  * **Data analytics and processing** : Cloud FTP provides a secure way for internal stakeholders to upload sensitive data to Cloud Storage for tasks like data processing, analytics, and machine learning.




Cloud FTP is compatible with open source clients, which means that you can use your existing applications and standard third-party file transfer tools to access data in Cloud Storage.

## Data security

Here's how Cloud FTP helps to secure your data:

  * You choose how to configure your network security when you create an SFTP server:

    * External servers are accessible to the internet, and access is restricted to the IP ranges that you specify.

    * Internal servers can be accessed only within your Virtual Private Cloud (VPC) network by using Private Service Connect. You specify the projects that are allowed to connect to the server.

  * Cloud FTP transfers data over an encrypted Secure Shell (SSH) channel.

  * The SFTP server's SSH host keys are managed by Google Cloud.

  * The SSH protocol provides data integrity checks between the client and the server.

  * Authentication and authorization works like this:

    * Users authenticate to their SFTP client by using public keys.

    * Each user is mapped to a service account. You grant the service account the IAM roles that are necessary to read or write data in the Cloud Storage bucket. The service account accesses Cloud Storage resources on behalf of the user.

    * The Cloud FTP Service Agent generates tokens for the user's service account. These tokens are used to access the bucket for SFTP functionality.

  * You can use VPC Service Controls to create a service perimeter that helps protect against data exfiltration risks.




## Best practices

We recommend the following best practices for using Cloud FTP:

  * Use a dedicated service account for each user so that you can manage SFTP access separately for each user.

  * Enable automatic retry mechanisms for your SFTP clients, if available. Automatic retries help to prevent file transfer sessions from disconnecting during Cloud FTP infrastructure upgrades.

  * To generate logs for SFTP file transfers, use [Cloud Audit Logs with Cloud Storage](https://docs.cloud.google.com/storage/docs/audit-logging). These logs capture the underlying Cloud Storage API operations that are performed during file transfers, such as creating Cloud Storage objects.

  * To help reduce server uptime costs, consider stopping your servers during periods when no data transfers are expected.




## Limitations

  * Cloud FTP resources aren't indexed in Cloud Asset Inventory.



## What's next

  * [Create an external SFTP server](https://docs.cloud.google.com/cloud-ftp/create-external-sftp-server) that can be accessed over the internet.
  * [Create an internal SFTP server](https://docs.cloud.google.com/cloud-ftp/create-internal-sftp-server) that can be accessed only within your VPC network.
  * [Add users to an SFTP server](https://docs.cloud.google.com/cloud-ftp/add-sftp-users).
  * Connect and transfer data: [connect to an external server](https://docs.cloud.google.com/cloud-ftp/connect-to-external-server) or [connect to an internal server](https://docs.cloud.google.com/cloud-ftp/connect-to-internal-server).
  * [Learn more about Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
