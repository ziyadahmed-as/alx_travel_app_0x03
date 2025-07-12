## 💳 Payment Integration (Chapa)

- Integrated Chapa API to securely handle payments
- Payments are initiated and verified via Django REST API
- Booking reference and transaction status stored in the Payment model
- Celery used to send confirmation emails


# ## Celery + RabbitMQ Setup

```bash
# Start broker (docker)
docker run -d --name rabbit -p 5672:5672 -p 15672:15672 rabbitmq:3-management

# Install deps
pip install -r requirements.txt   # includes celery

# Run worker
celery -A alx_travel_app worker -l info
