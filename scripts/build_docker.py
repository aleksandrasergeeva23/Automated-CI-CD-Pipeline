import subprocess

def build_docker_image(image_name):
    try:
        subprocess.run(['docker', 'build', '-t', image_name, '.'], check=True)
        print(f"Docker image '{image_name}' built successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error building docker image: {e}")

if __name__ == "__main__":
    image_name = "my-flask-app"
    build_docker_image(image_name)