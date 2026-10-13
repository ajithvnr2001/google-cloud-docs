---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dns/latest/
title: Google Cloud DNS \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:14.847960+00:00
---

# Google Cloud DNS  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dns/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud DNS Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.1  1.0.0  0.37.0  0.36.1  0.35.1 

Google Cloud DNS is a high-performance, resilient, global DNS service that provides a cost-effective way to make your applications and services available to your users. This programmable, authoritative DNS service can be used to easily publish and manage DNS records using the same infrastructure relied upon by Google. To learn more, read [Cloud DNS Overview](https://cloud.google.com/dns/docs/overview).

The goal of google-cloud is to provide an API that is comfortable to Rubyists. Your authentication credentials are detected automatically in Google Cloud Platform (GCP), including Google Compute Engine (GCE), Google Kubernetes Engine (GKE), Google App Engine (GAE), Google Cloud Functions (GCF) and Cloud Run. In other environments you can configure authentication easily, either directly in your code or via environment variables. Read more about the options for connecting in the [Authentication Guide](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dns/latest/AUTHENTICATION "Authentication Guide").

## Creating Zones

To get started with Google Cloud DNS, use your DNS Project to create a new Zone. The second argument to [Google::Cloud::Dns::Project#create_zone](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dns/latest/Google-Cloud-Dns-Project#Google__Cloud__Dns__Project_create_zone_instance_ "Google::Cloud::Dns::Project#create_zone \(method\)") must be a unique domain name for which you can [verify ownership](https://www.google.com/webmasters/verification/home). Substitute a domain name of your own (ending with a dot to signify that it is [fully qualified](https://en.wikipedia.org/wiki/Fully_qualified_domain_name)) as you follow along with these examples.
    
    
    require "google/cloud/dns"
    
    dns = Google::Cloud::Dns.new
    zone = dns.create_zone "example-com", "example.com."
    puts zone.id # unique identifier defined by the server

For more information, see [Managing Zones](https://cloud.google.com/dns/zones/).

## Listing Zones

You can retrieve all the zones in your project.
    
    
    require "google/cloud/dns"
    
    dns = Google::Cloud::Dns.new
    zones = dns.zones
    zones.each do |zone|
      puts "#{zone.name} - #{zone.dns}"
    end

You can also retrieve a single zone by either name or id.
    
    
    require "google/cloud/dns"
    
    dns = Google::Cloud::Dns.new
    zone = dns.zone "example-com"

## Listing Records

When you create a zone, the Cloud DNS service automatically creates two Record instances for it, providing configuration for Cloud DNS nameservers. Let's take a look at these records.
    
    
    require "google/cloud/dns"
    
    dns = Google::Cloud::Dns.new
    zone = dns.zone "example-com"
    records = zone.records
    records.count #=> 2
    records.map &:type #=> ["NS", "SOA"]
    zone.records.first.data.count #=> 4
    zone.records.first.data #=> ["ns-cloud-d1.googledomains.com.", ...]

Note that [Google::Cloud::Dns::Record#data](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dns/latest/Google-Cloud-Dns-Record#Google__Cloud__Dns__Record_data_instance_ "Google::Cloud::Dns::Record#data \(method\)") returns an array. The Cloud DNS service only allows the zone to have one Record instance for each name and type combination. It supports multiple "resource records" (in this case, the four nameserver addresses) via this `data` collection.

## Managing Records

You can easily add your own records to the zone. Each call to [Google::Cloud::Dns::Zone#add](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dns/latest/Google-Cloud-Dns-Zone#Google__Cloud__Dns__Zone_add_instance_ "Google::Cloud::Dns::Zone#add \(method\)") results in a new Cloud DNS Change instance.
    
    
    require "google/cloud/dns"
    
    dns = Google::Cloud::Dns.new
    zone = dns.zone "example-com"
    change = zone.add "www", "A", 86400, ["1.2.3.4"]
    change.additions.map &:type #=> ["A", "SOA"]
    change.deletions.map &:type #=> ["SOA"]

Whenever you change the set of records belonging to a zone, the zone's start of authority (SOA) record should be updated with a higher serial number. The google-cloud library automates this update for you, deleting the old SOA record and adding an updated one, as shown in the example above. You can disable or modify this behavior, of course. See [Google::Cloud::Dns::Zone#update](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dns/latest/Google-Cloud-Dns-Zone#Google__Cloud__Dns__Zone_update_instance_ "Google::Cloud::Dns::Zone#update \(method\)") for details.

You can retrieve records by name and type. The name argument can be a subdomain (e.g., `www`) fragment for convenience, but notice that the retrieved record's domain name is always fully-qualified.
    
    
    require "google/cloud/dns"
    
    dns = Google::Cloud::Dns.new
    zone = dns.zone "example-com"
    records = zone.records "www", "A"
    records.first.name #=> "www.example.com."

You can use [Google::Cloud::Dns::Zone#replace](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dns/latest/Google-Cloud-Dns-Zone#Google__Cloud__Dns__Zone_replace_instance_ "Google::Cloud::Dns::Zone#replace \(method\)") to update the `ttl` and `data` for a record.
    
    
    require "google/cloud/dns"
    
    dns = Google::Cloud::Dns.new
    zone = dns.zone "example-com"
    change = zone.replace "www", "A", 86400, ["5.6.7.8"]

Or, you can use [Google::Cloud::Dns::Zone#modify](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dns/latest/Google-Cloud-Dns-Zone#Google__Cloud__Dns__Zone_modify_instance_ "Google::Cloud::Dns::Zone#modify \(method\)") to update just the `ttl` or `data`, without the risk of inadvertently changing values that you wish to leave unchanged.
    
    
    require "google/cloud/dns"
    
    dns = Google::Cloud::Dns.new
    zone = dns.zone "example-com"
    change = zone.modify "www", "A" do |r|
      r.ttl = 3600 # change only the TTL
    end

You can also delete records by name and type.
    
    
    require "google/cloud/dns"
    
    dns = Google::Cloud::Dns.new
    zone = dns.zone "example-com"
    change = zone.remove "www", "A"
    record = change.deletions.first

The best way to add, remove, and update multiple records in a single [transaction](https://cloud.google.com/dns/records) is to call [Google::Cloud::Dns::Zone#update](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dns/latest/Google-Cloud-Dns-Zone#Google__Cloud__Dns__Zone_update_instance_ "Google::Cloud::Dns::Zone#update \(method\)") with a block. See [Google::Cloud::Dns::Zone::Transaction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dns/latest/Google-Cloud-Dns-Zone-Transaction "Google::Cloud::Dns::Zone::Transaction \(class\)").
    
    
    require "google/cloud/dns"
    
    dns = Google::Cloud::Dns.new
    zone = dns.zone "example-com"
    change = zone.update do |tx|
      tx.add     "www", "A",  86400, "1.2.3.4"
      tx.remove  "example.com.", "TXT"
      tx.replace "example.com.", "MX", 86400, ["10 mail1.example.com.",
                                               "20 mail2.example.com."]
      tx.modify "www.example.com.", "CNAME" do |r|
        r.ttl = 86400 # only change the TTL
      end
    end

Finally, you can add and delete records by reference, using [Google::Cloud::Dns::Zone#update](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dns/latest/Google-Cloud-Dns-Zone#Google__Cloud__Dns__Zone_update_instance_ "Google::Cloud::Dns::Zone#update \(method\)").
    
    
    require "google/cloud/dns"
    
    dns = Google::Cloud::Dns.new
    zone = dns.zone "example-com"
    to_add = zone.record "www", "AAAA", 86400, ["2607:f8b0:400a:801::1005"]
    to_delete = zone.records "www", "A"
    change = zone.update to_add, to_delete

## Listing Changes

Because the transactions you execute against your zone do not always complete immediately, you can retrieve and inspect changes.
    
    
    require "google/cloud/dns"
    
    dns = Google::Cloud::Dns.new
    zone = dns.zone "example-com"
    changes = zone.changes
    changes.each do |change|
      puts "#{change.id} - #{change.started_at} - #{change.status}"
    end

## Importing and exporting zone files

You can import from a zone file. Because the Cloud DNS service only allows the zone to have one Record instance for each name and type combination, lines may be merged as needed into records with multiple `data` values.
    
    
    require "google/cloud/dns"
    
    dns = Google::Cloud::Dns.new
    zone = dns.zone "example-com"
    change = zone.import "path/to/db.example.com"

You can also export to a zone file.
    
    
    require "google/cloud/dns"
    
    dns = Google::Cloud::Dns.new
    zone = dns.zone "example-com"
    
    zone.export "path/to/db.example.com"

## Configuring retries and timeout

You can configure how many times API requests may be automatically retried. When an API request fails, the response will be inspected to see if the request meets criteria indicating that it may succeed on retry, such as `500` and `503` status codes or a specific internal error code such as `rateLimitExceeded`. If it meets the criteria, the request will be retried after a delay. If another error occurs, the delay will be increased before a subsequent attempt, until the `retries` limit is reached.

You can also set the request `timeout` value in seconds.
    
    
    require "google/cloud/dns"
    
    dns = Google::Cloud::Dns.new retries: 10, timeout: 120

## Additional information

Google Cloud DNS can be configured to use logging. To learn more, see the [Logging guide](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dns/latest/LOGGING "Logging guide").

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-25 UTC."],[],[]] 
