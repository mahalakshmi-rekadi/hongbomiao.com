#!/usr/bin/env bash
set -e

echo "# Install Postgres"
kubectl apply --filename=kubernetes/manifests/postgres
echo "=================================================="
