---
url: https://docs.cloud.google.com/shell/docs/quotas-limits/
title: Quotas and limits \u00a0|\u00a0 Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:51:31.670066+00:00
---

# Quotas and limits  |  Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/shell/docs/quotas-limits/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Shell ](https://docs.cloud.google.com/shell/docs)
  * [ Resources ](https://docs.cloud.google.com/shell/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and system limits that apply to Cloud Shell.

  * _Quotas_ have default values, but you can typically request adjustments.
  * _System limits_ are fixed values that can't be changed.



Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

There are also _system limits_ on Cloud Shell resources. System limits can't be changed. 

To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

**Note:** The majority of these limits are not present in [Cloud Workstations](https://docs.cloud.google.com/workstations/docs/overview). Cloud Workstations lets you customize, rightsize and secure your development environment. Upgrade from Cloud Shell to Cloud Workstations for managed secure development environments provisioned in your VPC. [Set up Cloud Workstations](https://docs.cloud.google.com/workstations/docs/quickstart-set-up-workstations-console) to get started.

## Usage quotas

The default weekly Cloud Shell quota is 50 hours.

### Viewing your weekly Cloud Shell quota

If you reach your quota, you'll need to wait until the date and time specified before you can use Cloud Shell again or upgrade to Cloud Workstations.

To view your weekly quota:

  * Click ![Session information](https://docs.cloud.google.com/static/shell/docs/images/session-info-icon.png)**Session information** and then click **Usage quota**. A dialog appears and displays the hours remaining in your quota, the total number of hours in your quota, and the date and time that the quota resets.



If you need more quota, we strongly recommend upgrading to [Cloud Workstations](https://docs.cloud.google.com/workstations/docs/overview), which does not have weekly usage limitations. Cloud Workstations lets you customize, rightsize and secure your development environment. Upgrade to Cloud Workstations for managed secure development environments provisioned in your VPC without usage limits.

### Cloud Shell inactivity

**Warning:** If you delete your `$HOME` directory, or if you don't access Cloud Shell for 120 days, Cloud Shell automatically deletes your `$HOME` directory and can't recover your files. You'll receive an email notification before this occurs.

To prevent your `$HOME` directory from being deleted due to inactivity for 120 days, start a session. For sensitive data you want to store long term, consider a different solution on [Cloud Storage](https://cloud.google.com/products/storage/).

### Non-interactive usage

Cloud Shell is intended for interactive use only. Non-interactive sessions are ended automatically after 40 minutes. Cloud Shell sessions are capped at 12 hours, after which sessions automatically terminate. You can start a new session immediately after.

### Restoring a session after a service limit violation

If your session is terminated or can't be established because you exceeded a service limit, Cloud Shell displays an error with a link to a form that allows you to appeal the limit violation. Click the feedback link and submit the form with more information about the tasks you were performing before your session was terminated.

**Warning:** Violating the [Terms of Service](https://cloud.google.com/terms/) will result in Cloud Shell being disabled for your account.   
This constitutes activity that adversely impacts Google Cloud services, other customers' or their end users' use of services, or the Google network used to provide these services. Coin mining and network scanning using Cloud Shell are strictly prohibited.

## Limitations and restrictions

### Custom installed software packages and persistence

The virtual machine instance that backs your Cloud Shell session isn't permanently allocated to your Cloud Shell session and terminates if your session is inactive for 40 minutes. After the instance is terminated, any modifications that you made outside your `$HOME` directory are lost.

To have your configurations persist across sessions, consider [customizing your environment](https://docs.cloud.google.com/shell/docs/configuring-cloud-shell#environment_customization_script).

### Users younger than 18 or whose age is unknown

Cloud Shell isn't available to users younger than 18 or whose age is unknown. By default, Google Workspace for Education blocks access to Cloud Shell for all users. If your institution has students older than 18 who you want to have access to age-restricted services including Cloud Shell, see [Control access to Google services by age](https://support.google.com/a/answer/10651918#zippy=%2Cservices-not-available-to-users-under) for steps to identify users who are 18 years or older.

### Cloud Shell Editor extensions

Cloud Shell Editor does not support the installation of custom editor extensions. However, the Cloud Shell Editor comes with a set of essential extensions already installed and kept up-to-date.

### `.bashrc` content

Cloud Shell can produce errors if the `.bashrc` file is modified or deleted. The `.bashrc` file must contain the following lines:
    
    
      if [ -f "/google/devshell/bashrc.google" ]; then
        source "/google/devshell/bashrc.google"
      fi
    

### `gcloud` output formatting

By default, Cloud Shell enables [`gcloud` accessibility features](https://docs.cloud.google.com/sdk/docs/enabling-accessibility-features). With accessibility features enabled, `gcloud` table output is rendered as a flattened list of items.

To restore the default behavior of boxed tables for many commands, append the following command to the end of your `$HOME/.bashrc` file:
    
    
      gcloud config set accessibility/screen_reader false
    

### Slow connection performance

Connecting to a Cloud Shell for the first time involves creating your home disk and can currently take up to 25 seconds. Subsequent connections to existing virtual machine instances take about five seconds. However, if you haven't used Cloud Shell for a week, connection performance will be slower since the home directory is restored from an archive.

Cloud Shell also offers [Ephemeral mode](https://docs.cloud.google.com/shell/docs/using-cloud-shell#choosing_ephemeral_mode) which is the Cloud Shell experience without persistent disk storage. Ephemeral mode offers faster connection performance but all the files you create in your session are lost on session end.

### Browser support

Cloud Shell supports the latest versions of Google Chrome, Mozilla Firefox, Microsoft Edge, Microsoft Internet Explorer 11+, and Apple Safari 8+. Safari in private browser mode is not supported.

### Private browsing and disabled third-party cookies

The Cloud Shell Editor can't load in Cloud Shell if third-party cookies are disabled. Some browsers have third-party cookies disabled by default and most browsers' Incognito or Private Browser modes block these cookies as well.

With third-party cookies disabled, you can still use the Cloud Shell Editor in its own window by clicking the **Open in New Window** button accessible when you open an editor session ![Code Editor Button](https://docs.cloud.google.com/static/shell/docs/images/open-editor.png).

Alternatively, you can navigate to port 970 using the Web Preview ![Web Preview Button](https://docs.cloud.google.com/static/shell/docs/images/web-preview-button.png).

![Editor panel explaining that the code editor could not be loaded because of third-party cookie blocking, with link to Open the editor in a new window](https://docs.cloud.google.com/static/shell/docs/images/openinnewwindow.png)

**Tip:** If you're using Google Chrome, you can enable third-party cookies by clicking the Third-party cookie blocking icon in your address bar ![Third-party cookie blocking icon](https://docs.cloud.google.com/static/shell/docs/images/cookieblock.png), selecting **Site not working?** , clicking **Allow cookies** , and reloading your page.

### Disk storage

Cloud Shell provisions 5 GB of free [persistent disk storage](https://docs.cloud.google.com/compute/docs/disks/persistent-disks) mounted as your `$HOME` directory on the virtual machine instance. This storage is on a per-user basis and is available across projects. All files you store in your home directory, including installed software, scripts, and user configuration files like `.bashrc` and `.vimrc`, persist between sessions and count towards the 5 GB limit.

#### Clearing disk space

If you encounter a `no space left on device` error, free up space by removing files from your home directory using the Cloud Shell terminal. Use the `du -hs $(ls -A)` command to see the space each file uses within each sub-directory. Consider removing those that are no longer needed or take up a large chunk of storage.

**Note:** If you don't access Cloud Shell regularly, the `$HOME` directory persistent storage may be recycled. You receive an email notification before this occurs. Starting a Cloud Shell session prevents the persistent storage from being recycled.

## What's next

  * [Learn about the Cloud Shell VM](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works)
  * [Start Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
