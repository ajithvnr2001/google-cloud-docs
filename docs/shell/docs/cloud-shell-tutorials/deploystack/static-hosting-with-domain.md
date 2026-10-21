---
url: https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/static-hosting-with-domain/
title: Static Hosting with Domain \u00a0|\u00a0 DeployStack \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:56.281188+00:00
---

# Static Hosting with Domain  |  DeployStack  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/static-hosting-with-domain/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Shell ](https://docs.cloud.google.com/shell/docs)
  * [ DeployStack ](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack)
  * [ Guides ](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/overview)



#  Static Hosting with Domain Stay organized with collections  Save and categorize content based on your preferences. 

[ ![Architecture](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/arch-yesornosite.svg)](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/arch-yesornosite.svg)

Static Hosting with Domain is a simple static website creator, that makes a simple site using a Storage Bucket to serve the website:

  * Storage - File Storage - Cloud Storage
  * Networking - Load Balancing - Cloud Load Balancer
  * Networking - DNS - Cloud DNS
  * Domain Management - Registrar - Cloud Domains



* * *

## Get Started

Click on the following link to a copy of the source code in Cloud Shell. Once there, a single command will spin up a working copy of the application in your project..

**Key Point:** Clicking on the following link will open a Cloud Shell session and download code from GitHub. You will have to authorize DeployStack to run. No actions will be taken until you do so. 

[ ![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/googlecloudplatform/deploystack-static-hosting-with-domain&shellonly=true&cloudshell_image=gcr.io/ds-artifacts-cloudshell/deploystack_custom_image)

[View source code on GitHub](https://github.com/googlecloudplatform/deploystack-static-hosting-with-domain)

* * *

## Static Hosting with Domain components

The Static Hosting with Domain architecture makes use of several products. The following lists the components, along with more information on the components, including links to related videos, product documentation, and interactive walkthroughs.  |  |  | Video | Docs | Walkthroughs  
---|---|---|---|---|---  
![](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/cloud_storage.svg) | **Cloud Storage** |  Cloud Storage provides file storage and public serving of images over http(s).  |  [smart_display](https://www.youtube.com/watch?v=zvqJ-pcQChE) |  [description](https://cloud.google.com/storage/docs/quickstart-console) |  [keyboard](https://console.cloud.google.com/?tutorial=storage--quickstart-basic-tasks)  
![](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/cloud_dns.svg) | **Cloud DNS** |  Cloud DNS provides DNS management - allowing you to run your own DNS infrastructure using Google's existing DNS infrastructure.  |  [smart_display](https://www.youtube.com/watch?v=OH_Jw8NhEGU) |  [description](https://cloud.google.com/dns/docs) |  [keyboard](https://console.cloud.google.com/?tutorial=static_dns_quickstart)  
![](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/cloud_load_balancing.svg) | **Cloud Load Balancing** |  Google Cloud Load Balancer allows you to place a load balancer in front of the Storage Bucket - allowing you to use SSL certificates, Logging and Monitoring.  |  [smart_display](https://www.youtube.com/watch?v=gdeOeu4E7eQ) |  [description](https://cloud.google.com/load-balancing/docs) |  [keyboard](https://console.cloud.google.com/?tutorial=load-balancing__ext-load-balancer-backend-buckets)  
![](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/cloud_domains.svg) | **Cloud Domains** |  Cloud Domains allows you to buy domains, acting like a Domain Registrar - but once you do, you can manage them and handle billing through your Google Cloud Account.  |  [smart_display](https://www.youtube.com/watch?v=971wi9Tt5Ds) |  [description](https://cloud.google.com/domains/docs) |  [keyboard](https://console.cloud.google.com/?walkthrough_id=domains__quickstart-register-domain)  
  
* * *

## Scripts

The install script uses an executable written in `go` and Terraform CLI tools to take an empty project and install the application in it. The output should be a working application and a url for the load balancing IP address.

**Note:** The following is a breakdown of the commands that run when deploying Static Hosting with Domain. _You don't need to run each command individually; Click the Open in Cloud Shell button in the Getting Started section and run all commands._

### `./main.tf`

#### Enable Services

Google Cloud Services are disabled in a project by default. In order to use any of the solutions here we have to activate the following:

  * **Cloud Domains** \- domain registration
  * **Cloud Storage** \- hosting the static files
  * **Cloud Compute** \- provide access to load balancers.
  * **Cloud DNS** \- provides DNS management


    
    
    variable "gcp_service_list" {
        description = "The list of apis necessary for the project"
        type        = list(string)
        default = [
            "domains.googleapis.com",
            "storage.googleapis.com",
            "compute.googleapis.com",
            "dns.googleapis.com",
        ]
    }
    
    resource "google_project_service" "all" {
        for_each                   = toset(var.gcp_service_list)
        project                    = var.project_number
        service                    = each.key
        disable_dependent_services = false
        disable_on_destroy         = false
    }
    

#### Create DNS Zone

Creates a DNS Zone for managing records, pointing them at load balancers, interacting with Domain Registrars and serving DNS requests to other DNS servers. 
    
    
    resource "google_dns_managed_zone" "dnszone" {
        project     = var.project_id
        name        = local.clouddnszone
        dns_name    = "${var.domain}."
        description = "A DNS Zone for managing ${var.domain}"
    }
    

#### Create SSL Certificate

SSL certificates are required for https protocol requests. This generates one that will be attached to the load balancer in a later command. 
    
    
    resource "google_compute_managed_ssl_certificate" "cert" {
        name        = "${local.basename}-cert"
        description = "Cert for ${local.basename}-microsite"
        project     = var.project_id
    
        managed {
            domains = [var.domain]
        }
    
        lifecycle {
            create_before_destroy = true
        }
    }
    

#### Create External IP Address

Needed to bind a host to the domain name, and communicate in general on the Internet. 
    
    
    resource "google_compute_global_address" "ip" {
        project    = var.project_id
        name       = "${local.basename}-ip"
        ip_version = "IPV4"
    }
    

#### Create Storage Bucket

This creates a bucket named after the domain, and then sets the bucket up with proper configuration to act as a webserver. Lastly, it copies the simple template for the site.
    
    
    resource "google_storage_bucket" "http_bucket" {
        name     = local.bucket
        project  = var.project_id
        location = var.location
        
        website {
            main_page_suffix = "index.html"
            not_found_page   = "404.html"
        }
    }
    
    resource "google_storage_bucket_iam_binding" "policy" {
        bucket = google_storage_bucket.http_bucket.name
        role   = "roles/storage.objectViewer"
        members = [
          "allUsers",
        ]
        depends_on = [google_storage_bucket.http_bucket]
      }
    
    resource "google_storage_bucket_object" "archive" {
        name   = "index.html"
        bucket = google_storage_bucket.http_bucket.name
        source = "code/${var.yesorno}/index.html"
        depends_on = [
            google_project_service.all,
            google_storage_bucket.http_bucket,
        ]
    }
    

#### Stand Up Load Balancer

This creates the load balancer and sets up the Storage Bucket as the source of the content to which the load balancer will provide access.
    
    
    resource "google_compute_backend_bucket" "be" {
        project     = var.project_id
        name        = "${local.basename}-be"
        bucket_name = google_storage_bucket.http_bucket.name
        depends_on = [google_storage_bucket.http_bucket]
    }
    
    resource "google_compute_url_map" "lb" {
        project         = var.project_id
        name            = "${local.basename}-lb"
        default_service = google_compute_backend_bucket.be.id
        depends_on = [google_compute_backend_bucket.be]
    }
    

#### Enable HTTP

Creates the necessary networking rules to point port 80 on the load balancer to the service we are running.
    
    
    resource "google_compute_target_http_proxy" "lb-proxy" {
        project = var.project_id
        name    = "${local.basename}-lb-proxy"
        url_map = google_compute_url_map.lb.id
        depends_on = [google_compute_url_map.lb]
    }
    
    resource "google_compute_forwarding_rule" "http-lb-forwarding-rule" {
        project               = var.project_id
        name                  = "${local.basename}-http-lb-forwarding-rule"
        provider              = google-beta
        region                = "none"
        load_balancing_scheme = "EXTERNAL"
        port_range            = "80"
        target                = google_compute_target_http_proxy.lb-proxy.id
        ip_address            = google_compute_global_address.ip.id
        depends_on = [google_compute_target_http_proxy.lb-proxy]
    }
    

#### Enable HTTPS

Creates the necessary networking rules to point port 443 on the load balancer to the service we are running. Also associates the certificate properly.
    
    
    resource "google_compute_target_https_proxy" "ssl-lb-proxy" {
        project          = var.project_id
        name             = "${local.basename}-ssl-lb-proxy"
        url_map          = google_compute_url_map.lb.id
        ssl_certificates = [google_compute_managed_ssl_certificate.cert.id]
        depends_on = [google_compute_url_map.lb,google_compute_managed_ssl_certificate.cert ]
    }
    
    resource "google_compute_forwarding_rule" "https-lb-forwarding-rule" {
        project               = var.project_id
        name                  = "${local.basename}-https-lb-forwarding-rule"
        provider              = google-beta
        region                = "none"
        load_balancing_scheme = "EXTERNAL"
        port_range            = "443"
        target                = google_compute_target_https_proxy.ssl-lb-proxy.id
        ip_address            = google_compute_global_address.ip.id
        depends_on = [google_compute_target_https_proxy.ssl-lb-proxy]
    }
    

#### Set A Record

Creates the proper rule in Cloud DNS that will make the domain name resolve to the IP address we created.
    
    
    resource "google_dns_record_set" "a" {
        project      = var.project_id
        name         = "${var.domain}."
        managed_zone = google_dns_managed_zone.dnszone.name
        type         = "A"
        ttl          = 60
    
    
        rrdatas = [google_compute_global_address.ip.address]
        depends_on = [google_compute_global_address.ip]
    }
    

### `./deploystack.go`

#### Query Domain availability

Gets information about the availability of the domain being requested 
    
    
    func domainsSearch(project, domain string) ([]*domainspb.RegisterParameters, error) {
        ctx := context.Background()
    
        c, err := domains.NewClient(ctx)
        if err != nil {
            return nil, err
        }
        defer c.Close()
    
        req := &domainspb.SearchDomainsRequest{
            Query:    domain,
            Location: fmt.Sprintf("projects/%s/locations/global", project),
        }
        resp, err := c.SearchDomains(ctx, req)
        if err != nil {
            return nil, err
        }
    
        return resp.RegisterParameters, nil
    }
    
    func domainIsAvailable(project, domain string) (*domainspb.RegisterParameters, error) {
        list, err := domainsSearch(project, domain)
        if err != nil {
            return nil, err
        }
        for _, v := range list {
            if v.DomainName == domain {
                return v, err
            }
        }
    
        return nil, err
    }
    

#### Query Domain Ownership

Gets information whether or not the current user owns the requested domain. 
    
    
    func domainsIsVerified(project, domain string) (bool, error) {
        ctx := context.Background()
    
        c, err := domains.NewClient(ctx)
        if err != nil {
            return false, err
        }
        defer c.Close()
    
        req := &domainspb.ListRegistrationsRequest{
            Filter: fmt.Sprintf("domainName=\"%s\"", domain),
            Parent: fmt.Sprintf("projects/%s/locations/global", project),
        }
        it := c.ListRegistrations(ctx, req)
        for {
            resp, err := it.Next()
            if err == iterator.Done {
                break
            }
            if err != nil {
                return false, err
            }
    
            if resp.DomainName == domain {
                return true, nil
            }
        }
    
        return false, nil
    }
    

#### Register Domain with Cloud Domains

Actually performs the operation to purchase the domain from the registrar. 
    
    
    func domainRegister(project string, domaininfo *domainspb.RegisterParameters, contact ContactData) error {
        ctx := context.Background()
    
        parent := fmt.Sprintf("projects/%s/locations/global", project)
    
        c, err := domains.NewClient(ctx)
        if err != nil {
            return err
        }
        defer c.Close()
    
        dnscontact, err := contact.DomainContact()
        if err != nil {
            return err
        }
    
        req := &domainspb.RegisterDomainRequest{
            Registration: &domainspb.Registration{
                Name:       fmt.Sprintf("%s/registrations/%s", parent, domaininfo.DomainName),
                DomainName: domaininfo.DomainName,
                DnsSettings: &domainspb.DnsSettings{
                    DnsProvider: &domainspb.DnsSettings_CustomDns_{
                        CustomDns: &domainspb.DnsSettings_CustomDns{
                            NameServers: []string{
                                "ns-cloud-e1.googledomains.com",
                                "ns-cloud-e2.googledomains.com",
                                "ns-cloud-e3.googledomains.com",
                                "ns-cloud-e4.googledomains.com",
                            },
                        },
                    },
                },
                ContactSettings: &dnscontact,
            },
            Parent:      parent,
            YearlyPrice: domaininfo.YearlyPrice,
        }
    
        if _, err := c.RegisterDomain(ctx, req); err != nil {
            return err
        }
    
        return nil
    }
    
    

* * *

## Conclusion

You now have a small website setup with a domain and a secure, static site. Additionally you should have all of the code to modify or extend this solution to fit your environment.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
