---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/configure-dst-connection-private-ip/
title: Configure private IP connectivity for Cloud SQL for PostgreSQL destinations \u00a0|\u00a0 Database Migration Service for heterogeneous SQL Server to Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:01:08.236172+00:00
---

# Configure private IP connectivity for Cloud SQL for PostgreSQL destinations  |  Database Migration Service for heterogeneous SQL Server to Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/configure-dst-connection-private-ip/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ SQL Server to Cloud SQL for PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/scenario-overview)



Send feedback 

#  Configure private IP connectivity for Cloud SQL for PostgreSQL destinations Stay organized with collections  Save and categorize content based on your preferences. 

Database Migration Service uses [ Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) to connect to your destination Cloud SQL instance using a private IP address. With Private Service Connect, you can expose your destination database to incoming secure connections, and control who can access the database.

Network architecture setup for Private Service Connect differs depending on whether you use a PSC-enabled or a non-PSC-enabled destination Cloud SQL instance.

For more information about destination connectivity methods, see [ Destination database connectivity methods overview](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/networking-methods-destination).

### Private Service Connect for PSC-enabled Cloud SQL instances

To use private connectivity with PSC-enabled Cloud SQL for PostgreSQL destinations, follow these steps:

  1. When you [ create and configure the destination instance](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/configure-destination-database), make sure you create it as a PSC-enabled instance with a private IP. You can't modify an existing Cloud SQL instance so that it becomes enabled for Private Service Connect. 
  2. At a later stage, when you [ create the destination connection profile](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/create-destination-connection-profile), in the **Define connectivity method** section, select **Private IP**. 

The **Service attachment name** field is automatically populated with the service attachment created for your destination instance. 




### Private Service Connect for non-PSC-enabled Cloud SQL instances

To use private IP connectivity for Cloud SQL for PostgreSQL destinations that aren't created with Private Service Connect enabled, you need to create additional network components for routing traffic between Database Migration Service and your destination. For more information, see [ Private IP destination connectivity for non-PSC Cloud SQL instances](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/networking-methods-destination#for_non-psc-enabled_instances).

If one bastion virtual machine (VM) is not sufficient for your networking needs, configure an _instance group_ for your network producer setup. For more information, see [ Network connectivity in managed services](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-managed-services).

To create the required Private Service Connect producer setup, we recommend that you use Google Cloud CLI or Terraform automation scripts. Before using any of the command data, make the following replacements:

  * PROJECT_ID with the project in which you create the Private Service Connect producer setup. 
  * REGION with the region in which you create the Private Service Connect producer setup.
  * ZONE with the zone within REGION in which you create all of the zonal resources (for example, the bastion VM). 
  * BASTION with the bastion VM to create.
  * DB_SUBNETWORK with the subnetwork to which the traffic will be forwarded. The subnetwork needs to have access to the Cloud SQL instance. 
  * DB_SUBNETWORK_GATEWAY with the IPv4 gateway of the subnetwork. 
  * CLOUD_SQL_INSTANCE_CONNECTION_NAME with the Cloud SQL instance connection name (formatted as `project:region:name`). 
  * PORT with the port that the bastion will use to expose the underlying database. 
  * CLOUD_SQL_INSTANCE_PRIVATE_IP with the private IP address of the destination Cloud SQL instance. 



### gcloud

The following bash script uses Google Cloud CLI to create the Private Service Connect producer setup for the destination database. Note that some defaults might need to be adjusted; for example, the Private Service Connect subnet [ CIDR ranges](https://docs.cloud.google.com/vpc/docs/alias-ip#subnet_primary_and_secondary_cidr_ranges).
    
    
    #!/bin/bash
    
    # Create the VPC network for the Database Migration Service Private Service Connect.
    gcloud compute networks create dms-psc-vpc \
    --project=PROJECT_ID \
    --subnet-mode=custom
    
    # Create a subnet for the Database Migration Service Private Service Connect.
    gcloud compute networks subnets create dms-psc-REGION \
    --project=PROJECT_ID \
    --range=10.0.0.0/16 --network=dms-psc-vpc \
    --region=REGION
    
    # Create a router required for the bastion to be able to install external
    # packages (for example, Dante SOCKS server):
    gcloud compute routers create ex-router-REGION \
    --network dms-psc-vpc \
    --project=PROJECT_ID \
    --region=REGION
    
    gcloud compute routers nats create ex-nat-REGION \
    --router=ex-router-REGION \
    --auto-allocate-nat-external-ips \
    --nat-all-subnet-ip-ranges \
    --enable-logging \
    --project=PROJECT_ID \
    --region=REGION
    
    # Create the bastion VM.
    gcloud compute instances create BASTION \
        --project=PROJECT_ID \
        --zone=ZONE \
        --image-family=debian-11 \
        --image-project=debian-cloud \
        --network-interface subnet=dms-psc-REGION,no-address \
        --network-interface subnet=DB_SUBNETWORK,no-address \
        --metadata=startup-script='#!/bin/bash
    
    # Route the private IP address using the gateway of the database subnetwork.
    # To find the gateway for the relevant subnetwork go to the VPC network page
    # in the Google Cloud console. Click VPC networks and select the database VPC
    # to see the details.
    ip route add CLOUD_SQL_INSTANCE_PRIVATE_IP via DB_SUBNETWORK_GATEWAY
    
    # Install Dante SOCKS server.
    apt-get install -y dante-server
    
    # Create the Dante configuration file.
    touch /etc/danted.conf
    
    # Create a proxy.log file.
    touch proxy.log
    
    # Add the following configuration for Dante:
    cat > /etc/danted.conf << EOF
    logoutput: /proxy.log
    user.privileged: proxy
    user.unprivileged: nobody
    
    internal: 0.0.0.0 port = PORT
    external: ens5
    
    clientmethod: none
    socksmethod: none
    
    client pass {
            from: 0.0.0.0/0
            to: 0.0.0.0/0
            log: connect error disconnect
    }
    client block {
            from: 0.0.0.0/0
            to: 0.0.0.0/0
            log: connect error
    }
    socks pass {
            from: 0.0.0.0/0
            to: CLOUD_SQL_INSTANCE_PRIVATE_IP/32
            protocol: tcp
            log: connect error disconnect
    }
    socks block {
            from: 0.0.0.0/0
            to: 0.0.0.0/0
            log: connect error
    }
    EOF
    
    # Start the Dante server.
    systemctl restart danted
    
    tail -f proxy.log'
    
    # Create the target instance from the created bastion VM.
    gcloud compute target-instances create bastion-ti-REGION \
    --instance=BASTION \
    --project=PROJECT_ID \
    --instance-zone=ZONE \
    --network=dms-psc-vpc
    
    # Create a forwarding rule for the backend service.
    gcloud compute forwarding-rules create dms-psc-forwarder-REGION \
    --project=PROJECT_ID \
    --region=REGION \
    --load-balancing-scheme=internal \
    --network=dms-psc-vpc \
    --subnet=dms-psc-REGION \
    --ip-protocol=TCP \
    --ports=all \
    --target-instance=bastion-ti-REGION \
    --target-instance-zone=ZONE
    
    # Create a TCP NAT subnet.
    gcloud compute networks subnets create dms-psc-nat-REGION-tcp \
    --network=dms-psc-vpc \
    --project=PROJECT_ID \
    --region=REGION \
    --range=10.1.0.0/16 \
    --purpose=private-service-connect
    
    # Create a service attachment.
    gcloud compute service-attachments create dms-psc-svc-att-REGION \
    --project=PROJECT_ID \
    --region=REGION \
    --producer-forwarding-rule=dms-psc-forwarder-REGION \
    --connection-preference=ACCEPT_MANUAL \
    --nat-subnets=dms-psc-nat-REGION-tcp
    
    # Create a firewall rule allowing the Private Service Connect NAT subnet.
    # access the Private Service Connect subnet
    gcloud compute \
    --project=PROJECT_ID firewall-rules create dms-allow-psc-tcp \
    --direction=INGRESS \
    --priority=1000 \
    --network=dms-psc-vpc \
    --action=ALLOW \
    --rules=all \
    --source-ranges=10.1.0.0/16 \
    --enable-logging
    
    # Print out the created service attachment.
    gcloud compute service-attachments describe dms-psc-svc-att-REGION \
    --project=PROJECT_ID \
    --region=REGION
    
    

### Terraform

The following bash script uses Google Cloud CLI to create the Private Service Connect producer setup for the destination database. Note that some defaults might need to be adjusted; for example, the Private Service Connect subnet [ CIDR ranges](https://docs.cloud.google.com/vpc/docs/alias-ip#subnet_primary_and_secondary_cidr_ranges).

`variables.tf`:
    
    
    variable "project_id" {
      type        = string
      description = <<DESC
    The Google Cloud project in which the setup is created. This should be the same project as
    the one that the Cloud SQL instance belongs to.
    DESC
    }
    
    variable "region" {
      type        = string
      description = "The Google Cloud region in which you create the Private Service Connect
    regional resources."
    }
    
    variable "zone" {
      type        = string
      description = <<DESC
    The Google Cloud zone in which you create the Private Service Connect zonal resources
    (should be in the same region as the one specified in the "region" variable).
    DESC
    }
    
    variable "cloud_sql_instance_name" {
      type        = string
      description = "The Cloud SQL instance name."
    }
    
    variable "port" {
      type        = string
      description = "The port that the bastion will use to expose the underlying database."
      default     = "5432"
    }
    
    variable "cloud_sql_instance_network" {
      type        = string
      description = <<DESC
    The VPC to which the Cloud SQL instance is peered. This is where the bastion will
    forward connections to (the destination database needs to be accessible in this VPC).
    DESC
    }
    

`main.tf`:
    
    
    /* To execute the call:
    terraform apply
    -var="project_id=PROJECT_ID"
    -var="region=REGION"
    -var="zone=ZONE"
    -var="cloud_sql_instance_name=CLOUD_SQL_INSTANCE_NAME"
    -var="port=PORT"
    -var="cloud_sql_instance_network=CLOUD_SQL_INSTANCE_NETWORK" */
    
    locals {
      cloud_sql_instance_connection_name = "${var.project_id}:${var.region}:${var.cloud_sql_instance_name}"
    }
    
    # Needed for getting the private IP address of the Cloud SQL instance.
    data "google_sql_database_instance" "csql_instance" {
      name    = var.cloud_sql_instance_name
      project = var.project_id
    }
    
    # Needed for getting the IPv4 gateway of the subnetwork for the database.
    data "google_compute_subnetwork" "db_network_subnet" {
      name    = var.cloud_sql_instance_network
      project = var.project_id
      region  = var.region
    }
    
    resource "google_compute_network" "psc_sp_network" {
      name                    = "dms-psc-network"
      project                 = var.project_id
      auto_create_subnetworks = false
    }
    
    resource "google_compute_subnetwork" "psc_sp_subnetwork" {
      name    = "dms-psc-subnet"
      region  = var.region
      project = var.project_id
    
      network = google_compute_network.psc_sp_network.id
      # CIDR range can be lower.
      ip_cidr_range = "10.0.0.0/16"
    }
    
    resource "google_compute_subnetwork" "psc_sp_nat" {
      provider = google-beta
      name     = "dms-psc-nat"
      region   = var.region
      project  = var.project_id
    
      network = google_compute_network.psc_sp_network.id
      purpose = "PRIVATE_SERVICE_CONNECT"
      # CIDR range can be lower.
      ip_cidr_range = "10.1.0.0/16"
    }
    
    resource "google_compute_service_attachment" "psc_sp_service_attachment" {
      provider = google-beta
      name     = "dms-psc-svc-att"
      region   = var.region
      project  = var.project_id
    
      enable_proxy_protocol = false
      connection_preference = "ACCEPT_MANUAL"
      nat_subnets           = [google_compute_subnetwork.psc_sp_nat.id]
      target_service        = google_compute_forwarding_rule.psc_sp_target_direct_rule.id
    }
    
    resource "google_compute_forwarding_rule" "psc_sp_target_direct_rule" {
      name       = "dms-psc-fr"
      region     = var.region
      project    = var.project_id
      network    = google_compute_network.psc_sp_network.id
      subnetwork = google_compute_subnetwork.psc_sp_subnetwork.id
    
      load_balancing_scheme = "INTERNAL"
      ip_protocol           = "TCP"
      all_ports             = true
    
      target = google_compute_target_instance.psc_sp_target.id
    
    }
    
    resource "google_compute_target_instance" "psc_sp_target" {
      provider = google-beta
      name     = "dms-psc-fr-target"
      zone     = var.zone
      instance = google_compute_instance.psc_sp_bastion.id
      network  = google_compute_network.psc_sp_network.id
    }
    
    resource "google_compute_instance" "psc_sp_bastion" {
      name           = "dms-psc-cloud-sql-bastion"
      project        = var.project_id
      machine_type   = "e2-medium"
      zone           = var.zone
      can_ip_forward = true
    
      boot_disk {
        initialize_params {
          image = "debian-cloud/debian-11"
        }
      }
    
      # The incoming NIC defines the default gateway which must be the Private Service Connect subnet.
      network_interface {
        network    = google_compute_network.psc_sp_network.id
        subnetwork = google_compute_subnetwork.psc_sp_subnetwork.id
      }
    
      # The outgoing NIC which is on the same network as the Cloud SQL instance.
      network_interface {
        network = data.google_compute_subnetwork.db_network_subnet.network
      }
    
      metadata_startup_script = <<SCRIPT
    
    #!/bin/bash
    
    # Route the private IP address of the database using the gateway of the database subnetwork.
    # To find the gateway for the relevant subnetwork, go to the VPC network page
    # in the Google Cloud console. Click VPC networks, and select the database VPC
    # to see the details.
    ip route add ${data.google_sql_database_instance.csql_instance.private_ip_address} \
    via ${data.google_compute_subnetwork.db_network_subnet.gateway_address}
    
    # Install Dante SOCKS server.
    apt-get install -y dante-server
    
    # Create the Dante configuration file.
    touch /etc/danted.conf
    
    # Create a proxy.log file.
    touch proxy.log
    
    # Add the following configuration for Dante:
    cat > /etc/danted.conf << EOF
    logoutput: /proxy.log
    user.privileged: proxy
    user.unprivileged: nobody
    
    internal: 0.0.0.0 port = ${var.port}
    external: ens5
    
    clientmethod: none
    socksmethod: none
    
    client pass {
            from: 0.0.0.0/0
            to: 0.0.0.0/0
            log: connect error disconnect
    }
    client block {
            from: 0.0.0.0/0
            to: 0.0.0.0/0
            log: connect error
    }
    socks pass {
            from: 0.0.0.0/0
            to: ${data.google_sql_database_instance.csql_instance.private_ip_address}/32
            protocol: tcp
            log: connect error disconnect
    }
    socks block {
            from: 0.0.0.0/0
            to: 0.0.0.0/0
            log: connect error
    }
    EOF
    
    # Start the Dante server.
    systemctl restart danted
    
    tail -f proxy.log
    
    SCRIPT
    }
    
    # Required firewall rules:
    
    /* Firewall rule allowing the Private Service Connect NAT subnet to access
    the Private Service Connect subnet. */
    resource "google_compute_firewall" "psc_sp_in_fw" {
      name    = "dms-psc-ingress-nat-fw"
      project = var.project_id
      network = google_compute_network.psc_sp_network.id
    
      log_config {
        metadata = "INCLUDE_ALL_METADATA"
      }
    
      allow {
        protocol = "all"
      }
    
      priority  = 1000
      direction = "INGRESS"
      source_ranges = [google_compute_subnetwork.psc_sp_nat.ip_cidr_range]
    }
    
    /* The router that the bastion VM uses to install external packages
    (for example, Dante SOCKS server). */
    
    resource "google_compute_router" "psc_sp_ex_router" {
      name    = "dms-psc-external-router"
      project = var.project_id
      region  = var.region
      network = google_compute_network.psc_sp_network.id
    }
    
    resource "google_compute_router_nat" "psc_sp_ex_router_nat" {
      name    = "dms-psc-external-router-nat"
      project = var.project_id
      region  = var.region
      router  = google_compute_router.psc_sp_ex_router.name
    
      nat_ip_allocate_option             = "AUTO_ONLY"
      source_subnetwork_ip_ranges_to_nat = "ALL_SUBNETWORKS_ALL_IP_RANGES"
    
      log_config {
        enable = true
        filter = "ERRORS_ONLY"
      }
    }
    
    

`outputs.tf`:
    
    
    # The Private Service Connect service attachment.
    output "service_attachment" {
      value = google_compute_service_attachment.psc_sp_service_attachment.id
    }
    
    

At a later stage, when you [ create the destination connection profile](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/create-destination-connection-profile), do the following: 

  1. In the **Define connectivity method** section, select **Private IP**.
  2. From the **Service attachment name** drop-down menu, select **dms-psc-svc-att- REGION**. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
