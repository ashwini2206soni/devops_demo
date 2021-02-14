variable "project" {
  type = string
  description = "Project ID of the project to be used"  
}
variable "region" {
  type = string
  description = "Region of the project"
}

variable "input_bucket" {
  type = map
  description = "Configuration of bucket to be created for cloud function source code"
}

variable "output_bucket" {
  type = map
  description = "Configuration of bucket to be created for cloud function source code"
}


