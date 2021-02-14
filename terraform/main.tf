resource "google_storage_bucket" "input_bucket" {
  name = lookup(var.input_bucket, "name", "")
  location = lookup(var.input_bucket, "location", "")
  storage_class = lookup(var.input_bucket, "storage_class", "")
}

resource "google_storage_bucket" "output_bucket" {
  name = lookup(var.output_bucket, "name", "")
  location = lookup(var.output_bucket, "location", "")
  storage_class = lookup(var.output_bucket, "storage_class", "")
}


resource "google_cloudbuild_trigger" "filename-trigger" {
  filename = "../tts/Dockerfile"
}


# resource "google_cloud_run_service" "default" {
#   name     = "test-container"
#   location = "us-central1"

#   template {
#     spec {
#       containers {
#         image = "gcr.io/end-to-end-security/tts:latest"
#         # gcr.io/end-to-end-security/test-img       us-docker.pkg.dev/cloudrun/container/test-img
#       }
#     }
#   }

#   traffic {
#     percent         = 100
#     latest_revision = true
#   }
  
# }
# data "google_iam_policy" "noauth" {
#   binding {
#     role = "roles/run.invoker"
#     members = [
#       "allUsers",
#     ]
#   }
# }

# resource "google_cloud_run_service_iam_policy" "noauth" {
#   location    = google_cloud_run_service.default.location
#   project     = google_cloud_run_service.default.project
#   service     = google_cloud_run_service.default.name

#   policy_data = data.google_iam_policy.noauth.policy_data
# }