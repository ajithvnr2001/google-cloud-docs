---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/quickstarts/create-multi-tenant-cluster/
title: Create a multi-tenant cluster using Terraform \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:34.882683+00:00
---

# Create a multi-tenant cluster using Terraform  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/quickstarts/create-multi-tenant-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a multi-tenant cluster using Terraform

A multi-tenant cluster in Google Kubernetes Engine is a Kubernetes cluster shared by multiple distinct teams or users, known as tenants. Each tenant typically has its own set of resources and applications within the cluster.

This Terraform tutorial lets you quickly create a GKE cluster shared by two teams, `backend` and `frontend`, that can deploy team-specific workloads on the cluster. This tutorial assumes that you are already familiar with Terraform. If not, you can use the following resources to get familiar with the basics of Terraform:

  * [Getting Started with Terraform](https://youtu.be/BUPenAjobjw?si=P9LH0iG3Ce_pu4mK) (video)
  * [Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands)

**What is Terraform?** Infrastructure as Code (IaC) is a practice of managing and provisioning software infrastructure resources using code. Terraform is a popular open source IaC tool created by HashiCorp that supports a wide range of Cloud services, including GKE. As a GKE platform administrator, you can use Terraform to standardize configuration of your Kubernetes clusters in production and streamline your DevOps workflows. To learn more, see [Terraform support for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/resources/use-terraform-gke). 

## Before you begin

Take the following steps to enable the Kubernetes Engine API:

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the GKE, GKE GKE Fleet, Cloud SQL, Resource Manager, IAM, Connect gateway APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,gkehub.googleapis.com,sqladmin.googleapis.com,cloudresourcemanager.googleapis.com,iam.googleapis.com,connectgateway.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the GKE, GKE GKE Fleet, Cloud SQL, Resource Manager, IAM, Connect gateway APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,gkehub.googleapis.com,sqladmin.googleapis.com,cloudresourcemanager.googleapis.com,iam.googleapis.com,connectgateway.googleapis.com)

  8. Make sure that you have the following role or roles on the project: roles/owner, roles/iam.serviceAccountTokenCreator 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 



## Prepare the environment

In this tutorial you use [Cloud Shell](https://docs.cloud.google.com/shell) to manage resources hosted on Google Cloud. Cloud Shell is preinstalled with the software you need for this tutorial, including [Terraform](https://docs.cloud.google.com/docs/terraform), [`kubectl`](https://kubernetes.io/docs/reference/kubectl/), and the the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

  1. Launch a Cloud Shell session from the Google Cloud console, by clicking the Cloud Shell activation icon **Activate Cloud Shell** ![Activate Shell Button](https://docs.cloud.google.com/static/kubernetes-engine/images/cloud-shell.png). This launches a session in the bottom pane of the Google Cloud console.

The service credentials associated with this virtual machine are automatic, so you don't have to set up or download a service account key.

  2. Before you run commands, set your default project in the gcloud CLI using the following command:
         
         gcloud config set project PROJECT_ID
         

Replace `PROJECT_ID` with your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

  3. Clone the GitHub repository:
         
         git clone https://github.com/terraform-google-modules/terraform-docs-samples.git --single-branch
         

  4. Change to the working directory:
         
         cd terraform-docs-samples/gke/quickstart/multitenant
         




## Review the Terraform files

The [Google Cloud provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs) is a plugin that lets you manage and provision Google Cloud resources using Terraform. It serves as a bridge between Terraform configurations and Google Cloud APIs, letting you declaratively define infrastructure resources, such as virtual machines and networks.

  1. Review the `main.tf` file, which describes a GKE cluster resource:
         
         cat main.tf
         

The output is similar to the following:
         
         resource "google_container_cluster" "default" {
           name               = "gke-enterprise-cluster"
           location           = "us-central1"
           initial_node_count = 3
           fleet {
             project = data.google_project.default.project_id
           }
           workload_identity_config {
             workload_pool = "${data.google_project.default.project_id}.svc.id.goog"
           }
           security_posture_config {
             mode               = "BASIC"
             vulnerability_mode = "VULNERABILITY_ENTERPRISE"
           }
           depends_on = [
             google_gke_hub_feature.policycontroller,
             google_gke_hub_namespace.default
           ]
           # Set `deletion_protection` to `true` will ensure that one cannot
           # accidentally delete this instance by use of Terraform.
           deletion_protection = false
         }
         
         resource "google_gke_hub_membership_binding" "default" {
           for_each = google_gke_hub_scope.default
         
           project               = data.google_project.default.project_id
           membership_binding_id = each.value.scope_id
           scope                 = each.value.name
           membership_id         = google_container_cluster.default.fleet[0].membership_id
           location              = google_container_cluster.default.fleet[0].membership_location
         }




## Create a cluster and SQL database

  1. In Cloud Shell, run this command to verify that Terraform is available:
         
         terraform
         

The output should be similar to the following:
         
         Usage: terraform [global options] <subcommand> [args]
         
         The available commands for execution are listed below.
         The primary workflow commands are given first, followed by
         less common or more advanced commands.
         
         Main commands:
           init          Prepare your working directory for other commands
           validate      Check whether the configuration is valid
           plan          Show changes required by the current configuration
           apply         Create or update infrastructure
           destroy       Destroy previously-created infrastructure
         

  2. Initialize Terraform:
         
         terraform init
         

  3. Optional: Plan the Terraform configuration:
         
         terraform plan
         

  4. Apply the Terraform configuration
         
         terraform apply
         

When prompted, enter `yes` to confirm actions. This command might take several minutes to complete. The output is similar to the following:
         
         Apply complete! Resources: 23 added, 0 changed, 0 destroyed.
         




## Deploy the backend team application

  1. Review the following Terraform file:
         
         cat backend.yaml
         

The output should be similar to the following:
         
         apiVersion: v1
         kind: ConfigMap
         metadata:
           name: backend-configmap
           namespace: backend-team
           labels:
             app: backend
         data:
           go.mod: |
             module multitenant
         
             go 1.22
         
             require github.com/go-sql-driver/mysql v1.8.1
         
             require filippo.io/edwards25519 v1.1.0 // indirect
         
           go.sum: |
             filippo.io/edwards25519 v1.1.0 h1:FNf4tywRC1HmFuKW5xopWpigGjJKiJSV0Cqo0cJWDaA=
             filippo.io/edwards25519 v1.1.0/go.mod h1:BxyFTGdWcka3PhytdK4V28tE5sGfRvvvRV7EaN4VDT4=
             github.com/go-sql-driver/mysql v1.8.1 h1:LedoTUt/eveggdHS9qUFC1EFSa8bU2+1pZjSRpvNJ1Y=
             github.com/go-sql-driver/mysql v1.8.1/go.mod h1:wEBSXgmK//2ZFJyE+qWnIsVGmvmEKlqwuVSjsCm7DZg=
         
           backend.go: |
             package main
         
             import (
               "database/sql"
               "fmt"
               "log"
               "math/rand"
               "net/http"
               "os"
         
               _ "github.com/go-sql-driver/mysql"
             )
         
             func main() {
               mux := http.NewServeMux()
               mux.HandleFunc("/", frontend)
         
               port := "8080"
         
               log.Printf("Server listening on port %s", port)
               log.Fatal(http.ListenAndServe(":"+port, mux))
             }
         
             func frontend(w http.ResponseWriter, r *http.Request) {
               log.Printf("Serving request: %s", r.URL.Path)
         
               host, _ := os.Hostname()
               fmt.Fprintf(w, "Backend!\n")
               fmt.Fprintf(w, "Hostname: %s\n", host)
         
               // Open database using cloud-sql-proxy sidecar
               db, err := sql.Open("mysql", "multitenant-app@tcp/multitenant-app")
               if err != nil {
                 fmt.Fprintf(w, "Error: %v\n", err)
                 return
               }
         
               // Create metadata Table if not exists
               _, err = db.Exec("CREATE TABLE IF NOT EXISTS metadata (metadata_key varchar(255) NOT NULL, metadata_value varchar(255) NOT NULL, PRIMARY KEY (metadata_key))")
               if err != nil {
                 fmt.Fprintf(w, "Error: %v\n", err)
                 return
               }
         
               // Pick random primary color
               var color string
               randInt := rand.Intn(3) + 1
               switch {
               case randInt == 1:
                 color = "red"
               case randInt == 2:
                 color = "green"
               case randInt == 3:
                 color = "blue"
               }
         
               // Set color in database
               _, err = db.Exec(fmt.Sprintf("REPLACE INTO metadata (metadata_key, metadata_value) VALUES ('color', '%s')", color))
               if err != nil {
                 fmt.Fprintf(w, "Error: %v\n", err)
                 return
               }
         
               fmt.Fprintf(w, "Set Color: %s\n", color)
             }
         
         ---
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: backendweb
           namespace: backend-team
           labels:
             app: backend
         spec:
           selector:
             matchLabels:
               app: backend
               tier: web
           template:
             metadata:
               labels:
                 app: backend
                 tier: web
             spec:
               containers:
               - name: backend-container
                 image: golang:1.22
                 command: ["go"]
                 args: ["run", "."]
                 workingDir: "/tmp/backend"
                 volumeMounts:
                   - name: backend-configmap
                     mountPath: /tmp/backend/
                     readOnly: true
               - name: cloud-sql-proxy
                 image: gcr.io/cloud-sql-connectors/cloud-sql-proxy:2.11.4
                 args:
                   - "--structured-logs"
                   - "--port=3306"
                   - "$(CONNECTION_NAME_KEY)"
                 securityContext:
                   runAsNonRoot: true
                 env:
                 - name: CONNECTION_NAME_KEY
                   valueFrom:
                     configMapKeyRef:
                       name: database-configmap
                       key: CONNECTION_NAME
               volumes:
                 - name: backend-configmap
                   configMap: { name: backend-configmap }
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: backendweb
           namespace: backend-team
           labels:
             app: backend
           annotations:
             networking.gke.io/load-balancer-type: "Internal" # Remove to create an external loadbalancer
         spec:
           selector:
             app: backend
             tier: web
           ports:
           - port: 80
             targetPort: 8080
           type: LoadBalancer

This file describes the following resources:

     * A [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) with a sample application.
     * A [Service of type LoadBalancer](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer). The Service exposes the Deployment on port 80. To expose your application to the internet, configure an external load balancer by removing the `networking.gke.io/load-balancer-type` annotation.
  2. In Cloud Shell, run the following command to impersonate the backend team's service account:
         
         gcloud config set auth/impersonate_service_account backend@PROJECT_ID.iam.gserviceaccount.com
         

Replace `PROJECT_ID` with your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

  3. Retrieve the cluster credentials:
         
         gcloud container fleet memberships get-credentials gke-enterprise-cluster --location us-central1
         

  4. Apply the backend team's manifest to the cluster:
         
         kubectl apply -f backend.yaml
         




## Verify the backend application is working

Do the following to confirm your cluster is running correctly:

  1. Go to the **Workloads** page in the Google Cloud console:

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload)

  2. Click the `backend` workload. The Pod details page displays. This page shows information about the Pod, such as annotations, containers running on the Pod, Services exposing the Pod, and metrics including CPU, Memory, and Disk usage.

  3. Click the `backend` LoadBalancer Service. The Service details page displays. This page shows information about the Service, such as the Pods associated with the Service, and the ports the Services uses.

  4. In the **Endpoints** section, click the **IPv4 link** to view your Service in the browser. The output is similar to the following:
         
         Backend!
         Hostname: backendweb-765f6c4fc9-cl7jx
         Set Color: green
         

Whenever a user accesses the backend endpoint, the Service randomly picks and stores a color from red, green, or blue in the shared database.




## Deploy a frontend team application

  1. Review the following Terraform file:
         
         cat frontend.yaml
         

The output should be similar to the following:
         
         apiVersion: v1
         kind: ConfigMap
         metadata:
           name: frontend-configmap
           namespace: frontend-team
           labels:
             app: frontend
         data:
           go.mod: |
             module multitenant
         
             go 1.22
         
             require github.com/go-sql-driver/mysql v1.8.1
         
             require filippo.io/edwards25519 v1.1.0 // indirect
         
           go.sum: |
             filippo.io/edwards25519 v1.1.0 h1:FNf4tywRC1HmFuKW5xopWpigGjJKiJSV0Cqo0cJWDaA=
             filippo.io/edwards25519 v1.1.0/go.mod h1:BxyFTGdWcka3PhytdK4V28tE5sGfRvvvRV7EaN4VDT4=
             github.com/go-sql-driver/mysql v1.8.1 h1:LedoTUt/eveggdHS9qUFC1EFSa8bU2+1pZjSRpvNJ1Y=
             github.com/go-sql-driver/mysql v1.8.1/go.mod h1:wEBSXgmK//2ZFJyE+qWnIsVGmvmEKlqwuVSjsCm7DZg=
         
           frontend.go: |
             package main
         
             import (
               "database/sql"
               "fmt"
               "log"
               "net/http"
               "os"
         
               _ "github.com/go-sql-driver/mysql"
             )
         
             func main() {
               mux := http.NewServeMux()
               mux.HandleFunc("/", frontend)
         
               port := "8080"
         
               log.Printf("Server listening on port %s", port)
               log.Fatal(http.ListenAndServe(":"+port, mux))
             }
         
             func frontend(w http.ResponseWriter, r *http.Request) {
               log.Printf("Serving request: %s", r.URL.Path)
         
               host, _ := os.Hostname()
               fmt.Fprintf(w, "Frontend!\n")
               fmt.Fprintf(w, "Hostname: %s\n", host)
         
               // Open database using cloud-sql-proxy sidecar
               db, err := sql.Open("mysql", "multitenant-app@tcp/multitenant-app")
               if err != nil {
                 fmt.Fprint(w, "Error: %v\n", err)
                 return
               }
         
               // Retrieve color from the database
               var color string
               err = db.QueryRow("SELECT metadata_value FROM metadata WHERE metadata_key='color'").Scan(&color)
               switch {
               case err == sql.ErrNoRows:
                 fmt.Fprintf(w, "Error: color not found in database\n")
               case err != nil:
                 fmt.Fprintf(w, "Error: %v\n", err)
               default:
                 fmt.Fprintf(w, "Got Color: %s\n", color)
               }
             }
         
         ---
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: frontendweb
           namespace: frontend-team
           labels:
             app: frontend
         spec:
           selector:
             matchLabels:
               app: frontend
               tier: web
           template:
             metadata:
               labels:
                 app: frontend
                 tier: web
             spec:
               containers:
               - name: frontend-container
                 image: golang:1.22
                 command: ["go"]
                 args: ["run", "."]
                 workingDir: "/tmp/frontend"
                 volumeMounts:
                   - name: frontend-configmap
                     mountPath: /tmp/frontend/
                     readOnly: true
               - name: cloud-sql-proxy
                 image: gcr.io/cloud-sql-connectors/cloud-sql-proxy:2.11.4
                 args:
                   - "--structured-logs"
                   - "--port=3306"
                   - "$(CONNECTION_NAME_KEY)"
                 securityContext:
                   runAsNonRoot: true
                 env:
                 - name: CONNECTION_NAME_KEY
                   valueFrom:
                     configMapKeyRef:
                       name: database-configmap
                       key: CONNECTION_NAME
               volumes:
                 - name: frontend-configmap
                   configMap: { name: frontend-configmap }
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: frontendweb
           namespace: frontend-team
           labels:
             app: frontend
           annotations:
             networking.gke.io/load-balancer-type: "Internal" # Remove to create an external loadbalancer
         spec:
           selector:
             app: frontend
             tier: web
           ports:
           - port: 80
             targetPort: 8080
           type: LoadBalancer

This file describes the following resources:

     * A [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) with a sample application.
     * A [Service of type LoadBalancer](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer). The Service exposes the Deployment on port 80. To expose your application to the internet, configure an external load balancer by removing the `networking.gke.io/load-balancer-type` annotation.
  2. In Cloud Shell, run the following command to impersonate the frontend team's service account:
         
         gcloud config set auth/impersonate_service_account frontend@PROJECT_ID.iam.gserviceaccount.com
         

Replace `PROJECT_ID` with your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

  3. Retrieve the cluster credentials:
         
         gcloud container fleet memberships get-credentials gke-enterprise-cluster --location us-central1
         

  4. Apply the frontend team's manifest to the cluster:
         
         kubectl apply -f frontend.yaml
         




## Verify the frontend application is working

Do the following to confirm your cluster is running correctly:

  1. Go to the **Workloads** page in the Google Cloud console:

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload)

  2. Click the `frontend` workload. The Pod details page displays. This page shows information about the Pod, such as annotations, containers running on the Pod, Services exposing the Pod, and metrics including CPU, Memory, and Disk usage.

  3. Click the `frontend` LoadBalancer Service. The Service details page displays. This page shows information about the Service, such as the Pods associated with the Service, and the ports the Services uses.

  4. In the **Endpoints** section, click the **IPv4 link** to view your Service in the browser. The output is similar to the following:
         
         Frontend!
         Hostname: frontendweb-5cd888d88f-gwwtc
         Got Color: green
         




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. In Cloud Shell, run this command to unset service account impersonation:
         
         gcloud config unset auth/impersonate_service_account
         

  2. Run the following command to delete the Terraform resources:
         
         terraform destroy --auto-approve
         




## What's next

  * Explore the [Terraform resources for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/terraform#resources).

  * Explore opinionated configuration samples in the [Terraform GKE module](https://github.com/terraform-google-modules/terraform-google-kubernetes-engine) GitHub repository.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
