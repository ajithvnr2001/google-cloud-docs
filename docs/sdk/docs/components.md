---
url: https://docs.cloud.google.com/sdk/docs/components/
title: Managing gcloud CLI components \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:47:41.461979+00:00
---

# Managing gcloud CLI components  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/docs/components/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Guides ](https://docs.cloud.google.com/sdk/docs/overview)



Send feedback 

#  Managing gcloud CLI components Stay organized with collections  Save and categorize content based on your preferences. 

Components are the installable parts of the Google Cloud CLI. A component can be a command-line tool (`gcloud`, `bq`, and `gsutil`), a set of gcloud CLI commands at the Alpha, Beta, or Preview [release levels](https://docs.cloud.google.com/sdk/gcloud#release_levels), or a package that contains dependencies used by a tool in the gcloud CLI.

The most commonly-used components are installed by default. If you run a `gcloud alpha`, `gcloud beta`, or `gcloud preview` command interactively and the `alpha`, `beta`, or `preview` component is not installed, the gcloud CLI asks you whether you want to install it. An affirmative response installs the component and then runs the command. Other components are installed on-demand by the gcloud CLI when you run commands that require them.

##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Get started for free ](https://console.cloud.google.com/freetrial)

## Default components

When you install the gcloud CLI, the following components are installed by default:

ID | Name | Description  
---|---|---  
[`gcloud`](https://docs.cloud.google.com/sdk/gcloud/reference) | Default gcloud CLI commands | Tool for interacting with Google Cloud. Only commands at the General Availability release level are installed with this component. You must separately install the `gcloud alpha` Commands, `gcloud beta` Commands, and/or `gcloud preview` Commands components if you want to use commands at other release levels.  
[`bq`](https://docs.cloud.google.com/bigquery/bq-command-line-tool) | BigQuery command-line tool | Tool for working with data in BigQuery  
`gsutil` |  | Legacy tool for performing Cloud Storage tasks. Use [`gcloud storage` commands](https://docs.cloud.google.com/sdk/gcloud/reference/storage) instead.  
`core` | gcloud CLI core libraries | Libraries used internally by the gcloud CLI tools.  
  
## Alpha, beta, and preview components

The gcloud CLI provides components that contain gcloud CLI alpha, beta, and preview commands. These components aren't installed by default, but you can install them manually at any time after the initial gcloud CLI installation. These components are:

ID | Name | Description  
---|---|---  
[`alpha`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha) | gcloud CLI alpha commands | gcloud CLI commands at the alpha release level.  
[`beta`](https://docs.cloud.google.com/sdk/gcloud/reference/beta) | gcloud CLI beta commands | gcloud CLI commands at the beta release level.  
[`preview`](https://docs.cloud.google.com/sdk/gcloud/reference/preview) | gcloud CLI preview commands | gcloud CLI commands at the preview release level.  
  
gcloud CLI commands at the General Availability release level are part of the gcloud CLI component and are installed automatically when you install the gcloud CLI.

A list of all available additional components and external package managers, which aren't installed by default, appears below.

## Managing gcloud CLI components

You can list, install, update, and remove gcloud CLI components to suit your needs.

Note: These instructions won't work if you have installed gcloud CLI using a package manager such as APT or `yum` because gcloud CLI component manager is disabled when using that method of installation. Use these [packages](https://docs.cloud.google.com/sdk/docs/components#external_package_managers) instead. **Caution:** When modifying your installation, the current directory of your terminal must be outside the `google-cloud-cli` directory of the gcloud CLI installation. On Windows, you will need to open your terminal as an Administrator if you have performed an _All Users_ installation.

### Listing components

To see a list of components that are available and currently installed, run [`gcloud components list`](https://docs.cloud.google.com/sdk/gcloud/reference/components/list):
    
    
    gcloud components list
    

The following sample isn't a complete listing of all available components. To view the latest component offerings, update your gcloud CLI installation and then run [`gcloud components list`](https://docs.cloud.google.com/sdk/gcloud/reference/components/list).

**Status** | **Component Name** | **ID** | **Size**  
---|---|---|---  
Installed | App Engine Go Extensions | app-engine-go | 97.7 MiB  
Installed | Cloud Bigtable Command Line Tool | cbt | 4.0 MiB  
Installed | Cloud Bigtable Emulator | bigtable | 3.8 MiB  
Installed | Cloud Datastore Emulator | cloud-datastore-emulator | 17.8 MiB  
Not Installed | Cloud Firestore Emulator | cloud-firestore-emulator | 60.4 MiB  
Installed | Cloud Pub/Sub Emulator | pubsub-emulator | 33.2 MiB  
Installed | Cloud Spanner Emulator | cloud-spanner-emulator | 21.8 MiB  
Installed | Google Cloud Build Local Builder | cloud-build-local | 4.4 MiB  
Installed | gcloud app Java Extensions | app-engine-java | 118.9 MiB  
Installed | gcloud app PHP Extensions | app-engine-php | 21.9 MiB  
Installed | gcloud app Python Extensions (Extra Libraries) | app-engine-python-extras | 27.8 MiB  
Installed | kubectl | kubectl | 12.2 MiB  
Installed | Cloud BigQuery Command Line Tool | bq | < 1 MiB  
Installed | Cloud SDK Core Libraries | core | 7.2 MiB  
Installed | Cloud Storage Command Line Tool | gsutil | 3.3 MiB  
Installed | gcloud Alpha Commands | alpha | < 1 MiB  
Installed | gcloud Beta Commands | beta | < 1 MiB  
Not Installed | gcloud Preview Commands | preview | < 1 MiB  
Installed | gcloud app Python Extensions | app-engine-python | 6.1 MiB  
  
### Installing components

To install a component at the current version of your gcloud CLI installation, run [`gcloud components install`](https://docs.cloud.google.com/sdk/gcloud/reference/components/install):
    
    
    gcloud components install [COMPONENT-ID]
    

The gcloud CLI installs the specified component.

For example, if you want to install the `kubectl` command:
    
    
    gcloud components install kubectl
    

### Updating components

Use the [`gcloud components update`](https://docs.cloud.google.com/sdk/gcloud/reference/components/update) command to update all installed components to the latest available version of gcloud CLI:
    
    
    gcloud components update
    

If you have an older version of the gcloud CLI installed, the gcloud CLI updates all the installed components.

If you need to revert to a previously known good version and installed the gcloud CLI directly (outside of a package manager, including using the interactive installer, static versions, Windows installer, or Homebrew), use `gcloud components update` to revert to the specified version:
    
    
    gcloud components update --version VERSION
    

For downgrading versions of the gcloud CLI installed using a package manager, refer to these instructions for specifying versions when downloading using [`apt-get`](https://docs.cloud.google.com/sdk/docs/install#deb) or [`yum`](https://docs.cloud.google.com/sdk/docs/install#rpm). 

### Removing components

Use the [`gcloud components remove`](https://docs.cloud.google.com/sdk/gcloud/reference/components/remove) command to remove a specified component by its ID:
    
    
    gcloud components remove [COMPONENT-ID]
    

You can re-install a component using the `gcloud components install` command at any time.

## Additional components

Additional components that contain dependencies for gcloud CLI commands are also available in the gcloud CLI, but aren't installed by default. For an exhaustive list of components, run [`gcloud components list`](https://docs.cloud.google.com/sdk/gcloud/reference/components/list). Additional components that can be installed are marked with the status `Not Installed`.

## External package managers

If you installed the gcloud CLI through the `apt` or `yum` package managers, you can also install additional gcloud CLI components using those same package managers. If your package manager cannot find these packages, read the [installing with apt](https://docs.cloud.google.com/sdk/docs/install#deb) or [installing with yum](https://docs.cloud.google.com/sdk/docs/install#rpm) guides to learn how to configure `https://packages.cloud.google.com/` as a package source.

gcloud CLI component | APT Package | YUM Package  
---|---|---  
`app-engine-go` | `google-cloud-cli-app-engine-go` | `google-cloud-cli-app-engine-go`  
`app-engine-java` | `google-cloud-cli-app-engine-java` | `google-cloud-cli-app-engine-java`  
`app-engine-python` | `google-cloud-cli-app-engine-python` | `google-cloud-cli-app-engine-python`  
`bigtable` | `google-cloud-cli-bigtable-emulator` | `google-cloud-cli-bigtable-emulator`  
`cbt` | `google-cloud-cli-cbt` | `google-cloud-cli-cbt`  
`cloud-build-local` | `google-cloud-cli-cloud-build-local` | `google-cloud-cli-cloud-build-local`  
`docker-credential-gcr` | `google-cloud-cli-docker-credential-gcr` | `google-cloud-cli-docker-credential-gcr`  
`gcd-emulator` | `google-cloud-cli-datastore-emulator` | `google-cloud-cli-datastore-emulator`  
`kubectl` | `kubectl` | `kubectl`  
`pubsub-emulator` | `google-cloud-cli-pubsub-emulator` | `google-cloud-cli-pubsub-emulator`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
