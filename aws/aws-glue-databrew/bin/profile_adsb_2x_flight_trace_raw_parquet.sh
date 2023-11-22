#!/usr/bin/env bash

profile_job_name="hm-profile-adsb-2x-flight-trace-raw-parquet"
dates=(
  "2023-10-01"
  "2023-10-02"
  "2023-10-03"
  "2023-10-04"
  "2023-10-05"
  "2023-10-06"
  "2023-10-07"
  "2023-10-08"
  "2023-10-09"
  "2023-10-10"
  "2023-10-11"
  "2023-10-12"
  "2023-10-13"
  "2023-10-14"
  "2023-10-15"
  "2023-10-16"
  "2023-10-17"
  "2023-10-18"
  "2023-10-19"
  "2023-10-20"
  "2023-10-21"
  "2023-10-22"
  "2023-10-23"
  "2023-10-24"
  "2023-10-25"
  "2023-10-26"
  "2023-10-27"
  "2023-10-28"
  "2023-10-29"
  "2023-10-30"
)

for date in "${dates[@]}"
do
    aws databrew start-job-run --name="${profile_job_name}-${date}" --no-cli-pager
    sleep 1
done
