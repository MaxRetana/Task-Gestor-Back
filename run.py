import subprocess

def run_management_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar '{command}': {e}")

def main():
    # Ejecutar makemigrations
    run_management_command("python manage.py makemigrations")
    
    # Ejecutar migrate
    run_management_command("python manage.py migrate")
    
    # Ejecutar runserver
    run_management_command("python manage.py runserver")


if __name__ == '__main__':
    main()