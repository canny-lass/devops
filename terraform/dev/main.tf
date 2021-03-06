terraform {
  required_providers {
    heroku = {
      source  = "heroku/heroku"
      version = "~> 4.0"
    }
  }
}

provider "heroku" {
  email   = "ibrahimayodeji15@gmail.com"
  api_key = "e045de78-b3ad-49e6-9611-3fe6e857bcea"
}

resource "heroku_app" "default" {
  name   = "canny-lass-app-dev"
  region = "us"
}

# Build code & release to the app
resource "heroku_build" "default" {
  app        = "canny-lass-app-dev"
  buildpacks = ["https://github.com/heroku/heroku-buildpack-python.git"]

  source {
    path = "../../src"
  }
}

# # Launch the app's web process by scaling-up
# resource "heroku_formation" "example" {
#   app        = heroku_app.example.name
#   type       = "web"
#   quantity   = 1
#   size       = "Standard-1x"
#   depends_on = [heroku_build.example]
# }

output "app_url" {
  value = "https://${heroku_app.default.name}.herokuapp.com"
}
