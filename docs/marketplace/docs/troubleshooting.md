---
url: https://docs.cloud.google.com/marketplace/docs/troubleshooting/
title: Troubleshooting deployments \u00a0|\u00a0 Google Cloud Marketplace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:06.015746+00:00
---

# Troubleshooting deployments  |  Google Cloud Marketplace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Guides ](https://docs.cloud.google.com/marketplace/docs/overview)



Send feedback 

#  Troubleshooting deployments Stay organized with collections  Save and categorize content based on your preferences. 

If a deployment fails, check your instances or deployments to identify the problem. Go to [Cloud Deployment Manager](https://console.cloud.google.com/deployments) to see detailed messages that indicate what caused the deployment to fail.

A deployment might fail to complete successfully for one of the following reasons:

  * Deployment Manager fails to create the necessary resources, such as an instance, disk, or load-balancing forwarding rule.
  * You're missing an Identity and Access Management (IAM) role.
  * The software fails to install and configure.
  * The deployment does not configure the firewall rules correctly on the Virtual Private Cloud (VPC) network.



## Contents

Accessing your deployment  
Deployment Manager failure  
Missing permissions  
Software installation failure  
Network and firewall issues  
Sending email from software deployments  
Using SaaS products with Workforce Identity Federation

### Accessing your deployment

You can return to your solutions by revisiting the [Cloud Marketplace](https://console.cloud.google.com/marketplace). Go to the solution page where you'll see a menu that shows your previous deployments. For services, you can update the service options directly from that page.

Otherwise, if your deployment is running a VM instance, you can go to [Deployment Manager](https://console.cloud.google.com/deployments) in the Google Cloud console. From there, you can manage your deployment and view of all the Google Cloud resources that make up the deployment.

### Deployment Manager failure

Sometimes your project might not have enough CPU quota to create the deployment resources. Check the remaining quota for your project at [Compute Engine Quotas](https://console.cloud.google.com/iam-admin/quotas), and request additional quota if necessary. Then try to deploy the software package again.

### Missing permissions

You might not have the `roles/deploymentmanager.editor` role applied to your account for the project. Review [Access control for users](https://docs.cloud.google.com/deployment-manager/docs/access-control#roles) to ensure that your user account is added to the correct project and that you have the correct roles applied to the account.

### Software installation failure

Most solutions provide logging for your instances so you can troubleshoot software installation failures. If your deployment creates all of the requested resources but you see a deployment error message in [Deployment Manager](https://console.cloud.google.com/deployments), it's possible that the software failed to install or configure successfully. Connect to the instances in the deployment and check the logs to identify the issue.

Each entry in the log corresponds to the sequenced command that was executed on that instance. Execution terminates on the first command to exit with a non-zero exit code. The specific cause of failure will be typically be found at the end of the error log.

### Network and firewall issues

If your software deployment hosts content on an [external IP address](https://docs.cloud.google.com/compute/docs/ip-addresses#externaladdresses), the software deployment automatically configures [firewall](https://docs.cloud.google.com/vpc/docs/firewalls) rules on the network where your deployment runs. For example, [Wordpress](https://docs.cloud.google.com/marketplace/solution/bitnami-launchpad/wordpress) deployments open ports so that you can access the web console and display content over HTTP and HTTPS. If the firewall configuration fails, you might receive a HTTP 404 error when you try to connect to the web console on the external IP address.

If you need to configure the firewall manually or open additional ports for other services that run on your instances, [add firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules) to the VPC network that your deployments run on.

### Sending email from software deployments

Some software packages try to send email over specific ports. However, Compute Engine does not allow outbound connections on port 25. To send email from the instances that host your software packages, you must follow the tutorial on [sending mail](https://docs.cloud.google.com/compute/docs/tutorials/sending-mail).

### Using SaaS products with Workforce Identity Federation

Some software as a service (SaaS) products in Cloud Marketplace don't support [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) (also known as bring your own identity, or BYOID). If you sign in to the Google Cloud console using a federated identity and can't configure or use a SaaS product, you must [create a Google Account](https://support.google.com/accounts/answer/27441) that links to your existing email address. Then, sign in to that Google Account to configure and use the SaaS product. For step-by-step instructions, see [Use SaaS products with Workforce Identity Federation](https://docs.cloud.google.com/marketplace/docs/get-products#workforce-identity-federation).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
