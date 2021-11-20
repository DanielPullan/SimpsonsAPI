terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "2.13.0"
    }
  }
}

provider "docker" {
  host = "unix:///var/run/docker.sock" # to use local docker provider
}
 
resource "docker_container" "simpsonsapi" {
  image = "simpsonsapi" # local image tag
  name  = "simpsonsapi" # 

  ports {
    internal = 80 
    external = 80 
  }
}

