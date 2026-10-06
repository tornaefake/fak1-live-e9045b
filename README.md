# tenant-python-app-template

Tenant application scaffold (Python/FastAPI): app/, tests/, Dockerfile, CI.

CI: gitleaks + pytest, then build-scan-push via galan-projects/shared-workflows
docker-build hub on push (image: registry.nas.local:8443/<harbor_project>/<image_name>).
On first use: rename image_name/harbor_project, create the Harbor project, and point the
tenant's values repo (tenant-values-template) at the published tag.
