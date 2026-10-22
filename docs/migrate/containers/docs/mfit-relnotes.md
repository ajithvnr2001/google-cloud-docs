---
url: https://docs.cloud.google.com/migrate/containers/docs/mfit-relnotes/
title: Release notes \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:37.245825+00:00
---

# Release notes  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/mfit-relnotes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Resources ](https://docs.cloud.google.com/migrate/containers/docs/resources)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Release notes

## Migrate Fit Assessment is now Migration Center discovery client CLI

The Fit Assessment tool or `mfit` has now been renamed to Migration Center discovery client CLI or `mcdc` CLI. For the latest version, see the [`mcdc` CLI documentation](https://docs.cloud.google.com/migration-center/docs/discovery-client-cli-overview).

## Updates for version 1.15.3

On August 16, 2023, we released Migrate Fit Assessment 1.15.3, which lets you upgrade to Migration Center discovery client CLI.

Alternatively, to upgrade to the `mcdc` CLI directly, you can [download the `mcdc` CLI and collection scripts](https://docs.cloud.google.com/migration-center/docs/download-collector-cli) again in the same directories where you installed the previous version of `mfit`.

For more information, see the [`mcdc` CLI overview](https://docs.cloud.google.com/migration-center/docs/discovery-client-cli-overview).

## Updates for version 1.15.2

On July 4, 2023, we released Migrate Fit Assessment 1.15.2, which includes bug fixes to the HTML Fit Assessment reports.

## Updates for version 1.15.1

On June 27, 2023, we released Migrate Fit Assessment 1.15.1, which includes security improvements and bug fixes.

## Updates for version 1.15.0

On June 19, 2023, we released Migrate Fit Assessment 1.15.0.

### Features

#### Fit Assessment of WebSphere applications

The Fit Assessment tool can now assess WebSphere applications fit for containerization to Google Kubernetes Engine (GKE), GKE Enterprise clusters, or Cloud Run platform.

Added the following rules for WebSphere Application Server Fit Assessment:

  * A10N-APP-1 - matched when an external database is used
  * A10N-APP-2 - matched when an external web server is used
  * A10N-STO-1 - matched when network mounts are found
  * A10N-STO-2 - matched when NFS is exporting a local directory



For more information about WebSphere application containerization, see the [Migrate to Containers documentation](https://docs.cloud.google.com/migrate/containers/docs/getting-started).

### Changes

#### Enhanced Microsoft Excel workbook reports

The Microsoft Excel workbook (XLSX) report now has a new **Contents** worksheet that provides information about report generation and assessment. This worksheet also contains a table of contents that lists all the worksheets in your report.

The **App Components** worksheet has been modified to better reflect the components' running state, version, and containerization fit information.

![Enhanced Microsoft Excel workbook reports](https://docs.cloud.google.com/static/migrate/containers/docs/images/enhanced_xlsx_report.png)

For more information about the XLSX report, see [Generate Fit Assessment report](https://docs.cloud.google.com/migrate/containers/docs/mfit-reports#xlsx).

### Fixed

#### WordPress journey is now assessed with all target platforms

When you generate a Fit Assessment report using `mfit`, you can [specify the target platform](https://docs.cloud.google.com/migrate/containers/docs/mfit-reports#specify_the_target_platform). By default, the `--target-platform` flag is set to `all` and all possible journeys are assessed.

In the previous version, if you changed the value of the `--target-platform` flag to anything other than `all`, then the WordPress journey was not assessed. Now, the WordPress journey is assessed for all target platforms and is included in the generated report.

## Updates for version 1.14.4

On May 2, 2023, we released Migrate Fit Assessment 1.14.4.

### Features

#### Support for WordPress

The Fit Assessment tool now detects and assesses WordPress applications in Apache WebHosts.

#### Support for AWS collection and assessment

  * **Inventory collection** : The Fit Assessment tool now supports AWS inventory collection via the `mfit discover aws` command.
  * **Guest collection** : The collection scripts collect more information about AWS when run on an AWS virtual machine instance (VM).

To learn how to perform a guest collection against AWS VMs, see [Collect mfit guest data from EC2 VMs](https://docs.cloud.google.com/migrate/containers/docs/mfit-aws-collection-tutorial).

  * **Fit Assessment** : New rules have been added specifically for VMs migrated from AWS.




#### Generate large reports in a Microsoft Excel workbook

The Fit Assessment tool can now generate a report in a Microsoft Excel workbook file (XLSX) format. The XLSX report can handle large amounts of data, and therefore is suitable for cases where there are higher number of VMs which the HTML report might not be able to handle.

To generate a report in an XLSX file, run the following command:
    
    
    ./mfit report --format xlsx >  REPORT_NAME.xlsx
    

#### Prevent overwriting later collections on import

When importing an archive using `mfit discover import`, if that archive overwrites an archive collected at a later date for the same machine, the import fails unless you provide the `--force` flag.

### Fixed

#### Empty fingerprints are now ignored

The Fit Assessment tool detects fingerprints for each VM. If two collections contain a VM with the same fingerprints, then the tool knows that it is the same VM.

This fixes an issue where VMs with only empty fingerprints are imported successfully, but don't appear in reports. Now in such cases, the collection fails and displays a warning instead.

## Updates for version 1.14.3

On March 16, 2023, we released Migrate Fit Assessment 1.14.3.

### Features

#### New design for Fit Assessment detailed report

In this release we have introduced new report design with details about VM application components like Tomcat, Windows IIS, JBoss, and Websphere applications. The new report comes with an improved text-based filtering along with a detailed inventory of application components identified on VM.

![Detailed assessment report Virtual Machine list](https://docs.cloud.google.com/static/migrate/containers/docs/images/detailed_mfit_report.png)

To generate an HTML file in the old format, use the flag `--html-v0`:

`mfit report --format html --full --html-v0`

#### Windows IIS application Fit Assessment

We have introduced a detailed Fit Assessment of Windows IIS applications which lets you view the fit for modernization to Windows IIS application containers.

![Windows IIS Application assessment view](https://docs.cloud.google.com/static/migrate/containers/docs/images/iis_application_assessment_view.png)

## Updates for version 1.14.2

On March 15, 2023, we released Migrate Fit Assessment 1.14.2 which includes bug fixes.

## Updates for version 1.14.1

On February 19, 2023, we released Migrate Fit Assessment 1.14.1.

### Features

#### Manual recovery from upgrade failure

We added a manual recovery option that lets you [manually recover](https://docs.cloud.google.com/migrate/containers/docs/troubleshooting/mfit-issues-after-upgrade) from a rare case of failure which causes loss of data during the upgrade process. After upgrading `mfit`, when you run the latest version, if you see an error which indicates that the database upgrade failed, you can issue the following command:
    
    
    ./mfit discover recover-db
    

This command reverts the internal data store to its condition before the upgrade and preserves the information collected.

**Note:** You must use this command only if after an upgrade, when you run the latest version, you see an error which indicates that that the database upgrade failed, or if Customer Support recommends you to use the command.

### Changes

#### Enhanced JBoss applications Fit Assessment

Added the following rules for JBoss applications Fit Assessment:

  * A8N-APP-4 - matched when the source Java version is newer than the expected target image Java version.
  * A8N-APP-5 - matched when an external database is used.
  * A8N-APP-6 - matched when an external web server is used.
  * A8N-FIT-1 - matched when VM data exists.
  * A8N-STO-1 - matched when network mounts are found.
  * N-STO-2 - matched when NFS is exporting local directory.



#### Updated reports texts

Updated reports texts to provide more information on the GKE Enterprise VM Runtime journey.

## Updates for version 1.14.0

On January 17, 2023, we released Migrate Fit Assessment 1.14.0.

### Features

#### Report applications fit to Google containers platforms

Added a new report category to help you focus assessment report on applications fit for Google containers platforms—GKE Enterprise, GKE, Autopilot and Cloud Run. When generating a report you can ask to include only assessment to containers platforms using the following command:

`./mfit report --format html --target-platform containers --full > REPORT_NAME.html`

#### Fit assessment of JBoss and Apache 2 applications

The Migrate Fit Assessment tool can assess JBoss and Apache 2 applications fit for containerization to GKE, GKE Enterprise, and Cloud Run platforms. To learn more about JBoss and Apache 2 containerization, see the Migrate to Containers 1.14.0 [release notes](https://docs.cloud.google.com/migrate/containers/docs/release-notes#December_06_2022).

#### Guest level collection without the need for root permission

Updated the Migrate Fit Assessment collection scripts for Linux to enable running them through `sudo`. The added capability allows you to run Linux guest collection script with `sudo` and without the need for a root user.

The Linux guest collection script will attempt to run using passwordless `sudo`. This change takes effect in all Linux guest collection methods, such as:

  * `mfit discover ssh`
  * `mfit discover vsphere guest`
  * `mfit discover vsphere guest all`
  * When running the collection script manually and using `mfit discover import`.



If a passwordless sudoer credentials are supplied, the Linux guest collection script uses `sudo`, resulting in fuller, and more reliable collection results.

Note that sudoer permissions that require a password prompt are not supported for this feature. In this case, the script runs with the permissions of the original user.

#### New detailed assessment report added under experimental flag

A new design of the detailed assessment report is now available running the command `./mfit report --format html --full > REPORT_NAME.html --experimental`.

The new design introduces enhanced filtering and text-based search to help you locate candidate workloads for modernization.

![Detailed assessment report](https://docs.cloud.google.com/static/migrate/containers/docs/images/detailed-assessment-report-design.png)

### Changes

#### Deprecation of `--user` flag in Linux collection script

Previously, running with a non-root user required supplying a `--user` flag to the Linux guest collection script. This is no longer required, and the `--user` flag is ignored and entered a deprecation period.

### Fixed

#### Renamed the `discover ssh connect-timeout` flag

Renamed the flag called `--timeout` in the `discover ssh` command to `--connect-timeout`. The flag can be used with the native SSH client. The new name removes the overlap with the global `--timeout` flag.

#### Failure when providing embedded SSH client with no authentication

Fixed failure in case the `discover ssh` command without authentication parameters. When using the embedded SSH client and providing no identity file and no password or an empty one, panic occurred instead of stating unsuccessful authentication.

#### Error when failing to create a tar file in Linux guest collection

If the collection script fails to create the required tar file, it throws an error. Previously, a failure to create a tar in the Linux guest collection script was ignored. From this version, an error message is displayed, and the script exits with status code 1.

#### Saving guest collection tar file to different location

To provide a different location for saving the collection tar file, you can use the `--output` flag to save it to the specified path. Previously, arguments supplied after the `--output` flag were ignored due to parsing issues.

## Updates for version 1.13.1

On November 3, 2022 we released Migrate Fit Assessment 1.13.1.

### Changes

#### Deprecated JSON v0 reports

We introduced changes in the structure of the generated JSON file to expand the scope of the assessment details report. Starting with release 1.13.1, the default JSON output will use the file structure version v1. To generate a JSON file in the previous version, apply the flag `--json-v0`.
    
    
    ./mfit report --format json --json-v0  <file.json>
    

The v0 JSON report is now deprecated. In Q1, 2023, v0 JSON report format will reach end of life. New releases of mFit will not support v0 JSON report generation.

### Fixed

#### Decreased database file size

The SQLite database used by mFit has been optimized to reduce the disk space it consumes.

#### Fixed `too many SQL parameters` error

Fixed an error that might occur when running `discover ls` or `report` commands on an mFit installation with a very large number of discovered assets.

## Updates for version 1.13.0

On October 18, 2022 we released Migrate Fit Assessment 1.13.0.

### Changes

#### Enhanced vSphere guest collection at scale with scope option

You can now perform guest collection for a subset of VMs by applying a scope via the `--path` flag.
    
    
    mfit discover vsphere guest all --url https://VSPHERE_URL --path dc-1/host/esx-1
    

#### Enhanced error reporting in RVTools import

RVTools discovery now identifies unsupported file formats and provides you with an error message on unsupported versions.

### Fixed

#### Fixed RAM and storage size conversions in reports

Adjusted unit measures in reports to GiB instead of GB, inline with the internal units of measure.

## Updates for version 1.12.1

### Features

#### Perform guest collection at scale

You can now perform guest collections in parallel for all VMs managed by a single VMware vCenter. This comes in handy for collecting information from large quantities of VMs having the same credentials.

To collect guest-level information from multiple VMs, run:
    
    
    mfit discover vsphere guest all --url https://VSPHERE_URL
    

### Changes

#### Update to Cloud Run fit assessment

Cloud Run fit assessment has been updated to accommodate improvements done in Cloud Run resources limitations. Previous values were 4 CPUs, 16 GB of memory, and the new limits are 8 CPUs, 32 GB of memory. See details at [Cloud Run Quotas and Limits](https://docs.cloud.google.com/run/quotas).

#### Unify report and assess commands

We simplified the process of assessing data and generating a report, by combining the two commands into one. In previous releases, you needed to first perform an assessment (`$ mfit assess`), and then you could generate a report on the collected data. Now you can run the report command, and the assessment is done automatically. The `report` command now has an optional `--target-platform` flag.

The available options are: `gcp`, `anthos`, `anthosbm` and `all`. Each option specifies a different set of journeys to evaluate. If you don't specify a target platform, all journeys are assessed.

  * `gcp` assesses shift journeys to Compute Engine, Google Cloud VMware Engine, and containerization journeys to Google Kubernetes Engine, Google Kubernetes Engine Autopilot and Cloud Run.

  * `anthos` assesses shift to Google Distributed Cloud and containerization journeys to Google Kubernetes Engine and Cloud Run.

  * `anthosbm` is equivalent to `anthos`.

  * `all` assesses all possible journeys.




With this change, the `report sample` command replaces the now deprecated `assess sample` command.

**Note:** Both the `assess` and `assess sample` commands continue functioning, with a deprecation notice for backwards compatibility.

### Fixed

#### Fix mentions of private / public previews in html reports

In previous releases, any containerize target is shown as private preview. Now only Tomcat targets are shown as public preview.

#### mfit collection scripts cleanup temporary directory

In previous releases, collection scripts would create a temp directory on the guest, but didn't remove it. In the latest release, collection scripts automatically remove the temp directory.

#### Fix wrong RAM size conversions

We corrected a conversion where base 2 was mixed base 10 (MiB vs MB) and resulted in inaccurate conversions.

#### Windows guest collection

We fall back to non-WMI based collection methods for some data to avoid sporadic failures.

## Updates for version 1.12.0

### Changes

  * Assessment of VMs to Google Distributed Cloud _Attach_ mode was removed from the executive report and detailed assessment report.
  * Modified the default assessment of Google Distributed Cloud as part of the executive report. In order to assess VMs for Google Distributed Cloud you must run the command: `mfit assess --target-platform anthosbm`
  * You'll see a warning if you issue a CLI command that attempts to assess an empty DB.
  * Updated the default behavior of `assess –target-platform` flag to use the `all` option.



### Fixed

  * Fixed a bug in the executive summary section which caused inaccurate counts of high CPU and high memory VMs.
  * Improved the sorting on the fit assessment full report, so that results sorted by rule ID are correctly sorted.
  * Improved the fit assessment full report middle chart sorting so rows sorted from highest to lowest aggregated fit score.
  * Fixed an incorrect regex in the Linux collect script affecting Tomcat assessment.
  * Fixed a bug that prevented correct detection of centos OS version name and caused empty OS names on fit assessment full report.
  * Fixed a bug which caused duplicated VM information when VMs were discovered multiple times.
  * Improved handling of partially collected VM information which may lead to inconsistent data. Warn users when collecting an asset with the inconsistent VM information and skip storing the VM data.



## Updates for version 1.11.3

### Features

  * Fit assessment cost analysis - Use this new section on the fit assessment report to estimate the cost of running modernized workloads in Google Cloud. The report groups your VMs by modernization strategy and shows the estimated costs by strategy, as well as an estimated total cost. Cost analysis will help you decide whether a low-effort or high modernization strategy suits your needs. To view the cost benefits of a modernization journey, you need to run the collection scripts on an assessed VM. For more detailed instructions, see [Discover and collect data](https://docs.cloud.google.com/migrate/containers/docs/fit-assessment#discovery-collect).

  * Improved recommendation listing for fit journeys - The full fit assessment report now sorts journeys based on their fit and the sum severity of all failed conditions. The first journey in the list has the highest recommendation, with journeys of higher failure severity ranking lower.




### Fixed

  * Fixed an issue where features were only calculated when running the `discover` command.



## Updates for version 1.11.2

### Features

  * Report filter – A new filter was added on the fit assessment detailed report to enable filtering VMs which have fit for specific journeys. Once the filter is applied, only VMs which have a fit for the selected journey are listed.

  * StratoZone – Added mFIT collection script to StratoZone StratoProbe collector 5.0.2.1. The information required to make an assessment is collected by StratoProbe collector, and is made available for assessment for users that have deployed StratoProbe.




### Fixed

  * Removed the fit score column from full report table for better readability.

  * Updated fit assessment summary report to resolve mismatch of percentage presented on the summary part and guidance part of the report.

  * Changed the severity information to use text instead of numeric value on the summary report.

  * Fixed wrong identification of OS which was marked as Other OS on fit assessment reports.




### Changes

  * Added the option to purge the fit assessment local database by using the command `mfit discover purge-db`

  * Added information on the existence of VMware tools in the CSV report. To allow users to automate guest level data collection through automated scripts.

  * Added a (`--minimal`) flag to Windows collection script which helps to minimize the amount of collected information and provide only the specific information required for assessing containerization to Windows IIS applications.

  * Added the option to manually check for newer versions of the fit assessment tool by using the command `mfit version --check`.




## Updates for version 1.11.1

  * Bug fixes.



## Updates for version 1.11.0

  * Executive summary report – This release includes a new type of report, and a change in the default behavior. The new executive summary report gives you an overview of your modernization journeys. At a high level, the report sorts your modernization journeys into two different buckets: low effort versus high modernization. Looking at these two extremes, and the benefits and effort required, should help you make key business decisions. In addition, there are subsections of the report that show the fit and technical limitations of migrating VMs (lift and shift analysis), refactoring to containers, and on-premises VM modernization (via shifting or attaching VMs to Google Distributed Cloud). The default report type is the new executive summary report; in previous releases, the default report was a detailed report.
  * Assess workloads for migrating to Google Cloud VMware Engine – The fit assessment tool added new assessment capability to assess workloads for lift and shift to Google Cloud VMware Engine.



## Updates for version 1.10.0

The fit assessment tool for version 1.10.0 adds new functionality, including:

  * [Support for Autopilot, Cloud Run, and Compute Engine assessment](https://docs.cloud.google.com/migrate/containers/docs/mfit-about#modernization_journeys)
  * [Tomcat rules added for fit assessment](https://docs.cloud.google.com/migrate/containers/docs/fit-assessment-rules)
  * [Ability to acquire vSphere data from RVTools export](https://docs.cloud.google.com/migrate/containers/docs/mfit-data-discovery#discovery-collect)
  * [Automatic version check](https://docs.cloud.google.com/migrate/containers/docs/mfit-install#automatic_version_check)
  * [Fit assessment tool configuration](https://docs.cloud.google.com/migrate/containers/docs/mfit-tool-config)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
