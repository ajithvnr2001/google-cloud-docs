---
url: https://docs.cloud.google.com/talent-solution/job-search/v4beta1/libs/20170123-job-discovery-nodejs-client-example.txt
title: https://docs.cloud.google.com/talent-solution/job-search/v4beta1/libs/20170123-job-discovery-nodejs-client-example.txt
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:23:39.771452+00:00
---

# https://docs.cloud.google.com/talent-solution/job-search/v4beta1/libs/20170123-job-discovery-nodejs-client-example.txt

> Source: https://docs.cloud.google.com/talent-solution/job-search/v4beta1/libs/20170123-job-discovery-nodejs-client-example.txt

var google = require('googleapis'); var discoveryDoc = '/path/to/your/jobs_discovery_v2beta1_distrib.json'; var jobs, authClient; function getJobService (callback) { // Used the cached service if (jobs) { callback(null, jobs); return; } google.discoverAPI(discoveryDoc, function (err, _jobs) { if (err) { console.error('Failed to generate jobs client!'); callback(err); return; } jobs = _jobs; callback(null, jobs); }); } function authorize (callback) { // Used the cached auth client if (!authClient) { var key = require('/usr/local/google/home/xinyunh/Downloads/garage-test5-0919e99ee4cc.json'); var authClient = new google.auth.JWT(key.client_email, null, key.private_key, ["https://www.googleapis.com/auth/jobs"], null); } callback(null, authClient); } getJobService(function (err, jobs) { if (err) throw err; authorize(function (err, authClient) { if (err) { console.log(err); throw err; } jobs.companies.list({ auth: authClient }, function (err, response) { if (err) { console.error('Failed to retrieve companies!'); throw err; } console.log('Companies:', response.companies); }); }); });
