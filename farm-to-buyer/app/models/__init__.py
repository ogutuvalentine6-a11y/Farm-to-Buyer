from app.models.user import User, Role
from app.models.farm import Farm
from app.models.produce import Produce
from app.models.agrovet import Agrovet
from app.models.product import Product
from app.models.order import Order
from app.models.delivery import Delivery
from app.models.payment import Payment
from app.models.knowledge import Knowledge
from app.models.message import Message
from app.models.notification import Notification

ALL_MODELS = [
    User, Farm, Produce, Agrovet, Product, Order,
    Delivery, Payment, Knowledge, Message, Notification,
]
