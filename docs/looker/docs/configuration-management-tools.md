---
url: https://docs.cloud.google.com/looker/docs/configuration-management-tools/
title: Configuration management tools \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:00:39.865052+00:00
---

# Configuration management tools  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/configuration-management-tools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Configuration management tools Stay organized with collections  Save and categorize content based on your preferences. 

Configuration management tools can provide simplified deployment of a customer-hosted Looker instance.

## Example Ansible role for Looker deployment

Looker provides an example Ansible role on our [Looker GitHub repository](https://github.com/looker/customer-scripts). This example is based on roles that Looker uses internally to deploy the Looker application to EC2 instances. It is provided as an example and is not supported by Looker Support.

### Notes about this Ansible role

  * The included `init` script is written for Ubuntu, so it might need to be modified for other Linux distributions.

  * The scripts assume that Looker is being run by user **looker** in group **looker** , which is the recommended configuration. Modify `defaults/main.yml` and `files/looker_init` if you want to change this.

  * `templates/looker.j2` sets the memory based on the EC2 instance type, using an array in `defaults.main.yml`. You will likely need to change this. The default is `2800m`.

  * `templates/looker.j2` shows the arguments to use for JMX monitoring of Looker if desired.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
