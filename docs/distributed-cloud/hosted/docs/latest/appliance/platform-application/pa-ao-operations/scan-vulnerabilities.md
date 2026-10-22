---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/scan-vulnerabilities/
title: Scan for vulnerabilities \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:04.261600+00:00
---

# Scan for vulnerabilities  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/scan-vulnerabilities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Scan for vulnerabilities Stay organized with collections  Save and categorize content based on your preferences. 

Every Harbor instance created in Harbor-as-a-Service connects to a Trivy vulnerability scanner to help you identify and address security risks in your container images. Trivy is the default scanner in Harbor versions 2.2 and later. Trivy analyzes the contents of your container images, comparing them against known vulnerability databases, like the National Vulnerability Database, to identify potential issues.For more information, see <https://github.com/aquasecurity/trivy>.

## Before you begin

You must configure your environment with the necessary tools and permissions to run vulnerability scans.

### Required prerequisites

  * **Trivy scanner** : You must have enabled Trivy when you installed your Harbor instance by appending the `--with-trivy` installation option. For more information, see the Harbor documentation on running the installer script: <https://goharbor.io/docs/2.12.0/install-config/run-installer-script/>.
  * **Harbor project** : you must have an existing Harbor project. For more information, see [Create Harbor projects](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/create-harbor-projects).



### Required Harbor RBAC roles

Unlike GDC IAM roles, vulnerability scanning requires specific permissions within Harbor's internal role-based access control (RBAC) system. Request the necessary permissions from your administrator. Enforce least privilege access by requesting only the roles required for your specific tasks.

  * **ProjectAdmin** : required to configure scanners, initiate manual vulnerability scans, and update project-level vulnerability settings. The user that creates the Harbor project is automatically assigned the `ProjectAdmin` role for that project, and can assign roles to other users. For more information on all available roles, see the Harbor documentation on User permissions by role: <https://goharbor.io/docs/2.12.0/administration/managing-users/user-permissions-by-role/>.



## Scan individual artifacts in Harbor

Follow these steps to scan individual artifacts in Harbor:

  1. Sign in to the Harbor interface with an account that has the `ProjectAdmin` role.
  2. Go to **Projects** and select a project.
  3. Click the **Scanner** tab. The **Scanner** tab shows the current scanner in use for this project.
  4. Click **Edit** to select a different scanner from the list of scanners that are connected to this Harbor instance, and click **OK**.
  5. Click the **Repositories** tab and select a repository.
  6. For each artifact in the repository, the **Vulnerabilities** column displays the vulnerability scanning status and related information.
  7. Select an artifact, or use the checkbox at the top to select all artifacts in the repository, and click **Scan** to run the vulnerability scan on this artifact.

**Note:** You can start a scan at any time, unless the status is Queued or Scanning.
  8. Hold the pointer over the number of fixable vulnerabilities to see a summary of the vulnerability report.

  9. Click the artifact digest to see a detailed vulnerability report.




For more information, see the Harbor documentation: <https://goharbor.io/docs/2.12.0/administration/vulnerability-scanning/scan-individual-artifact/>.

## Scan all artifacts in Harbor

Follow these steps to scan all of the artifacts in your Harbor instance:

  1. Sign in to the Harbor interface with an account that has the `ProjectAdmin` role.
  2. In the **Administration** menu, click **Interrogation Services**.
  3. To perform a scan of all artifacts in your Harbor instance, select the **Vulnerability** tab and click **Scan now**.

**Note:** **Scan now** becomes unavailable while the scan is in progress.



For more information, see the Harbor documentation: <https://goharbor.io/docs/2.12.0/administration/vulnerability-scanning/scan-all-artifacts/>.

## Configure vulnerability settings in Harbor projects

Integrate vulnerability scanning into your Harbor workflow to proactively manage the security of your containerized applications and protect your organization from potential threats. Configure projects so that images with vulnerabilities cannot be run, and to automatically scan images as soon as they are pushed into the project.

Follow these steps to configure vulnerability settings for a Harbor project:

  1. Sign in to the Harbor interface with an account that has the `ProjectAdmin` role.
  2. Go to **Projects** and select a project.
  3. Click the **Configuration** tab.
  4. To prevent vulnerable images under the project from being pulled, enable the **Prevent vulnerable images from running** checkbox.
  5. Select the severity level of vulnerabilities to prevent images from running.

**Note:** Images cannot be pulled if their level is equal to or higher than the selected level of severity. Harbor does not prevent images with a vulnerability severity of negligible from running.
  6. To activate an immediate vulnerability scan on new images that are pushed to the project, select the **Automatically scan images on push** checkbox.




For more information, see the Harbor documentation: <https://goharbor.io/docs/2.12.0/working-with-projects/project-configuration/>.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
