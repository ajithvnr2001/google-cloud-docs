---
url: https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/ops-agent/
title: Ops Agent \u00a0|\u00a0 DeployStack \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:30:45.238636+00:00
---

# Ops Agent  |  DeployStack  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/ops-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Shell ](https://docs.cloud.google.com/shell/docs)
  * [ DeployStack ](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack)
  * [ Guides ](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/overview)



#  Ops Agent Stay organized with collections  Save and categorize content based on your preferences. 

[ ![Architecture](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/arch-ops-agent.svg)](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/arch-ops-agent.svg)

Ops Agent creates a virtual machine and installs the Ops Agent for integrating with Monitoring and Logging services. It uses:

  * Compute Engine
  * Monitoring
  * Logging



Example sets up a simple single virtual machine and wires it up to report to Logging.

* * *

## Get Started

Click on the following link to a copy of the source code in Cloud Shell. Once there, a single command will spin up a working copy of the application in your project..

**Key Point:** Clicking on the following link will open a Cloud Shell session and download code from GitHub. You will have to authorize DeployStack to run. No actions will be taken until you do so. 

[ ![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/googlecloudplatform/deploystack-ops-agent&shellonly=true&cloudshell_image=gcr.io/ds-artifacts-cloudshell/deploystack_custom_image)

[View source code on GitHub](https://github.com/googlecloudplatform/deploystack-ops-agent)

* * *

## Ops Agent components

The Ops Agent architecture makes use of several products. The following lists the components, along with more information on the components, including links to related videos, product documentation, and interactive walkthroughs.  |  |  | Video | Docs | Walkthroughs  
---|---|---|---|---|---  
![](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/compute_engine.svg) | **Compute Engine** |  Compute Engine is Google Cloud's Virtual technology. With it you can spin up many different configurations of VM to fit the shape of whatever computing needs you have.  |  [smart_display](https://www.youtube.com/watch?v=1XH0gLlGDdk) |  [description](https://cloud.google.com/compute/docs/quickstart-linux) |  [keyboard](https://console.cloud.google.com/?tutorial=compute_quickstart)  
![](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/cloud_monitoring.svg) | **Cloud Monitoring** |  Cloud Monitoring exposes visibility into the performance, availability, and health of your applications and infrastructure  |  [smart_display](https://www.youtube.com/watch?v=wY8cmFY4ua8&t=2s) |  [description](https://cloud.google.com/monitoring/docs/) |   
![](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/cloud_logging.svg) | **Cloud Logging** |  Cloud Logging provides fully managed, real-time log management with storage, search, analysis and alerting at exabyte scale.  |  [smart_display](https://www.youtube.com/watch?v=gyDp-Cl_MdA) |  [description](https://cloud.google.com/logging/docs/) |  [keyboard](https://console.cloud.google.com/?walkthrough_id=logging--cloud_ops_logging_quickstart)  
  
* * *

## Scripts

The install script uses an executable written in `go` and Terraform CLI tools to take an empty project and install the application in it. The output should be a working application and a url for the load balancing IP address.

**Note:** The following is a breakdown of the commands that run when deploying Ops Agent. _You don't need to run each command individually; Click the Open in Cloud Shell button in the Getting Started section and run all commands._

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
    
    
    resource "google_compute_instance" "default" {
      project      = var.project_id
      name         = "${var.basename}-instance"
      machine_type = "f1-micro"
      zone         = var.zone
    
      boot_disk {
        initialize_params {
          image = "centos-cloud/centos-8-v20210817"
        }
      }
      labels = {
        env        = "prod"
        app        = "myproduct"
        created_by = "terraform"
      }
    
      network_interface {
        network = "default"
    
        access_config {
          // Include this section to give the VM an external ip address
        }
      }
      service_account {
        // Google recommends custom service accounts that have cloud-platform scope and permissions granted via IAM Roles.
        // This non production example uses the default compute service account.
        email  = local.sacompute
        scopes = ["cloud-platform"]
      }
    }
    

#### Install Ops Agent

The Ops Agent is the primary agent for collecting telemetry from your Compute Engine instances. This will show you how to install it, using terraform.
    
    
    module "agent_policy" {
        source  = "terraform-google-modules/cloud-operations/google//modules/agent-policy"
        version = "~> 0.1.0"
        
        project_id = var.project_id
        policy_id  = "ops-agents-example-policy"
        agent_rules = [
            {
            type               = "ops-agent"
            version            = "current-major"
            package_state      = "installed"
            enable_autoupgrade = true
            },
        ]
        group_labels = [
            {
            env        = "prod"
            app        = "myproduct"
            created_by = "terraform"
            }
        ]
        
        os_types = [
            {
            short_name = "centos"
            version    = "8"
            },
        ]
    }
    

* * *

## Conclusion

Once run, you should now have a VM that's been properly configured to log events to Google Cloud Logging. Additionally you should have all of the code to modify or extend this solution to fit your environment.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
