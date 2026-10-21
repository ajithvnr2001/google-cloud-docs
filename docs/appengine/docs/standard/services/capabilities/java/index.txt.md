---
url: https://docs.cloud.google.com/appengine/docs/standard/services/capabilities/java/index.txt
title: https://docs.cloud.google.com/appengine/docs/standard/services/capabilities/java/index.txt
method: crawl4ai+scrapegraph (scrapling: scrapling thin content (724 chars), fallback to crawl4ai)
fetched_at: 2026-10-15T20:47:54.071747+00:00
---

# https://docs.cloud.google.com/appengine/docs/standard/services/capabilities/java/index.txt

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/capabilities/java/index.txt


    // [START image_resize]
    import com.google.appengine.api.capabilities.*;
    
    CapabilitiesService service =
        CapabilitiesServiceFactory.getCapabilitiesService();
    CapabilityStatus status = service.getStatus(Capability.IMAGES).getStatus();
    
    if (status == CapabilityStatus.DISABLED) {
        // Images API is not available.
    }
    // [END image_resize]
    
    // [START intro]
    CapabilityStatus status =
        service.getStatus(Capability.DATASTORE_WRITE).getStatus();
    
    if (status == CapabilityStatus.DISABLED) {
        // Datastore is in read-only mode.
    }
    // [END intro]
    
