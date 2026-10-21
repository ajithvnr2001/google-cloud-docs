---
url: https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/nosql-client-server/
title: NoSQL Client Server \u00a0|\u00a0 DeployStack \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:55.400588+00:00
---

# NoSQL Client Server  |  DeployStack  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/nosql-client-server/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Shell ](https://docs.cloud.google.com/shell/docs)
  * [ DeployStack ](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack)
  * [ Guides ](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/overview)



#  NoSQL Client Server Stay organized with collections  Save and categorize content based on your preferences. 

[ ![Architecture](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/arch-nosql-client-server.svg)](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/arch-nosql-client-server.svg)

NoSQL Client Server will configure and create two Compute Engine instances:

  * **Server** — which will run MongoDB
  * **Client** — which will run a custom go application that talks to MongoDB and then exposes an API where you consume data from MongoDB



* * *

## Get Started

Click on the following link to a copy of the source code in Cloud Shell. Once there, a single command will spin up a working copy of the application in your project..

**Key Point:** Clicking on the following link will open a Cloud Shell session and download code from GitHub. You will have to authorize DeployStack to run. No actions will be taken until you do so. 

[ ![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/googlecloudplatform/deploystack-nosql-client-server&shellonly=true&cloudshell_image=gcr.io/ds-artifacts-cloudshell/deploystack_custom_image)

[View source code on GitHub](https://github.com/googlecloudplatform/deploystack-nosql-client-server)

* * *

## NoSQL Client Server components

The NoSQL Client Server architecture makes use of one key product. The following highlights that product, along with more information, including links to related videos, product documentation, and interactive walkthroughs.  |  |  | Video | Docs | Walkthroughs  
---|---|---|---|---|---  
![](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/compute_engine.svg) | **Compute Engine** |  Compute Engine is Google Cloud's Virtual technology. With it you can spin up many different configurations of VM to fit the shape of whatever computing needs you have.  |  [smart_display](https://www.youtube.com/watch?v=1XH0gLlGDdk) |  [description](https://cloud.google.com/compute/docs/quickstart-linux) |  [keyboard](https://console.cloud.google.com/?tutorial=compute_quickstart)  
  
* * *

## Scripts

The install script uses an executable written in `go` and Terraform CLI tools to take an empty project and install the application in it. The output should be a working application and a url for the load balancing IP address.

**Note:** The following is a breakdown of the commands that run when deploying NoSQL Client Server. _You don't need to run each command individually; Click the Open in Cloud Shell button in the Getting Started section and run all commands._

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
    

#### Create Firewall rule

Makes a rule that opens up port 80 on the firewall and then applies it to any machine labeled `http-server`
    
    
    resource "google_compute_firewall" "default-allow-http" {
      name    = "deploystack-allow-http"
      project = var.project_number
      network = "projects/${var.project_id}/global/networks/default"
    
      allow {
        protocol = "tcp"
        ports    = ["80"]
      }
    
      source_ranges = ["0.0.0.0/0"]
    
      target_tags = ["http-server"]
    }
    

#### Create Server Instance

Spins up a VM that will act as the server, and serve up MongoDB
    
    
    # Create Instances
    resource "google_compute_instance" "server" {
      name         = "server"
      zone         = var.zone
      project      = var.project_id
      machine_type = "e2-standard-2"
      tags         = ["http-server"]
    
    
      boot_disk {
        auto_delete = true
        device_name = "server"
        initialize_params {
          image = "family/ubuntu-1804-lts"
          size  = 10
          type  = "pd-standard"
        }
      }
    
      network_interface {
        network = "default"
        access_config {
          // Ephemeral public IP
        }
      }
    
      metadata_startup_script = <<SCRIPT
        apt-get update
        apt-get install -y mongodb
        service mongodb stop
        sed -i 's/bind_ip = 127.0.0.1/bind_ip = 0.0.0.0/' /etc/mongodb.conf
        iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 27017
        service mongodb start
      SCRIPT
      depends_on              = [google_project_service.all]
    }
    

#### Create Client Instance

Spins up a VM that will act as the client, and consume data from MongoDB
    
    
    resource "google_compute_instance" "client" {
      name         = "client"
      zone         = var.zone
      project      = var.project_id
      machine_type = "e2-standard-2"
      tags         = ["http-server", "https-server"]
    
      boot_disk {
        auto_delete = true
        device_name = "client"
        initialize_params {
          image = "family/ubuntu-1804-lts"
          size  = 10
          type  = "pd-standard"
        }
      }
    
      network_interface {
        network = "default"
    
        access_config {
          // Ephemeral public IP
        }
      }
    
      metadata_startup_script = <<SCRIPT
        add-apt-repository ppa:longsleep/golang-backports -y && \
        apt update -y && \
        apt install golang-go -y
        mkdir /modcache
        mkdir /go
        mkdir /app && cd /app
        curl https://raw.githubusercontent.com/GoogleCloudPlatform/golang-samples/main/compute/quickstart/compute_quickstart_sample.go --output main.go
        go mod init exec
        GOPATH=/go GOMODCACHE=/modcache GOCACHE=/modcache go mod tidy
        GOPATH=/go GOMODCACHE=/modcache GOCACHE=/modcache go get -u 
        sed -i 's/mongoport = "80"/mongoport = "27017"/' /app/main.go
        echo "GOPATH=/go GOMODCACHE=/modcache GOCACHE=/modcache HOST=${google_compute_instance.server.network_interface.0.network_ip} go run main.go"
        GOPATH=/go GOMODCACHE=/modcache GOCACHE=/modcache HOST=${google_compute_instance.server.network_interface.0.network_ip} go run main.go &
      SCRIPT
    
      depends_on = [google_project_service.all]
    }
    

* * *

## Conclusion

Once run you should now have a client server api using MongoDB running on two Compute Engine instances. Additionally you should have all of the code to modify or extend this solution to fit your environment.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
