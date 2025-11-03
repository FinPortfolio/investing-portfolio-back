# app/adapters/taskiq/tasks/email_tasks.py
import logging

from app.adapters.taskiq import broker


async def send_email(recipient, subject, body):
    print("INFORMATION: ")
    print(recipient)
    print(subject)
    print(body)
    return


async def send_welcome_email():
    message = "Getting some information from DB"

    await send_email(
        recipient="lasowskiwlodzimierz@gmail.com",
        subject="Welcome message",
        body=message,
    )


logger = logging.getLogger(__name__)


@broker.task
async def taskiq_send_welcome_email():
    logger.info("Start sending welcome email")
    await send_welcome_email()
    logger.info("Finish sending welcome email")