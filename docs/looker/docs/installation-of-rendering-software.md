---
url: https://docs.cloud.google.com/looker/docs/installation-of-rendering-software/
title: Customer-hosted installation of rendering software \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:13:21.402268+00:00
---

# Customer-hosted installation of rendering software  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/installation-of-rendering-software/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Customer-hosted installation of rendering software Stay organized with collections  Save and categorize content based on your preferences. 

Looker requires rendering software called Chromium to send or download data in image-based formats — HTML and PNG or PDF files — and to use features such as [Paper size](https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards#paper_size) and [Expand tables](https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards#expand_tables_to_show_all_rows). This page explains how to install rendering software on a customer-hosted instance of Looker.

**Note:** Chromium is already installed for Looker-hosted instances.

Chromium rendering waits for all resources that have been requested by the page to be completed before it sends the "finished" signal that prompts Looker to produce the rendered content. Because of the number and frequency of these resource requests, some networks can falsely flag the requests as malicious, causing them to drop, which will delay your rendered jobs.

The Chromium Project is an open source project that was started by Google to share the non-proprietary parts of Google Chrome.

## Before you begin

Before you install Chromium, learn more about the following topics:

  * Chromium installation requirements and prerequisites
  * Things to know about installing Chromium on specific distributions
  * Install font packages



### Chromium installation requirements and prerequisites

This page provides example instructions for installing Chromium that are independent from a distribution type. You can also [download Chromium](https://chromium.googlesource.com/chromium/src/+/main/docs/linux/build_instructions.md) and then follow the remaining installation instructions on this page.

To run Chromium on a Looker instance, Chromium 97, Chromium 109, or Chromium 114 are required. Chromium must be installed into an executable path on the machine that hosts the Looker instance. The Looker application needs to access Chromium either by using the `chromium` command or by using a custom path that is set with the `CHROMIUM_PATH` [environment variable(#optional_chromium_environment_variables).

If you are installing Chromium on a clustered Looker installation, the Chromium version on each node must be fully identical. Even minor differences, such as different build numbers, can interfere with Looker's rendering capabilities.

### Things to know about installing Chromium on specific distributions

Looker supports release versions of all major enterprise Linux distributions, including Ubuntu (LTS releases), Debian 9+, RedHat Enterprise Linux (RHEL) 7+, CentOS 7+, and Amazon Linux.

For Ubuntu installations, you must install the Chromium web browser and then set an alias so that the Looker application can find the installation.

For Debian installations, Chromium requires Debian 9 (stretch) or later. If your Looker instance uses Docker with a bare-bones Debian installation, install [procps](https://gitlab.com/procps-ng/procps) and ensure that you are not running as root.

### Install font packages

A Microsoft OpenType font (OTF) package must be installed on the system for Chromium to start. OTF packages use `.otf` file extensions. You can download any OTF package, such as this [OTF package from Google Fonts](https://fonts.google.com).

If your data contains non-English characters, you must also install [the Google Noto Fonts package](https://fonts.google.com/noto) (which is several GB in size).

After installing these packages, run the following commands:
    
    
    cd $HOME
    rm -rf /tmp/fonts
    

## Installing Chromium

**Tip:** Don't install Chromium when you're logged in as the root user; instead use `sudo` to perform any steps that require elevated permissions. If you install Chromium while you are logged in as the root user, Looker might not be able to execute PDF or PNG rendering.

  1. To install Chromium, run the installation command that is applicable to your system. For example:
         
         apt-get update && apt-get install -y chromium-browser
         

  2. You must either alias `chromium-browser` as `chromium` or export the `CHROMIUM_PATH` environment variable. To alias `chromium-browser` as `chromium`, place the following in the shell file that is applicable to your system. For example:
         
         alias chromium='chromium-browser'
         

To make this alias known to Looker, run this command on the command line:
         
         sudo ln -s /usr/bin/chromium-browser /usr/bin/chromium
         

  3. After you set any of the optional environment variables, restart the Looker application so the variables can take effect. You may also need to restart any open terminal sessions, or source your shell file, to get the terminal to read the new configuration.




After installing Chromium you should get a valid response from running `chromium --version` (if you have not set the `CHROMIUM_PATH` environment variable) or from running `$CHROMIUM_PATH --version` (if you have set the `CHROMIUM_PATH` environment variable).

### Optional Chromium environment variables

  * `CHROMIUM_PATH`: Path to the Chromium binary, defaults to `chromium`.

  * `CHROMIUM_PID_DIR`: Path to where the library can store Chromium PID files, defaults to `chromium_pid_files` in the Looker application working directory.

  * `CHROMIUM_PORT_RANGE_START` & `CHROMIUM_PORT_RANGE_END`: The Chromium application needs a range of ports to communicate between processes on the local machine. The default range is 40000-40500 but you can override this default by setting both of these environment variables. Unused ports are selected at random from the range and are only used for the duration of a single render.

  * `DISABLE_EXTERNAL_RENDER_ACCESS`: Admins of customer-hosted Looker instances or servers that have no external or blocked internet access should set `DISABLE_EXTERNAL_RENDER_ACCESS=true`. Typically, the Chromium renderer will wait for all resources that are requested by the page to be completed before the renderer sends the "finished" signal that prompts Looker to produce the content. Some of these requests may be dropped because of a lack of connection, resulting in timeouts or very long render times. Setting this environment variable to `true` prevents the renderer from waiting for all requests to finish. Some map visualizations and some custom visualizations that are installed from the Looker Marketplace may require internet access.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
