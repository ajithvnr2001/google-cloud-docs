---
url: https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/load-balanced-vms/
title: Load Balanced Vms \u00a0|\u00a0 DeployStack \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:24:23.504085+00:00
---

# Load Balanced Vms  |  DeployStack  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/load-balanced-vms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Shell ](https://docs.cloud.google.com/shell/docs)
  * [ DeployStack ](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack)
  * [ Guides ](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/overview)



#  Load Balanced Vms Stay organized with collections  Save and categorize content based on your preferences. 

[ ![Architecture](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/arch-basiclb.svg)](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/arch-basiclb.svg)

Load Balanced Vms is an infrastructure-building script that sets up a cluster of VMs and configures a Load Balancer to expose a public route to the VMs:

  * Compute - VMs - Compute Engine
  * Compute - Cluster - Managed Instance Group
  * Compute - Machine Template - Instance Template
  * Networking - Load Balancing - Cloud Load Balancer



This example application sets up a simple static HTML site using NGINX, and load balances across your cluster.

* * *

## Get Started

Click on the following link to a copy of the source code in Cloud Shell. Once there, a single command will spin up a working copy of the application in your project..

**Key Point:** Clicking on the following link will open a Cloud Shell session and download code from GitHub. You will have to authorize DeployStack to run. No actions will be taken until you do so. 

[ ![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/googlecloudplatform/deploystack-load-balanced-vms&shellonly=true&cloudshell_image=gcr.io/ds-artifacts-cloudshell/deploystack_custom_image)

[View source code on GitHub](https://github.com/googlecloudplatform/deploystack-load-balanced-vms)

* * *

## Load Balanced Vms components

The Load Balanced Vms architecture makes use of several products. The following lists the components, along with more information on the components, including links to related videos, product documentation, and interactive walkthroughs.  |  |  | Video | Docs | Walkthroughs  
---|---|---|---|---|---  
![](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/compute_engine.svg) | **Compute Engine** |  Compute Engine is Google Cloud's Virtual technology. With it you can spin up many different configurations of VM to fit the shape of whatever computing needs you have.  |  [smart_display](https://www.youtube.com/watch?v=1XH0gLlGDdk) |  [description](https://cloud.google.com/compute/docs/quickstart-linux) |  [keyboard](https://console.cloud.google.com/?tutorial=compute_quickstart)  
![](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/cloud_load_balancing.svg) | **Cloud Load Balancing** |  Google Cloud Load Balancer allows you to place a load balancer in front of the Storage Bucket - allowing you to use SSL certificates, Logging and Monitoring.  |  [smart_display](https://www.youtube.com/watch?v=gdeOeu4E7eQ) |  [description](https://cloud.google.com/load-balancing/docs) |  [keyboard](https://console.cloud.google.com/?tutorial=load-balancing__ext-load-balancer-backend-buckets)  
  
* * *

## Scripts

The install script uses an executable written in `go` and Terraform CLI tools to take an empty project and install the application in it. The output should be a working application and a url for the load balancing IP address.

**Note:** The following is a breakdown of the commands that run when deploying Load Balanced Vms. _You don't need to run each command individually; Click the Open in Cloud Shell button in the Getting Started section and run all commands._

### `./main.tf`

#### Enable services

Google Cloud Services are disabled in a project by default. Activate the following required services:

  * Compute Engine - Virtual machines and networking services (like Load Balancer)


    
    
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
    

#### Create instance exemplar on which to base managed VMs

The following command creates a VM, installs the required software on it, and deploys code.
    
    
    resource "google_compute_instance" "exemplar" {
        name         = "${var.basename}-exemplar"
        machine_type = "n1-standard-1"
        zone         = var.zone
        project      = var.project_id
    
        tags                    = ["http-server"]
        metadata_startup_script = "apt-get update -y \n apt-get install nginx -y \n  printf '${data.local_file.index.content}'  | tee /var/www/html/index.html \n chgrp root /var/www/html/index.html \n chown root /var/www/html/index.html \n chmod +r /var/www/html/index.html"
    
        boot_disk {
            auto_delete = true
            device_name = "${var.basename}-exemplar"
            initialize_params {
            image = "family/debian-10"
            size  = 200
            type  = "pd-standard"
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
    

#### Create snapshot and disk image

The following command uses the VM to create a snapshot. The snapshot is then used to create a Disk Image. All VMs in the cluster are based on this image.
    
    
    resource "google_compute_snapshot" "snapshot" {
        project           = var.project_id
        name              = "${var.basename}-snapshot"
        source_disk       = google_compute_instance.exemplar.boot_disk[0].source
        zone              = var.zone
        storage_locations = ["${var.region}"]
        depends_on        = [time_sleep.startup_completion]
    }
    
    resource "google_compute_image" "exemplar" {
        project         = var.project_id
        name            = "${var.basename}-latest"
        family          = var.basename
        source_snapshot = google_compute_snapshot.snapshot.self_link
        depends_on      = [google_compute_snapshot.snapshot]
    }
    

#### Create instance template

The following command creates a template with the settings and configuration for all of the VMs in the cluster. It uses the disk image created in the previous command. 

The command includes a startup script that customizes the HTML that is served up by the VMs in the cluster.
    
    
     resource "google_compute_instance_template" "default" {
        project     = var.project_id
        name        = "${var.basename}-template"
        description = "This template is used to create app server instances."
        tags        = ["httpserver"]
    
        metadata_startup_script = "sed -i.bak \"s/\{\{NODENAME\}\}/$HOSTNAME/\" /var/www/html/index.html"
    
        instance_description = "BasicLB node"
        machine_type         = "n1-standard-1"
        can_ip_forward       = false
    
        // Create a new boot disk from an image
        disk {
            source_image = google_compute_image.exemplar.self_link
            auto_delete  = true
            boot         = true
        }
    
        network_interface {
            network = "default"
        }
    
        depends_on = [google_compute_image.exemplar]
    }
    

#### Create Managed Instance Group

Requests N number of machines of the Instance Template to be managed as part of this group.
    
    
    resource "google_compute_instance_group_manager" "default" {
        project            = var.project_id
        name               = "${var.basename}-mig"
        zone               = var.zone
        target_size        = var.nodes
        base_instance_name = "${var.basename}-mig"
    
    
        version {
            instance_template = google_compute_instance_template.default.id
        }
    
        named_port {
            name = "http"
            port = "80"
        }
    
        depends_on = [google_compute_instance_template.default]
    }
    

#### Create External IP Address

Needed to bind a host to the domain name, and communicate in general on the Internet.
    
    
    resource "google_compute_global_address" "default" {
        project    = var.project_id
        name       = "${var.basename}-ip"
        ip_version = "IPV4"
    }
    

#### Create load balancer

The following command creates a load balancer and implements health checks and backend services. It configures the load balancer to connect to the instance group.
    
    
    resource "google_compute_health_check" "http" {
        project = var.project_id
        name    = "${var.basename}-health-chk"
    
        tcp_health_check {
            port = "80"
        }
    }
    
    resource "google_compute_firewall" "allow-health-check" {
        project       = var.project_id
        name          = "allow-health-check"
        network       = local.defaultnetwork
        source_ranges = ["130.211.0.0/22", "35.191.0.0/16"]
    
        allow {
            protocol = "tcp"
            ports    = ["80"]
        }
    }
    
    resource "google_compute_backend_service" "default" {
        project               = var.project_id
        name                  = "${var.basename}-service"
        load_balancing_scheme = "EXTERNAL"
        protocol              = "HTTP"
        port_name             = "http"
        backend {
            group = google_compute_instance_group_manager.default.instance_group
        }
    
        health_checks = [google_compute_health_check.http.id]
        }
    
        resource "google_compute_url_map" "lb" {
        project         = var.project_id
        name            = "${var.basename}-lb"
        default_service = google_compute_backend_service.default.id
    }
    

#### Enable HTTP

The following command configures networking rules that point port 80 on the load balancer to the service.
    
    
    resource "google_compute_target_http_proxy" "default" {
        project = var.project_id
        name    = "${var.basename}-lb-proxy"
        url_map = google_compute_url_map.lb.id
    }
    
    resource "google_compute_forwarding_rule" "google_compute_forwarding_rule" {
        project               = var.project_id
        name                  = "${var.basename}-http-lb-forwarding-rule"
        provider              = google-beta
        region                = "none"
        load_balancing_scheme = "EXTERNAL"
        port_range            = "80"
        target                = google_compute_target_http_proxy.default.id
        ip_address            = google_compute_global_address.default.id
    }
    

* * *

## Conclusion

Once run you should now have a simple web site running on multiple Compute Engine instances, fronted by a load balancer in your project. Additionally you should have all of the code to modify or extend this solution to fit your environment.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
