---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-use-web-security-scanner/
title: Use Web Security Scanner \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:20.241637+00:00
---

# Use Web Security Scanner  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-use-web-security-scanner/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Use Web Security Scanner Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page shows you how to use Web Security Scanner managed scan features and review findings in the Google Cloud console. Examples of Web Security Scanner findings are also shown.

Web Security Scanner is a built-in service for Security Command Center that identifies common security vulnerabilities in your App Engine, Google Kubernetes Engine (GKE), and Compute Engine web applications. To view Web Security Scanner findings, it must be enabled in Security Command Center [Services](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#enable-service) settings.

**Note:** Attack path simulations don't support Web Security Scanner findings, so the findings don't get [attack exposure scores or attack paths](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn).

**Caution** : Web Security Scanner can adversely affect the reliability of some applications and might not be suitable for use in a production environment. Also, Web Security Scanner cannot detect all possible vulnerabilities in an application. For more information, see the following:

  * [Usage caveats](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview#usage_caveats)
  * [Best practices](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview#best_practices)



Learn more about [how Web Security Scanner works](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview).

## Reviewing findings

Web Security Scanner's [managed scan](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview#managed_scans) feature automatically configures and schedules scans for each of your in-scope projects. Web Security Scanner scans can take up to 24 hours to start after the service is enabled and run weekly after the first scan. Findings are viewed in Security Command Center.

Managed scans are separate from Web Security Scanner custom scans. Custom scans are more thorough than default managed scans and provide granular information about application vulnerability findings. For information about custom scans, see the [Web Security Scanner custom scan guide](https://docs.cloud.google.com/security-command-center/docs/how-to-web-security-scanner-custom-scans).

### Review findings in the console

The IAM roles for Security Command Center can be granted at the organization, folder, or project level. Your ability to view, edit, create, or update findings, assets, and security sources depends on the level that you're granted access for. To learn more about Security Command Center roles, see [Access control](https://docs.cloud.google.com/security-command-center/docs/access-control). 

To review Web Security Scanner findings in Security Command Center, follow these steps:

If [data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support) is enabled for your organization, you must access the page using the jurisdictional console. For more information, see [Use the console with data residency enabled](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center#console-jconsole).

  1. In the Google Cloud console, go to the **Findings** page of Security Command Center.

[Go to Findings](https://console.cloud.google.com/security/command-center/findingsv2)

  2. Select your Google Cloud project or organization.
  3. In the **Quick filters** section, in the **Source display name** subsection, select **Web Security Scanner**. The findings query results are updated to show only the findings from this source. 
  4. To view the details of a specific finding, click the finding name in the **Category** column. The details panel for the finding opens and displays the **Summary** tab. 
  5. On the **Summary** tab, review the details of the finding, including information about what was detected, the affected resource, and—if available—steps that you can take to remediate the finding. 
  6. Optional: To view the full JSON definition of the finding, click the **JSON** tab.



### View all findings associated with a specific URL

A scan can produce findings from several base URLs. To display all findings associated with a given URL in a scan, follow these steps:

  1. Open the finding and view its JSON definition.
  2. Copy the URL next to **`externalUri`**.
  3. Close the finding detail pane.
  4. In the **Query editor** , enter the following query:
         
         externalUri:"AFFECTED_URI"
         

Replace AFFECTED_URI with the URL you previously copied.




Security Command Center displays all the findings that are associated with the URL.

### Example findings

Example Web Security Scanner managed scan findings include the following:

**Table A.** Web Security Scanner managed scan finding types  Vulnerability | Description  
---|---  
Mixed-content |  A page that was served over HTTPS also serves resources over HTTP. A man-in-the-middle attacker could tamper with the HTTP resource and gain full access to the website that loads the resource or monitor users' actions.   
Clear text password |  An application returns sensitive content with an invalid content type, or without an `X-Content-Type-Options: nosniff` header.   
Outdated Library |  The version of an included library is known to contain a security issue. The scanner checks the version of library in use against a known list of vulnerable libraries. False positives are possible if the version detection fails or if the library has been manually patched. Web Security Scanner identifies some vulnerable versions of the following popular libraries:

  * jQuery, for example: [CVE-2011-4969](https://nvd.nist.gov/vuln/detail/CVE-2011-4969)
  * jQuery Mobile, for example: [known XSS vulnerability](https://github.com/jquery-archive/jquery-mobile/issues/4787)
  * AngularJS, for example: [XSS through SVG vulnerability](https://vulnerabledoma.in/ngSanitize1.6.8_bypass.html)

This list is updated periodically with new libraries and updated vulnerabilities as applicable.  
  
Learn more about [using Security Command Center in the Google Cloud console](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center).

## Filtering findings in the Google Cloud console

A large organization might have many vulnerability findings across their deployment to review, triage, and track. By using filters that are available on the Security Command Center **Vulnerabilities** and **Findings** pages in the Google Cloud console, you can focus on the highest severity vulnerabilities across your organization, and review vulnerabilities by asset type, project, and more.

For more information about filtering vulnerability findings, see [Filter vulnerability findings in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/filter-vulnerability-findings).

## Mute findings

To control the volume of findings in Security Command Center, you can manually or programmatically mute individual findings or create mute rules that automatically mute current _and_ future findings based on filters you define.

Muted findings are hidden and silenced, but continue to be logged for audit and compliance purposes. You can view muted findings or unmute them at any time. To learn more, see [Mute findings in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/how-to-mute-findings).

## Scan configurations

If Web Security Scanner is given access credentials, it will perform all actions using that level of access. To reduce risk to your production resources, and to catch vulnerabilities before they reach production, it is recommended that you run scans in development, testing, staging, or quality assurance environments.

Scanning production resources is useful because even small changes to resources between testing and production can introduce vulnerabilities. However, you might want to use limit access during production scans. See [Best practices](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview#best_practices) for more information.

To review managed scan configurations and manually start scans, use the Google Cloud console.

To see the managed scan configuration for a project:

  1. Go to the Web Security Scanner page in the Google Cloud console.   
[Go to the Web Security Scanner page](https://console.cloud.google.com/security/web-scanner)
  2. Select a project. A page appears with a list of your managed and custom scans.
  3. Under **Scan configs** , click **`managed_scan`**. The page that appears shows the results of the most recent managed scan, including scan status, URLs crawled, and vulnerabilities found. Use the drop-down list to see the results of previous scans.



Web Security Scanner administers and maintains managed scans, so you cannot modify scan configurations. Managed scans can only be edited or deleted in Security Command Center, as discussed in Disabling managed scans.

## Static IP address ranges for managed scans

When Web Security Scanner is enabled in Security Command Center, managed scans start automatically using static IP addresses in the following ranges:

  * `8.34.210.32/27`
  * `34.66.18.0/26`
  * `34.66.114.64/26`
  * `34.68.34.64/27`



### On-demand scans

Managed scans run automatically on a set schedule. However, you can use the Web Security Scanner page to run on-demand managed scans:

  1. Go to the Web Security Scanner page in the Google Cloud console.   
[Go to the Web Security Scanner page](https://console.cloud.google.com/security/web-scanner)
  2. Select a project. A page appears with a list of your managed and custom scans.
  3. Under **Scan configs** , click **`managed_scan`**.
  4. On the next page, click **Run** at the top of the page; or
  5. Click **Run scan again** in the **Results** tab.



The scan begins and findings are updated in Security Command Center when completed. On-demand managed scans are useful when you want to capture findings for new or updated projects in between scheduled scans. On-demand scans don't impact the timing of scheduled weekly scans.

You can find more information about the scan in the project [logs page](https://console.cloud.google.com/project/_/logs).

## Disable managed scans

To disable managed scans for an organization, folder, or project, disable the Web Security Scanner service in Security Command Center. For instructions, see [Enable or disable a built-in service](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#enable-service).

You can continue to use Web Security Scanner as a standalone product to [perform custom scans](https://docs.cloud.google.com/security-command-center/docs/how-to-web-security-scanner-custom-scans). Consider the following:

  * You must configure and manage [custom scans](https://docs.cloud.google.com/security-command-center/docs/how-to-web-security-scanner-custom-scans) for each project that you want to scan.
  * Managed scan configurations are archived. Existing managed scan findings remain viewable in the Google Cloud console.
  * Managed scans are only available in Security Command Center, so managed scan configurations and existing managed scan findings are removed from the standalone Web Security Scanner page.



If you re-enable Web Security Scanner in Security Command Center, managed scan configurations and findings reappear on the Web Security Scanner page. Generally, if new scans find the same vulnerabilities, existing findings are updated. If your application or website changed substantially since the last scan, new findings might be created.

## What's next

  * Learn about [remediating Web Security Scanner findings](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
