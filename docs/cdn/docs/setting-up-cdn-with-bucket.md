---
url: https://docs.cloud.google.com/cdn/docs/setting-up-cdn-with-bucket/
title: Set up a backend bucket \u00a0|\u00a0 Cloud CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:30:49.390101+00:00
---

# Set up a backend bucket  |  Cloud CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cdn/docs/setting-up-cdn-with-bucket/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud CDN ](https://docs.cloud.google.com/cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/cdn/docs/overview)



Send feedback 

#  Set up a backend bucket Stay organized with collections  Save and categorize content based on your preferences. 

Cloud CDN leverages your choice of either the global external Application Load Balancer or the classic Application Load Balancer to provide routing, health checking, and anycast IP support. Because global external Application Load Balancers can have [multiple backend instance types](https://docs.cloud.google.com/load-balancing/docs/features#backends)— Compute Engine VM instances, Google Kubernetes Engine Pods, Cloud Storage buckets, or external backends outside of Google Cloud—you can choose which backends (_origins_) to enable Cloud CDN for.

This setup guide shows you how to create an external Application Load Balancer with Cloud CDN enabled. The example uses the following resources:

  * The default Virtual Private Cloud (VPC) network
  * A default URL map
  * A reserved external IP address
  * A Cloud Storage bucket as the backend
  * A single load balancer backend bucket that acts as a wrapper around the Cloud Storage bucket



A backend bucket supports the following:

  * Cloud Storage buckets of any [storage class](https://docs.cloud.google.com/storage/docs/storage-classes), including [multi-region](https://docs.cloud.google.com/storage/docs/locations#location-mr) buckets
  * Cloud CDN policies for caching content at Google's global edge



To learn how Cloud CDN works, see the [Cloud CDN overview](https://docs.cloud.google.com/cdn/docs/overview).

By default, Cloud Storage [uses the same cache](https://docs.cloud.google.com/storage/docs/caching) that Cloud CDN uses. If you enable Cloud CDN on the backend bucket, you can use Cloud CDN controls on your content. Cloud CDN controls include, for example, cache modes, signed URLs, and invalidation. Cloud CDN also lets you cache large content (> 10 MB). If you don't enable Cloud CDN on your backend bucket, you can only use origin `Cache-Control` headers to control caching for smaller content, as set by the Cloud Storage metadata. When Cloud CDN is enabled, you can utilize both `CDN-Cache-Control` and standard `Cache-Control` origin headers to manage edge caching behavior.

## Load balancer backends

An external Application Load Balancer uses a URL map to direct traffic from specified URLs to specified services. The following table summarizes the types of backends where you can host content and services.

Load balancer backend configuration | Typical media type | Backend types  
---|---|---  
Backend service | Dynamic (such as data) | 

  * Unmanaged instance groups
  * Managed instance groups
  * Network endpoint groups internal to Google Cloud
  * Network endpoint groups external to Google Cloud

  
Backend bucket | Static (such as images) | 

  * Cloud Storage buckets (discussed on this page)

  
  
## Before you begin

  * If you're using HTTPS for the frontend, create an [SSL certificate](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates), either [self-managed](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs) or [Google-managed](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs). We recommend using a Google-managed certificate.
  * If you're using the Google Cloud CLI, see [Discover object storage with the gcloud tool](https://docs.cloud.google.com/storage/docs/discover-object-storage-gcloud) to install it.
  * [Set a default project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set).




###  Console 

**Note:** For global external Application Load Balancers, the Google Cloud console isn't supported.

  1. In the Google Cloud console, go to the **Home** page. 

[Go to the Google Cloud home page](https://console.cloud.google.com/home/)

  2. To the right of Google Cloud, select a project from the pull-down menu.



###  gcloud 
    
    
         gcloud config set project PROJECT_ID
       

Replace `PROJECT_ID` with your Google Cloud project ID.

###  Terraform 
    
    
        export GOOGLE_CLOUD_PROJECT=PROJECT_ID
       

## Reserve an external IP address

Now that your Cloud Storage bucket is up and running, set up a [global static external IP address](https://docs.cloud.google.com/compute/docs/ip-addresses#externaladdresses) that your customers use to reach your load balancer.

This step is optional, but recommended, because a static external IP address provides a single address to point your domain at.

**Note:** You can skip this step and have Google Cloud associate an ephemeral IP address with your load balancer's forwarding rule. An ephemeral IP address remains constant while the forwarding rule exists. If you need to delete the forwarding rule and re-add it, the forwarding rule might receive a new IP address.

###  Console 

**Note:** For global external Application Load Balancers, the Google Cloud console isn't supported.

  1. In the Google Cloud console, go to the **External IP addresses** page. 

[Go to the External IP addresses page](https://console.cloud.google.com/addresses/list)

  2. To reserve an IPv4 address, click **Reserve static address**.
  3. Assign a **Name** of `example-ip`.
  4. Set the **Network Service Tier** to **Premium**.
  5. Set the **IP version** to **IPv4**.
  6. Set the **Type** to **Global**.
  7. Click **Reserve**.



###  gcloud 
    
    
    gcloud compute addresses create example-ip \
        --network-tier=PREMIUM \
        --ip-version=IPV4 \
        --global
    

Note the IPv4 address that was reserved:
    
    
    gcloud compute addresses describe example-ip \
        --format="get(address)" \
        --global
    

###  Terraform 

To reserve an IP address, use the [`google_compute_global_address` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_global_address).
    
    
    # reserve IP address
    resource "google_compute_global_address" "default" {
      name = "example-ip"
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

### Optional: Use BYOIP addresses

With bring your own IP (BYOIP), you can import your own public addresses to Google Cloud to use the addresses with Google Cloud resources. For example, if you import your own IPv4 addresses, you can assign one to the forwarding rule when you configure your load balancer. When you follow the instructions in this document to [Create the external Application Load Balancer](https://docs.cloud.google.com/cdn/docs/setting-up-cdn-with-bucket#create_the), provide the BYOIP address as the **IP address**.

For more information about using BYOIP, see [Bring your own IP addresses](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip).

## Create a Cloud Storage bucket

If you have an existing Cloud Storage bucket that isn't already assigned to a load balancer, you can skip to the next step.

When you create a Cloud Storage bucket to use as the backend for an external Application Load Balancer with Cloud CDN, we recommend that you choose a [multi-region bucket](https://docs.cloud.google.com/storage/docs/locations#location-mr), which automatically replicates objects across multiple Google Cloud regions. This can improve the availability of your content and improve failure tolerance across your application.

###  Console 

**Note:** For global external Application Load Balancers, the Google Cloud console isn't supported.

  1. In the Google Cloud console, open the **Cloud Storage Buckets** page. 

[Open the Buckets page](https://console.cloud.google.com/storage/browser)

  2. Click **Create bucket**.
  3. Specify values for the fields in the following table, leaving all others at their defaults.

Property | Value (type the value or select an option as specified)  
---|---  
Name | For each bucket, enter a globally unique name. _If the name you enter is not unique, you see a message to try another name._  
Location type | **Multi-region**  
Location | Select a region, such as **us (multiple regions in United States)**.  
Default storage class | **Standard**  
Access control | **Uniform**  
  4. Click **Create**.

  5. Note the name of the newly created Cloud Storage bucket for the next step.




###  gcloud 
    
    
    gcloud storage buckets create gs://BUCKET_NAME --project=PROJECT_ID --default-storage-class=standard --location=us-east1 --uniform-bucket-level-access
    

###  Terraform 

To create a bucket, use the [`google_storage_bucket` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket).
    
    
    # Cloud Storage bucket
    resource "random_id" "bucket_prefix" {
      byte_length = 8
    }
    
    resource "google_storage_bucket" "default" {
      name                        = "${random_id.bucket_prefix.hex}-my-bucket"
      location                    = "us-east1"
      uniform_bucket_level_access = true
      storage_class               = "STANDARD"
      // delete bucket and contents on destroy.
      force_destroy = true
      // Assign specialty files
      website {
        main_page_suffix = "index.html"
        not_found_page   = "404.html"
      }
    }
    

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

## Copy a graphic file into your Cloud Storage bucket

To enable you to test the setup, copy a graphic file from a public Cloud Storage bucket to your own Cloud Storage bucket.

###  gcloud 

Run the following command in Cloud Shell. Replace `BUCKET_NAME` with your unique Cloud Storage bucket name:
    
    
    gcloud storage cp gs://gcp-external-http-lb-with-bucket/three-cats.jpg gs://BUCKET_NAME/never-fetch/
    

###  Terraform 

To copy the object, use the [`local-exec Provisioner`](https://www.terraform.io/language/resources/provisioners/local-exec) with the `gcloud storage cp` command.
    
    
    resource "null_resource" "upload_image" {
      provisioner "local-exec" {
        command = "gcloud storage cp gs://gcp-external-http-lb-with-bucket/three-cats.jpg gs://${google_storage_bucket.default.name}/never-fetch/ --recursive"
      }
    }
    

Alternatively, to upload an object, use the [`google_storage_bucket_object` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket_object).
    
    
    # image object for testing, try to access http://<your_lb_ip_address>/test.jpg
    resource "google_storage_bucket_object" "test_image" {
      name = "test-object"
      # Uncomment and add valid path to an object.
      #  source       = "/path/to/an/object"
      #  content_type = "image/jpeg"
    
      # Delete after uncommenting above source and content_type attributes
      content      = "Data as string to be uploaded"
      content_type = "text/plain"
    
      bucket = google_storage_bucket.default.name
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

In the Google Cloud console, click **Refresh** to verify that the graphic file is copied.

## Create the external Application Load Balancer

In this procedure, you create the load balancer's backend bucket, which serves as a wrapper for your Cloud Storage bucket. When creating or editing a backend bucket, you can enable Cloud CDN.

###  Console 

#### Start the external Application Load Balancer configuration process

  1. In the Google Cloud console, go to the **Load balancing** page. 

[Go to the Load balancing page](https://console.cloud.google.com/networking/loadbalancing/add)

  2. Under **HTTP(S) load balancing** , click **Start configuration**.
  3. Select **From Internet to my VMs** , and then click **Continue**.
  4. Under **[Advanced traffic management](https://docs.cloud.google.com/load-balancing/docs/https#load-balancer-mode)** , select one of the following: 
     * For classic Application Load Balancers, select **Classic HTTP(S) Load Balancer**.
     * For global external Application Load Balancers, select **HTTP(S) Load Balancer with Advanced Traffic Management**.
  5. Set **Name** to `http-lb`, and then go to the next step.



#### Configure the backend and enable Cloud CDN

Create the load balancer's backend bucket, which serves as a wrapper for your Cloud Storage bucket. When creating or editing a backend bucket, you can enable Cloud CDN.

  1. Click **Backend configuration**.
  2. Under **Backend services & backend buckets**, click **Create or select backend services & backend buckets**, and then click **Backend buckets > Create a backend bucket**.
  3. Set the **Name** to `cat-backend-bucket`. This name doesn't need to be globally unique and can be different from the name of the actual Cloud Storage bucket.
  4. Under **Cloud Storage bucket** , click **Browse**.
  5. Select the Cloud Storage globally unique `BUCKET_NAME` that you created, and then click **Select**.
  6. Click **Enable Cloud CDN**.

**Important:** Make sure that you select **Enable Cloud CDN** at this step. Forgetting to do this causes objects to be served directly from the Cloud Storage bucket and not from Google's global CDN caches.
  7. (Optional) Modify the [cache mode](https://docs.cloud.google.com/cdn/docs/using-cache-modes) and [TTL](https://docs.cloud.google.com/cdn/docs/using-ttl-overrides) settings.

  8. Click **Create**.




#### Configure host rules and path matchers

Host rules and path matchers are configuration components of an external Application Load Balancer's [URL map](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts).

In **Host and path rules** , you can retain the default settings.

For a customized setup example, see [Adding backend buckets to load balancers](https://docs.cloud.google.com/load-balancing/docs/https/adding-backend-buckets-to-load-balancers).

To learn more about host rules and path matchers, see [URL maps overview](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts).

#### Configure the frontend

  1. Click **Frontend configuration**.
  2. Verify that the options are configured with these values.

Property | Value (type a value or select an option as specified)  
---|---  
Protocol | **HTTP**  
Network Service Tier | **Premium**  
IP version | **IPv4**  
IP address | `example-ip`  
Port | **80**  
  
If you want to create an HTTPS load balancer instead of an HTTP load balancer, you must have an [SSL certificate](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates) (`gcloud compute ssl-certificates list`), and you must fill in the fields as follows.

Property | Value (type a value or select an option as specified)  
---|---  
Protocol | **HTTPS**  
Network Service Tier | **Premium**  
IP version | **IPv4**  
IP address | `example-ip`  
Port | **443**  
Certificate | **Select a certificate** or **Create a new certificate**  
  3. Click **Done**.




#### Review the configuration

  1. Click **Review and finalize**.
  2. Review the **Backend buckets** , **Host and path rules** , and **Frontend** sections.
  3. Click **Create**.
  4. Wait for the load balancer to be created.
  5. Click the name of the load balancer (**http-lb**).
  6. Note the IP address of the load balancer for the next task. It's referred to as `IP_ADDRESS`.



###  gcloud 

#### Configure the backend
    
    
    gcloud compute backend-buckets create cat-backend-bucket \
        --gcs-bucket-name=BUCKET_NAME \
        --enable-cdn \
        --cache-mode=CACHE_MODE
    

Set the [cache mode](https://docs.cloud.google.com/cdn/docs/caching#cache-modes) by replacing CACHE_MODE with one of the following:

  * `CACHE_ALL_STATIC` or `USE_ORIGIN_HEADERS`: Uses the headers set according to [cache control metadata](https://docs.cloud.google.com/storage/docs/metadata#cache-control) in Cloud Storage. Cloud Storage always provides a `Cache-Control` header to Cloud CDN. If no value is explicitly chosen, it sends a default value.

  * `FORCE_CACHE_ALL`: Caches all content, ignoring any `private`, `no-store`, or `no-cache` directives in `Cache-Control` response headers sent by Cloud Storage.




#### Configure the URL map
    
    
    gcloud compute url-maps create http-lb \
        --default-backend-bucket=cat-backend-bucket
    

#### Configure the target proxy
    
    
    gcloud compute target-http-proxies create http-lb-proxy \
        --url-map=http-lb
    

#### Configure the forwarding rule

  * For a global external Application Load Balancer, use the gcloud CLI command with `load-balancing-scheme=EXTERNAL_MANAGED`. This setting offers [advanced traffic management capability](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management-global).
  * For an classic Application Load Balancer, use `load-balancing-scheme=EXTERNAL`.


    
    
    gcloud compute forwarding-rules create http-lb-forwarding-rule \
        --load-balancing-scheme=LOAD_BALANCING_SCHEME \
        --network-tier=PREMIUM \
        --address=example-ip \
        --global \
        --target-http-proxy=http-lb-proxy \
        --ports=80
    

###  Terraform 

#### Configure the backend

To configure the backend, use the [`google_compute_backend_bucket` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_backend_bucket).
    
    
    # backend bucket with CDN policy with default ttl settings
    resource "google_compute_backend_bucket" "default" {
      name        = "cat-backend-bucket"
      description = "Contains beautiful images"
      bucket_name = google_storage_bucket.default.name
      enable_cdn  = true
      cdn_policy {
        cache_mode        = "CACHE_ALL_STATIC"
        client_ttl        = 3600
        default_ttl       = 3600
        max_ttl           = 86400
        negative_caching  = true
        serve_while_stale = 86400
      }
    }

#### Configure the URL map

To configure the backend, use the [`google_compute_url_map` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_url_map).
    
    
    # url map
    resource "google_compute_url_map" "default" {
      name            = "http-lb"
      default_service = google_compute_backend_bucket.default.id
    }

#### Configure the target proxy

To configure the target proxy, use the [`google_compute_target_http_proxy` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_target_http_proxy) or the [`google_compute_target_https_proxy` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_target_https_proxy).
    
    
    # http proxy
    resource "google_compute_target_http_proxy" "default" {
      name    = "http-lb-proxy"
      url_map = google_compute_url_map.default.id
    }

#### Configure the forwarding rule

To configure the forwarding rule, use the [`google_compute_global_forwarding_rule` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_global_forwarding_rule).
    
    
    # forwarding rule
    resource "google_compute_global_forwarding_rule" "default" {
      name                  = "http-lb-forwarding-rule"
      ip_protocol           = "TCP"
      load_balancing_scheme = "EXTERNAL"
      port_range            = "80"
      target                = google_compute_target_http_proxy.default.id
      ip_address            = google_compute_global_address.default.id
    }

  * For a global external Application Load Balancer, use with `load_balancing_scheme="EXTERNAL_MANAGED"`. This setting offers [advanced traffic management capability](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management-global).
  * For a classic Application Load Balancer, use `load_balancing_scheme="EXTERNAL"`.



To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

## Make your Cloud Storage bucket accessible

You can make your Cloud Storage bucket publicly readable or restrict access to it.

### Make your Cloud Storage bucket public

This example makes your [Cloud Storage bucket publicly readable](https://docs.cloud.google.com/storage/docs/access-control/making-data-public#buckets). This is the recommended approach for public content. With this setting, anyone on the internet can view and list your objects and their metadata, excluding ACLs. To reduce the risk of unintended data exposure, you should typically dedicate specific Cloud Storage buckets for public objects.

**Important:** When objects are served from a public Cloud Storage bucket, [by default](https://docs.cloud.google.com/storage/docs/metadata#caching_data) they have a `Cache-Control: public, max-age=3600` response header applied. This allows the objects to be cached when Cloud CDN is enabled.

The following are alternatives to making an entire Cloud Storage bucket public:

  * Use [managed folders](https://docs.cloud.google.com/storage/docs/managed-folders) to [make a portion of your bucket publicly readable](https://docs.cloud.google.com/storage/docs/access-control/making-data-public#managed-folders).

  * [Make individual objects publicly readable](https://docs.cloud.google.com/storage/docs/access-control/create-manage-lists#set-an-acl). We don't recommend this approach, because it uses a legacy, Cloud Storage-specific permissioning system.

  * Use [signed URLs](https://docs.cloud.google.com/cdn/docs/using-signed-urls).




The following procedure grants all users access to view objects in your Cloud Storage bucket, making the bucket publicly readable.

###  Console 

**Note:** For global external Application Load Balancers, the Google Cloud console isn't supported.

  1. In the Google Cloud console, open the **Cloud Storage Buckets** page. 

[Open the Buckets page](https://console.cloud.google.com/storage/browser)

  2. Navigate to the bucket and click the **Permissions** tab.
  3. Click **Add principals**.
  4. In **New principals** , enter `allUsers`.
  5. For the role, select **Cloud Storage > Storage Object Viewer**.
  6. Click **Save**.



###  gcloud 
    
    
    gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME --member=allUsers --role=roles/storage.objectViewer
    

###  Terraform 

To make your Cloud Storage bucket public, use the [`google_storage_bucket_iam_member` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket_iam#google_storage_bucket_iam_member).
    
    
    # make bucket public
    resource "google_storage_bucket_iam_member" "default" {
      bucket = google_storage_bucket.default.name
      role   = "roles/storage.objectViewer"
      member = "allUsers"
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

### Make your Cloud Storage bucket private

To enable access to your private buckets, grant the required IAM roles to the service account that performs cache fills.

###  Console 

  1. In the Google Cloud console, go to the **Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Navigate to the bucket that you want to enable access to and click the **Permissions** tab.

  3. In the **Permissions** section, on the **View by principals** tab, click person_add**Grant Access**.

  4. In the **Add principals** section, in the **New principals** field, enter the email address of the calling service account: `**service- PROJECT_NUM@https-lb.iam.gserviceaccount.com**`.

**Important:** This service account is only available for `PROJECT_NUM` after you have created at least one backend bucket resource in the project.
  5. In the **Assign roles** section, in the **Select a role** field, select **Cloud Storage > Storage Object Viewer**. This role provides read-only access.

**Caution:** Private bucket access is designed for read-only content delivery. It doesn't support methods that modify or delete data, such as `POST`, `PUT`, `PATCH`, or `DELETE`.**Important:** When setting permissions for private bucket access, select the Storage Object Viewer role (`roles/storage.objectViewer`) only.
  6. Click **Save**.




Additionally, so that all content served from the bucket is cached, [set the cache mode](https://docs.cloud.google.com/cdn/docs/using-cache-modes#cache-mode) to **Force cache all content** and [specify a maximum TTL value](https://docs.cloud.google.com/cdn/docs/using-ttl-overrides#default-ttl).

###  gcloud 

To grant Cloud CDN access to a bucket, grant the `objectViewer` role to the service account:
    
    
      gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
          --member=serviceAccount:service-PROJECT_NUM@https-lb.iam.gserviceaccount.com \
          --role=roles/storage.objectViewer
    

Replace the following:

  * `BUCKET_NAME`: the name of the Cloud Storage bucket to use
  * `PROJECT_NUM`: the number of your Google Cloud project

**Caution:** Private bucket access is designed for read-only content delivery. It doesn't support methods that modify or delete data, such as `POST`, `PUT`, `PATCH`, or `DELETE`.**Important:** When setting permissions for private bucket access, you must only select the Storage Object Viewer role (`roles/storage.objectViewer`).



Additionally, so that all content served from the bucket is cached, [set the cache mode](https://docs.cloud.google.com/cdn/docs/using-cache-modes#cache-mode) to `force-cache-all` and [set a `max-ttl` value](https://docs.cloud.google.com/cdn/docs/using-ttl-overrides#max-ttl).

## Send traffic to your backend bucket

After creating the global forwarding rule, it can take several minutes for your configuration to propagate worldwide. After several minutes have passed, you can start sending traffic to the load balancer's IP address.

###  Console 

**Note:** For global external Application Load Balancers, the Google Cloud console isn't supported.

  1. In the Google Cloud console, go to the **Load balancing** page. 

[Go to the Load balancing page](https://console.cloud.google.com/networking/loadbalancing/)

  2. Click `http-lb` to expand the load balancer that you just created.

In the **Backend** section, confirm that the backend bucket is healthy. There should be a green checkmark next to your backend bucket. If you see otherwise, first try reloading the page. It can take a few moments for the Google Cloud console to indicate that backends are healthy.

  3. After the Google Cloud console shows that the backend bucket is healthy, you can test your load balancer using a web browser by going to `http://IP_ADDRESS/never-fetch/three-cats.jpg`. Replace `IP_ADDRESS` with the load balancer's IP address. Your browser should render a page with content showing the graphic file.




###  gcloud 

Use the `curl` command to test the response from the URL. Replace `IP_ADDRESS` with the load balancer's IPv4 address.

Note the IPv4 address that was reserved:
    
    
    gcloud compute addresses describe example-ip \
        --format="get(address)" \
        --global
    

Send a curl request:
    
    
    curl http://IP_ADDRESS/never-fetch/three-cats.jpg
    

## Verify that Cloud CDN is working

If you reload the `http://IP_ADDRESS/never-fetch/three-cats.jpg` page several times in quick succession, there should be several cache hits.

The following log entry shows a cache hit. You can view cache hits in the Google Cloud console by opening Logs Explorer and filtering by the forwarding rule name.

[Open the Logs Explorer](https://console.cloud.google.com/logs?service=network.googleapis.com)

**Note:** If you don't specify a forwarding rule name when you set up your load balancer, the forwarding rule name is the load balancer name plus `-forwarding-rule`. In this case, `http-lb-forwarding-rule`.

###  Logs Explorer 
    
    
    {
        insertId: "1oek5rg3l3fxj7"
        jsonPayload: {
            @type: "type.googleapis.com/google.cloud.loadbalancing.type.LoadBalancerLogEntry"
            cacheId: "SFO-fbae48ad"
            statusDetails: "response_from_cache"
        }
        httpRequest: {
            requestMethod: "GET"
            requestUrl: "http://LOAD_BALANCER_IP_ADDRESS/never-fetch/three-cats.jpg"
            requestSize: "577"
            status: 254
            responseSize: "157"
            userAgent: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
            remoteIp: "CLIENT_IP_ADDRESS"
            cacheHit: truecacheLookup: true
        }
        resource: {
            type: "http_load_balancer"
            labels: {
                zone: "global"
                url_map_name: "URL_MAP_NAME"
                forwarding_rule_name: "FORWARDING_RULE_NAME"
                target_proxy_name: "TARGET_PROXY_NAME"
                backend_service_name: ""
                project_id: "PROJECT_ID"
            }
        }
        timestamp: "2020-06-08T23:41:25.078651Z"
        severity: "INFO"
        logName: "projects/PROJECT_ID/logs/requests"
        trace: "projects/PROJECT_ID/traces/241d69833e64b3bf83fabac8c873d992"
        receiveTimestamp: "2020-06-08T23:41:25.588272510Z"
        spanId: "7b6537d3672e08e1"
    }
    

###  Console 

**Note:** For global external Application Load Balancers, the Google Cloud console isn't supported.

  1. In the Google Cloud console, go to the **Load balancing** page. 

[Go to the Load balancing page](https://console.cloud.google.com/networking/loadbalancing/)

  2. Click `http-lb` to expand the load balancer that you just created.

In the **Backend** section, confirm that the backend bucket is healthy. There should be a green checkmark next to your backend bucket. If you see otherwise, first try reloading the page. It can take a few moments for the Google Cloud console to indicate that backends are healthy.

  3. After the Google Cloud console shows that the backend bucket is healthy, you can test your load balancer using a web browser by going to `http://IP_ADDRESS/never-fetch/three-cats.jpg`. Replace `IP_ADDRESS` with the load balancer's IP address. Your browser should render a page with content showing the graphic file.




###  gcloud 

Use the `curl` command to test the response from the URL. Replace `IP_ADDRESS` with the load balancer's IPv4 address.

Note the IPv4 address that was reserved:
    
    
    gcloud compute addresses describe example-ip \
        --format="get(address)" \
        --global
    

Send a curl request:
    
    
    curl -D- -o /dev/null /dev/null http://IP_ADDRESS/never-fetch/three-cats.jpg
    

Content is fetched from Cloud Storage, cached by Cloud CDN, and then validated and re-fetched when it expires or is otherwise evicted from the cache.

Content from cache has an `Age` header that is greater than zero.

Content that needs to be refreshed earlier than the TTL can be [invalidated](https://docs.cloud.google.com/cdn/docs/invalidating-cached-content) and re-fetched from Cloud Storage.

## Disable Cloud CDN

###  Console 

**Note:** For global external Application Load Balancers, the Google Cloud console isn't supported.

#### Disable Cloud CDN for a single backend bucket

  1. In the Google Cloud console, go to the **Cloud CDN** page. 

[Go to the Cloud CDN page](https://console.cloud.google.com/networking/cdn/list)

  2. On the right side of the origin row, click **Menu** more_vert and then select **Edit**.
  3. Clear the checkboxes of any backend buckets that you want to stop from using Cloud CDN.
  4. Click **Update**.



#### Remove Cloud CDN for all backend buckets for an origin

  1. In the Google Cloud console, go to the **Cloud CDN** page. 

[Go to the Cloud CDN page](https://console.cloud.google.com/networking/cdn/list)

  2. On the right side of the origin row, click **Menu** more_vert and then select **Remove**.
  3. To confirm, click **Remove**.



###  gcloud 
    
    
    gcloud compute backend-buckets update BACKEND_BUCKET_NAME \
        --no-enable-cdn
    

Disabling Cloud CDN does not invalidate or purge caches. If you turn Cloud CDN off and back on again, most or all of your cached content might still be cached. To prevent content from being used by the caches, you must [invalidate that content](https://docs.cloud.google.com/cdn/docs/invalidating-cached-content).

## What's next

  * To learn about what content is cached, see the [Caching overview](https://docs.cloud.google.com/cdn/docs/caching).
  * To use Cloud CDN in GKE, see [Ingress features](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-features).
  * To check whether Cloud CDN is serving responses from cache, see [Viewing logs](https://docs.cloud.google.com/cdn/docs/logging).
  * To find information about common problems and solutions, see [Troubleshooting](https://docs.cloud.google.com/cdn/docs/troubleshooting-steps).
  * To configure filtering and access control policies for your content, see [Edge security policies](https://docs.cloud.google.com/armor/docs/security-policy-overview#edge-policies).
  * To set up cache policies in URL maps, see [Configure a Cloud CDN cache policy](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-global-traffic-mgmt#cdn-cache-policy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
