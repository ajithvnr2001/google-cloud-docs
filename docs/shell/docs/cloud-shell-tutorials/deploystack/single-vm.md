---
url: https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/single-vm/
title: Single VM \u00a0|\u00a0 DeployStack \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:55.650477+00:00
---

# Single VM  |  DeployStack  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/single-vm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Shell ](https://docs.cloud.google.com/shell/docs)
  * [ DeployStack ](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack)
  * [ Guides ](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/overview)



#  Single VM Stay organized with collections  Save and categorize content based on your preferences. 

[ ![Architecture](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/arch-single-vm.svg)](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/arch-single-vm.svg)

Single VM stack creates an individual VM with a smart default, but also the ability to customize the Virtual Machine. It uses:

  * Compute - VMs - Compute Engine



Example sets up a simple single virtual machine, and allows you to ssh into it.

* * *

## Get Started

Click on the following link to a copy of the source code in Cloud Shell. Once there, a single command will spin up a working copy of the application in your project..

**Key Point:** Clicking on the following link will open a Cloud Shell session and download code from GitHub. You will have to authorize DeployStack to run. No actions will be taken until you do so. 

[ ![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/googlecloudplatform/deploystack-single-vm&shellonly=true&cloudshell_image=gcr.io/ds-artifacts-cloudshell/deploystack_custom_image)

[View source code on GitHub](https://github.com/googlecloudplatform/deploystack-single-vm)

* * *

## Single VM components

The Single VM architecture makes use of one key product. The following highlights that product, along with more information, including links to related videos, product documentation, and interactive walkthroughs.  |  |  | Video | Docs | Walkthroughs  
---|---|---|---|---|---  
![](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/compute_engine.svg) | **Compute Engine** |  Compute Engine is Google Cloud's Virtual technology. With it you can spin up many different configurations of VM to fit the shape of whatever computing needs you have.  |  [smart_display](https://www.youtube.com/watch?v=1XH0gLlGDdk) |  [description](https://cloud.google.com/compute/docs/quickstart-linux) |  [keyboard](https://console.cloud.google.com/?tutorial=compute_quickstart)  
  
* * *

## Scripts

The install script uses an executable written in `go` and Terraform CLI tools to take an empty project and install the application in it. The output should be a working application and a url for the load balancing IP address.

**Note:** The following is a breakdown of the commands that run when deploying Single VM. _You don't need to run each command individually; Click the Open in Cloud Shell button in the Getting Started section and run all commands._

### `./main.tf`

#### Enable Services

Google Cloud Services are disabled in a project by default. In order to use any of the solutions here, we have to activate the following:

  * **Compute Engine** — virtual machines and networking


    
    
    variable "gcp_service_list" {
        description = "The list of apis necessary for the project"
        type        = list(string)
        default = [
            "compute.googleapis.com",
        ]
    }
    
    resource "google_project_service" "all" {
      for_each                   = toset(var.gcp_service_list)
      project                    = var.project_number
      service                    = each.key
      disable_dependent_services = false
      disable_on_destroy         = false
    }
    

#### Create a virtual machine

Creates a VM.
    
    
    resource "google_compute_instance" "instance" {
        name         = var.instance-name
        machine_type = var.instance-machine-type
        zone         = var.zone
        project      = var.project_id
        tags         = var.instance-tags
    
    
        boot_disk {
            auto_delete = true
            device_name = var.instance-name
            initialize_params {
            image = var.instance-image
            size  = var.instance-disksize
            type  = var.instance-disktype
            }
        }
    
        network_interface {
            network = "default"
            access_config {
            // Ephemeral public IP
            }
        }
    
        depends_on = [google_project_service.all]
        }
    

* * *

## Conclusion

Once run, you should now have a single VM. You can ssh into it and configure it however you'd like. Additionally you should have all of the code to modify or extend this solution to fit your environment.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
