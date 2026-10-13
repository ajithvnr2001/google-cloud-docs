---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/upgrade-python-versions/
title: Upgrade the Python version \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:26:09.074683+00:00
---

# Upgrade the Python version  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/upgrade-python-versions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Upgrade the Python version 

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document explains how to upgrade certified and custom integrations, remote agents and connectors in the Content Hub to the latest Python version. As older Python versions are deprecated, integrations using unsupported versions must be updated to facilitate continued operation. After you update the integration to the latest Python version, you must upgrade each connector as well.

If your certified or custom integration code uses a deprecated Python version, you must manually update it. Use **IDE Staging** mode to update integration code without impacting production environments.

**Note:** After a Python version reaches end of life, integrations using it will stop running on the platform. For more information and deprecation dates, refer to [ Feature deprecations](https://docs.cloud.google.com/chronicle/docs/deprecations).**Note:** Updating code in staging does not automatically update production connectors or jobs. You must upgrade each connector and job individually after deploying new code to production.

## Before you begin

Make sure that your permission group includes **All Environments** access. For more information, refer to [ Work with permission groups](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/permissions/working-with-permission-groups). 

## Upgrade integrations

  1. Go to **Response > IDE**; if any integrations are using outdated Python versions, a banner appears in the IDE, Content Hub, and Playbooks pages.
  2. Click **View Integration** to see a list of integrations.
  3. Click **Close** to dismiss the banner.
  4. In the integrations list, select the integration to upgrade.
  5. Click  more_vert  **More > Push to staging**. This step creates a copy of the integration for testing. 
  6. Click the **Production** toggle from **Production** to **Staging**.
  7. On the same integration, click  more_vert  **More > Configure instance**.
  8. Continue with either of the following upgrade paths:
     * Upgrade certified integrations to the latest Python version
     * Upgrade custom integrations to the latest Python version



For information on how to configure instances, read [ Configure instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances). This creates a staging instance that does not appear in the main configuration list. Only one staging instance is allowed per integration.

Make sure to  update each connector as well.

## Upgrade certified integrations to the latest Python version

  1. In **Response > IDE**, click **Upgrade** to switch the integration and its dependencies to the latest Python version.
  2. If this integration includes custom elements, update their code accordingly.
  3. In the **Testing** section, enter the required parameters, including the staging instance that you configured earlier. 
  4. Verify that there are no errors in the **Debug Output**.
  5. On the same integration, click  more_vert **More > Push to production**.
  6. Click the **Production** toggle back to **Production** mode, if needed.



## Upgrade custom integrations to the latest Python version

Follow this procedure to update the **Script Dependencies** in custom integrations.

  1. Click  more_vert  **More** > **Configure custom integration**.
  2. In the dialog **Running on Python** field, change the **Running on Python** field to the latest Python version (for example, **Python 3.11**).
  3. Under **Script Dependencies** , copy and save the dependency names locally.
  4. Delete these dependencies from the list, and click **Save**.
  5. Copy each of the dependency names (without the version or target OS) from your file to the **Libraries** field and click **Add**. For example, change `requests-2.27.1-none-any.whl` to `requests` and then add it to the **Libraries** field. The platform downloads each dependency with the latest Python version already configured. 



## Upgrade remote agents 

If you're working with Remote Agents, you need to upgrade both the agent and its integrations, running on them as follows: 

  1. Go to **SOAR Settings > Advanced > Remote Agents**.
  2. Click **Update Available**. 
  3. Upgrade the agent using the appropriate method:
     * Docker: Follow [ Perform a major upgrade of a Docker image](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-agent-docker-image).
     * Red Hat (RHEL): See [ Perform a major upgrade using installer for RHEL](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-agent-requirements-for-rhel).
     * CentOS: See [ Perform a major upgrade using installer for CentOS](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-agent-requirements-for-centos).
  4. After upgrading the agent, follow the integration upgrade steps described in this document.



##  Upgrade connectors 

You need to upgrade connectors, both custom and commercial, to the latest Python versions. 

  1. Go to **SOAR Settings > Ingestion > Connectors**.
  2. Click the yellow **Update** button on the top of the screen. 
  3. Click **Save**. 



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
