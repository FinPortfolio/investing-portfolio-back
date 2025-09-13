import subprocess
import time


def main():
    try:
        # 1. Поднимаем контейнеры
        subprocess.run(
            ["docker", "compose", "-f", "docker-compose.test.yaml", "up", "--build", "-d", "--remove-orphans"],
            check=True
        )

        # 2. Ждём, пока backend_test станет готов
        time.sleep(5)  # можно заменить на проверку healthcheck

        # 3. Запускаем pytest внутри контейнера через bash
        subprocess.run(
            'docker compose -f docker-compose.test.yaml exec -it backend_test bash -c "pytest --maxfail=5 -v"',
            shell=True,
            check=True
        )

    finally:
        # 4. Останавливаем контейнеры
        subprocess.run(
            ["docker", "compose", "-f", "docker-compose.test.yaml", "down"],
            check=True
        )


if __name__ == "__main__":
    main()
